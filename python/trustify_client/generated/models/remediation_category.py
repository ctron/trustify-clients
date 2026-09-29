from enum import StrEnum


class RemediationCategory(StrEnum):
    MITIGATION = "mitigation"
    NONE_AVAILABLE = "none_available"
    NO_FIX_PLANNED = "no_fix_planned"
    VENDOR_FIX = "vendor_fix"
    WILL_NOT_FIX = "will_not_fix"
    WORKAROUND = "workaround"

    def __str__(self) -> str:
        return str(self.value)
