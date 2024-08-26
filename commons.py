from bs4 import BeautifulSoup
import requests
from models.page import Page
from models.anime import *
from typing import List

BASE_URL = 'https://9animetv.to'

def getPosterSrc(url: str):
    response = requests.get(BASE_URL + url)
    soup = BeautifulSoup(response.content, 'html.parser')

    wrapper = soup.select_one('.anime-poster')

    return wrapper.select_one('img.film-poster-img')['src']

def getAnimeInfo(animeId: int):
    try:
        response = requests.get(f'{BASE_URL}/ajax/movie/qtip/{animeId}')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        wrapper = soup.select('.pre-qtip-line > a')

        return Anime(
            id = animeId,
            poster_src = getPosterSrc(soup.find(class_='btn btn-block btn-play')['href']),
            title = soup.find(class_='pre-qtip-title').text,
            type = Type.SERIE if soup.find(class_='pqd-li badge badge-type').text == 'TV Series' else Type.MOVIE,
            description = soup.find(class_='pre-qtip-description').text,
            genres = [genre.text for genre in wrapper]
        )
    except:
        return None

def generic(path: str):
    response = requests.get(BASE_URL + path)

    soup = BeautifulSoup(response.content, 'html.parser')

    nextBtn = soup.find('div', class_='ap__-btn ap__-btn-next')
    next: bool = False

    if nextBtn:
        next = False if nextBtn.find(class_='btn btn-sm btn-focus more-padding disabled') else True

    wrapper = soup.find('div', class_='film_list-wrap')
    items = wrapper.find_all('div', class_='flw-item item-qtip')

    animes: List[Anime] = []

    for item in items:
        info = getAnimeInfo(item['data-id'])

        if not info:
            continue
        
        animes.append(info)

    return Page(
        hasNext=next,
        data=animes
    )