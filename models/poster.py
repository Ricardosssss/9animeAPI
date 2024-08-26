from pydantic import BaseModel

class Poster(BaseModel):
    id: int
    image: str
    title: str