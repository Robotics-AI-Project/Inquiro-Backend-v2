from fastapi import APIRouter, Depends, HTTPException
from app.modules.chat.message.dto import CreateMessageDTO
from app.utils import prisma

from app.dependencies.auth import get_user

router = APIRouter(
    prefix="/{chat_id}/message", tags=["message"], dependencies=[Depends(get_user)]
)


@router.get("/")
async def get_messages(chat_id: str):
    try:
        chat = await prisma.chatlog.find_many(
            where={"chatId": chat_id}, order={"createdAt": "desc"}
        )
        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/")
async def create_message(chat_id: str, body: CreateMessageDTO):
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
