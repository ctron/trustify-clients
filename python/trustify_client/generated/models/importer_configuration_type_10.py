from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.http_importer import HttpImporter


T = TypeVar("T", bound="ImporterConfigurationType10")


@_attrs_define
class ImporterConfigurationType10:
    """
    Attributes:
        http (HttpImporter): Configuration for the HTTP-based importer.

            Fetches documents from an HTTP repository, using a pluggable
            discovery strategy to enumerate files and an optional credential
            for authenticated sources.
    """

    http: HttpImporter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        http = self.http.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "http": http,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.http_importer import HttpImporter

        d = dict(src_dict)
        http = HttpImporter.from_dict(d.pop("http"))

        importer_configuration_type_10 = cls(
            http=http,
        )

        importer_configuration_type_10.additional_properties = d
        return importer_configuration_type_10

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
