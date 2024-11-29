from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base

# Правильные импорты роутеров
from app.api.auth import router as auth_router
from app.api.worlds import router as worlds_router
from app.api.channels import router as channels_router
from app.api.members import router as members_router
from app.api.messages import router as messages_router
from app.api.invites import router as invites_router  # Изменили
from app.api.roles import router as roles_router
from app.api.subscribers import router as subscribers_router
from app.api.user import router as user_router
from app.api.bots import router as bots_router
from app.api.voice import router as voice_router

# Импорт моделей отдельно
from app.models import bots, channels, invites, members, messages, user, worlds

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Подключаем роутеры
app.include_router(messages_router, prefix="/messages", tags=["messages"])
app.include_router(auth_router)
app.include_router(worlds_router)
app.include_router(channels_router)
app.include_router(members_router, prefix="/worlds")
app.include_router(roles_router, prefix="/worlds", tags=["roles"])
app.include_router(subscribers_router, prefix="/worlds", tags=["subscribers"])
app.include_router(invites_router)  # Изменили
app.include_router(user_router)
app.include_router(bots_router, tags=["bots"])
app.include_router(voice_router)