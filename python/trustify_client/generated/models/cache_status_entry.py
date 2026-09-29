from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CacheStatusEntry")


@_attrs_define
class CacheStatusEntry:
    """
    Attributes:
        edges (int): The number of edges in the graph
        nodes (int): The number of nodes in the graph
        sbom_id (str): The ID of the SBOM
        size (int): The size of the cache entry, in bytes
        size_human (str):
    """

    edges: int
    nodes: int
    sbom_id: str
    size: int
    size_human: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edges = self.edges

        nodes = self.nodes

        sbom_id = self.sbom_id

        size = self.size

        size_human = self.size_human

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edges": edges,
                "nodes": nodes,
                "sbom_id": sbom_id,
                "size": size,
                "size_human": size_human,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        edges = d.pop("edges")

        nodes = d.pop("nodes")

        sbom_id = d.pop("sbom_id")

        size = d.pop("size")

        size_human = d.pop("size_human")

        cache_status_entry = cls(
            edges=edges,
            nodes=nodes,
            sbom_id=sbom_id,
            size=size,
            size_human=size_human,
        )

        cache_status_entry.additional_properties = d
        return cache_status_entry

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
