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
        chat = await prisma.message.find_many(
            where={"chatId": chat_id}, order={"createdAt": "asc"}
        )
        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/")
async def create_message(chat_id: str, body: CreateMessageDTO):
    try:
        async with prisma.tx() as transaction:
            chat = await transaction.message.create(
                data={
                    "chatId": chat_id,
                    "content": body.content,
                    "agent": body.agent,
                }
            )
            await transaction.message.create(
                data={
                    "chatId": chat_id,
                    "content": body.content,
                    "agent": "CHATBOT" if body.agent == "USER" else "USER",
                }
            )

        return chat
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
