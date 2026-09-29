from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report import Report


T = TypeVar("T", bound="ImporterReport")


@_attrs_define
class ImporterReport:
    """
    Attributes:
        creation (datetime.datetime): The time the report was created
        id (str): The ID of the report
        importer (str): The name of the importer this report belongs to
        error (None | str | Unset): Errors captured by the report
        report (None | Report | Unset): Detailed report information
    """

    creation: datetime.datetime
    id: str
    importer: str
    error: None | str | Unset = UNSET
    report: None | Report | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.report import Report

        creation = self.creation.isoformat()

        id = self.id

        importer = self.importer

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        report: dict[str, Any] | None | Unset
        if isinstance(self.report, Unset):
            report = UNSET
        elif isinstance(self.report, Report):
            report = self.report.to_dict()
        else:
            report = self.report

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creation": creation,
                "id": id,
                "importer": importer,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if report is not UNSET:
            field_dict["report"] = report

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report import Report

        d = dict(src_dict)
        creation = datetime.datetime.fromisoformat(d.pop("creation"))

        id = d.pop("id")

        importer = d.pop("importer")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_report(data: object) -> None | Report | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_type_1 = Report.from_dict(data)

                return report_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Report | Unset, data)

        report = _parse_report(d.pop("report", UNSET))

        importer_report = cls(
            creation=creation,
            id=id,
            importer=importer,
            error=error,
            report=report,
        )

        importer_report.additional_properties = d
        return importer_report

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
