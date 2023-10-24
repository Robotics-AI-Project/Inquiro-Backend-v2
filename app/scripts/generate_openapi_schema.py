from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import json


def generate_openapi_schema(app: FastAPI):
    with open("app/schemas/openapi.json", "w") as f:
        json.dump(
            get_openapi(
                title=app.title,
                version=app.version,
                openapi_version=app.openapi_version,
                description=app.description,
                routes=app.routes,
            ),
            f,
        )
