from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecommendReportSbom")


@_attrs_define
class RecommendReportSbom:
    """Per-SBOM summary in a recommendation report.

    Attributes:
        addressable_packages (int): Number of packages in this SBOM that have a vendor recommendation.
        id (UUID): SBOM identifier.
        name (str): SBOM document name.
        vulnerability_count (int): Number of distinct vulnerabilities across addressable packages in this SBOM.
    """

    addressable_packages: int
    id: UUID
    name: str
    vulnerability_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addressable_packages = self.addressable_packages

        id = str(self.id)

        name = self.name

        vulnerability_count = self.vulnerability_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addressable_packages": addressable_packages,
                "id": id,
                "name": name,
                "vulnerability_count": vulnerability_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        addressable_packages = d.pop("addressable_packages")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        vulnerability_count = d.pop("vulnerability_count")

        recommend_report_sbom = cls(
            addressable_packages=addressable_packages,
            id=id,
            name=name,
            vulnerability_count=vulnerability_count,
        )

        recommend_report_sbom.additional_properties = d
        return recommend_report_sbom

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
