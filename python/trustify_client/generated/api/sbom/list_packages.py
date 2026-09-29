from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_results_sbom_package import PaginatedResultsSbomPackage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["offset"] = offset

    params["limit"] = limit

    params["total"] = total

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/sbom/{id}/packages".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PaginatedResultsSbomPackage | None:
    if response.status_code == 200:
        response_200 = PaginatedResultsSbomPackage.from_dict(response.json())

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
) -> Response[Any | PaginatedResultsSbomPackage]:
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
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Response[Any | PaginatedResultsSbomPackage]:
    """Search for packages of an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedResultsSbomPackage]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Any | PaginatedResultsSbomPackage | None:
    """Search for packages of an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedResultsSbomPackage
    """

    return sync_detailed(
        id=id,
        client=client,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Response[Any | PaginatedResultsSbomPackage]:
    """Search for packages of an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedResultsSbomPackage]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Any | PaginatedResultsSbomPackage | None:
    """Search for packages of an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedResultsSbomPackage
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            q=q,
            sort=sort,
            offset=offset,
            limit=limit,
            total=total,
        )
    ).parsed
