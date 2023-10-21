from typing import Annotated

from fastapi import APIRouter, Depends
from prisma.models import User

from app.dependencies.auth import get_user

router = APIRouter(
    prefix="/snippet",
    tags=["snippet"],
)


@router.get("/")
async def root(user: Annotated[User, Depends(get_user)]):
    return {"message": user}
