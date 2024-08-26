from pydantic import BaseModel
from typing import List

from models.poster import Poster

class Page(BaseModel):
    hasNext: bool = False
    data: List[Poster]