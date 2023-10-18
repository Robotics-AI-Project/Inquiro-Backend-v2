from app.utils.llm.model import LLMModel
from app.utils.llm.gpt_4 import GPT4
from app.utils.llm.gpt_35_turbo import GPT35Turbo

_model_list = {
    "GPT-4": GPT4,
    "GPT-3.5-turbo": GPT35Turbo,
}


def get_model(model_name: str) -> LLMModel:
    try:
        return _model_list[model_name]()
    except KeyError:
        raise ValueError(
            f"Invalid model name: {model_name}, only available models are: {list(_model_list.keys())}"
        )
