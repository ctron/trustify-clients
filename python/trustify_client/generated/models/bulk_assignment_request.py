from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkAssignmentRequest")


@_attrs_define
class BulkAssignmentRequest:
    """Request to assign multiple SBOMs to the same set of groups.

    Attributes:
        group_ids (list[str]): The group IDs to assign to each SBOM (replaces existing assignments).
        sbom_ids (list[str]): The IDs of the SBOMs to update.
    """

    group_ids: list[str]
    sbom_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_ids = self.group_ids

        sbom_ids = self.sbom_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_ids": group_ids,
                "sbom_ids": sbom_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        group_ids = cast(list[str], d.pop("group_ids"))

        sbom_ids = cast(list[str], d.pop("sbom_ids"))

        bulk_assignment_request = cls(
            group_ids=group_ids,
            sbom_ids=sbom_ids,
        )

        bulk_assignment_request.additional_properties = d
        return bulk_assignment_request

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
