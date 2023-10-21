from abc import ABC, abstractmethod


class Generator(ABC):
    name: str

    @abstractmethod
    def generate_sql(self, prompt: str, *args, **kwargs) -> str:
        pass
