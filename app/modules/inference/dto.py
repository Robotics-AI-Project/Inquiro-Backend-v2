from dataclasses import dataclass


@dataclass
class GenerateSQLDTO:
    prompt: str
    dbUrl: str

    generationType: str = "DIN-SQL"
    model: str = "GPT-4"
