import requests
from bs4 import BeautifulSoup
from models.anime import *
from models.source import *
import json
from typing import List, Union

BASE_URL = 'https://9animetv.to'

def getPosterSrc(url: str):
    response = requests.get(BASE_URL + url)
    soup = BeautifulSoup(response.content, 'html.parser')

    wrapper = soup.select_one('.anime-poster')
    img_url = wrapper.select_one('img.film-poster-img')['src']

    return img_url

def getAnimeInfo(animeId: int):
    response = requests.get(BASE_URL + f'/ajax/movie/qtip/{animeId}')
    soup = BeautifulSoup(response.content, 'html.parser')

    type = Type.SERIE if soup.find(class_='pqd-li badge badge-type').text == 'TV Series' else Type.MOVIE
    
    wrapper = soup.select('.pre-qtip-line > a')
    genres = [genre.text for genre in wrapper]

    poster = getPosterSrc(soup.find(class_='btn btn-block btn-play')['href'])

    return Anime(
        id = animeId,
        poster_src = poster,
        title = soup.find(class_='pre-qtip-title').text,
        type = type.value,
        description = soup.find(class_='pre-qtip-description').text,
        genres = genres
    )

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

def getSource(episodeId: int):
    serversResponse = requests.get(BASE_URL + f'/ajax/episode/servers?episodeId={episodeId}')
    serversHtml = json.loads(serversResponse.content)['html']
    soup = BeautifulSoup(serversHtml, 'html.parser')

    providerId = soup.find('div', class_='item server-item', attrs={'data-type': 'sub', 'data-server-id': '4'})['data-id']

    idkResponse = requests.get(BASE_URL + f'/ajax/episode/sources?id={providerId}')
    idkLink: str = json.loads(idkResponse.content)["link"]

    sourceId = idkLink.split('/embed-6-v2/')[1].split('?')[0]

    sourceResponse = requests.get(f'https://rapid-cloud.co/ajax/embed-6-v2/getSources?id={sourceId}')
    source = json.loads(sourceResponse.content)

    intro = Intro(
        start=source["intro"]["start"],
        end=source["intro"]["end"]
    )

    tracks = source["tracks"]
    tracksM: Union[List[Track], None] = []

    if tracks:
        for a in tracks:
            tracksM.append(Track(
                file=a["file"],
                label=a["label"]
            ))
    else:
        tracksM = None

    return Source(
        file = source["sources"][0]["file"],
        intro=intro,
        tracks=tracksM
    )