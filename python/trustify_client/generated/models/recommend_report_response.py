from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recommend_report_impact_summary import RecommendReportImpactSummary
    from ..models.recommend_report_package import RecommendReportPackage
    from ..models.recommend_report_sbom import RecommendReportSbom


T = TypeVar("T", bound="RecommendReportResponse")


@_attrs_define
class RecommendReportResponse:
    """Aggregated recommendation report for a set of SBOMs.

    Attributes:
        impact_summary (RecommendReportImpactSummary): High-level impact summary for a recommendation report.
        packages (list[RecommendReportPackage]): Deduplicated list of packages with vendor recommendations.
        sboms (list[RecommendReportSbom]): Per-SBOM breakdown.
    """

    impact_summary: RecommendReportImpactSummary
    packages: list[RecommendReportPackage]
    sboms: list[RecommendReportSbom]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        impact_summary = self.impact_summary.to_dict()

        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)

        sboms = []
        for sboms_item_data in self.sboms:
            sboms_item = sboms_item_data.to_dict()
            sboms.append(sboms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "impact_summary": impact_summary,
                "packages": packages,
                "sboms": sboms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.recommend_report_impact_summary import (
            RecommendReportImpactSummary,
        )
        from ..models.recommend_report_package import (
            RecommendReportPackage,
        )
        from ..models.recommend_report_sbom import RecommendReportSbom

        d = dict(src_dict)
        impact_summary = RecommendReportImpactSummary.from_dict(d.pop("impact_summary"))

        packages = []
        _packages = d.pop("packages")
        for packages_item_data in _packages:
            packages_item = RecommendReportPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        sboms = []
        _sboms = d.pop("sboms")
        for sboms_item_data in _sboms:
            sboms_item = RecommendReportSbom.from_dict(sboms_item_data)

            sboms.append(sboms_item)

        recommend_report_response = cls(
            impact_summary=impact_summary,
            packages=packages,
            sboms=sboms,
        )

        recommend_report_response.additional_properties = d
        return recommend_report_response

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
