from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.importer_configuration_type_0 import ImporterConfigurationType0
from ...models.importer_configuration_type_1 import ImporterConfigurationType1
from ...models.importer_configuration_type_2 import ImporterConfigurationType2
from ...models.importer_configuration_type_3 import ImporterConfigurationType3
from ...models.importer_configuration_type_4 import ImporterConfigurationType4
from ...models.importer_configuration_type_5 import ImporterConfigurationType5
from ...models.importer_configuration_type_6 import ImporterConfigurationType6
from ...models.importer_configuration_type_7 import ImporterConfigurationType7
from ...models.importer_configuration_type_8 import ImporterConfigurationType8
from ...models.importer_configuration_type_9 import ImporterConfigurationType9
from ...models.importer_configuration_type_10 import ImporterConfigurationType10
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: ImporterConfigurationType0
    | ImporterConfigurationType1
    | ImporterConfigurationType10
    | ImporterConfigurationType2
    | ImporterConfigurationType3
    | ImporterConfigurationType4
    | ImporterConfigurationType5
    | ImporterConfigurationType6
    | ImporterConfigurationType7
    | ImporterConfigurationType8
    | ImporterConfigurationType9,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/importer/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    if (
        isinstance(body, ImporterConfigurationType0)
        or isinstance(body, ImporterConfigurationType1)
        or isinstance(body, ImporterConfigurationType2)
        or isinstance(body, ImporterConfigurationType3)
        or isinstance(body, ImporterConfigurationType4)
        or isinstance(body, ImporterConfigurationType5)
        or isinstance(body, ImporterConfigurationType6)
        or isinstance(body, ImporterConfigurationType7)
        or isinstance(body, ImporterConfigurationType8)
        or isinstance(body, ImporterConfigurationType9)
    ):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 201:
        return None

    if response.status_code == 409:
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
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImporterConfigurationType0
    | ImporterConfigurationType1
    | ImporterConfigurationType10
    | ImporterConfigurationType2
    | ImporterConfigurationType3
    | ImporterConfigurationType4
    | ImporterConfigurationType5
    | ImporterConfigurationType6
    | ImporterConfigurationType7
    | ImporterConfigurationType8
    | ImporterConfigurationType9,
) -> Response[Any]:
    """Create a new importer configuration

    Args:
        name (str):
        body (ImporterConfigurationType0 | ImporterConfigurationType1 |
            ImporterConfigurationType10 | ImporterConfigurationType2 | ImporterConfigurationType3 |
            ImporterConfigurationType4 | ImporterConfigurationType5 | ImporterConfigurationType6 |
            ImporterConfigurationType7 | ImporterConfigurationType8 | ImporterConfigurationType9):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImporterConfigurationType0
    | ImporterConfigurationType1
    | ImporterConfigurationType10
    | ImporterConfigurationType2
    | ImporterConfigurationType3
    | ImporterConfigurationType4
    | ImporterConfigurationType5
    | ImporterConfigurationType6
    | ImporterConfigurationType7
    | ImporterConfigurationType8
    | ImporterConfigurationType9,
) -> Response[Any]:
    """Create a new importer configuration

    Args:
        name (str):
        body (ImporterConfigurationType0 | ImporterConfigurationType1 |
            ImporterConfigurationType10 | ImporterConfigurationType2 | ImporterConfigurationType3 |
            ImporterConfigurationType4 | ImporterConfigurationType5 | ImporterConfigurationType6 |
            ImporterConfigurationType7 | ImporterConfigurationType8 | ImporterConfigurationType9):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
