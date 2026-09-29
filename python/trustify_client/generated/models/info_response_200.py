from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.info_response_200_build import InfoResponse200Build


T = TypeVar("T", bound="InfoResponse200")


@_attrs_define
class InfoResponse200:
    """
    Attributes:
        exploit_intelligence (bool):
        read_only (bool):
        version (str):
        build (InfoResponse200Build | Unset):
    """

    exploit_intelligence: bool
    read_only: bool
    version: str
    build: InfoResponse200Build | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exploit_intelligence = self.exploit_intelligence

        read_only = self.read_only

        version = self.version

        build: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build, Unset):
            build = self.build.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exploitIntelligence": exploit_intelligence,
                "readOnly": read_only,
                "version": version,
            }
        )
        if build is not UNSET:
            field_dict["build"] = build

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.info_response_200_build import (
            InfoResponse200Build,
        )

        d = dict(src_dict)
        exploit_intelligence = d.pop("exploitIntelligence")

        read_only = d.pop("readOnly")

        version = d.pop("version")

        _build = d.pop("build", UNSET)
        build: InfoResponse200Build | Unset
        if isinstance(_build, Unset):
            build = UNSET
        else:
            build = InfoResponse200Build.from_dict(_build)

        info_response_200 = cls(
            exploit_intelligence=exploit_intelligence,
            read_only=read_only,
            version=version,
            build=build,
        )

        info_response_200.additional_properties = d
        return info_response_200

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
