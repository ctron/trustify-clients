from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recommend_response_recommendations import (
        RecommendResponseRecommendations,
    )


T = TypeVar("T", bound="RecommendResponse")


@_attrs_define
class RecommendResponse:
    """
    Attributes:
        recommendations (RecommendResponseRecommendations):
    """

    recommendations: RecommendResponseRecommendations
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recommendations = self.recommendations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recommendations": recommendations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.recommend_response_recommendations import (
            RecommendResponseRecommendations,
        )

        d = dict(src_dict)
        recommendations = RecommendResponseRecommendations.from_dict(
            d.pop("recommendations")
        )

        recommend_response = cls(
            recommendations=recommendations,
        )

        recommend_response.additional_properties = d
        return recommend_response

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
