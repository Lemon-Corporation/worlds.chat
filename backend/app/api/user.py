from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.models.worlds import World
from app.models.members import WorldMember
from app.schemas.worlds import WorldResponse, UserWorldsList


router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/worlds", response_model=UserWorldsList)
def get_participating_worlds(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    worlds = db \
        .query(World, WorldMember) \
        .join(WorldMember, WorldMember.world_id == World.id) \
        .filter(WorldMember.user_id == current_user.id) \
    
    world_responses = [
        WorldResponse(
            id=world.id,
            name=world.name,
            description=world.description,
            created_at=world.created_at,
            updated_at=world.updated_at,
            owner_id=world.owner_id,
            is_personal_chat=world.is_personal_chat
        ) for world, _ in worlds
    ]

    return {"worlds": world_responses}

