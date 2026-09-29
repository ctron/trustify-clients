from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.score_type import ScoreType
from ..models.severity import Severity

T = TypeVar("T", bound="Score")


@_attrs_define
class Score:
    """A parsed CVSS score: the scoring system version, numeric value, and derived severity.

    Example:
        {'type': '3.1', 'value': 7.5, 'severity': 'high'}

    Attributes:
        severity (Severity): Severity rating derived from a CVSS score value.
        type_ (ScoreType): The type of score, indicating the scoring system and version used.
        value (float): The numeric score, rounded to one decimal place.
    """

    severity: Severity
    type_: ScoreType
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity = self.severity.value

        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        severity = Severity(d.pop("severity"))

        type_ = ScoreType(d.pop("type"))

        value = d.pop("value")

        score = cls(
            severity=severity,
            type_=type_,
            value=value,
        )

        score.additional_properties = d
        return score

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
