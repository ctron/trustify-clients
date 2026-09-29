from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state import State
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.importer_configuration_type_0 import ImporterConfigurationType0
    from ..models.importer_configuration_type_1 import ImporterConfigurationType1
    from ..models.importer_configuration_type_2 import ImporterConfigurationType2
    from ..models.importer_configuration_type_3 import ImporterConfigurationType3
    from ..models.importer_configuration_type_4 import ImporterConfigurationType4
    from ..models.importer_configuration_type_5 import ImporterConfigurationType5
    from ..models.importer_configuration_type_6 import ImporterConfigurationType6
    from ..models.importer_configuration_type_7 import ImporterConfigurationType7
    from ..models.importer_configuration_type_8 import ImporterConfigurationType8
    from ..models.importer_configuration_type_9 import ImporterConfigurationType9
    from ..models.importer_configuration_type_10 import ImporterConfigurationType10
    from ..models.progress import Progress


T = TypeVar("T", bound="RevisionedImporterValue")


@_attrs_define
class RevisionedImporterValue:
    """
    Attributes:
        configuration (ImporterConfigurationType0 | ImporterConfigurationType1 | ImporterConfigurationType10 |
            ImporterConfigurationType2 | ImporterConfigurationType3 | ImporterConfigurationType4 |
            ImporterConfigurationType5 | ImporterConfigurationType6 | ImporterConfigurationType7 |
            ImporterConfigurationType8 | ImporterConfigurationType9):
        last_change (datetime.datetime): The last state change
        state (State):
        name (str):
        continuation (Any | Unset): The continuation token of the importer.
        last_error (None | str | Unset): The error of the last run (empty if successful)
        last_run (datetime.datetime | None | Unset): The last run (successful or not)
        last_success (datetime.datetime | None | Unset): The last successful run
        progress (Progress | Unset):
    """

    configuration: (
        ImporterConfigurationType0
        | ImporterConfigurationType1
        | ImporterConfigurationType10
        | ImporterConfigurationType2
        | ImporterConfigurationType3
        | ImporterConfigurationType4
        | ImporterConfigurationType5
        | ImporterConfigurationType6
        | ImporterConfigurationType7
        | ImporterConfigurationType8
        | ImporterConfigurationType9
    )
    last_change: datetime.datetime
    state: State
    name: str
    continuation: Any | Unset = UNSET
    last_error: None | str | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    last_success: datetime.datetime | None | Unset = UNSET
    progress: Progress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.importer_configuration_type_0 import (
            ImporterConfigurationType0,
        )
        from ..models.importer_configuration_type_1 import (
            ImporterConfigurationType1,
        )
        from ..models.importer_configuration_type_2 import (
            ImporterConfigurationType2,
        )
        from ..models.importer_configuration_type_3 import (
            ImporterConfigurationType3,
        )
        from ..models.importer_configuration_type_4 import (
            ImporterConfigurationType4,
        )
        from ..models.importer_configuration_type_5 import (
            ImporterConfigurationType5,
        )
        from ..models.importer_configuration_type_6 import (
            ImporterConfigurationType6,
        )
        from ..models.importer_configuration_type_7 import (
            ImporterConfigurationType7,
        )
        from ..models.importer_configuration_type_8 import (
            ImporterConfigurationType8,
        )
        from ..models.importer_configuration_type_9 import (
            ImporterConfigurationType9,
        )

        configuration: dict[str, Any]
        if (
            isinstance(self.configuration, ImporterConfigurationType0)
            or isinstance(self.configuration, ImporterConfigurationType1)
            or isinstance(self.configuration, ImporterConfigurationType2)
            or isinstance(self.configuration, ImporterConfigurationType3)
            or isinstance(self.configuration, ImporterConfigurationType4)
            or isinstance(self.configuration, ImporterConfigurationType5)
            or isinstance(self.configuration, ImporterConfigurationType6)
            or isinstance(self.configuration, ImporterConfigurationType7)
            or isinstance(self.configuration, ImporterConfigurationType8)
            or isinstance(self.configuration, ImporterConfigurationType9)
        ):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration.to_dict()

        last_change = self.last_change.isoformat()

        state = self.state.value

        name = self.name

        continuation = self.continuation

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        last_run: None | str | Unset
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_success: None | str | Unset
        if isinstance(self.last_success, Unset):
            last_success = UNSET
        elif isinstance(self.last_success, datetime.datetime):
            last_success = self.last_success.isoformat()
        else:
            last_success = self.last_success

        progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "lastChange": last_change,
                "state": state,
                "name": name,
            }
        )
        if continuation is not UNSET:
            field_dict["continuation"] = continuation
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_success is not UNSET:
            field_dict["lastSuccess"] = last_success
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.importer_configuration_type_0 import (
            ImporterConfigurationType0,
        )
        from ..models.importer_configuration_type_1 import (
            ImporterConfigurationType1,
        )
        from ..models.importer_configuration_type_2 import (
            ImporterConfigurationType2,
        )
        from ..models.importer_configuration_type_3 import (
            ImporterConfigurationType3,
        )
        from ..models.importer_configuration_type_4 import (
            ImporterConfigurationType4,
        )
        from ..models.importer_configuration_type_5 import (
            ImporterConfigurationType5,
        )
        from ..models.importer_configuration_type_6 import (
            ImporterConfigurationType6,
        )
        from ..models.importer_configuration_type_7 import (
            ImporterConfigurationType7,
        )
        from ..models.importer_configuration_type_8 import (
            ImporterConfigurationType8,
        )
        from ..models.importer_configuration_type_9 import (
            ImporterConfigurationType9,
        )
        from ..models.importer_configuration_type_10 import (
            ImporterConfigurationType10,
        )
        from ..models.progress import Progress

        d = dict(src_dict)

        def _parse_configuration(
            data: object,
        ) -> (
            ImporterConfigurationType0
            | ImporterConfigurationType1
            | ImporterConfigurationType10
            | ImporterConfigurationType2
            | ImporterConfigurationType3
            | ImporterConfigurationType4
            | ImporterConfigurationType5
            | ImporterConfigurationType6
            | ImporterConfigurationType7
            | ImporterConfigurationType8
            | ImporterConfigurationType9
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_0 = (
                    ImporterConfigurationType0.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_1 = (
                    ImporterConfigurationType1.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_2 = (
                    ImporterConfigurationType2.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_3 = (
                    ImporterConfigurationType3.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_4 = (
                    ImporterConfigurationType4.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_5 = (
                    ImporterConfigurationType5.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_6 = (
                    ImporterConfigurationType6.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_7 = (
                    ImporterConfigurationType7.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_8 = (
                    ImporterConfigurationType8.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_importer_configuration_type_9 = (
                    ImporterConfigurationType9.from_dict(data)
                )

                return componentsschemas_importer_configuration_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_importer_configuration_type_10 = (
                ImporterConfigurationType10.from_dict(data)
            )

            return componentsschemas_importer_configuration_type_10

        configuration = _parse_configuration(d.pop("configuration"))

        last_change = datetime.datetime.fromisoformat(d.pop("lastChange"))

        state = State(d.pop("state"))

        name = d.pop("name")

        continuation = d.pop("continuation", UNSET)

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))

        def _parse_last_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = datetime.datetime.fromisoformat(data)

                return last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        def _parse_last_success(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_type_0 = datetime.datetime.fromisoformat(data)

                return last_success_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_success = _parse_last_success(d.pop("lastSuccess", UNSET))

        _progress = d.pop("progress", UNSET)
        progress: Progress | Unset
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = Progress.from_dict(_progress)

        revisioned_importer_value = cls(
            configuration=configuration,
            last_change=last_change,
            state=state,
            name=name,
            continuation=continuation,
            last_error=last_error,
            last_run=last_run,
            last_success=last_success,
            progress=progress,
        )

        revisioned_importer_value.additional_properties = d
        return revisioned_importer_value

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
