import openai

from app.config import settings
from app.utils.llm import LLMModel


class GPT35Turbo(LLMModel):
    def generate(self, prompt: str, *args, **kwargs) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[{"role": "user", "content": prompt}],
            n=1,
            stream=False,
            temperature=0.0,
            max_tokens=600,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            *args,
            **kwargs,
        )
        return response["choices"][0]["message"]["content"]
