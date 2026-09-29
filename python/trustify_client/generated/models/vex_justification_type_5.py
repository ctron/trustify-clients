from enum import StrEnum


class VexJustificationType5(StrEnum):
    NOTPROVIDED = "NotProvided"

    def __str__(self) -> str:
        return str(self.value)
