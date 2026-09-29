from enum import StrEnum


class VexStatusType0(StrEnum):
    AFFECTED = "Affected"

    def __str__(self) -> str:
        return str(self.value)
