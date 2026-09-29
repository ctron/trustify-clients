from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_sbom_head import ProductSbomHead


T = TypeVar("T", bound="ProductVersionDetails")


@_attrs_define
class ProductVersionDetails:
    """
    Attributes:
        id (str):
        version (str):
        sbom_id (str | Unset):
        sbom (None | ProductSbomHead | Unset):
    """

    id: str
    version: str
    sbom_id: str | Unset = UNSET
    sbom: None | ProductSbomHead | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_sbom_head import ProductSbomHead

        id = self.id

        version = self.version

        sbom_id = self.sbom_id

        sbom: dict[str, Any] | None | Unset
        if isinstance(self.sbom, Unset):
            sbom = UNSET
        elif isinstance(self.sbom, ProductSbomHead):
            sbom = self.sbom.to_dict()
        else:
            sbom = self.sbom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
            }
        )
        if sbom_id is not UNSET:
            field_dict["sbom_id"] = sbom_id
        if sbom is not UNSET:
            field_dict["sbom"] = sbom

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_sbom_head import ProductSbomHead

        d = dict(src_dict)
        id = d.pop("id")

        version = d.pop("version")

        sbom_id = d.pop("sbom_id", UNSET)

        def _parse_sbom(data: object) -> None | ProductSbomHead | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sbom_type_1 = ProductSbomHead.from_dict(data)

                return sbom_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductSbomHead | Unset, data)

        sbom = _parse_sbom(d.pop("sbom", UNSET))

        product_version_details = cls(
            id=id,
            version=version,
            sbom_id=sbom_id,
            sbom=sbom,
        )

        product_version_details.additional_properties = d
        return product_version_details

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
