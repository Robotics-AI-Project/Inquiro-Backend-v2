from app.utils.llm.model import LLMModel
from app.utils.llm.gpt_4 import GPT4

_model_list = {
    "GPT-4": GPT4,
}


def get_model(model_name: str) -> LLMModel:
    try:
        return _model_list[model_name]()
    except KeyError:
        raise ValueError(
            f"Invalid model name: {model_name}, only available models are: {list(_model_list.keys())}"
        )
