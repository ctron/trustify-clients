from enum import StrEnum


class VexStatusType3(StrEnum):
    UNDERINVESTIGATION = "UnderInvestigation"

    def __str__(self) -> str:
        return str(self.value)
