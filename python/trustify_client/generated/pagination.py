"""Helpers for offset-based Trustify API endpoints."""

from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class OffsetPage(Generic[T]):
    """Items and optional total count returned by one API page."""

    items: Sequence[T]
    total: int | None = None


def collect_offset_pages(
    page_size: int,
    fetch_page: Callable[[int, int], OffsetPage[T]],
) -> list[T]:
    """Fetch pages until the known total or an unknown-total short page."""
    if page_size <= 0:
        raise ValueError("page_size must be greater than zero")

    offset = 0
    items: list[T] = []
    while True:
        page = fetch_page(offset, page_size)
        count = len(page.items)
        next_offset = offset + count
        done = (
            next_offset >= page.total if page.total is not None else count < page_size
        )
        items.extend(page.items)
        if count == 0 or done:
            return items
        offset = next_offset


async def collect_offset_pages_async(
    page_size: int,
    fetch_page: Callable[[int, int], Awaitable[OffsetPage[T]]],
) -> list[T]:
    """Asynchronously fetch pages until the known total or a short page."""
    if page_size <= 0:
        raise ValueError("page_size must be greater than zero")

    offset = 0
    items: list[T] = []
    while True:
        page = await fetch_page(offset, page_size)
        count = len(page.items)
        next_offset = offset + count
        done = (
            next_offset >= page.total if page.total is not None else count < page_size
        )
        items.extend(page.items)
        if count == 0 or done:
            return items
        offset = next_offset
