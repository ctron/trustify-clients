from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sbom_importer import SbomImporter


T = TypeVar("T", bound="ImporterConfigurationType0")


@_attrs_define
class ImporterConfigurationType0:
    """
    Attributes:
        sbom (SbomImporter):
    """

    sbom: SbomImporter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sbom = self.sbom.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sbom": sbom,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sbom_importer import SbomImporter

        d = dict(src_dict)
        sbom = SbomImporter.from_dict(d.pop("sbom"))

        importer_configuration_type_0 = cls(
            sbom=sbom,
        )

        importer_configuration_type_0.additional_properties = d
        return importer_configuration_type_0

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
