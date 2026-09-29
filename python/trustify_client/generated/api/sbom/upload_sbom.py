from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ingest_result import IngestResult
from ...models.labels import Labels
from ...models.upload_sbom_cache import UploadSbomCache
from ...models.upload_sbom_format import UploadSbomFormat
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    body: File,
    labels: Labels | Unset = UNSET,
    format_: UploadSbomFormat | Unset = UNSET,
    cache: UploadSbomCache | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_labels: dict[str, Any] | Unset = UNSET
    if not isinstance(labels, Unset):
        json_labels = labels.to_dict()
    if not isinstance(json_labels, Unset):
        params.update(json_labels)

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_cache: str | Unset = UNSET
    if not isinstance(cache, Unset):
        json_cache = cache.value

    params["cache"] = json_cache

    json_group: list[str] | Unset = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/sbom",
        "params": params,
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | IngestResult | None:
    if response.status_code == 201:
        response_201 = IngestResult.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | IngestResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    labels: Labels | Unset = UNSET,
    format_: UploadSbomFormat | Unset = UNSET,
    cache: UploadSbomCache | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> Response[Any | IngestResult]:
    """Upload a new SBOM

    Args:
        labels (Labels | Unset):
        format_ (UploadSbomFormat | Unset):
        cache (UploadSbomCache | Unset):
        group (list[str] | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IngestResult]
    """

    kwargs = _get_kwargs(
        body=body,
        labels=labels,
        format_=format_,
        cache=cache,
        group=group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    labels: Labels | Unset = UNSET,
    format_: UploadSbomFormat | Unset = UNSET,
    cache: UploadSbomCache | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> Any | IngestResult | None:
    """Upload a new SBOM

    Args:
        labels (Labels | Unset):
        format_ (UploadSbomFormat | Unset):
        cache (UploadSbomCache | Unset):
        group (list[str] | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IngestResult
    """

    return sync_detailed(
        client=client,
        body=body,
        labels=labels,
        format_=format_,
        cache=cache,
        group=group,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    labels: Labels | Unset = UNSET,
    format_: UploadSbomFormat | Unset = UNSET,
    cache: UploadSbomCache | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> Response[Any | IngestResult]:
    """Upload a new SBOM

    Args:
        labels (Labels | Unset):
        format_ (UploadSbomFormat | Unset):
        cache (UploadSbomCache | Unset):
        group (list[str] | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IngestResult]
    """

    kwargs = _get_kwargs(
        body=body,
        labels=labels,
        format_=format_,
        cache=cache,
        group=group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    labels: Labels | Unset = UNSET,
    format_: UploadSbomFormat | Unset = UNSET,
    cache: UploadSbomCache | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> Any | IngestResult | None:
    """Upload a new SBOM

    Args:
        labels (Labels | Unset):
        format_ (UploadSbomFormat | Unset):
        cache (UploadSbomCache | Unset):
        group (list[str] | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IngestResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            labels=labels,
            format_=format_,
            cache=cache,
            group=group,
        )
    ).parsed
