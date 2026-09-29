from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_related_packages_which import ListRelatedPackagesWhich
from ...models.paginated_results_sbom_package_relation_sbom_package import (
    PaginatedResultsSbomPackageRelationSbomPackage,
)
from ...models.relationship import Relationship
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    reference: None | str | Unset = UNSET,
    which: ListRelatedPackagesWhich | Unset = UNSET,
    relationship: None | Relationship | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_reference: None | str | Unset
    if isinstance(reference, Unset):
        json_reference = UNSET
    else:
        json_reference = reference
    params["reference"] = json_reference

    json_which: str | Unset = UNSET
    if not isinstance(which, Unset):
        json_which = which.value

    params["which"] = json_which

    json_relationship: None | str | Unset
    if isinstance(relationship, Unset):
        json_relationship = UNSET
    elif isinstance(relationship, Relationship):
        json_relationship = relationship.value
    else:
        json_relationship = relationship
    params["relationship"] = json_relationship

    params["q"] = q

    params["sort"] = sort

    params["offset"] = offset

    params["limit"] = limit

    params["total"] = total

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/sbom/{id}/related".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PaginatedResultsSbomPackageRelationSbomPackage | None:
    if response.status_code == 200:
        response_200 = PaginatedResultsSbomPackageRelationSbomPackage.from_dict(
            response.json()
        )

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
) -> Response[Any | PaginatedResultsSbomPackageRelationSbomPackage]:
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
    reference: None | str | Unset = UNSET,
    which: ListRelatedPackagesWhich | Unset = UNSET,
    relationship: None | Relationship | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Response[Any | PaginatedResultsSbomPackageRelationSbomPackage]:
    """Search for related packages in an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        reference (None | str | Unset):
        which (ListRelatedPackagesWhich | Unset):
        relationship (None | Relationship | Unset):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedResultsSbomPackageRelationSbomPackage]
    """

    kwargs = _get_kwargs(
        id=id,
        reference=reference,
        which=which,
        relationship=relationship,
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
    reference: None | str | Unset = UNSET,
    which: ListRelatedPackagesWhich | Unset = UNSET,
    relationship: None | Relationship | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Any | PaginatedResultsSbomPackageRelationSbomPackage | None:
    """Search for related packages in an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        reference (None | str | Unset):
        which (ListRelatedPackagesWhich | Unset):
        relationship (None | Relationship | Unset):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedResultsSbomPackageRelationSbomPackage
    """

    return sync_detailed(
        id=id,
        client=client,
        reference=reference,
        which=which,
        relationship=relationship,
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
    reference: None | str | Unset = UNSET,
    which: ListRelatedPackagesWhich | Unset = UNSET,
    relationship: None | Relationship | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Response[Any | PaginatedResultsSbomPackageRelationSbomPackage]:
    """Search for related packages in an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        reference (None | str | Unset):
        which (ListRelatedPackagesWhich | Unset):
        relationship (None | Relationship | Unset):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedResultsSbomPackageRelationSbomPackage]
    """

    kwargs = _get_kwargs(
        id=id,
        reference=reference,
        which=which,
        relationship=relationship,
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
    reference: None | str | Unset = UNSET,
    which: ListRelatedPackagesWhich | Unset = UNSET,
    relationship: None | Relationship | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    total: bool | Unset = UNSET,
) -> Any | PaginatedResultsSbomPackageRelationSbomPackage | None:
    """Search for related packages in an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        reference (None | str | Unset):
        which (ListRelatedPackagesWhich | Unset):
        relationship (None | Relationship | Unset):
        q (str | Unset):
        sort (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        total (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedResultsSbomPackageRelationSbomPackage
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            reference=reference,
            which=which,
            relationship=relationship,
            q=q,
            sort=sort,
            offset=offset,
            limit=limit,
            total=total,
        )
    ).parsed
