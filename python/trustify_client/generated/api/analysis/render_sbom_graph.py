from http import HTTPStatus
from io import BytesIO
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.render_sbom_graph_ext import RenderSbomGraphExt
from ...types import File, Response


def _get_kwargs(
    sbom: str,
    ext: RenderSbomGraphExt,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/analysis/sbom/{sbom}/render.{ext}".format(
            sbom=quote(str(sbom), safe=""),
            ext=quote(str(ext), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 415:
        response_415 = cast(Any, None)
        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sbom: str,
    ext: RenderSbomGraphExt,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | File]:
    """Render an SBOM graph

    Args:
        sbom (str):
        ext (RenderSbomGraphExt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        sbom=sbom,
        ext=ext,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sbom: str,
    ext: RenderSbomGraphExt,
    *,
    client: AuthenticatedClient | Client,
) -> Any | File | None:
    """Render an SBOM graph

    Args:
        sbom (str):
        ext (RenderSbomGraphExt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return sync_detailed(
        sbom=sbom,
        ext=ext,
        client=client,
    ).parsed


async def asyncio_detailed(
    sbom: str,
    ext: RenderSbomGraphExt,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | File]:
    """Render an SBOM graph

    Args:
        sbom (str):
        ext (RenderSbomGraphExt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | File]
    """

    kwargs = _get_kwargs(
        sbom=sbom,
        ext=ext,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sbom: str,
    ext: RenderSbomGraphExt,
    *,
    client: AuthenticatedClient | Client,
) -> Any | File | None:
    """Render an SBOM graph

    Args:
        sbom (str):
        ext (RenderSbomGraphExt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | File
    """

    return (
        await asyncio_detailed(
            sbom=sbom,
            ext=ext,
            client=client,
        )
    ).parsed
