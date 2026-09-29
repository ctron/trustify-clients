from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cache_status_entry import CacheStatusEntry


T = TypeVar("T", bound="CacheStatusDetails")


@_attrs_define
class CacheStatusDetails:
    """
    Attributes:
        capacity (int): The maximum number of bytes the cache will hold
        entries (list[CacheStatusEntry]): Entries in the cache
        free (int): The number of bytes which are still free
        usage (float): The percentage the cache is filled (0..1)
    """

    capacity: int
    entries: list[CacheStatusEntry]
    free: int
    usage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacity = self.capacity

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        free = self.free

        usage = self.usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capacity": capacity,
                "entries": entries,
                "free": free,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cache_status_entry import CacheStatusEntry

        d = dict(src_dict)
        capacity = d.pop("capacity")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = CacheStatusEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        free = d.pop("free")

        usage = d.pop("usage")

        cache_status_details = cls(
            capacity=capacity,
            entries=entries,
            free=free,
            usage=usage,
        )

        cache_status_details.additional_properties = d
        return cache_status_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
