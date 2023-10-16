from fastapi import APIRouter, Depends

from app.dependencies import get_auth_header
from app.modules.sql.dto import GenerateSQLDTO
from app.utils.llm import get_model

router = APIRouter(prefix="/sql", tags=["sql"], dependencies=[Depends(get_auth_header)])


@router.post("/")
async def generate_sql(body: GenerateSQLDTO):
    model = get_model(body.model)
    result = model.generate(body.prompt)
    return {"message": result}
