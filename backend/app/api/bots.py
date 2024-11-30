from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import httpx

from app.db.database import get_db
from app.models.bots import Bot
from app.schemas.bots import BotCreate, BotResponse

router = APIRouter()

GEMINI_API_KEY = "AIzaSyBtZNAxvo7_xvVBwIdbaqzLrhBH3DlObRk"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

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

@router.post("/bots/{name}/chat", response_model=dict)
async def chat_with_bot(name: str, message: dict, db: Session = Depends(get_db)):
    # Получаем бота из БД
    bot = db.query(Bot).filter(Bot.name == name).first()
    if not bot:
        raise HTTPException(status_code=404, detail="Bot not found")
    
    # Формируем запрос к Gemini
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [{
            "parts": [{
                "text": f"{bot.prompt}\nUser: {message['message']}\nAssistant:"
            }]
        }]
    }
    
    # Отправляем запрос
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"AI model error: {response.text}")
            
        result = response.json()
        return {"response": result["candidates"][0]["content"]["parts"][0]["text"]}