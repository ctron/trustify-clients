from enum import StrEnum


class AuthMethodType0Type(StrEnum):
    BASIC = "basic"

    def __str__(self) -> str:
        return str(self.value)
