from dataclasses import dataclass
from typing import Literal


@dataclass
class CreateMessageDTO:
    message: str
    agent: Literal["USER"] | Literal["CHATBOT"]
