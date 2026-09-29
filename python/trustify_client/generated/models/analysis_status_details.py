from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cache_status_details import CacheStatusDetails


T = TypeVar("T", bound="AnalysisStatusDetails")


@_attrs_define
class AnalysisStatusDetails:
    """
    Attributes:
        cache (CacheStatusDetails):
    """

    cache: CacheStatusDetails
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache = self.cache.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cache": cache,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cache_status_details import CacheStatusDetails

        d = dict(src_dict)
        cache = CacheStatusDetails.from_dict(d.pop("cache"))

        analysis_status_details = cls(
            cache=cache,
        )

        analysis_status_details.additional_properties = d
        return analysis_status_details

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
