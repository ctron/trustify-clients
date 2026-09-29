from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clearly_defined_importer import ClearlyDefinedImporter


T = TypeVar("T", bound="ImporterConfigurationType5")


@_attrs_define
class ImporterConfigurationType5:
    """
    Attributes:
        clearly_defined (ClearlyDefinedImporter):
    """

    clearly_defined: ClearlyDefinedImporter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clearly_defined = self.clearly_defined.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clearlyDefined": clearly_defined,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clearly_defined_importer import (
            ClearlyDefinedImporter,
        )

        d = dict(src_dict)
        clearly_defined = ClearlyDefinedImporter.from_dict(d.pop("clearlyDefined"))

        importer_configuration_type_5 = cls(
            clearly_defined=clearly_defined,
        )

        importer_configuration_type_5.additional_properties = d
        return importer_configuration_type_5

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
