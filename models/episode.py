from pydantic import BaseModel

class Episode(BaseModel):
    id: int
    number: int
    title: str