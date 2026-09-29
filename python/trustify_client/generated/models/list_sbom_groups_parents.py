from enum import StrEnum


class ListSbomGroupsParents(StrEnum):
    ID = "id"
    RESOLVE = "resolve"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
