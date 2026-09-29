from enum import StrEnum


class LicenseCategory(StrEnum):
    CONCLUDED = "concluded"
    DECLARED = "declared"

    def __str__(self) -> str:
        return str(self.value)
