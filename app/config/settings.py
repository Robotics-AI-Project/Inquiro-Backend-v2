import os

from pydantic import MySQLDsn, EmailStr
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    DATABASE_URL: MySQLDsn
    OPENAI_API_KEY: str
    FIREBASE_PROJECT_ID: str
    FIREBASE_PRIVATE_KEY_ID: str
    FIREBASE_PRIVATE_KEY: str
    FIREBASE_CLIENT_ID: str
    FIREBASE_CLIENT_EMAIL: EmailStr


settings = AppSettings()

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
