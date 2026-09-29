from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.score_type import ScoreType
from ..models.severity import Severity

T = TypeVar("T", bound="ScoredVector")


@_attrs_define
class ScoredVector:
    """A CVSS score combined with its raw vector string, for contexts where clients need both
    the pre-parsed numeric values and the original vector for display or re-parsing.

        Example:
            {'type': '3.1', 'value': 7.5, 'severity': 'high', 'vector': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H'}

        Attributes:
            severity (Severity): Severity rating derived from a CVSS score value.
            type_ (ScoreType): The type of score, indicating the scoring system and version used.
            value (float): The numeric score, rounded to one decimal place.
            vector (str): The raw CVSS vector string (e.g. `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`).
    """

    severity: Severity
    type_: ScoreType
    value: float
    vector: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity = self.severity.value

        type_ = self.type_.value

        value = self.value

        vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
                "type": type_,
                "value": value,
                "vector": vector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        severity = Severity(d.pop("severity"))

        type_ = ScoreType(d.pop("type"))

        value = d.pop("value")

        vector = d.pop("vector")

        scored_vector = cls(
            severity=severity,
            type_=type_,
            value=value,
            vector=vector,
        )

        scored_vector.additional_properties = d
        return scored_vector

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
