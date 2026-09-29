from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clearly_defined_package_type import ClearlyDefinedPackageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.labels import Labels


T = TypeVar("T", bound="ClearlyDefinedCurationImporter")


@_attrs_define
class ClearlyDefinedCurationImporter:
    """
    Attributes:
        period (str): The period the importer should be run.
        description (None | str | Unset): A description for users.
        disabled (bool | Unset): A flag to disable the importer, without deleting it.
        labels (Labels | Unset):
        source (str | Unset):
        types (list[ClearlyDefinedPackageType] | Unset):
    """

    period: str
    description: None | str | Unset = UNSET
    disabled: bool | Unset = UNSET
    labels: Labels | Unset = UNSET
    source: str | Unset = UNSET
    types: list[ClearlyDefinedPackageType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        disabled = self.disabled

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        source = self.source

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.value
                types.append(types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if labels is not UNSET:
            field_dict["labels"] = labels
        if source is not UNSET:
            field_dict["source"] = source
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.labels import Labels

        d = dict(src_dict)
        period = d.pop("period")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        disabled = d.pop("disabled", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Labels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = Labels.from_dict(_labels)

        source = d.pop("source", UNSET)

        _types = d.pop("types", UNSET)
        types: list[ClearlyDefinedPackageType] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = ClearlyDefinedPackageType(types_item_data)

                types.append(types_item)

        clearly_defined_curation_importer = cls(
            period=period,
            description=description,
            disabled=disabled,
            labels=labels,
            source=source,
            types=types,
        )

        clearly_defined_curation_importer.additional_properties = d
        return clearly_defined_curation_importer

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
