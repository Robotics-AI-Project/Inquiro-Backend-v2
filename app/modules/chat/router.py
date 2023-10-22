from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from prisma.models import User

from app.modules.chat.dto import UpdateChatDTO
from app.utils import prisma

from app.dependencies.auth import get_user
from app.modules.chat.message import message_router

router = APIRouter(prefix="/chat", tags=["chat"])
router.include_router(message_router)


@router.get("/")
async def get_all_chats(user: Annotated[User, Depends(get_user)], n: int = 10):
    try:
        chats = await prisma.chat.find_many(
            where={"userId": user.id}, order={"createdAt": "desc"}, take=n
        )
        return chats
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/")
async def create_chat(user: Annotated[User, Depends(get_user)]):
    try:
        chat = await prisma.chat.create(data={"userId": user.id})
        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{chat_id}", dependencies=[Depends(get_user)])
async def update_chat(chat_id: int, body: UpdateChatDTO):
    try:
        chat = await prisma.chat.update(where={"id": chat_id}, data={"name": body.name})
        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
