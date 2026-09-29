from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.format_ import Format

if TYPE_CHECKING:
    from ..models.extract_result_packages import ExtractResultPackages


T = TypeVar("T", bound="ExtractResult")


@_attrs_define
class ExtractResult:
    """Information extracted from an SBOM

    Attributes:
        format_ (Format):
        packages (ExtractResultPackages): packages of the SBOM
        warnings (list[str]): warnings while parsing
    """

    format_: Format
    packages: ExtractResultPackages
    warnings: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        packages = self.packages.to_dict()

        warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "packages": packages,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.extract_result_packages import (
            ExtractResultPackages,
        )

        d = dict(src_dict)
        format_ = Format(d.pop("format"))

        packages = ExtractResultPackages.from_dict(d.pop("packages"))

        warnings = cast(list[str], d.pop("warnings"))

        extract_result = cls(
            format_=format_,
            packages=packages,
            warnings=warnings,
        )

        extract_result.additional_properties = d
        return extract_result

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
