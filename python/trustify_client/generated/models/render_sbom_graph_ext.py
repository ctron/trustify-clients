from enum import StrEnum


class RenderSbomGraphExt(StrEnum):
    GV = "gv"

    def __str__(self) -> str:
        return str(self.value)
