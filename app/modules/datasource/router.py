from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from prisma.errors import PrismaError

from app.modules.datasource.dto import CreateDatasourceDTO
from app.utils import prisma
from prisma.models import User

from app.dependencies.auth import get_user

router = APIRouter(
    prefix="/datasource",
    tags=["datasource"],
)


@router.get("/")
async def get_all_datasource(user: Annotated[User, Depends(get_user)]):
    try:
        datasource = await prisma.datasource.find_many(where={"userId": user.id})
        return datasource
    except PrismaError:
        return []


@router.delete("/{datasource_id}")
async def delete_datasource(datasource_id: int, _: Annotated[User, Depends(get_user)]):
    try:
        datasource = await prisma.datasource.delete(where={"id": datasource_id})
        return datasource
    except PrismaError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/")
async def create_datasource(
    body: CreateDatasourceDTO, user: Annotated[User, Depends(get_user)]
):
    try:
        datasource = await prisma.datasource.create(
            data={
                "userId": user.id,
                "name": body.name,
                "engine": body.engine,
                "url": body.url,
            }
        )
        return datasource
    except PrismaError as e:
        raise HTTPException(status_code=400, detail=str(e))
