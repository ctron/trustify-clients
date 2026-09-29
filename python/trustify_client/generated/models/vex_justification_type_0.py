from enum import StrEnum


class VexJustificationType0(StrEnum):
    COMPONENTNOTPRESENT = "ComponentNotPresent"

    def __str__(self) -> str:
        return str(self.value)
