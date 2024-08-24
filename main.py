from fastapi import FastAPI, Response
from routers import episodesRouter, watchRouter, searchRouter

app = FastAPI()

app.include_router(episodesRouter.router)
app.include_router(watchRouter.router)
app.include_router(searchRouter.router)

@app.get('/ping')
def ping():
    return Response('pong')