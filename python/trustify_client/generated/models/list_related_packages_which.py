from enum import StrEnum


class ListRelatedPackagesWhich(StrEnum):
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
