import together
from app.utils.llm import LLMModel


class CodeLlama34B(LLMModel):
    name = "CodeLlama-34b"

    def generate(self, prompt: str, *args, **kwargs) -> str:
        output = together.Complete.create(
            prompt=prompt,
            model="togethercomputer/CodeLlama-34b",
            max_tokens=256,
            temperature=0,
            top_k=60,
            top_p=0.6,
            stop=["Q:", "\n\n"],
            *args,
            **kwargs,
        )
        return output["output"]["choices"][0]["text"]
