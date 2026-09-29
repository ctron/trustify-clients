from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_list_result import GroupListResult
from ...models.list_sbom_groups_parents import ListSbomGroupsParents
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    totals: bool | Unset = UNSET,
    parents: ListSbomGroupsParents | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["totals"] = totals

    json_parents: str | Unset = UNSET
    if not isinstance(parents, Unset):
        json_parents = parents.value

    params["parents"] = json_parents

    params["offset"] = offset

    params["limit"] = limit

    params["total"] = total

    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/group/sbom",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GroupListResult | None:
    if response.status_code == 200:
        response_200 = GroupListResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GroupListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    totals: bool | Unset = UNSET,
    parents: ListSbomGroupsParents | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[Any | GroupListResult]:
    """List SBOM groups

    Args:
        totals (bool | Unset):
        parents (ListSbomGroupsParents | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupListResult]
    """

    kwargs = _get_kwargs(
        totals=totals,
        parents=parents,
        offset=offset,
        limit=limit,
        total=total,
        q=q,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    totals: bool | Unset = UNSET,
    parents: ListSbomGroupsParents | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Any | GroupListResult | None:
    """List SBOM groups

    Args:
        totals (bool | Unset):
        parents (ListSbomGroupsParents | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupListResult
    """

    return sync_detailed(
        client=client,
        totals=totals,
        parents=parents,
        offset=offset,
        limit=limit,
        total=total,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    totals: bool | Unset = UNSET,
    parents: ListSbomGroupsParents | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[Any | GroupListResult]:
    """List SBOM groups

    Args:
        totals (bool | Unset):
        parents (ListSbomGroupsParents | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupListResult]
    """

    kwargs = _get_kwargs(
        totals=totals,
        parents=parents,
        offset=offset,
        limit=limit,
        total=total,
        q=q,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    totals: bool | Unset = UNSET,
    parents: ListSbomGroupsParents | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Any | GroupListResult | None:
    """List SBOM groups

    Args:
        totals (bool | Unset):
        parents (ListSbomGroupsParents | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupListResult
    """

    return (
        await asyncio_detailed(
            client=client,
            totals=totals,
            parents=parents,
            offset=offset,
            limit=limit,
            total=total,
            q=q,
            sort=sort,
        )
    ).parsed
