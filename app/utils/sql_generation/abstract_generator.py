from abc import ABC, abstractmethod


class Generator(ABC):
    db_url = None

    @abstractmethod
    def generate_prompt(self, prompt: str) -> str:
        pass
