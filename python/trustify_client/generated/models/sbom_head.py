from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.labels import Labels


T = TypeVar("T", bound="SbomHead")


@_attrs_define
class SbomHead:
    """
    Attributes:
        authors (list[str]): Authors of the SBOM
        data_licenses (list[str]):
        id (str):
        labels (Labels):
        name (str):
        number_of_packages (int): The number of packages this SBOM has
        published (datetime.datetime | None):
        suppliers (list[str]): Suppliers of the SBOMs content
        document_id (None | str | Unset):
    """

    authors: list[str]
    data_licenses: list[str]
    id: str
    labels: Labels
    name: str
    number_of_packages: int
    published: datetime.datetime | None
    suppliers: list[str]
    document_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authors = self.authors

        data_licenses = self.data_licenses

        id = self.id

        labels = self.labels.to_dict()

        name = self.name

        number_of_packages = self.number_of_packages

        published: None | str
        if isinstance(self.published, datetime.datetime):
            published = self.published.isoformat()
        else:
            published = self.published

        suppliers = self.suppliers

        document_id: None | str | Unset
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authors": authors,
                "data_licenses": data_licenses,
                "id": id,
                "labels": labels,
                "name": name,
                "number_of_packages": number_of_packages,
                "published": published,
                "suppliers": suppliers,
            }
        )
        if document_id is not UNSET:
            field_dict["document_id"] = document_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.labels import Labels

        d = dict(src_dict)
        authors = cast(list[str], d.pop("authors"))

        data_licenses = cast(list[str], d.pop("data_licenses"))

        id = d.pop("id")

        labels = Labels.from_dict(d.pop("labels"))

        name = d.pop("name")

        number_of_packages = d.pop("number_of_packages")

        def _parse_published(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_type_0 = datetime.datetime.fromisoformat(data)

                return published_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        published = _parse_published(d.pop("published"))

        suppliers = cast(list[str], d.pop("suppliers"))

        def _parse_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        sbom_head = cls(
            authors=authors,
            data_licenses=data_licenses,
            id=id,
            labels=labels,
            name=name,
            number_of_packages=number_of_packages,
            published=published,
            suppliers=suppliers,
            document_id=document_id,
        )

        sbom_head.additional_properties = d
        return sbom_head

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
