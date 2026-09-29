from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_status_details import AnalysisStatusDetails


T = TypeVar("T", bound="AnalysisStatus")


@_attrs_define
class AnalysisStatus:
    """
    Attributes:
        graph_count (int): The number of graphs loaded in memory
        graph_max_memory (int): The maximum number of bytes the cache will hold
        graph_memory (int): The number of bytes consumed by entries in the graph
        loading_operations (int): The number of ongoing loading operations
        sbom_count (int): The number of SBOMs found in the database
        details (AnalysisStatusDetails | None | Unset): More details
    """

    graph_count: int
    graph_max_memory: int
    graph_memory: int
    loading_operations: int
    sbom_count: int
    details: AnalysisStatusDetails | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analysis_status_details import (
            AnalysisStatusDetails,
        )

        graph_count = self.graph_count

        graph_max_memory = self.graph_max_memory

        graph_memory = self.graph_memory

        loading_operations = self.loading_operations

        sbom_count = self.sbom_count

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, AnalysisStatusDetails):
            details = self.details.to_dict()
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "graph_count": graph_count,
                "graph_max_memory": graph_max_memory,
                "graph_memory": graph_memory,
                "loading_operations": loading_operations,
                "sbom_count": sbom_count,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analysis_status_details import (
            AnalysisStatusDetails,
        )

        d = dict(src_dict)
        graph_count = d.pop("graph_count")

        graph_max_memory = d.pop("graph_max_memory")

        graph_memory = d.pop("graph_memory")

        loading_operations = d.pop("loading_operations")

        sbom_count = d.pop("sbom_count")

        def _parse_details(data: object) -> AnalysisStatusDetails | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_1 = AnalysisStatusDetails.from_dict(data)

                return details_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalysisStatusDetails | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        analysis_status = cls(
            graph_count=graph_count,
            graph_max_memory=graph_max_memory,
            graph_memory=graph_memory,
            loading_operations=loading_operations,
            sbom_count=sbom_count,
            details=details,
        )

        analysis_status.additional_properties = d
        return analysis_status

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
