from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendReportPackage")


@_attrs_define
class RecommendReportPackage:
    """A deduplicated package entry in a recommendation report.

    Attributes:
        found_in (list[UUID]): IDs of the SBOMs that contain this upstream package.
        purl (str): The upstream package PURL (type+namespace+name+version, no qualifiers).
        recommended_purl (str): The recommended vendor-rebuilt PURL.
        vulnerabilities (list[str]): CVE identifiers associated with this recommendation.
        advisory_id (None | str | Unset): Advisory ID that provides provenance for the recommendation.
    """

    found_in: list[UUID]
    purl: str
    recommended_purl: str
    vulnerabilities: list[str]
    advisory_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        found_in = []
        for found_in_item_data in self.found_in:
            found_in_item = str(found_in_item_data)
            found_in.append(found_in_item)

        purl = self.purl

        recommended_purl = self.recommended_purl

        vulnerabilities = self.vulnerabilities

        advisory_id: None | str | Unset
        if isinstance(self.advisory_id, Unset):
            advisory_id = UNSET
        else:
            advisory_id = self.advisory_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "found_in": found_in,
                "purl": purl,
                "recommended_purl": recommended_purl,
                "vulnerabilities": vulnerabilities,
            }
        )
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        found_in = []
        _found_in = d.pop("found_in")
        for found_in_item_data in _found_in:
            found_in_item = UUID(found_in_item_data)

            found_in.append(found_in_item)

        purl = d.pop("purl")

        recommended_purl = d.pop("recommended_purl")

        vulnerabilities = cast(list[str], d.pop("vulnerabilities"))

        def _parse_advisory_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        advisory_id = _parse_advisory_id(d.pop("advisory_id", UNSET))

        recommend_report_package = cls(
            found_in=found_in,
            purl=purl,
            recommended_purl=recommended_purl,
            vulnerabilities=vulnerabilities,
            advisory_id=advisory_id,
        )

        recommend_report_package.additional_properties = d
        return recommend_report_package

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
