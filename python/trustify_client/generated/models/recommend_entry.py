from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vulnerability_status import VulnerabilityStatus


T = TypeVar("T", bound="RecommendEntry")


@_attrs_define
class RecommendEntry:
    """
    Attributes:
        package (str):
        vulnerabilities (list[VulnerabilityStatus]):
    """

    package: str
    vulnerabilities: list[VulnerabilityStatus]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package = self.package

        vulnerabilities = []
        for vulnerabilities_item_data in self.vulnerabilities:
            vulnerabilities_item = vulnerabilities_item_data.to_dict()
            vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
                "vulnerabilities": vulnerabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vulnerability_status import VulnerabilityStatus

        d = dict(src_dict)
        package = d.pop("package")

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities")
        for vulnerabilities_item_data in _vulnerabilities:
            vulnerabilities_item = VulnerabilityStatus.from_dict(
                vulnerabilities_item_data
            )

            vulnerabilities.append(vulnerabilities_item)

        recommend_entry = cls(
            package=package,
            vulnerabilities=vulnerabilities,
        )

        recommend_entry.additional_properties = d
        return recommend_entry

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
