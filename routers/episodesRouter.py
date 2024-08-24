import json
from typing import List
from bs4 import BeautifulSoup
from fastapi import APIRouter, HTTPException
import requests

from commons import BASE_URL
from models.anime import Episode

router = APIRouter(
    prefix='/episodes'
)
    
@router.get('/{animeId}')
def episodesInfo(animeId: int):
    try:
        return getEpisodes(animeId)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404)



def getEpisodes(animeId: int):
    response = requests.get(BASE_URL + f'/ajax/episode/list/{animeId}')
    html = json.loads(response.content)['html']
    soup = BeautifulSoup(html, 'html.parser')

    aTags = soup.findAll('a', class_='item ep-item')

    episodes: List[Episode] = []

    for a in aTags:
        episodes.append(Episode(
            id = a['data-id'],
            number = a['data-number'],
            title = a['title']
        ))

    return episodes