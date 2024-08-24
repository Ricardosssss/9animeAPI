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
    img_url = wrapper.select_one('img.film-poster-img')['src']

    return img_url

def getAnimeInfo(animeId: int):
    response = requests.get(f'{BASE_URL}/ajax/movie/qtip/{animeId}')
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

def generic(path: str):
    response = requests.get(BASE_URL + path)
    print(response.url)

    soup = BeautifulSoup(response.content, 'html.parser')

    nextBtn = soup.find('div', class_='ap__-btn ap__-btn-next')
    next: bool = False

    if nextBtn:
        next = False if nextBtn.find(class_='btn btn-sm btn-focus more-padding disabled') else True

    wrapper = soup.find('div', class_='film_list-wrap')
    items = wrapper.find_all('div', class_='flw-item item-qtip')

    animes: List[Anime] = []

    for item in items:
        try:
            animes.append(getAnimeInfo(item['data-id']))
            print(item['data-id'])
        except:
            continue

    return Page(
        hasNext=next,
        data=animes
    )