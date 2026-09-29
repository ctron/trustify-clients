from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProgressDetails")


@_attrs_define
class ProgressDetails:
    """
    Attributes:
        current (int): The current processed items.
        estimated_completion (datetime.datetime): The estimated time of completion.
        estimated_seconds_remaining (int): The estimated remaining time in seconds.
        percent (float): Progress in percent (0..=1)
        rate (float): The average processing rate (per second).
        total (int): The total number of items to be processed.
    """

    current: int
    estimated_completion: datetime.datetime
    estimated_seconds_remaining: int
    percent: float
    rate: float
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = self.current

        estimated_completion = self.estimated_completion.isoformat()

        estimated_seconds_remaining = self.estimated_seconds_remaining

        percent = self.percent

        rate = self.rate

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "estimatedCompletion": estimated_completion,
                "estimatedSecondsRemaining": estimated_seconds_remaining,
                "percent": percent,
                "rate": rate,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        current = d.pop("current")

        estimated_completion = datetime.datetime.fromisoformat(
            d.pop("estimatedCompletion")
        )

        estimated_seconds_remaining = d.pop("estimatedSecondsRemaining")

        percent = d.pop("percent")

        rate = d.pop("rate")

        total = d.pop("total")

        progress_details = cls(
            current=current,
            estimated_completion=estimated_completion,
            estimated_seconds_remaining=estimated_seconds_remaining,
            percent=percent,
            rate=rate,
            total=total,
        )

        progress_details.additional_properties = d
        return progress_details

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
