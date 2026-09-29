from enum import StrEnum


class State(StrEnum):
    RUNNING = "running"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
