from app.utils.sql_generation import Generator


class DINSQLGenerator(Generator):
    def __init__(self, db_url: str):
        self.db_url = db_url

    def generate_prompt(self, prompt: str) -> str:
        print(self.db_url)
        return prompt
