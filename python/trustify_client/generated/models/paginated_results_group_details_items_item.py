from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.labels import Labels


T = TypeVar("T", bound="PaginatedResultsGroupDetailsItemsItem")


@_attrs_define
class PaginatedResultsGroupDetailsItemsItem:
    """Detailed group information, extends [`Group`]

    Attributes:
        id (str): The ID of the group
        name (str): The name of the group, in the context of its parent
        description (None | str | Unset): A user friendly description
        labels (Labels | Unset):
        parent (None | str | Unset): The direct parent of this group
        number_of_groups (int | None | Unset): The number of groups owned directly by this group

            This information is only present when requested.
        number_of_sboms (int | None | Unset): The number of SBOMs directly assigned to this group

            This information is only present when requested.
        parents (list[str] | None | Unset): The path, of IDs, from the root to this group

            This information is only present when requested.
    """

    id: str
    name: str
    description: None | str | Unset = UNSET
    labels: Labels | Unset = UNSET
    parent: None | str | Unset = UNSET
    number_of_groups: int | None | Unset = UNSET
    number_of_sboms: int | None | Unset = UNSET
    parents: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        number_of_groups: int | None | Unset
        if isinstance(self.number_of_groups, Unset):
            number_of_groups = UNSET
        else:
            number_of_groups = self.number_of_groups

        number_of_sboms: int | None | Unset
        if isinstance(self.number_of_sboms, Unset):
            number_of_sboms = UNSET
        else:
            number_of_sboms = self.number_of_sboms

        parents: list[str] | None | Unset
        if isinstance(self.parents, Unset):
            parents = UNSET
        elif isinstance(self.parents, list):
            parents = self.parents

        else:
            parents = self.parents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if parent is not UNSET:
            field_dict["parent"] = parent
        if number_of_groups is not UNSET:
            field_dict["number_of_groups"] = number_of_groups
        if number_of_sboms is not UNSET:
            field_dict["number_of_sboms"] = number_of_sboms
        if parents is not UNSET:
            field_dict["parents"] = parents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.labels import Labels

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: Labels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = Labels.from_dict(_labels)

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_number_of_groups(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_groups = _parse_number_of_groups(d.pop("number_of_groups", UNSET))

        def _parse_number_of_sboms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_sboms = _parse_number_of_sboms(d.pop("number_of_sboms", UNSET))

        def _parse_parents(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parents_type_0 = cast(list[str], data)

                return parents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        parents = _parse_parents(d.pop("parents", UNSET))

        paginated_results_group_details_items_item = cls(
            id=id,
            name=name,
            description=description,
            labels=labels,
            parent=parent,
            number_of_groups=number_of_groups,
            number_of_sboms=number_of_sboms,
            parents=parents,
        )

        paginated_results_group_details_items_item.additional_properties = d
        return paginated_results_group_details_items_item

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
