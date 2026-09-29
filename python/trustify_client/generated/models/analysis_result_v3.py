from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analysis_details_v3 import AnalysisDetailsV3


T = TypeVar("T", bound="AnalysisResultV3")


@_attrs_define
class AnalysisResultV3:
    """
    Attributes:
        details (list[AnalysisDetailsV3]):
        warnings (list[str]):
    """

    details: list[AnalysisDetailsV3]
    warnings: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = []
        for details_item_data in self.details:
            details_item = details_item_data.to_dict()
            details.append(details_item)

        warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "details": details,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analysis_details_v3 import AnalysisDetailsV3

        d = dict(src_dict)
        details = []
        _details = d.pop("details")
        for details_item_data in _details:
            details_item = AnalysisDetailsV3.from_dict(details_item_data)

            details.append(details_item)

        warnings = cast(list[str], d.pop("warnings"))

        analysis_result_v3 = cls(
            details=details,
            warnings=warnings,
        )

        analysis_result_v3.additional_properties = d
        return analysis_result_v3

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
