from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sbom_summary import SbomSummary
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/sbom/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SbomSummary | None:
    if response.status_code == 200:
        response_200 = SbomSummary.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SbomSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SbomSummary]:
    """Get information about an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SbomSummary]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SbomSummary | None:
    """Get information about an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SbomSummary
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SbomSummary]:
    """Get information about an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SbomSummary]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SbomSummary | None:
    """Get information about an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SbomSummary
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
