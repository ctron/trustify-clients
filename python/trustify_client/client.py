"""Shared request configuration for the generated Trustify API."""

import asyncio
import inspect
import math
import ssl
import time
from collections.abc import Callable, Mapping
from typing import Any, Optional
from urllib.parse import urlsplit

import httpx

from .generated import Client as GeneratedClient

TokenProvider = Callable[[], Any]


class RetryPolicy:
    """Opt-in retries for idempotent API reads."""

    def __init__(
        self,
        max_retries: int = 0,
        initial_backoff: float = 0.1,
        max_backoff: float = 2.0,
    ) -> None:
        if (
            not isinstance(max_retries, int)
            or isinstance(max_retries, bool)
            or max_retries < 0
            or not math.isfinite(initial_backoff)
            or not math.isfinite(max_backoff)
            or initial_backoff < 0
            or max_backoff < 0
        ):
            raise ValueError("retry counts and backoff values must be non-negative")
        self.max_retries = max_retries
        self.initial_backoff = initial_backoff
        self.max_backoff = max_backoff

    @classmethod
    def disabled(cls) -> "RetryPolicy":
        return cls()

    @classmethod
    def for_idempotent_requests(cls, max_retries: int) -> "RetryPolicy":
        return cls(max_retries, 0.1, 2.0)

    def delay(self, attempt: int) -> float:
        return min(self.initial_backoff * (2 ** min(attempt, 31)), self.max_backoff)

    def response_delay(self, response: httpx.Response, attempt: int) -> float:
        retry_after = response.headers.get("Retry-After", "")
        if retry_after.isascii() and retry_after.isdecimal():
            return min(float(retry_after), self.max_backoff)
        return self.delay(attempt)


class _RequestBehavior(httpx.Auth):
    def __init__(self, token_provider: Optional[TokenProvider]) -> None:
        self.token_provider = token_provider

    def auth_flow(self, request: httpx.Request):
        self._prepare_request(request, self._sync_token())
        yield request

    async def async_auth_flow(self, request: httpx.Request):
        self._prepare_request(request, await self._async_token())
        yield request

    def _sync_token(self) -> Optional[str]:
        if self.token_provider is None:
            return None
        token = self.token_provider()
        if inspect.isawaitable(token):
            close = getattr(token, "close", None)
            if close is not None:
                close()
            raise TypeError("an async token provider requires an async API operation")
        return token

    async def _async_token(self) -> Optional[str]:
        if self.token_provider is None:
            return None
        token = self.token_provider()
        if inspect.isawaitable(token):
            token = await token
        return token

    @staticmethod
    def _prepare_request(request: httpx.Request, token: Optional[str]) -> None:
        if token is not None and not isinstance(token, str):
            raise TypeError("token_provider must return str or None")
        if token is not None:
            request.headers["Authorization"] = f"Bearer {token}"

        path = request.url.path
        if request.method == "PATCH" and "/api/v3/importer/" in path:
            request.headers["Content-Type"] = "application/merge-patch+json"
        elif "/api/v3/importer/" in path and (
            (request.method == "PUT" and path.endswith("/enabled"))
            or (request.method == "POST" and path.endswith("/force"))
        ):
            request.headers["Content-Type"] = "text/plain"


class _RetryTransport(httpx.BaseTransport, httpx.AsyncBaseTransport):
    def __init__(
        self,
        sync_transport: httpx.BaseTransport,
        async_transport: httpx.AsyncBaseTransport,
        retry_policy: RetryPolicy,
    ) -> None:
        self._sync_transport = sync_transport
        self._async_transport = async_transport
        self._retry_policy = retry_policy

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = self._sync_transport.handle_request(request)
            except (httpx.ConnectError, httpx.TimeoutException):
                if not self._can_retry(request, attempt):
                    raise
                time.sleep(self._retry_policy.delay(attempt))
            else:
                if not self._retry_response(request, response, attempt):
                    return response
                delay = self._retry_policy.response_delay(response, attempt)
                response.close()
                time.sleep(delay)
            attempt += 1

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = await self._async_transport.handle_async_request(request)
            except (httpx.ConnectError, httpx.TimeoutException):
                if not self._can_retry(request, attempt):
                    raise
                await asyncio.sleep(self._retry_policy.delay(attempt))
            else:
                if not self._retry_response(request, response, attempt):
                    return response
                delay = self._retry_policy.response_delay(response, attempt)
                await response.aclose()
                await asyncio.sleep(delay)
            attempt += 1

    def _can_retry(self, request: httpx.Request, attempt: int) -> bool:
        return (
            request.method in {"GET", "HEAD"}
            and attempt < self._retry_policy.max_retries
        )

    def _retry_response(
        self, request: httpx.Request, response: httpx.Response, attempt: int
    ) -> bool:
        return self._can_retry(request, attempt) and response.status_code in {
            429,
            502,
            503,
            504,
        }

    def close(self) -> None:
        self._sync_transport.close()

    async def aclose(self) -> None:
        await self._async_transport.aclose()


class TrustifyClient:
    """Shared client configuration for a Trustify server."""

    def __init__(
        self,
        base_url: str,
        *,
        bearer_token: Optional[str] = None,
        token_provider: Optional[TokenProvider] = None,
        retry_policy: Optional[RetryPolicy] = None,
        connect_timeout: float = 15.0,
        request_timeout: float = 120.0,
        verify_ssl: bool | str | ssl.SSLContext = True,
        httpx_args: Optional[Mapping[str, Any]] = None,
        raise_on_unexpected_status: bool = False,
    ) -> None:
        try:
            parsed = urlsplit(base_url)
            parsed.port
        except ValueError:
            raise ValueError("base_url must be an absolute HTTP or HTTPS URL") from None
        if parsed.scheme not in {"http", "https"} or parsed.hostname is None:
            raise ValueError("base_url must be an absolute HTTP or HTTPS URL")
        if bearer_token is not None and token_provider is not None:
            raise ValueError("configure bearer_token or token_provider, not both")

        options = dict(httpx_args or {})
        reserved = {"auth", "base_url", "cookies", "headers", "timeout", "verify"}
        if reserved.intersection(options):
            raise ValueError(
                "auth, base_url, cookies, headers, timeout, and verify are configured separately"
            )

        provider = token_provider
        if bearer_token is not None:

            def fixed_token() -> str:
                return bearer_token

            provider = fixed_token

        policy = retry_policy or RetryPolicy()
        transport_options = {
            key: options[key]
            for key in (
                "cert",
                "http1",
                "http2",
                "limits",
                "local_address",
                "proxy",
                "socket_options",
                "trust_env",
                "uds",
            )
            if key in options
        }
        sync_transport = options.pop("transport", None)
        async_transport = options.pop("async_transport", None)
        if sync_transport is not None and not isinstance(
            sync_transport, httpx.BaseTransport
        ):
            raise TypeError("httpx_args['transport'] must be an HTTPX sync transport")
        if async_transport is not None and not isinstance(
            async_transport, httpx.AsyncBaseTransport
        ):
            raise TypeError(
                "httpx_args['async_transport'] must be an HTTPX async transport"
            )
        for key in ("cert", "local_address", "proxy", "socket_options", "uds"):
            options.pop(key, None)
        if sync_transport is None:
            sync_transport = httpx.HTTPTransport(verify=verify_ssl, **transport_options)
        if async_transport is None:
            if isinstance(sync_transport, httpx.AsyncBaseTransport):
                async_transport = sync_transport
            else:
                async_transport = httpx.AsyncHTTPTransport(
                    verify=verify_ssl, **transport_options
                )

        options["auth"] = _RequestBehavior(provider)
        options["transport"] = _RetryTransport(sync_transport, async_transport, policy)

        self._base_url = base_url.rstrip("/")
        self._api = GeneratedClient(
            base_url=self._base_url,
            timeout=httpx.Timeout(request_timeout, connect=connect_timeout),
            verify_ssl=verify_ssl,
            httpx_args=options,
            raise_on_unexpected_status=raise_on_unexpected_status,
        )

    @property
    def base_url(self) -> str:
        """Return the normalized base URL."""
        return self._base_url

    @property
    def api(self) -> GeneratedClient:
        """Access the generated low-level client used by endpoint functions."""
        return self._api

    def __enter__(self) -> "TrustifyClient":
        self._api.__enter__()
        return self

    def __exit__(self, *args: object, **kwargs: Any) -> None:
        self._api.__exit__(*args, **kwargs)

    async def __aenter__(self) -> "TrustifyClient":
        await self._api.__aenter__()
        return self

    async def __aexit__(self, *args: object, **kwargs: Any) -> None:
        await self._api.__aexit__(*args, **kwargs)
