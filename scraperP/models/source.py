from pydantic import BaseModel
from typing import Union, List

class Intro(BaseModel):
    start: int = 0
    end: int = 0

class Track(BaseModel):
    file: str
    label: str

class Source(BaseModel):
    file: str
    intro: Intro
    tracks: Union[List[Track], None]