from fastapi import APIRouter, HTTPException
import requests
from bs4 import BeautifulSoup

from commons import BASE_URL
from models.anime import Anime, ContentType

router = APIRouter(
    prefix="/infos"
)

@router.get("/{animeId}")
def infos(animeId: int) -> Anime:
    infos = getAnimeInfo(animeId)

    if not infos:
        raise HTTPException(404)
    
    return infos



def getAnimeInfo(animeId: int):
    try:
        response = requests.get(f"{BASE_URL}/ajax/movie/qtip/{animeId}")
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Genres wrapper
        wrapper = soup.select(".pre-qtip-line > a")

        return Anime(
            id = animeId,
            image = getImage(soup.find(class_="btn btn-block btn-play")["href"]),
            title = soup.find(class_="pre-qtip-title").text,
            contentType = ContentType.MOVIE if soup.find(class_="pqd-li badge badge-type").text == "Movie" else ContentType.SERIE,
            description = soup.find(class_="pre-qtip-description").text,
            genres = [genre.text for genre in wrapper]
        )
    except:
        return None


def getImage(url: str):
    response = requests.get(BASE_URL + url)
    soup = BeautifulSoup(response.content, "html.parser")
    wrapper = soup.select_one(".anime-poster")
    return wrapper.select_one("img.film-poster-img")["src"]