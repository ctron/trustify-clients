from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BaseSummary")


@_attrs_define
class BaseSummary:
    """
    Attributes:
        cpe (list[str]):
        document_id (str):
        name (str):
        node_id (str):
        product_name (str):
        product_version (str):
        published (str):
        purl (list[str]):
        sbom_id (str):
        version (str):
    """

    cpe: list[str]
    document_id: str
    name: str
    node_id: str
    product_name: str
    product_version: str
    published: str
    purl: list[str]
    sbom_id: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe = self.cpe

        document_id = self.document_id

        name = self.name

        node_id = self.node_id

        product_name = self.product_name

        product_version = self.product_version

        published = self.published

        purl = self.purl

        sbom_id = self.sbom_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpe": cpe,
                "document_id": document_id,
                "name": name,
                "node_id": node_id,
                "product_name": product_name,
                "product_version": product_version,
                "published": published,
                "purl": purl,
                "sbom_id": sbom_id,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cpe = cast(list[str], d.pop("cpe"))

        document_id = d.pop("document_id")

        name = d.pop("name")

        node_id = d.pop("node_id")

        product_name = d.pop("product_name")

        product_version = d.pop("product_version")

        published = d.pop("published")

        purl = cast(list[str], d.pop("purl"))

        sbom_id = d.pop("sbom_id")

        version = d.pop("version")

        base_summary = cls(
            cpe=cpe,
            document_id=document_id,
            name=name,
            node_id=node_id,
            product_name=product_name,
            product_version=product_version,
            published=published,
            purl=purl,
            sbom_id=sbom_id,
            version=version,
        )

        base_summary.additional_properties = d
        return base_summary

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
