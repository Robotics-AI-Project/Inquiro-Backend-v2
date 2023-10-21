from typing import Annotated

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import firebase_admin as fb
from firebase_admin import credentials
from firebase_admin import auth

from app.modules import api
from app.lifecycle import register_startup_event, register_shutdown_event

app = FastAPI()

origins = ["http://localhost:3000", "http://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_startup_event(app)
register_shutdown_event(app)


app.include_router(api)

security = HTTPBearer()


@app.get("/test")
async def test_token(
    credential: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
    decoded_token = auth.verify_id_token(credential.credentials)
    return {"message": decoded_token}


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/health")
async def health():
    return {"message": "OK"}
