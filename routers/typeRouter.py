from fastapi import APIRouter, HTTPException

from commons import generic

router = APIRouter()

@router.get("/series")
def series(page: int = 1):
    series = generic(f"/tv?page={page}")
    
    if not series:
        raise HTTPException(status_code=404)
    
    return series

@router.get("/movies")
def movies(page: int = 1):
    movies = generic(f"/movie?page={page}")
    
    if not movies:
        raise HTTPException(status_code=404)
    
    return movies