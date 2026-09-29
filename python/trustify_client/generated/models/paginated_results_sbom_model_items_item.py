from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_results_sbom_model_items_item_properties import (
        PaginatedResultsSbomModelItemsItemProperties,
    )
    from ..models.purl_summary import PurlSummary


T = TypeVar("T", bound="PaginatedResultsSbomModelItemsItem")


@_attrs_define
class PaginatedResultsSbomModelItemsItem:
    """
    Attributes:
        id (str): The internal ID of a model
        name (str): The name of the model in the SBOM
        properties (PaginatedResultsSbomModelItemsItemProperties): The properties associated with the model
        purls (list[PurlSummary]): The model's PURL
        sbom_count (int | None):
    """

    id: str
    name: str
    properties: PaginatedResultsSbomModelItemsItemProperties
    purls: list[PurlSummary]
    sbom_count: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        properties = self.properties.to_dict()

        purls = []
        for purls_item_data in self.purls:
            purls_item = purls_item_data.to_dict()
            purls.append(purls_item)

        sbom_count: int | None
        sbom_count = self.sbom_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "properties": properties,
                "purls": purls,
                "sbom_count": sbom_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.paginated_results_sbom_model_items_item_properties import (
            PaginatedResultsSbomModelItemsItemProperties,
        )
        from ..models.purl_summary import PurlSummary

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        properties = PaginatedResultsSbomModelItemsItemProperties.from_dict(
            d.pop("properties")
        )

        purls = []
        _purls = d.pop("purls")
        for purls_item_data in _purls:
            purls_item = PurlSummary.from_dict(purls_item_data)

            purls.append(purls_item)

        def _parse_sbom_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sbom_count = _parse_sbom_count(d.pop("sbom_count"))

        paginated_results_sbom_model_items_item = cls(
            id=id,
            name=name,
            properties=properties,
            purls=purls,
            sbom_count=sbom_count,
        )

        paginated_results_sbom_model_items_item.additional_properties = d
        return paginated_results_sbom_model_items_item

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
