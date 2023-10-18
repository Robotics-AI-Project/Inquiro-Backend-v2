from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.dependencies import get_auth_header, AuthPayload

router = APIRouter(
    prefix="/snippet",
    tags=["snippet"],
    dependencies=[Depends(get_auth_header)],
)


@router.get("/")
async def root(request: Request):
    payload: AuthPayload = request.state.payload
    return {"message": payload["user_id"]}