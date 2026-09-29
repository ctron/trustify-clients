from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.revisioned_importer_value import RevisionedImporterValue


T = TypeVar("T", bound="RevisionedImporter")


@_attrs_define
class RevisionedImporter:
    """A struct wrapping an item with a revision.

    If the revision should not be part of the payload, but e.g. an HTTP header (like `ETag`), this
    struct can help carrying both pieces.

        Attributes:
            revision (str): The revision.

                An opaque string that should have no meaning to the user, only to the backend.
            value (RevisionedImporterValue):
    """

    revision: str
    value: RevisionedImporterValue
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision = self.revision

        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revision": revision,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.revisioned_importer_value import (
            RevisionedImporterValue,
        )

        d = dict(src_dict)
        revision = d.pop("revision")

        value = RevisionedImporterValue.from_dict(d.pop("value"))

        revisioned_importer = cls(
            revision=revision,
            value=value,
        )

        revisioned_importer.additional_properties = d
        return revisioned_importer

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
