from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update import Update
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Update,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v3/sbom/{id}/label".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
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
    body: Update,
) -> Response[Any]:
    """Modify existing labels of an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        body (Update): An update set for labels.

            This is a key/value set, where the value can be a string for setting that value, or `null`
            for removing the label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Update,
) -> Response[Any]:
    """Modify existing labels of an SBOM

    Args:
        id (str): Identifier to a document, prefixed with the ID type.

            Either an internal ID of the document with the `urn:uuid:` scheme. Or using a digest, with
            the digest prefix. For example, `sha256:`.
        body (Update): An update set for labels.

            This is a key/value set, where the value can be a string for setting that value, or `null`
            for removing the label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
