from fastapi import FastAPI, Response
from routers.infosRouter import router as infoR
from routers.watchRouter import router as infoW

app = FastAPI()

app.include_router(infoR)
app.include_router(infoW)

@app.get('/ping')
def pong():
    return Response('pong')