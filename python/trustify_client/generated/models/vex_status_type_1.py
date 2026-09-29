from enum import StrEnum


class VexStatusType1(StrEnum):
    FIXED = "Fixed"

    def __str__(self) -> str:
        return str(self.value)
