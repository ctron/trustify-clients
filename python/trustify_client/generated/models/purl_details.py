from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.base_purl_head import BasePurlHead
    from ..models.license_info import LicenseInfo
    from ..models.license_ref_mapping import LicenseRefMapping
    from ..models.purl_advisory import PurlAdvisory
    from ..models.versioned_purl_head import VersionedPurlHead


T = TypeVar("T", bound="PurlDetails")


@_attrs_define
class PurlDetails:
    """
    Attributes:
        purl (str):
        uuid (UUID): The ID of the qualified PURL
        advisories (list[PurlAdvisory]):
        base (BasePurlHead):
        licenses (list[LicenseInfo]):
        licenses_ref_mapping (list[LicenseRefMapping]):
        version (VersionedPurlHead):
    """

    purl: str
    uuid: UUID
    advisories: list[PurlAdvisory]
    base: BasePurlHead
    licenses: list[LicenseInfo]
    licenses_ref_mapping: list[LicenseRefMapping]
    version: VersionedPurlHead
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purl = self.purl

        uuid = str(self.uuid)

        advisories = []
        for advisories_item_data in self.advisories:
            advisories_item = advisories_item_data.to_dict()
            advisories.append(advisories_item)

        base = self.base.to_dict()

        licenses = []
        for licenses_item_data in self.licenses:
            licenses_item = licenses_item_data.to_dict()
            licenses.append(licenses_item)

        licenses_ref_mapping = []
        for licenses_ref_mapping_item_data in self.licenses_ref_mapping:
            licenses_ref_mapping_item = licenses_ref_mapping_item_data.to_dict()
            licenses_ref_mapping.append(licenses_ref_mapping_item)

        version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purl": purl,
                "uuid": uuid,
                "advisories": advisories,
                "base": base,
                "licenses": licenses,
                "licenses_ref_mapping": licenses_ref_mapping,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_purl_head import BasePurlHead
        from ..models.license_info import LicenseInfo
        from ..models.license_ref_mapping import LicenseRefMapping
        from ..models.purl_advisory import PurlAdvisory
        from ..models.versioned_purl_head import VersionedPurlHead

        d = dict(src_dict)
        purl = d.pop("purl")

        uuid = UUID(d.pop("uuid"))

        advisories = []
        _advisories = d.pop("advisories")
        for advisories_item_data in _advisories:
            advisories_item = PurlAdvisory.from_dict(advisories_item_data)

            advisories.append(advisories_item)

        base = BasePurlHead.from_dict(d.pop("base"))

        licenses = []
        _licenses = d.pop("licenses")
        for licenses_item_data in _licenses:
            licenses_item = LicenseInfo.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        licenses_ref_mapping = []
        _licenses_ref_mapping = d.pop("licenses_ref_mapping")
        for licenses_ref_mapping_item_data in _licenses_ref_mapping:
            licenses_ref_mapping_item = LicenseRefMapping.from_dict(
                licenses_ref_mapping_item_data
            )

            licenses_ref_mapping.append(licenses_ref_mapping_item)

        version = VersionedPurlHead.from_dict(d.pop("version"))

        purl_details = cls(
            purl=purl,
            uuid=uuid,
            advisories=advisories,
            base=base,
            licenses=licenses,
            licenses_ref_mapping=licenses_ref_mapping,
            version=version,
        )

        purl_details.additional_properties = d
        return purl_details

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
