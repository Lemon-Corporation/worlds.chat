from typing import List  # Добавляем импорт
from pydantic import BaseModel
from datetime import datetime

class MemberResponse(BaseModel):
    user_id: int
    username: str
    role: str
    joined_at: datetime

    class Config:
        from_attributes = True

class MemberListResponse(BaseModel):
    world_id: int
    members: List[MemberResponse]  # Используем List из typing
    
class RoleUpdate(BaseModel):
    role: str

class RoleUpdateResponse(BaseModel):
    message: str
    user_id: int
    new_role: str