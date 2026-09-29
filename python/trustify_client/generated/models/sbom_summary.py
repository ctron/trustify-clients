from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.labels import Labels
    from ..models.requested_field_hash_map_hash_map_type_0 import (
        RequestedFieldHashMapHashMapType0,
    )
    from ..models.sbom_package import SbomPackage


T = TypeVar("T", bound="SbomSummary")


@_attrs_define
class SbomSummary:
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
        ingested (datetime.datetime): The timestamp the document was ingested
        sha256 (str):
        sha384 (str):
        sha512 (str):
        size (int):
        described_by (list[SbomPackage]):
        document_id (None | str | Unset):
        advisories (None | RequestedFieldHashMapHashMapType0 | Unset):
    """

    authors: list[str]
    data_licenses: list[str]
    id: str
    labels: Labels
    name: str
    number_of_packages: int
    published: datetime.datetime | None
    suppliers: list[str]
    ingested: datetime.datetime
    sha256: str
    sha384: str
    sha512: str
    size: int
    described_by: list[SbomPackage]
    document_id: None | str | Unset = UNSET
    advisories: None | RequestedFieldHashMapHashMapType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.requested_field_hash_map_hash_map_type_0 import (
            RequestedFieldHashMapHashMapType0,
        )

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

        ingested = self.ingested.isoformat()

        sha256 = self.sha256

        sha384 = self.sha384

        sha512 = self.sha512

        size = self.size

        described_by = []
        for described_by_item_data in self.described_by:
            described_by_item = described_by_item_data.to_dict()
            described_by.append(described_by_item)

        document_id: None | str | Unset
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        advisories: dict[str, Any] | None | Unset
        if isinstance(self.advisories, Unset):
            advisories = UNSET
        elif isinstance(self.advisories, RequestedFieldHashMapHashMapType0):
            advisories = self.advisories.to_dict()
        else:
            advisories = self.advisories

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
                "ingested": ingested,
                "sha256": sha256,
                "sha384": sha384,
                "sha512": sha512,
                "size": size,
                "described_by": described_by,
            }
        )
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if advisories is not UNSET:
            field_dict["advisories"] = advisories

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.labels import Labels
        from ..models.requested_field_hash_map_hash_map_type_0 import (
            RequestedFieldHashMapHashMapType0,
        )
        from ..models.sbom_package import SbomPackage

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

        ingested = datetime.datetime.fromisoformat(d.pop("ingested"))

        sha256 = d.pop("sha256")

        sha384 = d.pop("sha384")

        sha512 = d.pop("sha512")

        size = d.pop("size")

        described_by = []
        _described_by = d.pop("described_by")
        for described_by_item_data in _described_by:
            described_by_item = SbomPackage.from_dict(described_by_item_data)

            described_by.append(described_by_item)

        def _parse_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        def _parse_advisories(
            data: object,
        ) -> None | RequestedFieldHashMapHashMapType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_requested_field_hash_map_hash_map_type_0 = (
                    RequestedFieldHashMapHashMapType0.from_dict(data)
                )

                return componentsschemas_requested_field_hash_map_hash_map_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RequestedFieldHashMapHashMapType0 | Unset, data)

        advisories = _parse_advisories(d.pop("advisories", UNSET))

        sbom_summary = cls(
            authors=authors,
            data_licenses=data_licenses,
            id=id,
            labels=labels,
            name=name,
            number_of_packages=number_of_packages,
            published=published,
            suppliers=suppliers,
            ingested=ingested,
            sha256=sha256,
            sha384=sha384,
            sha512=sha512,
            size=size,
            described_by=described_by,
            document_id=document_id,
            advisories=advisories,
        )

        sbom_summary.additional_properties = d
        return sbom_summary

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
