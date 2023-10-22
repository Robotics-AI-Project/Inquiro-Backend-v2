import importlib.metadata

from fastapi import FastAPI
from fastapi.security import HTTPBearer
from starlette.middleware.cors import CORSMiddleware

from app.lifecycle import register_startup_event, register_shutdown_event
from app.modules import api

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


@app.get("/")
async def get_version():
    version = importlib.metadata.version("fastapi")
    return {"message": version}


@app.get("/health")
async def health_check():
    return {"message": "OK"}
