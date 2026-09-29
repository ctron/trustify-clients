from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.recommend_report_request import RecommendReportRequest
from ...models.recommend_report_response import RecommendReportResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RecommendReportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/recommend/report",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RecommendReportResponse | None:
    if response.status_code == 200:
        response_200 = RecommendReportResponse.from_dict(response.json())

        return response_200

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RecommendReportResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendReportRequest,
) -> Response[Any | RecommendReportResponse]:
    """Generate an aggregated vendor recommendation report for a set of SBOMs.

    Args:
        body (RecommendReportRequest): Request body for the `POST /v3/recommend/report` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecommendReportResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendReportRequest,
) -> Any | RecommendReportResponse | None:
    """Generate an aggregated vendor recommendation report for a set of SBOMs.

    Args:
        body (RecommendReportRequest): Request body for the `POST /v3/recommend/report` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecommendReportResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendReportRequest,
) -> Response[Any | RecommendReportResponse]:
    """Generate an aggregated vendor recommendation report for a set of SBOMs.

    Args:
        body (RecommendReportRequest): Request body for the `POST /v3/recommend/report` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecommendReportResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendReportRequest,
) -> Any | RecommendReportResponse | None:
    """Generate an aggregated vendor recommendation report for a set of SBOMs.

    Args:
        body (RecommendReportRequest): Request body for the `POST /v3/recommend/report` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecommendReportResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
