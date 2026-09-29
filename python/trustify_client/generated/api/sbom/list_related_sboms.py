from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_results_sbom_summary import PaginatedResultsSbomSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    purl: None | str | Unset = UNSET,
    cpe: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["offset"] = offset

    params["limit"] = limit

    params["total"] = total

    json_purl: None | str | Unset
    if isinstance(purl, Unset):
        json_purl = UNSET
    else:
        json_purl = purl
    params["purl"] = json_purl

    json_cpe: None | str | Unset
    if isinstance(cpe, Unset):
        json_cpe = UNSET
    else:
        json_cpe = cpe
    params["cpe"] = json_cpe

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/sbom/by-package",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResultsSbomSummary | None:
    if response.status_code == 200:
        response_200 = PaginatedResultsSbomSummary.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedResultsSbomSummary]:
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
    purl: None | str | Unset = UNSET,
    cpe: None | str | Unset = UNSET,
) -> Response[PaginatedResultsSbomSummary]:
    """Find all SBOMs containing the provided package.

     The package can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        purl (None | str | Unset):
        cpe (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultsSbomSummary]
    """

    kwargs = _get_kwargs(
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        purl=purl,
        cpe=cpe,
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
    purl: None | str | Unset = UNSET,
    cpe: None | str | Unset = UNSET,
) -> PaginatedResultsSbomSummary | None:
    """Find all SBOMs containing the provided package.

     The package can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        purl (None | str | Unset):
        cpe (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultsSbomSummary
    """

    return sync_detailed(
        client=client,
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        purl=purl,
        cpe=cpe,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
    purl: None | str | Unset = UNSET,
    cpe: None | str | Unset = UNSET,
) -> Response[PaginatedResultsSbomSummary]:
    """Find all SBOMs containing the provided package.

     The package can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        purl (None | str | Unset):
        cpe (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultsSbomSummary]
    """

    kwargs = _get_kwargs(
        q=q,
        sort=sort,
        offset=offset,
        limit=limit,
        total=total,
        purl=purl,
        cpe=cpe,
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
    purl: None | str | Unset = UNSET,
    cpe: None | str | Unset = UNSET,
) -> PaginatedResultsSbomSummary | None:
    """Find all SBOMs containing the provided package.

     The package can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):
        purl (None | str | Unset):
        cpe (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultsSbomSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            sort=sort,
            offset=offset,
            limit=limit,
            total=total,
            purl=purl,
            cpe=cpe,
        )
    ).parsed
