from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analysis_status import AnalysisStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    details: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["details"] = details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/analysis/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalysisStatus | Any | None:
    if response.status_code == 200:
        response_200 = AnalysisStatus.from_dict(response.json())

        return response_200

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
) -> Response[AnalysisStatus | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    details: bool | Unset = UNSET,
) -> Response[AnalysisStatus | Any]:
    """Get the status of the analysis service.

    Args:
        details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisStatus | Any]
    """

    kwargs = _get_kwargs(
        details=details,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    details: bool | Unset = UNSET,
) -> AnalysisStatus | Any | None:
    """Get the status of the analysis service.

    Args:
        details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisStatus | Any
    """

    return sync_detailed(
        client=client,
        details=details,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    details: bool | Unset = UNSET,
) -> Response[AnalysisStatus | Any]:
    """Get the status of the analysis service.

    Args:
        details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalysisStatus | Any]
    """

    kwargs = _get_kwargs(
        details=details,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    details: bool | Unset = UNSET,
) -> AnalysisStatus | Any | None:
    """Get the status of the analysis service.

    Args:
        details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalysisStatus | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            details=details,
        )
    ).parsed
