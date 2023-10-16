from dataclasses import dataclass
from typing import Annotated
from jose import jwt, JWTError
from fastapi import Header, HTTPException, Depends
from starlette.requests import Request
from typing import TypedDict

from app.config import Settings, get_settings


class AuthPayload(TypedDict):
    user_id: str


async def get_auth_header(
    request: Request,
    authorization: Annotated[str, Header()],
    settings: Annotated[Settings, Depends(get_settings)],
):
    if authorization is None:
        raise HTTPException(status_code=400, detail="No Authorization header provided")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid Authorization header")
    token = authorization.split("Bearer ")[1]
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid JWT token")
    request.state.payload = payload
