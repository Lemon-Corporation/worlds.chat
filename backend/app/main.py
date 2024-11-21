from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.auth import router as auth_router
from app.api.worlds import router as worlds_router
from app.api.channels import router as channels_router
from app.api.members import router as members_router
from app.api import roles, subscribers, messages, invites, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Замените на URL вашего фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Подключаем роутеры
app.include_router(messages.router, prefix="/messages", tags=["messages"])
app.include_router(auth_router)
app.include_router(worlds_router)
app.include_router(channels_router)
app.include_router(members_router, prefix="/worlds")
app.include_router(roles.router, prefix="/worlds", tags=["roles"])
app.include_router(subscribers.router, prefix="/worlds", tags=["subscribers"])
app.include_router(invites.router)
app.include_router(user.router)