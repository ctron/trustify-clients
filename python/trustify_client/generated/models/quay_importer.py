from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_config import AuthConfig
    from ..models.labels import Labels


T = TypeVar("T", bound="QuayImporter")


@_attrs_define
class QuayImporter:
    """
    Attributes:
        period (str): The period the importer should be run.
        description (None | str | Unset): A description for users.
        disabled (bool | Unset): A flag to disable the importer, without deleting it.
        labels (Labels | Unset):
        auth (AuthConfig | None | Unset): Authentication configuration for accessing the Quay registry.
        concurrency (int | None | Unset): The maximum concurrent repository fetches
        namespace (None | str | Unset): The namespace of the registry to "walk"
        size_limit (None | str | Unset): The max size of the ingested SBOM's (None is unlimited)
        source (str | Unset): The name of the quay registry, e.g. quay.io
        unencrypted (bool | Unset): Whether the scheme used is 'http' [true] or 'https' [false]
    """

    period: str
    description: None | str | Unset = UNSET
    disabled: bool | Unset = UNSET
    labels: Labels | Unset = UNSET
    auth: AuthConfig | None | Unset = UNSET
    concurrency: int | None | Unset = UNSET
    namespace: None | str | Unset = UNSET
    size_limit: None | str | Unset = UNSET
    source: str | Unset = UNSET
    unencrypted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_config import AuthConfig

        period = self.period

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

        concurrency: int | None | Unset
        if isinstance(self.concurrency, Unset):
            concurrency = UNSET
        else:
            concurrency = self.concurrency

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        size_limit: None | str | Unset
        if isinstance(self.size_limit, Unset):
            size_limit = UNSET
        else:
            size_limit = self.size_limit

        source = self.source

        unencrypted = self.unencrypted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
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
        if concurrency is not UNSET:
            field_dict["concurrency"] = concurrency
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if size_limit is not UNSET:
            field_dict["sizeLimit"] = size_limit
        if source is not UNSET:
            field_dict["source"] = source
        if unencrypted is not UNSET:
            field_dict["unencrypted"] = unencrypted

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_config import AuthConfig
        from ..models.labels import Labels

        d = dict(src_dict)
        period = d.pop("period")

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

        def _parse_concurrency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        concurrency = _parse_concurrency(d.pop("concurrency", UNSET))

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_size_limit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        size_limit = _parse_size_limit(d.pop("sizeLimit", UNSET))

        source = d.pop("source", UNSET)

        unencrypted = d.pop("unencrypted", UNSET)

        quay_importer = cls(
            period=period,
            description=description,
            disabled=disabled,
            labels=labels,
            auth=auth,
            concurrency=concurrency,
            namespace=namespace,
            size_limit=size_limit,
            source=source,
            unencrypted=unencrypted,
        )

        quay_importer.additional_properties = d
        return quay_importer

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
