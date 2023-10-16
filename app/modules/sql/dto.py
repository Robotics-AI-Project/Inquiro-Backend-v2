from dataclasses import dataclass


@dataclass
class GenerateSQLDTO:
    prompt: str
    db_url: str

    generation_type: str = "DIN-SQL"
    model: str = "GPT-4"
