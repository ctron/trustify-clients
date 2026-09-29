from enum import StrEnum


class CredentialSourceType2Type(StrEnum):
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
