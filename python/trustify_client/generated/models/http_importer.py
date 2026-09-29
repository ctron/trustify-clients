from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_config import AuthConfig
    from ..models.http_discovery_type_0 import HttpDiscoveryType0
    from ..models.labels import Labels


T = TypeVar("T", bound="HttpImporter")


@_attrs_define
class HttpImporter:
    """Configuration for the HTTP-based importer.

    Fetches documents from an HTTP repository, using a pluggable
    discovery strategy to enumerate files and an optional credential
    for authenticated sources.

        Attributes:
            period (str): The period the importer should be run.
            discovery (HttpDiscoveryType0): Pluggable file-discovery strategy for the HTTP importer.
            source (str): Base URL of the HTTP repository to import documents from.
            description (None | str | Unset): A description for users.
            disabled (bool | Unset): A flag to disable the importer, without deleting it.
            labels (Labels | Unset):
            auth (AuthConfig | None | Unset): Optional authentication configuration for accessing the source.
            fetch_retries (int | None | Unset): Number of fetch retries for individual file downloads.
                Defaults to the fetcher's built-in retry count when absent.
            only_patterns (list[str] | Unset): Optional list of regex patterns restricting which discovered files are
                imported. An empty list imports all discovered files.
    """

    period: str
    discovery: HttpDiscoveryType0
    source: str
    description: None | str | Unset = UNSET
    disabled: bool | Unset = UNSET
    labels: Labels | Unset = UNSET
    auth: AuthConfig | None | Unset = UNSET
    fetch_retries: int | None | Unset = UNSET
    only_patterns: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_config import AuthConfig
        from ..models.http_discovery_type_0 import HttpDiscoveryType0

        period = self.period

        discovery: dict[str, Any]
        if isinstance(self.discovery, HttpDiscoveryType0):
            discovery = self.discovery.to_dict()

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

        auth: dict[str, Any] | None | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, AuthConfig):
            auth = self.auth.to_dict()
        else:
            auth = self.auth

        fetch_retries: int | None | Unset
        if isinstance(self.fetch_retries, Unset):
            fetch_retries = UNSET
        else:
            fetch_retries = self.fetch_retries

        only_patterns: list[str] | Unset = UNSET
        if not isinstance(self.only_patterns, Unset):
            only_patterns = self.only_patterns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "discovery": discovery,
                "source": source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if labels is not UNSET:
            field_dict["labels"] = labels
        if auth is not UNSET:
            field_dict["auth"] = auth
        if fetch_retries is not UNSET:
            field_dict["fetchRetries"] = fetch_retries
        if only_patterns is not UNSET:
            field_dict["onlyPatterns"] = only_patterns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_config import AuthConfig
        from ..models.http_discovery_type_0 import HttpDiscoveryType0
        from ..models.labels import Labels

        d = dict(src_dict)
        period = d.pop("period")

        def _parse_discovery(data: object) -> HttpDiscoveryType0:
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_http_discovery_type_0 = HttpDiscoveryType0.from_dict(data)

            return componentsschemas_http_discovery_type_0

        discovery = _parse_discovery(d.pop("discovery"))

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

        def _parse_auth(data: object) -> AuthConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_1 = AuthConfig.from_dict(data)

                return auth_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuthConfig | None | Unset, data)

        auth = _parse_auth(d.pop("auth", UNSET))

        def _parse_fetch_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fetch_retries = _parse_fetch_retries(d.pop("fetchRetries", UNSET))

        only_patterns = cast(list[str], d.pop("onlyPatterns", UNSET))

        http_importer = cls(
            period=period,
            discovery=discovery,
            source=source,
            description=description,
            disabled=disabled,
            labels=labels,
            auth=auth,
            fetch_retries=fetch_retries,
            only_patterns=only_patterns,
        )

        http_importer.additional_properties = d
        return http_importer

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
