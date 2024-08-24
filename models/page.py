from pydantic import BaseModel
from typing import List

from models.anime import Anime

class Page(BaseModel):
    hasNext: bool
    data: List[Anime]