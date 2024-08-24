from fastapi import APIRouter, Response

from commons import generic

router = APIRouter(
    prefix='/search'
)

@router.get('/')
def search(keyword: str, page: int = 1):
    return generic(f'/search?keyword={keyword}&page={page}')