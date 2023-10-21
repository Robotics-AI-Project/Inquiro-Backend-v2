from fastapi import APIRouter

from app.modules.inference.dto import GenerateSQLDTO
from app.utils.sql_generation import get_generator

router = APIRouter(prefix="/inference", tags=["inference"])


@router.post("/sql")
async def generate_sql(body: GenerateSQLDTO):
    generator = get_generator(body.generation_type)
    result = generator.generate_sql(body.prompt)
    return {"message": result}
