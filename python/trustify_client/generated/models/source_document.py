from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SourceDocument")


@_attrs_define
class SourceDocument:
    """
    Attributes:
        ingested (datetime.datetime): The timestamp the document was ingested
        sha256 (str):
        sha384 (str):
        sha512 (str):
        size (int):
    """

    ingested: datetime.datetime
    sha256: str
    sha384: str
    sha512: str
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ingested = self.ingested.isoformat()

        sha256 = self.sha256

        sha384 = self.sha384

        sha512 = self.sha512

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ingested": ingested,
                "sha256": sha256,
                "sha384": sha384,
                "sha512": sha512,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ingested = datetime.datetime.fromisoformat(d.pop("ingested"))

        sha256 = d.pop("sha256")

        sha384 = d.pop("sha384")

        sha512 = d.pop("sha512")

        size = d.pop("size")

        source_document = cls(
            ingested=ingested,
            sha256=sha256,
            sha384=sha384,
            sha512=sha512,
            size=size,
        )

        source_document.additional_properties = d
        return source_document

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
