from enum import StrEnum


class ScoreType(StrEnum):
    VALUE_0 = "2.0"
    VALUE_1 = "3.0"
    VALUE_2 = "3.1"
    VALUE_3 = "4.0"

    def __str__(self) -> str:
        return str(self.value)
