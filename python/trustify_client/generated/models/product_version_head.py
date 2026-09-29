from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductVersionHead")


@_attrs_define
class ProductVersionHead:
    """
    Attributes:
        id (str):
        version (str):
        sbom_id (str | Unset):
    """

    id: str
    version: str
    sbom_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version = self.version

        sbom_id = self.sbom_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
            }
        )
        if sbom_id is not UNSET:
            field_dict["sbom_id"] = sbom_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        version = d.pop("version")

        sbom_id = d.pop("sbom_id", UNSET)

        product_version_head = cls(
            id=id,
            version=version,
            sbom_id=sbom_id,
        )

        product_version_head.additional_properties = d
        return product_version_head

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
