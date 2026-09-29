from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.base_purl_head import BasePurlHead
    from ..models.paginated_results_purl_summary_items_item_qualifiers import (
        PaginatedResultsPurlSummaryItemsItemQualifiers,
    )
    from ..models.versioned_purl_head import VersionedPurlHead


T = TypeVar("T", bound="PaginatedResultsPurlSummaryItemsItem")


@_attrs_define
class PaginatedResultsPurlSummaryItemsItem:
    """
    Attributes:
        purl (str):
        uuid (UUID): The ID of the qualified PURL
        base (BasePurlHead):
        qualifiers (PaginatedResultsPurlSummaryItemsItemQualifiers):
        version (VersionedPurlHead):
    """

    purl: str
    uuid: UUID
    base: BasePurlHead
    qualifiers: PaginatedResultsPurlSummaryItemsItemQualifiers
    version: VersionedPurlHead
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purl = self.purl

        uuid = str(self.uuid)

        base = self.base.to_dict()

        qualifiers = self.qualifiers.to_dict()

        version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purl": purl,
                "uuid": uuid,
                "base": base,
                "qualifiers": qualifiers,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_purl_head import BasePurlHead
        from ..models.paginated_results_purl_summary_items_item_qualifiers import (
            PaginatedResultsPurlSummaryItemsItemQualifiers,
        )
        from ..models.versioned_purl_head import VersionedPurlHead

        d = dict(src_dict)
        purl = d.pop("purl")

        uuid = UUID(d.pop("uuid"))

        base = BasePurlHead.from_dict(d.pop("base"))

        qualifiers = PaginatedResultsPurlSummaryItemsItemQualifiers.from_dict(
            d.pop("qualifiers")
        )

        version = VersionedPurlHead.from_dict(d.pop("version"))

        paginated_results_purl_summary_items_item = cls(
            purl=purl,
            uuid=uuid,
            base=base,
            qualifiers=qualifiers,
            version=version,
        )

        paginated_results_purl_summary_items_item.additional_properties = d
        return paginated_results_purl_summary_items_item

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
