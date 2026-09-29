from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.labels import Labels


T = TypeVar("T", bound="CsafImporter")


@_attrs_define
class CsafImporter:
    """
    Attributes:
        period (str): The period the importer should be run.
        source (str):
        description (None | str | Unset): A description for users.
        disabled (bool | Unset): A flag to disable the importer, without deleting it.
        labels (Labels | Unset):
        fetch_retries (int | None | Unset):
        ignore_missing (bool | Unset):
        only_patterns (list[str] | Unset):
        v_3_signatures (bool | Unset):
    """

    period: str
    source: str
    description: None | str | Unset = UNSET
    disabled: bool | Unset = UNSET
    labels: Labels | Unset = UNSET
    fetch_retries: int | None | Unset = UNSET
    ignore_missing: bool | Unset = UNSET
    only_patterns: list[str] | Unset = UNSET
    v_3_signatures: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        source = self.source

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        disabled = self.disabled

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        fetch_retries: int | None | Unset
        if isinstance(self.fetch_retries, Unset):
            fetch_retries = UNSET
        else:
            fetch_retries = self.fetch_retries

        ignore_missing = self.ignore_missing

        only_patterns: list[str] | Unset = UNSET
        if not isinstance(self.only_patterns, Unset):
            only_patterns = self.only_patterns

        v_3_signatures = self.v_3_signatures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "source": source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if labels is not UNSET:
            field_dict["labels"] = labels
        if fetch_retries is not UNSET:
            field_dict["fetchRetries"] = fetch_retries
        if ignore_missing is not UNSET:
            field_dict["ignoreMissing"] = ignore_missing
        if only_patterns is not UNSET:
            field_dict["onlyPatterns"] = only_patterns
        if v_3_signatures is not UNSET:
            field_dict["v3Signatures"] = v_3_signatures

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.labels import Labels

        d = dict(src_dict)
        period = d.pop("period")

        source = d.pop("source")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        disabled = d.pop("disabled", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Labels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = Labels.from_dict(_labels)

        def _parse_fetch_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fetch_retries = _parse_fetch_retries(d.pop("fetchRetries", UNSET))

        ignore_missing = d.pop("ignoreMissing", UNSET)

        only_patterns = cast(list[str], d.pop("onlyPatterns", UNSET))

        v_3_signatures = d.pop("v3Signatures", UNSET)

        csaf_importer = cls(
            period=period,
            source=source,
            description=description,
            disabled=disabled,
            labels=labels,
            fetch_retries=fetch_retries,
            ignore_missing=ignore_missing,
            only_patterns=only_patterns,
            v_3_signatures=v_3_signatures,
        )

        csaf_importer.additional_properties = d
        return csaf_importer

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
