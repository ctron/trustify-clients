from enum import StrEnum


class AuthMethodType2Type(StrEnum):
    APIKEY = "apiKey"

    def __str__(self) -> str:
        return str(self.value)
