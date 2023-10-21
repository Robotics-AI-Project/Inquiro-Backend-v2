from fastapi import APIRouter, Depends

from app.modules.sql.dto import GenerateSQLDTO
from app.utils.sql_generation import get_generator

router = APIRouter(prefix="/sql", tags=["sql"])


@router.post("/")
async def generate_sql(body: GenerateSQLDTO):
    generator = get_generator(body.generation_type)
    result = generator.generate_sql(body.prompt)
    return {"message": result}
