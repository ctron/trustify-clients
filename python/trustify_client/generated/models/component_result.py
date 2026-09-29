from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exploit_intelligence_finding import ExploitIntelligenceFinding
from ..models.exploit_intelligence_job_status import ExploitIntelligenceJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentResult")


@_attrs_define
class ComponentResult:
    """Per-component analysis result within an analysis job.

    Attributes:
        component_ref (str): Identifier of the component (purl or container image reference).
        created (str): Timestamp when the component record was created.
        excluded (bool): Whether this component was excluded by the EI service (e.g.,
            unsupported ecosystem) rather than genuinely failing.
        id (UUID): The unique component record identifier.
        status (ExploitIntelligenceJobStatus): Lifecycle status of an Exploit Intelligence analysis job.
        updated (str): Timestamp when the component record was last updated.
        advisory_id (None | Unset | UUID): FK to advisory — set when a VEX document is ingested from the result.
        finding (ExploitIntelligenceFinding | None | Unset): Analysis result from Exploit Intelligence, if completed.
        report_url (None | str | Unset): Link to the EI human-readable justification report for this component.
    """

    component_ref: str
    created: str
    excluded: bool
    id: UUID
    status: ExploitIntelligenceJobStatus
    updated: str
    advisory_id: None | Unset | UUID = UNSET
    finding: ExploitIntelligenceFinding | None | Unset = UNSET
    report_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_ref = self.component_ref

        created = self.created

        excluded = self.excluded

        id = str(self.id)

        status = self.status.value

        updated = self.updated

        advisory_id: None | str | Unset
        if isinstance(self.advisory_id, Unset):
            advisory_id = UNSET
        elif isinstance(self.advisory_id, UUID):
            advisory_id = str(self.advisory_id)
        else:
            advisory_id = self.advisory_id

        finding: None | str | Unset
        if isinstance(self.finding, Unset):
            finding = UNSET
        elif isinstance(self.finding, ExploitIntelligenceFinding):
            finding = self.finding.value
        else:
            finding = self.finding

        report_url: None | str | Unset
        if isinstance(self.report_url, Unset):
            report_url = UNSET
        else:
            report_url = self.report_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_ref": component_ref,
                "created": created,
                "excluded": excluded,
                "id": id,
                "status": status,
                "updated": updated,
            }
        )
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id
        if finding is not UNSET:
            field_dict["finding"] = finding
        if report_url is not UNSET:
            field_dict["report_url"] = report_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component_ref = d.pop("component_ref")

        created = d.pop("created")

        excluded = d.pop("excluded")

        id = UUID(d.pop("id"))

        status = ExploitIntelligenceJobStatus(d.pop("status"))

        updated = d.pop("updated")

        def _parse_advisory_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                advisory_id_type_0 = UUID(data)

                return advisory_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        advisory_id = _parse_advisory_id(d.pop("advisory_id", UNSET))

        def _parse_finding(data: object) -> ExploitIntelligenceFinding | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finding_type_1 = ExploitIntelligenceFinding(data)

                return finding_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExploitIntelligenceFinding | None | Unset, data)

        finding = _parse_finding(d.pop("finding", UNSET))

        def _parse_report_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_url = _parse_report_url(d.pop("report_url", UNSET))

        component_result = cls(
            component_ref=component_ref,
            created=created,
            excluded=excluded,
            id=id,
            status=status,
            updated=updated,
            advisory_id=advisory_id,
            finding=finding,
            report_url=report_url,
        )

        component_result.additional_properties = d
        return component_result

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
