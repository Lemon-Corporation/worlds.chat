from sqlalchemy.orm import Session
from app.models.worlds import World  # Исправленный импорт
from app.models.user import User

def get_world_members(db: Session, world_id: int):
    # Получаем мир и его владельца
    world_with_owner = (
        db.query(World, User)
        .join(User, World.owner_id == User.id)
        .filter(World.id == world_id)
        .first()
    )
    
    if not world_with_owner:
        return None
        
    world, owner = world_with_owner
    
    # Формируем ответ с владельцем как единственным участником
    return [{
        "user_id": owner.id,
        "username": owner.username,
        "role": "owner",
        "joined_at": world.created_at
    }]