"""Helpers for offset-based Trustify API endpoints."""

from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class OffsetPage(Generic[T]):
    """Items and optional total count returned by one API page."""

    items: Sequence[T]
    total: Optional[int] = None

    def __post_init__(self) -> None:
        if self.total is not None and (
            not isinstance(self.total, int)
            or isinstance(self.total, bool)
            or not 0 <= self.total <= 2**64 - 1
        ):
            raise ValueError("total must be an unsigned 64-bit integer or None")


def collect_offset_pages(
    page_size: int,
    fetch_page: Callable[[int, int], OffsetPage[T]],
) -> list[T]:
    """Fetch pages until the known total or an unknown-total short page."""
    if (
        not isinstance(page_size, int)
        or isinstance(page_size, bool)
        or not 1 <= page_size <= 2**64 - 1
    ):
        raise ValueError("page_size must be a nonzero unsigned 64-bit integer")

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
    if (
        not isinstance(page_size, int)
        or isinstance(page_size, bool)
        or not 1 <= page_size <= 2**64 - 1
    ):
        raise ValueError("page_size must be a nonzero unsigned 64-bit integer")

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
