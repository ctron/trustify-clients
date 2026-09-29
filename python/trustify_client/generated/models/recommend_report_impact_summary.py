from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecommendReportImpactSummary")


@_attrs_define
class RecommendReportImpactSummary:
    """High-level impact summary for a recommendation report.

    Attributes:
        addressable_packages (int): Count of distinct upstream packages that have a vendor recommendation.
        sboms_with_recommendations (int): Number of SBOMs containing at least one package with a vendor recommendation.
    """

    addressable_packages: int
    sboms_with_recommendations: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addressable_packages = self.addressable_packages

        sboms_with_recommendations = self.sboms_with_recommendations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addressable_packages": addressable_packages,
                "sboms_with_recommendations": sboms_with_recommendations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        addressable_packages = d.pop("addressable_packages")

        sboms_with_recommendations = d.pop("sboms_with_recommendations")

        recommend_report_impact_summary = cls(
            addressable_packages=addressable_packages,
            sboms_with_recommendations=sboms_with_recommendations,
        )

        recommend_report_impact_summary.additional_properties = d
        return recommend_report_impact_summary

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
