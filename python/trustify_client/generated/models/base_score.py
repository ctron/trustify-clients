from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.score_type import ScoreType
from ..models.severity import Severity

T = TypeVar("T", bound="BaseScore")


@_attrs_define
class BaseScore:
    """Base score information in the context of a [`VulnerabilityHead`]. Notably, this excludes the
    raw CVSS vector string.

    Uses the same `ScoreType` and `Severity` serialization as [`crate::common::model::Score`]
    so that all score-related fields in API responses are consistent.

        Attributes:
            score (float):
            severity (Severity): Severity rating derived from a CVSS score value.
            type_ (ScoreType): The type of score, indicating the scoring system and version used.
    """

    score: float
    severity: Severity
    type_: ScoreType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        severity = self.severity.value

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "score": score,
                "severity": severity,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        score = d.pop("score")

        severity = Severity(d.pop("severity"))

        type_ = ScoreType(d.pop("type"))

        base_score = cls(
            score=score,
            severity=severity,
            type_=type_,
        )

        base_score.additional_properties = d
        return base_score

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
