from dataclasses import dataclass


@dataclass
class GenerateSQLDTO:
    prompt: str
    dbUrl: str

    generation_type: str = "DIN-SQL"
    model: str = "GPT-4"
