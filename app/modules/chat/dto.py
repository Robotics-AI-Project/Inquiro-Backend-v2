from dataclasses import dataclass
from typing import Literal


@dataclass
class UpdateChatDTO:
    name: str | None = None


@dataclass
class CreateChatDTO:
    message: str
    agent: Literal["USER"] | Literal["CHATBOT"] = "USER"
