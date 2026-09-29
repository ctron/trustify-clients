from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_purl_deprecated import GetPurlDeprecated
from ...models.purl_details import PurlDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    deprecated: GetPurlDeprecated | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_deprecated: str | Unset = UNSET
    if not isinstance(deprecated, Unset):
        json_deprecated = deprecated.value

    params["deprecated"] = json_deprecated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/purl/{key}".format(
            key=quote(str(key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PurlDetails | None:
    if response.status_code == 200:
        response_200 = PurlDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PurlDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    deprecated: GetPurlDeprecated | Unset = UNSET,
) -> Response[PurlDetails]:
    """Retrieve details of a fully-qualified pURL

    Args:
        key (str):
        deprecated (GetPurlDeprecated | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurlDetails]
    """

    kwargs = _get_kwargs(
        key=key,
        deprecated=deprecated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    deprecated: GetPurlDeprecated | Unset = UNSET,
) -> PurlDetails | None:
    """Retrieve details of a fully-qualified pURL

    Args:
        key (str):
        deprecated (GetPurlDeprecated | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurlDetails
    """

    return sync_detailed(
        key=key,
        client=client,
        deprecated=deprecated,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    deprecated: GetPurlDeprecated | Unset = UNSET,
) -> Response[PurlDetails]:
    """Retrieve details of a fully-qualified pURL

    Args:
        key (str):
        deprecated (GetPurlDeprecated | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurlDetails]
    """

    kwargs = _get_kwargs(
        key=key,
        deprecated=deprecated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    deprecated: GetPurlDeprecated | Unset = UNSET,
) -> PurlDetails | None:
    """Retrieve details of a fully-qualified pURL

    Args:
        key (str):
        deprecated (GetPurlDeprecated | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurlDetails
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            deprecated=deprecated,
        )
    ).parsed
