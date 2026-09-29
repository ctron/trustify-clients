from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_method_type_2_type import AuthMethodType2Type

if TYPE_CHECKING:
    from ..models.credential_source_type_0 import CredentialSourceType0
    from ..models.credential_source_type_1 import CredentialSourceType1
    from ..models.credential_source_type_2 import CredentialSourceType2


T = TypeVar("T", bound="AuthMethodType2")


@_attrs_define
class AuthMethodType2:
    """Arbitrary header/value pair (e.g. API key headers).

    Attributes:
        header (str):
        type_ (AuthMethodType2Type):
        value (CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2): How a credential value is sourced
            at import time.

            Inline stores the value directly (dev only). Env and File store
            only a reference — the value is resolved from the environment or
            filesystem at each import run, enabling K8s Secret rotation.
    """

    header: str
    type_: AuthMethodType2Type
    value: CredentialSourceType0 | CredentialSourceType1 | CredentialSourceType2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_source_type_0 import (
            CredentialSourceType0,
        )
        from ..models.credential_source_type_1 import (
            CredentialSourceType1,
        )

        header = self.header

        type_ = self.type_.value

        value: dict[str, Any]
        if isinstance(self.value, CredentialSourceType0) or isinstance(
            self.value, CredentialSourceType1
        ):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "header": header,
                "type": type_,
                "value": value,
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
        header = d.pop("header")

        type_ = AuthMethodType2Type(d.pop("type"))

        def _parse_value(
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

        value = _parse_value(d.pop("value"))

        auth_method_type_2 = cls(
            header=header,
            type_=type_,
            value=value,
        )

        auth_method_type_2.additional_properties = d
        return auth_method_type_2

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
