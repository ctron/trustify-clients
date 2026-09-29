from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationHead")


@_attrs_define
class OrganizationHead:
    """An organization who may issue advisories, product SBOMs, or
    otherwise be involved in supply-chain evidence.

        Attributes:
            cpe_key (None | str): The `CPE` key of the organization, if known.
            id (UUID): The opaque UUID of the organization.
            name (str): The name of the organization.
            website (None | str): The website of the organization, if known.
    """

    cpe_key: None | str
    id: UUID
    name: str
    website: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe_key: None | str
        cpe_key = self.cpe_key

        id = str(self.id)

        name = self.name

        website: None | str
        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpe_key": cpe_key,
                "id": id,
                "name": name,
                "website": website,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_cpe_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cpe_key = _parse_cpe_key(d.pop("cpe_key"))

        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        organization_head = cls(
            cpe_key=cpe_key,
            id=id,
            name=name,
            website=website,
        )

        organization_head.additional_properties = d
        return organization_head

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
