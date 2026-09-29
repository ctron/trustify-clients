from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_info import LicenseInfo
    from ..models.license_ref_mapping import LicenseRefMapping
    from ..models.purl_summary import PurlSummary


T = TypeVar("T", bound="PaginatedResultsSbomPackageItemsItem")


@_attrs_define
class PaginatedResultsSbomPackageItemsItem:
    """
    Attributes:
        cpe (list[str]): CPEs identifying the package
        id (str): The SBOM internal ID of a package
        licenses (list[LicenseInfo]): License info
        licenses_ref_mapping (list[LicenseRefMapping]): LicenseRef mappings

            **Deprecated**: Licenses are now pre-expanded at ingestion time via `expanded_license` /
            `sbom_license_expanded` tables. This field is always empty and will be removed in a future
            release.
        name (str): The name of the package in the SBOM
        purl (list[PurlSummary]): PURLs identifying the package
        group (None | str | Unset): An optional group/namespace for an SBOM package
        version (None | str | Unset): An optional version for an SBOM package
    """

    cpe: list[str]
    id: str
    licenses: list[LicenseInfo]
    licenses_ref_mapping: list[LicenseRefMapping]
    name: str
    purl: list[PurlSummary]
    group: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe = self.cpe

        id = self.id

        licenses = []
        for licenses_item_data in self.licenses:
            licenses_item = licenses_item_data.to_dict()
            licenses.append(licenses_item)

        licenses_ref_mapping = []
        for licenses_ref_mapping_item_data in self.licenses_ref_mapping:
            licenses_ref_mapping_item = licenses_ref_mapping_item_data.to_dict()
            licenses_ref_mapping.append(licenses_ref_mapping_item)

        name = self.name

        purl = []
        for purl_item_data in self.purl:
            purl_item = purl_item_data.to_dict()
            purl.append(purl_item)

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpe": cpe,
                "id": id,
                "licenses": licenses,
                "licenses_ref_mapping": licenses_ref_mapping,
                "name": name,
                "purl": purl,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.license_info import LicenseInfo
        from ..models.license_ref_mapping import LicenseRefMapping
        from ..models.purl_summary import PurlSummary

        d = dict(src_dict)
        cpe = cast(list[str], d.pop("cpe"))

        id = d.pop("id")

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

        name = d.pop("name")

        purl = []
        _purl = d.pop("purl")
        for purl_item_data in _purl:
            purl_item = PurlSummary.from_dict(purl_item_data)

            purl.append(purl_item)

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        paginated_results_sbom_package_items_item = cls(
            cpe=cpe,
            id=id,
            licenses=licenses,
            licenses_ref_mapping=licenses_ref_mapping,
            name=name,
            purl=purl,
            group=group,
            version=version,
        )

        paginated_results_sbom_package_items_item.additional_properties = d
        return paginated_results_sbom_package_items_item

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
