from enum import StrEnum


class ListAdvisoriesDeprecated(StrEnum):
    CONSIDER = "Consider"
    IGNORE = "Ignore"

    def __str__(self) -> str:
        return str(self.value)
