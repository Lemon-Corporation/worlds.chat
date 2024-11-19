from fastapi import FastAPI
from .routers import channels
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(channels.router, prefix="/channels", tags=["Channels"])
