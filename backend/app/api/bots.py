from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.bots import Bot
from app.schemas.bots import BotCreate, BotResponse

router = APIRouter()

@router.post("/bots/{name}", response_model=BotResponse)
def create_bot(name: str, bot: BotCreate, db: Session = Depends(get_db)):
    db_bot = Bot(name=name, prompt=bot.prompt, model=bot.model)
    db.add(db_bot)
    db.commit()
    db.refresh(db_bot)
    return db_bot

@router.get("/bots", response_model=List[BotResponse])
def get_bots(db: Session = Depends(get_db)):
    return db.query(Bot).all()