from enum import StrEnum


class UploadSbomCache(StrEnum):
    QUEUE = "queue"
    SKIP = "skip"
    WAIT = "wait"

    def __str__(self) -> str:
        return str(self.value)
