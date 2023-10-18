from app.utils.sql_generation import Generator
from app.utils.sql_generation.din_sql.module.classification import (
    classify_generation,
)
from app.utils.sql_generation.din_sql.module.schema_linking import get_schema_links


class DINSQLGenerator(Generator):
    # def __init__(self, db_url: str):
    #     self.db_url = db_url

    def generate_sql(self, prompt: str) -> str:
        schema_links = get_schema_links(prompt, "")
        # schema_links = "[singer.*]"
        # classification = classify_generation(prompt, "", schema_links)
        return schema_links
