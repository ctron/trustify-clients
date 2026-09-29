from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.base_purl_head import BasePurlHead
    from ..models.purl_head import PurlHead


T = TypeVar("T", bound="VersionedPurlSummary")


@_attrs_define
class VersionedPurlSummary:
    """
    Attributes:
        purl (str):
        uuid (UUID): The ID of the versioned PURL
        version (str): The version from the PURL
        base (BasePurlHead):
        purls (list[PurlHead]):
    """

    purl: str
    uuid: UUID
    version: str
    base: BasePurlHead
    purls: list[PurlHead]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purl = self.purl

        uuid = str(self.uuid)

        version = self.version

        base = self.base.to_dict()

        purls = []
        for purls_item_data in self.purls:
            purls_item = purls_item_data.to_dict()
            purls.append(purls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purl": purl,
                "uuid": uuid,
                "version": version,
                "base": base,
                "purls": purls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_purl_head import BasePurlHead
        from ..models.purl_head import PurlHead

        d = dict(src_dict)
        purl = d.pop("purl")

        uuid = UUID(d.pop("uuid"))

        version = d.pop("version")

        base = BasePurlHead.from_dict(d.pop("base"))

        purls = []
        _purls = d.pop("purls")
        for purls_item_data in _purls:
            purls_item = PurlHead.from_dict(purls_item_data)

            purls.append(purls_item)

        versioned_purl_summary = cls(
            purl=purl,
            uuid=uuid,
            version=version,
            base=base,
            purls=purls,
        )

        versioned_purl_summary.additional_properties = d
        return versioned_purl_summary

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
