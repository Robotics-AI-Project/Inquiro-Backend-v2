from pydantic import BaseModel


class CreateDatasourceDTO(BaseModel):
    name: str
    engine: str
    url: str | None = None
