from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.deps import get_current_user
from app.models.user import User  # Исправленный импорт
from app.schemas.members import MemberListResponse
from app.crud import members as crud

router = APIRouter()

@router.get("/{world_id}/members", response_model=MemberListResponse)
def get_members(
    world_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    members = crud.get_world_members(db, world_id)
    if not members:
        raise HTTPException(status_code=404, detail="World not found or no members")
    
    return {
        "world_id": world_id,
        "members": members
    }