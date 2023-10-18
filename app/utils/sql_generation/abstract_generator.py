from abc import ABC, abstractmethod


class Generator(ABC):
    @abstractmethod
    def generate_sql(self, prompt: str, *args, **kwargs) -> str:
        pass
