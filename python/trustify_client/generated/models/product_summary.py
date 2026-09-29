from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_head import OrganizationHead
    from ..models.product_version_head import ProductVersionHead


T = TypeVar("T", bound="ProductSummary")


@_attrs_define
class ProductSummary:
    """
    Attributes:
        id (str):
        name (str):
        vendor (None | OrganizationHead):
        versions (list[ProductVersionHead]):
    """

    id: str
    name: str
    vendor: None | OrganizationHead
    versions: list[ProductVersionHead]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_head import OrganizationHead

        id = self.id

        name = self.name

        vendor: dict[str, Any] | None
        if isinstance(self.vendor, OrganizationHead):
            vendor = self.vendor.to_dict()
        else:
            vendor = self.vendor

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "vendor": vendor,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.organization_head import OrganizationHead
        from ..models.product_version_head import ProductVersionHead

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_vendor(data: object) -> None | OrganizationHead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vendor_type_1 = OrganizationHead.from_dict(data)

                return vendor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationHead, data)

        vendor = _parse_vendor(d.pop("vendor"))

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = ProductVersionHead.from_dict(versions_item_data)

            versions.append(versions_item)

        product_summary = cls(
            id=id,
            name=name,
            vendor=vendor,
            versions=versions,
        )

        product_summary.additional_properties = d
        return product_summary

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
