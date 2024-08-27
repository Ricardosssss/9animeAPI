from fastapi import APIRouter

from commons import generic
from models.page import Page

router = APIRouter(
    prefix="/search"
)

@router.get("/")
def search(keyword: str, page: int = 1) -> Page:
    return generic(f"/search?keyword={keyword}&page={page}")