from fastapi import APIRouter

from commons import generic

router = APIRouter()

@router.get("/series")
def series(page: int = 1):
    return generic(f"/tv?page={page}")

@router.get("/movies")
def movies(page: int = 1):
    return generic(f"/movie?page={page}")