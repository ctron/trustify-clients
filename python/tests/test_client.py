import asyncio
import unittest

import httpx

from trustify_client import (
    OffsetPage,
    RetryPolicy,
    TrustifyClient,
    collect_offset_pages,
    collect_offset_pages_async,
)
from trustify_client.client import _RequestBehavior, _RetryTransport
from trustify_client.generated.api.default import info


class ClientTests(unittest.TestCase):
    def test_rejects_non_http_or_malformed_base_urls(self):
        for base_url in ("trustify.example", "ftp://trustify.example", "http://:80"):
            with self.subTest(base_url=base_url), self.assertRaises(ValueError):
                TrustifyClient(base_url)

    def test_retries_retryable_get_and_applies_bearer_token(self):
        requests = []

        def handle(request):
            requests.append(request)
            if len(requests) == 1:
                return httpx.Response(
                    503, headers={"Retry-After": "0"}, request=request
                )
            return httpx.Response(
                200,
                json={
                    "version": "test",
                    "readOnly": False,
                    "exploitIntelligence": False,
                },
                request=request,
            )

        policy = RetryPolicy.for_idempotent_requests(1)
        mock_transport = httpx.MockTransport(handle)
        transport = _RetryTransport(mock_transport, mock_transport, policy)
        auth = _RequestBehavior(lambda: "test-token")
        with httpx.Client(transport=transport, auth=auth) as client:
            response = client.get("https://trustify.example/api/v3/sbom")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0].headers["Authorization"], "Bearer test-token")

    def test_generated_operation_uses_shared_client_behavior(self):
        requests = []

        def handle(request):
            requests.append(request)
            if len(requests) == 1:
                return httpx.Response(
                    503, headers={"Retry-After": "0"}, request=request
                )
            return httpx.Response(
                200,
                json={
                    "version": "test",
                    "readOnly": False,
                    "exploitIntelligence": False,
                },
                request=request,
            )

        client = TrustifyClient(
            "https://trustify.example/",
            bearer_token="test-token",
            retry_policy=RetryPolicy.for_idempotent_requests(1),
            httpx_args={"transport": httpx.MockTransport(handle)},
        )
        with client:
            result = info.sync(client=client.api)

        self.assertEqual(result.version, "test")
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0].headers["Authorization"], "Bearer test-token")

    def test_retries_connect_errors_but_not_post_requests(self):
        get_calls = []

        def fail_once(request):
            get_calls.append(request)
            if len(get_calls) == 1:
                raise httpx.ConnectError("connection failed", request=request)
            return httpx.Response(200, request=request)

        policy = RetryPolicy(1, 0, 0)
        mock_transport = httpx.MockTransport(fail_once)
        transport = _RetryTransport(mock_transport, mock_transport, policy)
        auth = _RequestBehavior(None)
        with httpx.Client(transport=transport, auth=auth) as client:
            response = client.get("https://trustify.example/api/v3/sbom")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(get_calls), 2)

        post_calls = []

        def unavailable(request):
            post_calls.append(request)
            return httpx.Response(503, request=request)

        mock_transport = httpx.MockTransport(unavailable)
        transport = _RetryTransport(mock_transport, mock_transport, policy)
        with httpx.Client(transport=transport, auth=auth) as client:
            response = client.post("https://trustify.example/api/v3/sbom")
        self.assertEqual(response.status_code, 503)
        self.assertEqual(len(post_calls), 1)

    def test_restores_importer_merge_patch_content_type(self):
        def handle(request):
            self.assertEqual(
                request.headers["Content-Type"], "application/merge-patch+json"
            )
            return httpx.Response(204, request=request)

        auth = _RequestBehavior(None)
        with httpx.Client(transport=httpx.MockTransport(handle), auth=auth) as client:
            response = client.patch(
                "https://trustify.example/api/v3/importer/example",
                json={"enabled": True},
            )
        self.assertEqual(response.status_code, 204)

    def test_restores_importer_plain_text_content_type(self):
        def handle(request):
            self.assertEqual(request.headers["Content-Type"], "text/plain")
            self.assertEqual(request.content, b"true")
            return httpx.Response(201, request=request)

        auth = _RequestBehavior(None)
        with httpx.Client(transport=httpx.MockTransport(handle), auth=auth) as client:
            response = client.put(
                "https://trustify.example/api/v3/importer/example/enabled",
                content=b"true",
                headers={"Content-Type": "application/octet-stream"},
            )
        self.assertEqual(response.status_code, 201)

    def test_collects_offset_pages(self):
        offsets = []

        def fetch_page(offset, limit):
            offsets.append((offset, limit))
            values = ["a", "b", "c", "d", "e"]
            return OffsetPage(values[offset : offset + limit], total=len(values))

        self.assertEqual(collect_offset_pages(2, fetch_page), ["a", "b", "c", "d", "e"])
        self.assertEqual(offsets, [(0, 2), (2, 2), (4, 2)])

    def test_collects_async_offset_pages_without_total(self):
        calls = 0

        async def fetch_page(offset, limit):
            nonlocal calls
            calls += 1
            return OffsetPage([1, 2, 3] if calls == 1 else [], total=None)

        items = asyncio.run(collect_offset_pages_async(3, fetch_page))
        self.assertEqual(items, [1, 2, 3])
        self.assertEqual(calls, 2)

    def test_rejects_invalid_page_sizes_and_totals(self):
        with self.assertRaises(ValueError):
            collect_offset_pages(0, lambda _offset, _limit: OffsetPage([]))
        with self.assertRaises(ValueError):
            OffsetPage([], total=-1)

    def test_async_token_provider(self):
        requests = []

        def handle(request):
            requests.append(request)
            if len(requests) == 1:
                return httpx.Response(
                    503, headers={"Retry-After": "0"}, request=request
                )
            return httpx.Response(
                200,
                json={
                    "version": "test",
                    "readOnly": False,
                    "exploitIntelligence": False,
                },
                request=request,
            )

        async def token_provider():
            return "async-token"

        async def run():
            mock_transport = httpx.MockTransport(handle)
            client = TrustifyClient(
                "https://trustify.example",
                token_provider=token_provider,
                retry_policy=RetryPolicy(1, 0, 0),
                httpx_args={"transport": mock_transport},
            )
            async with client:
                return await info.asyncio(client=client.api)

        response = asyncio.run(run())
        self.assertEqual(response.version, "test")
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0].headers["Authorization"], "Bearer async-token")


if __name__ == "__main__":
    unittest.main()
