from fastapi import APIRouter, Depends
from starlette.requests import Request

router = APIRouter(prefix="/chat", tags=["chat"])


@router.get("/")
async def root():
    return {"message": "Hello"}
