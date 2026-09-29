from enum import StrEnum


class VexJustificationType1(StrEnum):
    VULNERABLECODENOTPRESENT = "VulnerableCodeNotPresent"

    def __str__(self) -> str:
        return str(self.value)
