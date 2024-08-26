from pydantic import BaseModel
from typing import List
from enum import Enum

class ContentType(Enum):
    SERIE = 'serie'
    MOVIE = 'movie'

class Anime(BaseModel):
    id: int
    image: str
    title: str
    contentType: ContentType
    description: str
    genres: List[str]