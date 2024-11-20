from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import get_db
from app.core.deps import get_current_user
from app.schemas.messages import MessageCreate, MessageResponse
from app.models.user import User
from app.models.messages import Message  # Добавляем импорт модели
from app.models.channels import Channel  # Тоже нужен

router = APIRouter()

@router.post("/send", response_model=MessageResponse, status_code=201)
def send_message(
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверяем существование канала
    channel = db.query(Channel).filter(Channel.id == message.channel_id).first()
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    # Проверяем, является ли пользователь участником мира
    member = db.execute(text("""
        SELECT 1 FROM world_members wm
        JOIN channels c ON c.world_id = wm.world_id
        WHERE c.id = :channel_id AND wm.user_id = :user_id
    """), {
        "channel_id": message.channel_id,
        "user_id": current_user.id
    }).first()
    
    if not member:
        raise HTTPException(
            status_code=403,
            detail="You must be a member of the world to send messages"
        )
    
    # Создаём сообщение
    db_message = Message(
        channel_id=message.channel_id,
        user_id=current_user.id,
        content=message.content
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    
    return {
        "message_id": db_message.id,
        "channel_id": db_message.channel_id,
        "content": db_message.content,
        "timestamp": db_message.created_at
    }