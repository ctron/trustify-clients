from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_information import ErrorInformation
from ...models.extract_result import ExtractResult
from ...models.format_ import Format
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    body: File,
    format_: Format | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/ui/extract-sbom-purls",
        "params": params,
    }

    _kwargs["json"] = body.to_tuple()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorInformation | ExtractResult | None:
    if response.status_code == 200:
        response_200 = ExtractResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorInformation.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorInformation | ExtractResult]:
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
    format_: Format | Unset = UNSET,
) -> Response[ErrorInformation | ExtractResult]:
    """Extract PURLs from an SBOM provided in the request

    Args:
        format_ (Format | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorInformation | ExtractResult]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    format_: Format | Unset = UNSET,
) -> ErrorInformation | ExtractResult | None:
    """Extract PURLs from an SBOM provided in the request

    Args:
        format_ (Format | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorInformation | ExtractResult
    """

    return sync_detailed(
        client=client,
        body=body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    format_: Format | Unset = UNSET,
) -> Response[ErrorInformation | ExtractResult]:
    """Extract PURLs from an SBOM provided in the request

    Args:
        format_ (Format | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorInformation | ExtractResult]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    format_: Format | Unset = UNSET,
) -> ErrorInformation | ExtractResult | None:
    """Extract PURLs from an SBOM provided in the request

    Args:
        format_ (Format | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorInformation | ExtractResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            format_=format_,
        )
    ).parsed
