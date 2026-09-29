from enum import StrEnum


class VexJustificationType2(StrEnum):
    VULNERABLECODENOTINEXECUTEPATH = "VulnerableCodeNotInExecutePath"

    def __str__(self) -> str:
        return str(self.value)
