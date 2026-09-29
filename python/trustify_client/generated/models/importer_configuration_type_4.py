from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nvd_importer import NvdImporter


T = TypeVar("T", bound="ImporterConfigurationType4")


@_attrs_define
class ImporterConfigurationType4:
    """
    Attributes:
        nvd (NvdImporter):
    """

    nvd: NvdImporter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nvd = self.nvd.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nvd": nvd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.nvd_importer import NvdImporter

        d = dict(src_dict)
        nvd = NvdImporter.from_dict(d.pop("nvd"))

        importer_configuration_type_4 = cls(
            nvd=nvd,
        )

        importer_configuration_type_4.additional_properties = d
        return importer_configuration_type_4

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
