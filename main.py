from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from routers import episodesRouter, watchRouter, searchRouter, infosRouter, typeRouter

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"]
)

app.include_router(episodesRouter.router)
app.include_router(watchRouter.router)
app.include_router(searchRouter.router)
app.include_router(infosRouter.router)
app.include_router(typeRouter.router)

@app.get("/ping")
def ping():
    return Response("pong")