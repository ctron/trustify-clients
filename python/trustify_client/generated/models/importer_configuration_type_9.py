from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quay_importer import QuayImporter


T = TypeVar("T", bound="ImporterConfigurationType9")


@_attrs_define
class ImporterConfigurationType9:
    """
    Attributes:
        quay (QuayImporter):
    """

    quay: QuayImporter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quay = self.quay.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quay": quay,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.quay_importer import QuayImporter

        d = dict(src_dict)
        quay = QuayImporter.from_dict(d.pop("quay"))

        importer_configuration_type_9 = cls(
            quay=quay,
        )

        importer_configuration_type_9.additional_properties = d
        return importer_configuration_type_9

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
