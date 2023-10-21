from app.utils.llm.models.gpt_35_turbo import GPT35Turbo
from app.utils.llm.models.gpt_4 import GPT4
from app.utils.llm.models.codellama_15b import CodeLlama15B
from app.utils.llm.models.codellama_34b import CodeLlama34B

models = [
    # OPEN AI
    GPT4,
    GPT35Turbo,
    # TOGETHER AI
    # CodeLlama
    CodeLlama15B,
    CodeLlama34B,
]
