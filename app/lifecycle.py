"""Template App
"""
from typing import Awaitable, Callable

from fastapi import FastAPI
import firebase_admin

from app.config import certificate
from app.utils import prisma


def register_startup_event(app: FastAPI) -> Callable[[], Awaitable[None]]:
    """Actions to run on app startup.

    This function uses fastAPI app to store data
    inthe state, such as db_engine.

    :param app: the fastAPI app.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _startup() -> None:
        firebase_admin.initialize_app(certificate)
        await prisma.connect()

    return _startup


def register_shutdown_event(app: FastAPI) -> Callable[[], Awaitable[None]]:
    """Actions to run on app's shutdown.

    :param app: fastAPI app.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:
        firebase_admin.delete_app(firebase_admin.get_app())
        await prisma.disconnect()

    return _shutdown
