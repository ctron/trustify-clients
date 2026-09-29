from enum import StrEnum


class VexStatusType2(StrEnum):
    NOTAFFECTED = "NotAffected"

    def __str__(self) -> str:
        return str(self.value)
