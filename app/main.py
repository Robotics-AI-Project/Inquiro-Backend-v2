from fastapi import FastAPI
from app.modules import api
from app.utils import prisma

app = FastAPI()

app.include_router(api)


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/health")
async def health():
    return {"message": "OK"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
