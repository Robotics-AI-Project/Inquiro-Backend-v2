from fastapi import APIRouter, Depends
from starlette.requests import Request

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"],
)


@router.get("/")
async def root():
    return {"message": "hello"}
