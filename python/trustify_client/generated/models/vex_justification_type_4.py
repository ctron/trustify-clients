from enum import StrEnum


class VexJustificationType4(StrEnum):
    INLINEMITIGATIONSALREADYEXIST = "InlineMitigationsAlreadyExist"

    def __str__(self) -> str:
        return str(self.value)
