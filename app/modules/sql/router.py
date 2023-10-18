from fastapi import APIRouter, Depends

from app.dependencies import get_auth_header
from app.modules.sql.dto import GenerateSQLDTO
from app.utils.llm import get_model
from app.utils.sql_generation import get_generator

router = APIRouter(prefix="/sql", tags=["sql"], dependencies=[Depends(get_auth_header)])


@router.post("/")
async def generate_sql(body: GenerateSQLDTO):
    generator = get_generator(body.generation_type)
    result = generator.generate_sql(body.prompt)
    return {"message": result}
