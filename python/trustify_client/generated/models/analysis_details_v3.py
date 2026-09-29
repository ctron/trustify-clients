from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_purl_status import AnalysisPurlStatus
    from ..models.base_score import BaseScore


T = TypeVar("T", bound="AnalysisDetailsV3")


@_attrs_define
class AnalysisDetailsV3:
    """
    Attributes:
        cwes (list[str]): Associated CWE, if any.
        description (None | str): The description of the vulnerability, if known.
        discovered (datetime.datetime | None): The date (in RFC3339 format) of when the vulnerability was discovered, if
            any.
        identifier (str): The globally-unique identifier for the vulnerability.
            Traditionally (but not required) refers to the assigned
            CVE identifier.
        modified (datetime.datetime | None): The date (in RFC3339 format) of when the vulnerability was last modified,
            if any.
        normative (bool):
        published (datetime.datetime | None): The date (in RFC3339 format) of when the vulnerability was published, if
            any.
        released (datetime.datetime | None): The date (in RFC3339 format) of when software containing the vulnerability
            first released, if known.
        reserved (datetime.datetime | None): The date (in RFC3339 format) of when the vulnerability identifier was
            reserved, if any.
        title (None | str): The title of the vulnerability, if known.
        withdrawn (datetime.datetime | None): The date (in RFC3339 format) of when the vulnerability was last withdrawn,
            if any.
        purl_statuses (list[AnalysisPurlStatus]): List of purl statuses & remediations
        base_score (BaseScore | None | Unset): The main, base score.
    """

    cwes: list[str]
    description: None | str
    discovered: datetime.datetime | None
    identifier: str
    modified: datetime.datetime | None
    normative: bool
    published: datetime.datetime | None
    released: datetime.datetime | None
    reserved: datetime.datetime | None
    title: None | str
    withdrawn: datetime.datetime | None
    purl_statuses: list[AnalysisPurlStatus]
    base_score: BaseScore | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_score import BaseScore

        cwes = self.cwes

        description: None | str
        description = self.description

        discovered: None | str
        if isinstance(self.discovered, datetime.datetime):
            discovered = self.discovered.isoformat()
        else:
            discovered = self.discovered

        identifier = self.identifier

        modified: None | str
        if isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        normative = self.normative

        published: None | str
        if isinstance(self.published, datetime.datetime):
            published = self.published.isoformat()
        else:
            published = self.published

        released: None | str
        if isinstance(self.released, datetime.datetime):
            released = self.released.isoformat()
        else:
            released = self.released

        reserved: None | str
        if isinstance(self.reserved, datetime.datetime):
            reserved = self.reserved.isoformat()
        else:
            reserved = self.reserved

        title: None | str
        title = self.title

        withdrawn: None | str
        if isinstance(self.withdrawn, datetime.datetime):
            withdrawn = self.withdrawn.isoformat()
        else:
            withdrawn = self.withdrawn

        purl_statuses = []
        for purl_statuses_item_data in self.purl_statuses:
            purl_statuses_item = purl_statuses_item_data.to_dict()
            purl_statuses.append(purl_statuses_item)

        base_score: dict[str, Any] | None | Unset
        if isinstance(self.base_score, Unset):
            base_score = UNSET
        elif isinstance(self.base_score, BaseScore):
            base_score = self.base_score.to_dict()
        else:
            base_score = self.base_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cwes": cwes,
                "description": description,
                "discovered": discovered,
                "identifier": identifier,
                "modified": modified,
                "normative": normative,
                "published": published,
                "released": released,
                "reserved": reserved,
                "title": title,
                "withdrawn": withdrawn,
                "purl_statuses": purl_statuses,
            }
        )
        if base_score is not UNSET:
            field_dict["base_score"] = base_score

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analysis_purl_status import AnalysisPurlStatus
        from ..models.base_score import BaseScore

        d = dict(src_dict)
        cwes = cast(list[str], d.pop("cwes"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_discovered(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discovered_type_0 = datetime.datetime.fromisoformat(data)

                return discovered_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        discovered = _parse_discovered(d.pop("discovered"))

        identifier = d.pop("identifier")

        def _parse_modified(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = datetime.datetime.fromisoformat(data)

                return modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        modified = _parse_modified(d.pop("modified"))

        normative = d.pop("normative")

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

        def _parse_released(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                released_type_0 = datetime.datetime.fromisoformat(data)

                return released_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        released = _parse_released(d.pop("released"))

        def _parse_reserved(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reserved_type_0 = datetime.datetime.fromisoformat(data)

                return reserved_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        reserved = _parse_reserved(d.pop("reserved"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

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

        purl_statuses = []
        _purl_statuses = d.pop("purl_statuses")
        for purl_statuses_item_data in _purl_statuses:
            purl_statuses_item = AnalysisPurlStatus.from_dict(purl_statuses_item_data)

            purl_statuses.append(purl_statuses_item)

        def _parse_base_score(data: object) -> BaseScore | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                base_score_type_1 = BaseScore.from_dict(data)

                return base_score_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseScore | None | Unset, data)

        base_score = _parse_base_score(d.pop("base_score", UNSET))

        analysis_details_v3 = cls(
            cwes=cwes,
            description=description,
            discovered=discovered,
            identifier=identifier,
            modified=modified,
            normative=normative,
            published=published,
            released=released,
            reserved=reserved,
            title=title,
            withdrawn=withdrawn,
            purl_statuses=purl_statuses,
            base_score=base_score,
        )

        analysis_details_v3.additional_properties = d
        return analysis_details_v3

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
