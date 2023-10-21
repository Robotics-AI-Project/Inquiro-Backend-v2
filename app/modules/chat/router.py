from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from prisma.models import User

from app.modules.chat.dto import CreateChatLogDTO, UpdateChatDTO
from app.utils import prisma

from app.dependencies.auth import get_user

router = APIRouter(prefix="/chat", tags=["chat"])


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


@router.patch("/{chat_id}")
async def update_chat(
    chat_id: int, _: Annotated[User, Depends(get_user)], body: UpdateChatDTO
):
    try:
        chat = await prisma.chat.update(where={"id": chat_id}, data={"name": body.name})
        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{chat_id}")
async def get_chat_log(chat_id: str, _: Annotated[User, Depends(get_user)]):
    try:
        chat = await prisma.chatlog.find_many(
            where={"chatId": chat_id}, order={"createdAt": "desc"}
        )
        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{chat_id}")
async def create_chat_log(
    chat_id: str, _: Annotated[User, Depends(get_user)], body: CreateChatLogDTO
):
    try:
        chat = await prisma.chatlog.create(
            data={
                "chatId": chat_id,
                "message": body.message,
                "agent": body.agent,
            }
        )
        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
