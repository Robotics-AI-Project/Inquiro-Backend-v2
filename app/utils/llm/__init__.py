from app.utils.llm.model import LLMModel
from app.utils.llm.models import models


class SelectedModel(LLMModel):
    def __init__(self):
        self.__model_list = {m.name: m for m in models}
        self.model: LLMModel | None = None

    def __get_model(self, model_name: str) -> LLMModel:
        try:
            return self.__model_list[model_name]()
        except KeyError:
            raise ValueError(
                f"Invalid model name: {model_name}, only available models are: {list(self.__model_list.keys())}"
            )

    def set_model(self, model_name: str) -> None:
        self.model = self.__get_model(model_name)

    def generate(self, prompt: str, *args, **kwargs) -> str:
        if self.model is None:
            raise ValueError("Model is not set")
        return self.model.generate(prompt, *args, **kwargs)


model = SelectedModel()
