from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WeaknessDetails")


@_attrs_define
class WeaknessDetails:
    """
    Attributes:
        id (str):
        description (None | str | Unset):
        can_also_be (list[str] | None | Unset):
        can_follow (list[str] | None | Unset):
        can_precede (list[str] | None | Unset):
        child_of (list[str] | None | Unset):
        extended_description (None | str | Unset):
        parent_of (list[str] | None | Unset):
        peer_of (list[str] | None | Unset):
        required_by (list[str] | None | Unset):
        requires (list[str] | None | Unset):
        starts_with (list[str] | None | Unset):
    """

    id: str
    description: None | str | Unset = UNSET
    can_also_be: list[str] | None | Unset = UNSET
    can_follow: list[str] | None | Unset = UNSET
    can_precede: list[str] | None | Unset = UNSET
    child_of: list[str] | None | Unset = UNSET
    extended_description: None | str | Unset = UNSET
    parent_of: list[str] | None | Unset = UNSET
    peer_of: list[str] | None | Unset = UNSET
    required_by: list[str] | None | Unset = UNSET
    requires: list[str] | None | Unset = UNSET
    starts_with: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        can_also_be: list[str] | None | Unset
        if isinstance(self.can_also_be, Unset):
            can_also_be = UNSET
        elif isinstance(self.can_also_be, list):
            can_also_be = self.can_also_be

        else:
            can_also_be = self.can_also_be

        can_follow: list[str] | None | Unset
        if isinstance(self.can_follow, Unset):
            can_follow = UNSET
        elif isinstance(self.can_follow, list):
            can_follow = self.can_follow

        else:
            can_follow = self.can_follow

        can_precede: list[str] | None | Unset
        if isinstance(self.can_precede, Unset):
            can_precede = UNSET
        elif isinstance(self.can_precede, list):
            can_precede = self.can_precede

        else:
            can_precede = self.can_precede

        child_of: list[str] | None | Unset
        if isinstance(self.child_of, Unset):
            child_of = UNSET
        elif isinstance(self.child_of, list):
            child_of = self.child_of

        else:
            child_of = self.child_of

        extended_description: None | str | Unset
        if isinstance(self.extended_description, Unset):
            extended_description = UNSET
        else:
            extended_description = self.extended_description

        parent_of: list[str] | None | Unset
        if isinstance(self.parent_of, Unset):
            parent_of = UNSET
        elif isinstance(self.parent_of, list):
            parent_of = self.parent_of

        else:
            parent_of = self.parent_of

        peer_of: list[str] | None | Unset
        if isinstance(self.peer_of, Unset):
            peer_of = UNSET
        elif isinstance(self.peer_of, list):
            peer_of = self.peer_of

        else:
            peer_of = self.peer_of

        required_by: list[str] | None | Unset
        if isinstance(self.required_by, Unset):
            required_by = UNSET
        elif isinstance(self.required_by, list):
            required_by = self.required_by

        else:
            required_by = self.required_by

        requires: list[str] | None | Unset
        if isinstance(self.requires, Unset):
            requires = UNSET
        elif isinstance(self.requires, list):
            requires = self.requires

        else:
            requires = self.requires

        starts_with: list[str] | None | Unset
        if isinstance(self.starts_with, Unset):
            starts_with = UNSET
        elif isinstance(self.starts_with, list):
            starts_with = self.starts_with

        else:
            starts_with = self.starts_with

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if can_also_be is not UNSET:
            field_dict["can_also_be"] = can_also_be
        if can_follow is not UNSET:
            field_dict["can_follow"] = can_follow
        if can_precede is not UNSET:
            field_dict["can_precede"] = can_precede
        if child_of is not UNSET:
            field_dict["child_of"] = child_of
        if extended_description is not UNSET:
            field_dict["extended_description"] = extended_description
        if parent_of is not UNSET:
            field_dict["parent_of"] = parent_of
        if peer_of is not UNSET:
            field_dict["peer_of"] = peer_of
        if required_by is not UNSET:
            field_dict["required_by"] = required_by
        if requires is not UNSET:
            field_dict["requires"] = requires
        if starts_with is not UNSET:
            field_dict["starts_with"] = starts_with

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_can_also_be(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                can_also_be_type_0 = cast(list[str], data)

                return can_also_be_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        can_also_be = _parse_can_also_be(d.pop("can_also_be", UNSET))

        def _parse_can_follow(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                can_follow_type_0 = cast(list[str], data)

                return can_follow_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        can_follow = _parse_can_follow(d.pop("can_follow", UNSET))

        def _parse_can_precede(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                can_precede_type_0 = cast(list[str], data)

                return can_precede_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        can_precede = _parse_can_precede(d.pop("can_precede", UNSET))

        def _parse_child_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                child_of_type_0 = cast(list[str], data)

                return child_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        child_of = _parse_child_of(d.pop("child_of", UNSET))

        def _parse_extended_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extended_description = _parse_extended_description(
            d.pop("extended_description", UNSET)
        )

        def _parse_parent_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parent_of_type_0 = cast(list[str], data)

                return parent_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        parent_of = _parse_parent_of(d.pop("parent_of", UNSET))

        def _parse_peer_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                peer_of_type_0 = cast(list[str], data)

                return peer_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        peer_of = _parse_peer_of(d.pop("peer_of", UNSET))

        def _parse_required_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_by_type_0 = cast(list[str], data)

                return required_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        required_by = _parse_required_by(d.pop("required_by", UNSET))

        def _parse_requires(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requires_type_0 = cast(list[str], data)

                return requires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        requires = _parse_requires(d.pop("requires", UNSET))

        def _parse_starts_with(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                starts_with_type_0 = cast(list[str], data)

                return starts_with_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        starts_with = _parse_starts_with(d.pop("starts_with", UNSET))

        weakness_details = cls(
            id=id,
            description=description,
            can_also_be=can_also_be,
            can_follow=can_follow,
            can_precede=can_precede,
            child_of=child_of,
            extended_description=extended_description,
            parent_of=parent_of,
            peer_of=peer_of,
            required_by=required_by,
            requires=requires,
            starts_with=starts_with,
        )

        weakness_details.additional_properties = d
        return weakness_details

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
