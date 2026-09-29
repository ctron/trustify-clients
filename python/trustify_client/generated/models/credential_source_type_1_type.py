from enum import StrEnum


class CredentialSourceType1Type(StrEnum):
    ENV = "env"

    def __str__(self) -> str:
        return str(self.value)
