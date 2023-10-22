from dataclasses import dataclass


@dataclass
class UpdateChatDTO:
    name: str | None = None
