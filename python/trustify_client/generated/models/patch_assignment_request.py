from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchAssignmentRequest")


@_attrs_define
class PatchAssignmentRequest:
    """Request to partially update SBOM group assignments (add and/or remove).

    Applies cartesian product semantics: each SBOM in `sbom_ids` gets all `add` groups
    added and all `remove` groups removed, while preserving other existing assignments.

        Attributes:
            sbom_ids (list[str]): The IDs of the SBOMs to update.
            add (list[str] | Unset): Group IDs to add to each SBOM's assignments.
            remove (list[str] | Unset): Group IDs to remove from each SBOM's assignments.
    """

    sbom_ids: list[str]
    add: list[str] | Unset = UNSET
    remove: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sbom_ids = self.sbom_ids

        add: list[str] | Unset = UNSET
        if not isinstance(self.add, Unset):
            add = self.add

        remove: list[str] | Unset = UNSET
        if not isinstance(self.remove, Unset):
            remove = self.remove

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sbom_ids": sbom_ids,
            }
        )
        if add is not UNSET:
            field_dict["add"] = add
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sbom_ids = cast(list[str], d.pop("sbom_ids"))

        add = cast(list[str], d.pop("add", UNSET))

        remove = cast(list[str], d.pop("remove", UNSET))

        patch_assignment_request = cls(
            sbom_ids=sbom_ids,
            add=add,
            remove=remove,
        )

        patch_assignment_request.additional_properties = d
        return patch_assignment_request

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
