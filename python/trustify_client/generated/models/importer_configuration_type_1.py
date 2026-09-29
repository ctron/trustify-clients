from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.csaf_importer import CsafImporter


T = TypeVar("T", bound="ImporterConfigurationType1")


@_attrs_define
class ImporterConfigurationType1:
    """
    Attributes:
        csaf (CsafImporter):
    """

    csaf: CsafImporter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csaf = self.csaf.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "csaf": csaf,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.csaf_importer import CsafImporter

        d = dict(src_dict)
        csaf = CsafImporter.from_dict(d.pop("csaf"))

        importer_configuration_type_1 = cls(
            csaf=csaf,
        )

        importer_configuration_type_1.additional_properties = d
        return importer_configuration_type_1

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
