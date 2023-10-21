from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth
from prisma.errors import RecordNotFoundError
from prisma.models import User

from app.utils import prisma

security = HTTPBearer()


async def get_user(
    credential: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> User:
    decoded_token = auth.verify_id_token(credential.credentials)
    try:
        user = await prisma.user.find_first_or_raise(
            where={"uid": decoded_token.get("uid")}
        )
    except RecordNotFoundError:
        user = await prisma.user.create(
            data={
                "name": decoded_token.get("name"),
                "email": decoded_token.get("email"),
                "username": decoded_token.get("email"),
                "image": decoded_token.get("picture"),
                "provider": decoded_token.get("firebase").get("sign_in_provider"),
                "uid": decoded_token.get("uid"),
            }
        )
    return user
