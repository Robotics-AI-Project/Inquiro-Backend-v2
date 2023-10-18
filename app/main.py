from fastapi import FastAPI
from app.modules import api

app = FastAPI()

app.include_router(api)


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/health")
async def health():
    return {"message": "OK"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
