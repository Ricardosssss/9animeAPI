from pydantic import BaseModel
from typing import List
from enum import Enum

class Type(Enum):
    SERIE = 'serie'
    MOVIE = 'movie'

class Anime(BaseModel):
    id: int
    poster_src: str
    title: str
    type: Type = Type.SERIE
    description: str
    genres: List[str]

class Episode(BaseModel):
    id: int
    number: int
    title: str