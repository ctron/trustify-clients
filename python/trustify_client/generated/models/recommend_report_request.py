from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecommendReportRequest")


@_attrs_define
class RecommendReportRequest:
    """Request body for the `POST /v3/recommend/report` endpoint.

    Attributes:
        sbom_ids (list[UUID]): SBOM IDs to include in the report.
    """

    sbom_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sbom_ids = []
        for sbom_ids_item_data in self.sbom_ids:
            sbom_ids_item = str(sbom_ids_item_data)
            sbom_ids.append(sbom_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sbom_ids": sbom_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sbom_ids = []
        _sbom_ids = d.pop("sbom_ids")
        for sbom_ids_item_data in _sbom_ids:
            sbom_ids_item = UUID(sbom_ids_item_data)

            sbom_ids.append(sbom_ids_item)

        recommend_report_request = cls(
            sbom_ids=sbom_ids,
        )

        recommend_report_request.additional_properties = d
        return recommend_report_request

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
