from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.report_messages_additional_property import (
        ReportMessagesAdditionalProperty,
    )


T = TypeVar("T", bound="ReportMessages")


@_attrs_define
class ReportMessages:
    """Messages emitted during processing"""

    additional_properties: dict[str, ReportMessagesAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report_messages_additional_property import (
            ReportMessagesAdditionalProperty,
        )

        d = dict(src_dict)
        report_messages = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ReportMessagesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        report_messages.additional_properties = additional_properties
        return report_messages

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ReportMessagesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ReportMessagesAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
