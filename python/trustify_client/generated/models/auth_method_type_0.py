from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_method_type_0_type import AuthMethodType0Type

if TYPE_CHECKING:
    from ..models.credential_source_type_0 import CredentialSourceType0
    from ..models.credential_source_type_1 import CredentialSourceType1
    from ..models.credential_source_type_2 import CredentialSourceType2


T = TypeVar("T", bound="AuthMethodType0")


@_attrs_define
class AuthMethodType0:
    """HTTP Basic authentication.

    Attributes:
        password (CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2): How a credential value is
            sourced at import time.

            Inline stores the value directly (dev only). Env and File store
            only a reference — the value is resolved from the environment or
            filesystem at each import run, enabling K8s Secret rotation.
        type_ (AuthMethodType0Type):
        username (CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2): How a credential value is
            sourced at import time.

            Inline stores the value directly (dev only). Env and File store
            only a reference — the value is resolved from the environment or
            filesystem at each import run, enabling K8s Secret rotation.
    """

    password: CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2
    type_: AuthMethodType0Type
    username: CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_source_type_0 import (
            CredentialSourceType0,
        )
        from ..models.credential_source_type_1 import (
            CredentialSourceType1,
        )

        password: dict[str, Any]
        if isinstance(self.password, CredentialSourceType0) or isinstance(
            self.password, CredentialSourceType1
        ):
            password = self.password.to_dict()
        else:
            password = self.password.to_dict()

        type_ = self.type_.value

        username: dict[str, Any]
        if isinstance(self.username, CredentialSourceType0) or isinstance(
            self.username, CredentialSourceType1
        ):
            username = self.username.to_dict()
        else:
            username = self.username.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "type": type_,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.credential_source_type_0 import (
            CredentialSourceType0,
        )
        from ..models.credential_source_type_1 import (
            CredentialSourceType1,
        )
        from ..models.credential_source_type_2 import (
            CredentialSourceType2,
        )

        d = dict(src_dict)

        def _parse_password(
            data: object,
        ) -> CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credential_source_type_0 = (
                    CredentialSourceType0.from_dict(data)
                )

                return componentsschemas_credential_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credential_source_type_1 = (
                    CredentialSourceType1.from_dict(data)
                )

                return componentsschemas_credential_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_credential_source_type_2 = (
                CredentialSourceType2.from_dict(data)
            )

            return componentsschemas_credential_source_type_2

        password = _parse_password(d.pop("password"))

        type_ = AuthMethodType0Type(d.pop("type"))

        def _parse_username(
            data: object,
        ) -> CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credential_source_type_0 = (
                    CredentialSourceType0.from_dict(data)
                )

                return componentsschemas_credential_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credential_source_type_1 = (
                    CredentialSourceType1.from_dict(data)
                )

                return componentsschemas_credential_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_credential_source_type_2 = (
                CredentialSourceType2.from_dict(data)
            )

            return componentsschemas_credential_source_type_2

        username = _parse_username(d.pop("username"))

        auth_method_type_0 = cls(
            password=password,
            type_=type_,
            username=username,
        )

        auth_method_type_0.additional_properties = d
        return auth_method_type_0

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
