import json
from bs4 import BeautifulSoup
from fastapi import APIRouter, HTTPException
import requests

from models.source import *
from commons import BASE_URL

router = APIRouter(
    prefix="/watch"
)

@router.get("/{epId}")
def watch(epId: int) -> Source:
    source = getSource(epId)
    
    if not source:
        raise HTTPException(status_code=404)
        
    return getSource(epId)



def getSource(episodeId: int):
    try:
        serversResponse = requests.get(BASE_URL + f"/ajax/episode/servers?episodeId={episodeId}")
        serversHtml = json.loads(serversResponse.content)["html"]
        soup = BeautifulSoup(serversHtml, "html.parser")

        providerId = soup.find("div", class_="item server-item", attrs={"data-type": "sub", "data-server-id": "4"})["data-id"]

        idkResponse = requests.get(BASE_URL + f"/ajax/episode/sources?id={providerId}")
        idkLink: str = json.loads(idkResponse.content)["link"]

        sourceId = idkLink.split("/embed-6-v2/")[1].split("?")[0]

        sourceResponse = requests.get(f"https://rapid-cloud.co/ajax/embed-6-v2/getSources?id={sourceId}")
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
    except:
        return None