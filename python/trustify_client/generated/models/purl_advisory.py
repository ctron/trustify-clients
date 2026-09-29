from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.labels import Labels
    from ..models.organization_head import OrganizationHead
    from ..models.purl_status import PurlStatus


T = TypeVar("T", bound="PurlAdvisory")


@_attrs_define
class PurlAdvisory:
    """
    Attributes:
        document_id (str): The identifier of the advisory, as provided by the document.
        identifier (str): The identifier of the advisory, as assigned by the issuing organization.
        issuer (None | OrganizationHead): The issuer of the advisory, if known. If no issuer is able to be
            determined, this field will not be included in a response.
        labels (Labels):
        published (datetime.datetime | None): The date (in RFC3339 format) of when the advisory was published, if any.
        title (None | str): The title of the advisory as assigned by the issuing organization.
        uuid (str): The opaque UUID of the advisory.
        withdrawn (datetime.datetime | None): The date (in RFC3339 format) of when the advisory was withdrawn, if any.
        status (list[PurlStatus]):
        modified (datetime.datetime | None | Unset): The date (in RFC3339 format) of when the advisory was last
            modified, if any.
    """

    document_id: str
    identifier: str
    issuer: None | OrganizationHead
    labels: Labels
    published: datetime.datetime | None
    title: None | str
    uuid: str
    withdrawn: datetime.datetime | None
    status: list[PurlStatus]
    modified: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_head import OrganizationHead

        document_id = self.document_id

        identifier = self.identifier

        issuer: dict[str, Any] | None
        if isinstance(self.issuer, OrganizationHead):
            issuer = self.issuer.to_dict()
        else:
            issuer = self.issuer

        labels = self.labels.to_dict()

        published: None | str
        if isinstance(self.published, datetime.datetime):
            published = self.published.isoformat()
        else:
            published = self.published

        title: None | str
        title = self.title

        uuid = self.uuid

        withdrawn: None | str
        if isinstance(self.withdrawn, datetime.datetime):
            withdrawn = self.withdrawn.isoformat()
        else:
            withdrawn = self.withdrawn

        status = []
        for status_item_data in self.status:
            status_item = status_item_data.to_dict()
            status.append(status_item)

        modified: None | str | Unset
        if isinstance(self.modified, Unset):
            modified = UNSET
        elif isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_id": document_id,
                "identifier": identifier,
                "issuer": issuer,
                "labels": labels,
                "published": published,
                "title": title,
                "uuid": uuid,
                "withdrawn": withdrawn,
                "status": status,
            }
        )
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.labels import Labels
        from ..models.organization_head import OrganizationHead
        from ..models.purl_status import PurlStatus

        d = dict(src_dict)
        document_id = d.pop("document_id")

        identifier = d.pop("identifier")

        def _parse_issuer(data: object) -> None | OrganizationHead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                issuer_type_1 = OrganizationHead.from_dict(data)

                return issuer_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationHead, data)

        issuer = _parse_issuer(d.pop("issuer"))

        labels = Labels.from_dict(d.pop("labels"))

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

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        uuid = d.pop("uuid")

        def _parse_withdrawn(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                withdrawn_type_0 = datetime.datetime.fromisoformat(data)

                return withdrawn_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        withdrawn = _parse_withdrawn(d.pop("withdrawn"))

        status = []
        _status = d.pop("status")
        for status_item_data in _status:
            status_item = PurlStatus.from_dict(status_item_data)

            status.append(status_item)

        def _parse_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = datetime.datetime.fromisoformat(data)

                return modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        modified = _parse_modified(d.pop("modified", UNSET))

        purl_advisory = cls(
            document_id=document_id,
            identifier=identifier,
            issuer=issuer,
            labels=labels,
            published=published,
            title=title,
            uuid=uuid,
            withdrawn=withdrawn,
            status=status,
            modified=modified,
        )

        purl_advisory.additional_properties = d
        return purl_advisory

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
