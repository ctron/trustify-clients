from enum import StrEnum


class VexStatusType4(StrEnum):
    RECOMMENDED = "Recommended"

    def __str__(self) -> str:
        return str(self.value)
