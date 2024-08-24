from fastapi import APIRouter, Query

from commons import generic

router = APIRouter(
    prefix='/search'
)

@router.get('/')
def search(keyword: str = Query(min_length=4), page: int = 1):
    return generic(f'/search?keyword={keyword}&page={page}')