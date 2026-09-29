from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.labels import Labels


T = TypeVar("T", bound="OsvImporter")


@_attrs_define
class OsvImporter:
    """
    Attributes:
        period (str): The period the importer should be run.
        source (str): The URL to the git repository of the OSV data
        description (None | str | Unset): A description for users.
        disabled (bool | Unset): A flag to disable the importer, without deleting it.
        labels (Labels | Unset):
        branch (None | str | Unset): An optional branch. Will use the default branch otherwise.
        path (None | str | Unset): An optional path to start searching for documents. Will use the root of the
            repository otherwise.
        start_year (int | None | Unset):
        years (list[int] | Unset):
    """

    period: str
    source: str
    description: None | str | Unset = UNSET
    disabled: bool | Unset = UNSET
    labels: Labels | Unset = UNSET
    branch: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    start_year: int | None | Unset = UNSET
    years: list[int] | Unset = UNSET
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

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        start_year: int | None | Unset
        if isinstance(self.start_year, Unset):
            start_year = UNSET
        else:
            start_year = self.start_year

        years: list[int] | Unset = UNSET
        if not isinstance(self.years, Unset):
            years = self.years

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
        if branch is not UNSET:
            field_dict["branch"] = branch
        if path is not UNSET:
            field_dict["path"] = path
        if start_year is not UNSET:
            field_dict["startYear"] = start_year
        if years is not UNSET:
            field_dict["years"] = years

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

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_start_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_year = _parse_start_year(d.pop("startYear", UNSET))

        years = cast(list[int], d.pop("years", UNSET))

        osv_importer = cls(
            period=period,
            source=source,
            description=description,
            disabled=disabled,
            labels=labels,
            branch=branch,
            path=path,
            start_year=start_year,
            years=years,
        )

        osv_importer.additional_properties = d
        return osv_importer

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
