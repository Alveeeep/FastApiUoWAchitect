from fastapi import FastAPI
from routers.kitties import router

app = FastAPI(
    title="REST API для администратора онлайн выставки котят"
)

app.include_router(router)
