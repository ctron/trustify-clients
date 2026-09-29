from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LicenseSummary")


@_attrs_define
class LicenseSummary:
    """
    Attributes:
        id (str):
        license_ (str):
        purls (int):
        spdx_license_exceptions (list[str]):
        spdx_licenses (list[str]):
    """

    id: str
    license_: str
    purls: int
    spdx_license_exceptions: list[str]
    spdx_licenses: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        license_ = self.license_

        purls = self.purls

        spdx_license_exceptions = self.spdx_license_exceptions

        spdx_licenses = self.spdx_licenses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "license": license_,
                "purls": purls,
                "spdx_license_exceptions": spdx_license_exceptions,
                "spdx_licenses": spdx_licenses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        license_ = d.pop("license")

        purls = d.pop("purls")

        spdx_license_exceptions = cast(list[str], d.pop("spdx_license_exceptions"))

        spdx_licenses = cast(list[str], d.pop("spdx_licenses"))

        license_summary = cls(
            id=id,
            license_=license_,
            purls=purls,
            spdx_license_exceptions=spdx_license_exceptions,
            spdx_licenses=spdx_licenses,
        )

        license_summary.additional_properties = d
        return license_summary

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
