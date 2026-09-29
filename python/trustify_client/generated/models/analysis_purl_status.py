from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_head import AdvisoryHead
    from ..models.remediation_summary import RemediationSummary
    from ..models.scored_vector import ScoredVector
    from ..models.status_context_type_0 import StatusContextType0
    from ..models.status_context_type_1 import StatusContextType1
    from ..models.version_range_type_1 import VersionRangeType1
    from ..models.vulnerability_head import VulnerabilityHead


T = TypeVar("T", bound="AnalysisPurlStatus")


@_attrs_define
class AnalysisPurlStatus:
    """
    Attributes:
        advisory (AdvisoryHead):
        context (None | StatusContextType0 | StatusContextType1):
        fixed_versions (list[str]):
        scores (list[ScoredVector]): All CVSS scores associated with the vulnerability
        status (str):
        vulnerability (VulnerabilityHead):
        remediations (list[RemediationSummary]):
        version_range (None | Unset | VersionRangeType1):
    """

    advisory: AdvisoryHead
    context: None | StatusContextType0 | StatusContextType1
    fixed_versions: list[str]
    scores: list[ScoredVector]
    status: str
    vulnerability: VulnerabilityHead
    remediations: list[RemediationSummary]
    version_range: None | Unset | VersionRangeType1 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.status_context_type_0 import StatusContextType0
        from ..models.status_context_type_1 import StatusContextType1
        from ..models.version_range_type_1 import VersionRangeType1

        advisory = self.advisory.to_dict()

        context: dict[str, Any] | None
        if isinstance(self.context, StatusContextType0) or isinstance(
            self.context, StatusContextType1
        ):
            context = self.context.to_dict()
        else:
            context = self.context

        fixed_versions = self.fixed_versions

        scores = []
        for scores_item_data in self.scores:
            scores_item = scores_item_data.to_dict()
            scores.append(scores_item)

        status = self.status

        vulnerability = self.vulnerability.to_dict()

        remediations = []
        for remediations_item_data in self.remediations:
            remediations_item = remediations_item_data.to_dict()
            remediations.append(remediations_item)

        version_range: dict[str, Any] | None | Unset
        if isinstance(self.version_range, Unset):
            version_range = UNSET
        elif isinstance(self.version_range, VersionRangeType1):
            version_range = self.version_range.to_dict()
        else:
            version_range = self.version_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "advisory": advisory,
                "context": context,
                "fixed_versions": fixed_versions,
                "scores": scores,
                "status": status,
                "vulnerability": vulnerability,
                "remediations": remediations,
            }
        )
        if version_range is not UNSET:
            field_dict["version_range"] = version_range

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.advisory_head import AdvisoryHead
        from ..models.remediation_summary import RemediationSummary
        from ..models.scored_vector import ScoredVector
        from ..models.status_context_type_0 import StatusContextType0
        from ..models.status_context_type_1 import StatusContextType1
        from ..models.version_range_type_1 import VersionRangeType1
        from ..models.vulnerability_head import VulnerabilityHead

        d = dict(src_dict)
        advisory = AdvisoryHead.from_dict(d.pop("advisory"))

        def _parse_context(
            data: object,
        ) -> None | StatusContextType0 | StatusContextType1:
            if data is None:
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
            return cast(None | StatusContextType0 | StatusContextType1, data)

        context = _parse_context(d.pop("context"))

        fixed_versions = cast(list[str], d.pop("fixed_versions"))

        scores = []
        _scores = d.pop("scores")
        for scores_item_data in _scores:
            scores_item = ScoredVector.from_dict(scores_item_data)

            scores.append(scores_item)

        status = d.pop("status")

        vulnerability = VulnerabilityHead.from_dict(d.pop("vulnerability"))

        remediations = []
        _remediations = d.pop("remediations")
        for remediations_item_data in _remediations:
            remediations_item = RemediationSummary.from_dict(remediations_item_data)

            remediations.append(remediations_item)

        def _parse_version_range(data: object) -> None | Unset | VersionRangeType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_version_range_type_1 = VersionRangeType1.from_dict(
                    data
                )

                return componentsschemas_version_range_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VersionRangeType1, data)

        version_range = _parse_version_range(d.pop("version_range", UNSET))

        analysis_purl_status = cls(
            advisory=advisory,
            context=context,
            fixed_versions=fixed_versions,
            scores=scores,
            status=status,
            vulnerability=vulnerability,
            remediations=remediations,
            version_range=version_range,
        )

        analysis_purl_status.additional_properties = d
        return analysis_purl_status

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
