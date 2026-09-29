from enum import StrEnum


class AuthMethodType1Type(StrEnum):
    BEARER = "bearer"

    def __str__(self) -> str:
        return str(self.value)
