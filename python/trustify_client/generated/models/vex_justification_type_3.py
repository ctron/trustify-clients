from enum import StrEnum


class VexJustificationType3(StrEnum):
    VULNERABLECODECANNOTBECONTROLLEDBYADVERSARY = (
        "VulnerableCodeCannotBeControlledByAdversary"
    )

    def __str__(self) -> str:
        return str(self.value)
