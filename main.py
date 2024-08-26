from fastapi import FastAPI, Response
from routers import episodesRouter, watchRouter, searchRouter, infosRouter

app = FastAPI()

app.include_router(episodesRouter.router)
app.include_router(watchRouter.router)
app.include_router(searchRouter.router)
app.include_router(infosRouter.router)

@app.get('/ping')
def ping():
    return Response('pong')