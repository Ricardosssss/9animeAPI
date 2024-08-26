from bs4 import BeautifulSoup
import requests
from models.page import Page
from models.poster import Poster
from typing import List

BASE_URL = 'https://9animetv.to'

def generic(path: str):
    response = requests.get(BASE_URL + path)

    soup = BeautifulSoup(response.content, 'html.parser')

    #check if exist next page
    nextBtn = soup.find('div', class_='ap__-btn ap__-btn-next')
    next: bool = False
    if nextBtn:
        next = False if nextBtn.find(class_='btn btn-sm btn-focus more-padding disabled') else True

    wrapper = soup.find('div', class_='film_list-wrap')
    items = wrapper.find_all('div', class_='flw-item item-qtip')

    posters: List[Poster] = []

    for item in items:
        try:
            titleWrapper = item.find(class_='film-name')

            posters.append(Poster(
                id=item['data-id'],
                image=item.find('img')['data-src'],
                title=titleWrapper.find(class_='dynamic-name')['title']
            ))
        except:
            continue

    return Page(
        hasNext=next,
        data=posters
    )