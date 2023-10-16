from app.utils.sql_generation.abstract_generator import Generator
from app.utils.sql_generation.din_sql.generator import DINSQLGenerator

_generator_list = {
    "DIN-SQL": DINSQLGenerator,
}


def get_generator(genetor_name: str) -> Generator:
    try:
        return _generator_list[genetor_name]()
    except KeyError:
        raise ValueError(
            f"Invalid generator name: {genetor_name}, only available generators are: {list(_generator_list.keys())}"
        )
