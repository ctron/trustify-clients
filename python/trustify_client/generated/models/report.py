from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_messages import ReportMessages


T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """
    Attributes:
        end_date (datetime.datetime): End of the import run
        start_date (datetime.datetime): Start of the import run
        messages (ReportMessages | Unset): Messages emitted during processing
        number_of_items (int | Unset): Number of processes items
    """

    end_date: datetime.datetime
    start_date: datetime.datetime
    messages: ReportMessages | Unset = UNSET
    number_of_items: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date.isoformat()

        start_date = self.start_date.isoformat()

        messages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages.to_dict()

        number_of_items = self.number_of_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endDate": end_date,
                "startDate": start_date,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages
        if number_of_items is not UNSET:
            field_dict["numberOfItems"] = number_of_items

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report_messages import ReportMessages

        d = dict(src_dict)
        end_date = datetime.datetime.fromisoformat(d.pop("endDate"))

        start_date = datetime.datetime.fromisoformat(d.pop("startDate"))

        _messages = d.pop("messages", UNSET)
        messages: ReportMessages | Unset
        if isinstance(_messages, Unset):
            messages = UNSET
        else:
            messages = ReportMessages.from_dict(_messages)

        number_of_items = d.pop("numberOfItems", UNSET)

        report = cls(
            end_date=end_date,
            start_date=start_date,
            messages=messages,
            number_of_items=number_of_items,
        )

        report.additional_properties = d
        return report

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
