from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.versioned_purl_summary import VersionedPurlSummary


T = TypeVar("T", bound="BasePurlDetails")


@_attrs_define
class BasePurlDetails:
    """
    Attributes:
        purl (str):
        uuid (UUID): The ID of the base PURL
        versions (list[VersionedPurlSummary]):
    """

    purl: str
    uuid: UUID
    versions: list[VersionedPurlSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purl = self.purl

        uuid = str(self.uuid)

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purl": purl,
                "uuid": uuid,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.versioned_purl_summary import (
            VersionedPurlSummary,
        )

        d = dict(src_dict)
        purl = d.pop("purl")

        uuid = UUID(d.pop("uuid"))

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = VersionedPurlSummary.from_dict(versions_item_data)

            versions.append(versions_item)

        base_purl_details = cls(
            purl=purl,
            uuid=uuid,
            versions=versions,
        )

        base_purl_details.additional_properties = d
        return base_purl_details

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
