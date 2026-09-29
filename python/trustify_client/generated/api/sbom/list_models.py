from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_results_sbom_model import PaginatedResultsSbomModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    counts: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["offset"] = offset

    params["limit"] = limit

    params["total"] = total

    params["counts"] = counts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/sbom/{id}/models".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResultsSbomModel | None:
    if response.status_code == 200:
        response_200 = PaginatedResultsSbomModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedResultsSbomModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    counts: bool | Unset = UNSET,
) -> Response[PaginatedResultsSbomModel]:
    """Search for AI models associated with an SBOM

    Args:
        id (UUID):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        counts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultsSbomModel]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        counts=counts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    counts: bool | Unset = UNSET,
) -> PaginatedResultsSbomModel | None:
    """Search for AI models associated with an SBOM

    Args:
        id (UUID):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        counts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultsSbomModel
    """

    return sync_detailed(
        id=id,
        client=client,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        counts=counts,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    counts: bool | Unset = UNSET,
) -> Response[PaginatedResultsSbomModel]:
    """Search for AI models associated with an SBOM

    Args:
        id (UUID):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        counts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultsSbomModel]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        counts=counts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    counts: bool | Unset = UNSET,
) -> PaginatedResultsSbomModel | None:
    """Search for AI models associated with an SBOM

    Args:
        id (UUID):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        counts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultsSbomModel
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
            counts=counts,
        )
    ).parsed
