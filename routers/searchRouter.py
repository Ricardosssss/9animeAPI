from fastapi import APIRouter, HTTPException

from commons import generic
from models.page import Page

router = APIRouter(
    prefix="/search"
)

@router.get("/")
def search(keyword: str, page: int = 1):
    search = generic(f"/search?keyword={keyword}&page={page}")
    
    if not search:
        raise HTTPException(status_code=404)
    
    return search