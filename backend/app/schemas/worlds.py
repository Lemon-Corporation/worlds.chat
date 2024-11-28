from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class WorldResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    owner_id: int
    is_personal_chat: bool
    icon_url: Optional[str]
    parent_world_id: Optional[int]
    partner_id: Optional[int]
    is_private: bool

    class Config:
        form_mode = True


class WorldCreate(BaseModel):
    name: str
    description: Optional[str]
    icon_url: Optional[str]
    is_personal_chat: Optional[bool] = False
    partner_id: Optional[int] | None = None
    parent_world_id: Optional[int] | None = None
    is_private: bool = False


class WorldUpdate(BaseModel):
    name: Optional[str] | None = None
    description: Optional[str] | None = None
    icon_url: Optional[str] | None = None
    parent_world_id: Optional[int] | None = None
    is_private: Optional[bool] | None = None


class UserWorldsList(BaseModel):
    worlds: List[WorldResponse]
