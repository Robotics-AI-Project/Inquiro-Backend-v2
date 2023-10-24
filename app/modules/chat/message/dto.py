from dataclasses import dataclass
from typing import Literal


@dataclass
class CreateMessageDTO:
    content: str
    agent: Literal["USER"] | Literal["CHATBOT"]
