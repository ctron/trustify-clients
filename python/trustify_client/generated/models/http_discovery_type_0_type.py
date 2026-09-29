from enum import StrEnum


class HttpDiscoveryType0Type(StrEnum):
    PULP = "pulp"

    def __str__(self) -> str:
        return str(self.value)
