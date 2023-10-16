from typing import Annotated

from fastapi import FastAPI
from .modules.chat.router import router

app = FastAPI()


app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/health")
async def health():
    return {"message": "OK"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
