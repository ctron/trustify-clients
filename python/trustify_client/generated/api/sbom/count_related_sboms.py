from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_reference_query import ExternalReferenceQuery
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: list[ExternalReferenceQuery],
    purl: None | str,
    cpe: None | str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_purl: None | str
    json_purl = purl
    params["purl"] = json_purl

    json_cpe: None | str
    json_cpe = cpe
    params["cpe"] = json_cpe

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/sbom/count-by-package",
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[int] | None:
    if response.status_code == 200:
        response_200 = cast(list[int], response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[int]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[ExternalReferenceQuery],
    purl: None | str,
    cpe: None | str,
) -> Response[list[int]]:
    """Count all SBOMs containing the provided packages.

     The packages can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        purl (None | str):
        cpe (None | str):
        body (list[ExternalReferenceQuery]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[int]]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: list[ExternalReferenceQuery],
    purl: None | str,
    cpe: None | str,
) -> list[int] | None:
    """Count all SBOMs containing the provided packages.

     The packages can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        purl (None | str):
        cpe (None | str):
        body (list[ExternalReferenceQuery]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[int]
    """

    return sync_detailed(
        client=client,
        body=body,
        purl=purl,
        cpe=cpe,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[ExternalReferenceQuery],
    purl: None | str,
    cpe: None | str,
) -> Response[list[int]]:
    """Count all SBOMs containing the provided packages.

     The packages can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        purl (None | str):
        cpe (None | str):
        body (list[ExternalReferenceQuery]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[int]]
    """

    kwargs = _get_kwargs(
        body=body,
        purl=purl,
        cpe=cpe,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[ExternalReferenceQuery],
    purl: None | str,
    cpe: None | str,
) -> list[int] | None:
    """Count all SBOMs containing the provided packages.

     The packages can be provided either via a PURL or using the ID of a package as returned by
    other APIs, but not both.

    Args:
        purl (None | str):
        cpe (None | str):
        body (list[ExternalReferenceQuery]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[int]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            purl=purl,
            cpe=cpe,
        )
    ).parsed
