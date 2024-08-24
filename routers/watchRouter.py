from fastapi import APIRouter, HTTPException
from scraperP.scraper import getSource

router = APIRouter(
    prefix='/watch'
)

@router.get('/')
def watch(epId: int):
    try:
        return(getSource(epId))
    except:
        HTTPException(status_code=404)