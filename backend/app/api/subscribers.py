from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy import text  # Добавляем импорт text
from app.db.database import get_db
from app.core.deps import get_current_user
from app.schemas.subscribers import SubscriberListResponse
from app.models.user import User
from app.models.worlds import World

router = APIRouter()

@router.get("/{world_id}/subscribers", response_model=SubscriberListResponse)
def get_subscribers(
    world_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверяем существование мира
    world = db.query(World).filter(World.id == world_id).first()
    if not world:
        raise HTTPException(status_code=404, detail="World not found")
    
    # Получаем список подписчиков
    subscribers = db.execute(text("""
        SELECT u.id as user_id, u.username, ws.subscribed_at
        FROM world_subscribers ws
        JOIN users u ON u.id = ws.user_id
        WHERE ws.world_id = :world_id
    """), {"world_id": world_id}).fetchall()
    
    return {
        "world_id": world_id,
        "subscribers": [
            {
                "user_id": sub.user_id,
                "username": sub.username,
                "subscribed_at": sub.subscribed_at
            } for sub in subscribers
        ]
    }
    
@router.post("/{world_id}/subscribe", status_code=201)
def subscribe_to_world(
    world_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверяем существование мира
    world = db.query(World).filter(World.id == world_id).first()
    if not world:
        raise HTTPException(status_code=404, detail="World not found")
    
    # Проверяем, не подписан ли уже
    existing = db.execute(
        text("SELECT 1 FROM world_subscribers WHERE world_id = :world_id AND user_id = :user_id"),
        {"world_id": world_id, "user_id": current_user.id}
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Already subscribed")
    
    # Добавляем подписку
    db.execute(
        text("INSERT INTO world_subscribers (world_id, user_id) VALUES (:world_id, :user_id)"),
        {"world_id": world_id, "user_id": current_user.id}
    )
    db.commit()
    
    return {"message": "Successfully subscribed to the world."}

@router.delete("/{world_id}/unsubscribe", status_code=204)
def unsubscribe_from_world(
    world_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверяем существование мира
    world = db.query(World).filter(World.id == world_id).first()
    if not world:
        raise HTTPException(status_code=404, detail="World not found")
    
    # Удаляем подписку
    result = db.execute(
        text("DELETE FROM world_subscribers WHERE world_id = :world_id AND user_id = :user_id"),
        {"world_id": world_id, "user_id": current_user.id}
    )
    db.commit()
    
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    return Response(status_code=204)