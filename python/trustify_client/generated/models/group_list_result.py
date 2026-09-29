from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.paginated_results_group_details_items_item import (
        PaginatedResultsGroupDetailsItemsItem,
    )


T = TypeVar("T", bound="GroupListResult")


@_attrs_define
class GroupListResult:
    """Result of listing SBOM groups, with optional resolved parent references.

    Attributes:
        items (list[PaginatedResultsGroupDetailsItemsItem]):
        total (int | None | Unset):
        referenced (list[Group] | None | Unset): Groups referenced by parent chains but not present in the primary
            result set.

            Only present when `parents=resolve` is requested.
    """

    items: list[PaginatedResultsGroupDetailsItemsItem]
    total: int | None | Unset = UNSET
    referenced: list[Group] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        referenced: list[dict[str, Any]] | None | Unset
        if isinstance(self.referenced, Unset):
            referenced = UNSET
        elif isinstance(self.referenced, list):
            referenced = []
            for referenced_type_0_item_data in self.referenced:
                referenced_type_0_item = referenced_type_0_item_data.to_dict()
                referenced.append(referenced_type_0_item)

        else:
            referenced = self.referenced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total
        if referenced is not UNSET:
            field_dict["referenced"] = referenced

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.group import Group
        from ..models.paginated_results_group_details_items_item import (
            PaginatedResultsGroupDetailsItemsItem,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = PaginatedResultsGroupDetailsItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        def _parse_referenced(data: object) -> list[Group] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                referenced_type_0 = []
                _referenced_type_0 = data
                for referenced_type_0_item_data in _referenced_type_0:
                    referenced_type_0_item = Group.from_dict(
                        referenced_type_0_item_data
                    )

                    referenced_type_0.append(referenced_type_0_item)

                return referenced_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Group] | None | Unset, data)

        referenced = _parse_referenced(d.pop("referenced", UNSET))

        group_list_result = cls(
            items=items,
            total=total,
            referenced=referenced,
        )

        group_list_result.additional_properties = d
        return group_list_result

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
