from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_score import BaseScore
    from ..models.sbom_package import SbomPackage
    from ..models.scored_vector import ScoredVector
    from ..models.status_context_type_0 import StatusContextType0
    from ..models.status_context_type_1 import StatusContextType1


T = TypeVar("T", bound="SbomStatus")


@_attrs_define
class SbomStatus:
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
        fixed_versions (list[str]): Versions that fix this vulnerability, extracted from "fixed" advisory entries
        packages (list[SbomPackage]):
        scores (list[ScoredVector]):
        status (str):
        base_score (BaseScore | None | Unset): The main, base score.
        context (None | StatusContextType0 | StatusContextType1 | Unset):
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
    fixed_versions: list[str]
    packages: list[SbomPackage]
    scores: list[ScoredVector]
    status: str
    base_score: BaseScore | None | Unset = UNSET
    context: None | StatusContextType0 | StatusContextType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_score import BaseScore
        from ..models.status_context_type_0 import StatusContextType0
        from ..models.status_context_type_1 import StatusContextType1

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

        fixed_versions = self.fixed_versions

        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)

        scores = []
        for scores_item_data in self.scores:
            scores_item = scores_item_data.to_dict()
            scores.append(scores_item)

        status = self.status

        base_score: dict[str, Any] | None | Unset
        if isinstance(self.base_score, Unset):
            base_score = UNSET
        elif isinstance(self.base_score, BaseScore):
            base_score = self.base_score.to_dict()
        else:
            base_score = self.base_score

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, StatusContextType0) or isinstance(
            self.context, StatusContextType1
        ):
            context = self.context.to_dict()
        else:
            context = self.context

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
                "fixed_versions": fixed_versions,
                "packages": packages,
                "scores": scores,
                "status": status,
            }
        )
        if base_score is not UNSET:
            field_dict["base_score"] = base_score
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_score import BaseScore
        from ..models.sbom_package import SbomPackage
        from ..models.scored_vector import ScoredVector
        from ..models.status_context_type_0 import StatusContextType0
        from ..models.status_context_type_1 import StatusContextType1

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

        fixed_versions = cast(list[str], d.pop("fixed_versions"))

        packages = []
        _packages = d.pop("packages")
        for packages_item_data in _packages:
            packages_item = SbomPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        scores = []
        _scores = d.pop("scores")
        for scores_item_data in _scores:
            scores_item = ScoredVector.from_dict(scores_item_data)

            scores.append(scores_item)

        status = d.pop("status")

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

        def _parse_context(
            data: object,
        ) -> None | StatusContextType0 | StatusContextType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_status_context_type_0 = StatusContextType0.from_dict(
                    data
                )

                return componentsschemas_status_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_status_context_type_1 = StatusContextType1.from_dict(
                    data
                )

                return componentsschemas_status_context_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StatusContextType0 | StatusContextType1 | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        sbom_status = cls(
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
            fixed_versions=fixed_versions,
            packages=packages,
            scores=scores,
            status=status,
            base_score=base_score,
            context=context,
        )

        sbom_status.additional_properties = d
        return sbom_status

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
