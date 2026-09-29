from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auth_method_type_0 import AuthMethodType0
    from ..models.auth_method_type_1 import AuthMethodType1
    from ..models.auth_method_type_2 import AuthMethodType2


T = TypeVar("T", bound="AuthConfig")


@_attrs_define
class AuthConfig:
    """Authentication configuration for HTTP-based importers.

    Wraps an [`AuthMethod`] whose credentials are resolved from
    a [`CredentialSource`] at import time — not at configuration time.

        Attributes:
            method (AuthMethodType0 | AuthMethodType1 | AuthMethodType2): HTTP authentication method applied on each import
                request.
    """

    method: AuthMethodType0 | AuthMethodType1 | AuthMethodType2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_method_type_0 import AuthMethodType0
        from ..models.auth_method_type_1 import AuthMethodType1

        method: dict[str, Any]
        if isinstance(self.method, AuthMethodType0) or isinstance(
            self.method, AuthMethodType1
        ):
            method = self.method.to_dict()
        else:
            method = self.method.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_method_type_0 import AuthMethodType0
        from ..models.auth_method_type_1 import AuthMethodType1
        from ..models.auth_method_type_2 import AuthMethodType2

        d = dict(src_dict)

        def _parse_method(
            data: object,
        ) -> AuthMethodType0 | AuthMethodType1 | AuthMethodType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_method_type_0 = AuthMethodType0.from_dict(data)

                return componentsschemas_auth_method_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_method_type_1 = AuthMethodType1.from_dict(data)

                return componentsschemas_auth_method_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_auth_method_type_2 = AuthMethodType2.from_dict(data)

            return componentsschemas_auth_method_type_2

        method = _parse_method(d.pop("method"))

        auth_config = cls(
            method=method,
        )

        auth_config.additional_properties = d
        return auth_config

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
