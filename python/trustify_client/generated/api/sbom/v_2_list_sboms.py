from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_results_sbom_summary_sbom_package import (
    PaginatedResultsSbomSummarySbomPackage,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["offset"] = offset

    params["limit"] = limit

    params["total"] = total

    json_group: list[str] | Unset = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/sbom",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResultsSbomSummarySbomPackage | None:
    if response.status_code == 200:
        response_200 = PaginatedResultsSbomSummarySbomPackage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedResultsSbomSummarySbomPackage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> Response[PaginatedResultsSbomSummarySbomPackage]:
    """List SBOMs

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        group (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultsSbomSummarySbomPackage]
    """

    kwargs = _get_kwargs(
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        group=group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> PaginatedResultsSbomSummarySbomPackage | None:
    """List SBOMs

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        group (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultsSbomSummarySbomPackage
    """

    return sync_detailed(
        client=client,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        group=group,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> Response[PaginatedResultsSbomSummarySbomPackage]:
    """List SBOMs

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        group (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultsSbomSummarySbomPackage]
    """

    kwargs = _get_kwargs(
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        group=group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    group: list[str] | Unset = UNSET,
) -> PaginatedResultsSbomSummarySbomPackage | None:
    """List SBOMs

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        group (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultsSbomSummarySbomPackage
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            sort=sort,
            offset=offset,
            limit=limit,
            total=total,
            group=group,
        )
    ).parsed
