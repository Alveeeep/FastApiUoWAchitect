from pydantic import BaseModel


class KittieDTO(BaseModel):
    color: str
    age: int
    description: str
