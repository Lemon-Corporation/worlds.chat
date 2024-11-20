from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.auth import router as auth_router
from app.api.worlds import router as worlds_router
from app.api.channels import router as channels_router

app = FastAPI()

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Подключаем роутеры
app.include_router(auth_router)
app.include_router(worlds_router)
app.include_router(channels_router)