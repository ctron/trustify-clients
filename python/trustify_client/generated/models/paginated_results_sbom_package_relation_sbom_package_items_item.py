from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relationship import Relationship

if TYPE_CHECKING:
    from ..models.paginated_results_sbom_package_relation_sbom_package_items_item_package import (
        PaginatedResultsSbomPackageRelationSbomPackageItemsItemPackage,
    )


T = TypeVar("T", bound="PaginatedResultsSbomPackageRelationSbomPackageItemsItem")


@_attrs_define
class PaginatedResultsSbomPackageRelationSbomPackageItemsItem:
    """
    Attributes:
        package (PaginatedResultsSbomPackageRelationSbomPackageItemsItemPackage):
        relationship (Relationship):
    """

    package: PaginatedResultsSbomPackageRelationSbomPackageItemsItemPackage
    relationship: Relationship
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package = self.package.to_dict()

        relationship = self.relationship.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
                "relationship": relationship,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.paginated_results_sbom_package_relation_sbom_package_items_item_package import (
            PaginatedResultsSbomPackageRelationSbomPackageItemsItemPackage,
        )

        d = dict(src_dict)
        package = (
            PaginatedResultsSbomPackageRelationSbomPackageItemsItemPackage.from_dict(
                d.pop("package")
            )
        )

        relationship = Relationship(d.pop("relationship"))

        paginated_results_sbom_package_relation_sbom_package_items_item = cls(
            package=package,
            relationship=relationship,
        )

        paginated_results_sbom_package_relation_sbom_package_items_item.additional_properties = d
        return paginated_results_sbom_package_relation_sbom_package_items_item

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
