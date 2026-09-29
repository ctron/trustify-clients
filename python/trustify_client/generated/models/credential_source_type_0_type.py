from enum import StrEnum


class CredentialSourceType0Type(StrEnum):
    INLINE = "inline"

    def __str__(self) -> str:
        return str(self.value)
