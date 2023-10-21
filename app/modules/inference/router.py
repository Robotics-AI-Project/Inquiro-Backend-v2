from fastapi import APIRouter, HTTPException

from app.modules.inference.dto import GenerateSQLDTO
from app.utils.llm import model
from app.utils.sql_generation import get_generator

router = APIRouter(prefix="/inference", tags=["inference"])


@router.post("/sql")
async def generate_sql(body: GenerateSQLDTO):
    try:
        model.set_model(body.model)
        generator = get_generator(body.generationType)
        result = generator.generate_sql(body.prompt)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
