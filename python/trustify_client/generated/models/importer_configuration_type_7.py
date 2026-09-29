from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cwe_importer import CweImporter


T = TypeVar("T", bound="ImporterConfigurationType7")


@_attrs_define
class ImporterConfigurationType7:
    """
    Attributes:
        cwe (CweImporter):
    """

    cwe: CweImporter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cwe = self.cwe.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cwe": cwe,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cwe_importer import CweImporter

        d = dict(src_dict)
        cwe = CweImporter.from_dict(d.pop("cwe"))

        importer_configuration_type_7 = cls(
            cwe=cwe,
        )

        importer_configuration_type_7.additional_properties = d
        return importer_configuration_type_7

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
