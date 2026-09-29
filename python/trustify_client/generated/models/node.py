from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relationship import Relationship
from ..types import UNSET, Unset

T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
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
        ancestors (list[Node] | None | Unset): All ancestors of this node. [`None`] if not requested on this level.
        descendants (list[Node] | None | Unset): All descendents of this node. [`None`] if not requested on this level.
        relationship (None | Relationship | Unset): The relationship the node has to it's containing node, if any.
        warnings (list[str] | Unset): Warnings when processing this node.
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
    ancestors: list[Node] | None | Unset = UNSET
    descendants: list[Node] | None | Unset = UNSET
    relationship: None | Relationship | Unset = UNSET
    warnings: list[str] | Unset = UNSET
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

        ancestors: list[dict[str, Any]] | None | Unset
        if isinstance(self.ancestors, Unset):
            ancestors = UNSET
        elif isinstance(self.ancestors, list):
            ancestors = []
            for ancestors_type_0_item_data in self.ancestors:
                ancestors_type_0_item = ancestors_type_0_item_data.to_dict()
                ancestors.append(ancestors_type_0_item)

        else:
            ancestors = self.ancestors

        descendants: list[dict[str, Any]] | None | Unset
        if isinstance(self.descendants, Unset):
            descendants = UNSET
        elif isinstance(self.descendants, list):
            descendants = []
            for descendants_type_0_item_data in self.descendants:
                descendants_type_0_item = descendants_type_0_item_data.to_dict()
                descendants.append(descendants_type_0_item)

        else:
            descendants = self.descendants

        relationship: None | str | Unset
        if isinstance(self.relationship, Unset):
            relationship = UNSET
        elif isinstance(self.relationship, Relationship):
            relationship = self.relationship.value
        else:
            relationship = self.relationship

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

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
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if descendants is not UNSET:
            field_dict["descendants"] = descendants
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

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

        def _parse_ancestors(data: object) -> list[Node] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ancestors_type_0 = []
                _ancestors_type_0 = data
                for ancestors_type_0_item_data in _ancestors_type_0:
                    ancestors_type_0_item = Node.from_dict(ancestors_type_0_item_data)

                    ancestors_type_0.append(ancestors_type_0_item)

                return ancestors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Node] | None | Unset, data)

        ancestors = _parse_ancestors(d.pop("ancestors", UNSET))

        def _parse_descendants(data: object) -> list[Node] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                descendants_type_0 = []
                _descendants_type_0 = data
                for descendants_type_0_item_data in _descendants_type_0:
                    descendants_type_0_item = Node.from_dict(
                        descendants_type_0_item_data
                    )

                    descendants_type_0.append(descendants_type_0_item)

                return descendants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Node] | None | Unset, data)

        descendants = _parse_descendants(d.pop("descendants", UNSET))

        def _parse_relationship(data: object) -> None | Relationship | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                relationship_type_1 = Relationship(data)

                return relationship_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Relationship | Unset, data)

        relationship = _parse_relationship(d.pop("relationship", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        node = cls(
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
            ancestors=ancestors,
            descendants=descendants,
            relationship=relationship,
            warnings=warnings,
        )

        node.additional_properties = d
        return node

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
