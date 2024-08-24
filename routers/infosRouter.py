from fastapi import APIRouter, HTTPException
from scraperP.scraper import getAnimeInfo, getEpisodes

router = APIRouter(
    prefix='/infos'
)

@router.get('/anime/{animeId}')
def animeInfo(animeId: int):
    try:
        return getAnimeInfo(animeId)
    except:
        raise HTTPException(status_code=404)
    
@router.get('/episodes/{animeId}')
def episodesInfo(animeId: int):
    try:
        return getEpisodes(animeId)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404)