from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.deps import get_current_user
from app.models.user import User  # Исправленный импорт
from app.schemas.members import MemberListResponse
from app.crud import members as crud
from app.schemas.members import RoleUpdate, RoleUpdateResponse
from app.models.worlds import World
from app.models.members import WorldMember

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
    
@router.patch("/{world_id}/members/{user_id}/role", response_model=RoleUpdateResponse)
def update_member_role(
    world_id: int,
    user_id: int,
    role_data: RoleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверяем, что текущий пользователь - владелец мира
    world = db.query(World).filter(World.id == world_id).first()
    if not world or world.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to change roles."
        )
    
    # Обновляем роль
    member = crud.update_member_role(db, world_id, user_id, role_data.role)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    
    return {
        "message": "Role updated successfully.",
        "user_id": user_id,
        "new_role": role_data.role
    }

@router.delete("/{world_id}/members/{user_id}", status_code=204)
def remove_member(
    world_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверяем, что текущий пользователь - владелец мира
    world = db.query(World).filter(World.id == world_id).first()
    if not world or world.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to remove members"
        )
    
    # Удаляем участника
    result = db.query(WorldMember).filter(
        WorldMember.world_id == world_id,
        WorldMember.user_id == user_id
    ).delete()
    
    if not result:
        raise HTTPException(status_code=404, detail="Member not found")
        
    db.commit()
    return Response(status_code=204)