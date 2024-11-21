from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class WorldResponse(BaseModel):
    id: int  # изменено с world_id
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    owner_id: int
    is_personal_chat: bool
    icon_url: Optional[str]

    class Config:
        form_mode = True


class WorldCreate(BaseModel):
    name: str
    description: Optional[str]
    icon_url: Optional[str]
    is_personal_chat: Optional[bool] = False
    partner_id: Optional[int] | None = None


class WorldUpdate(BaseModel):
    name: Optional[str] | None = None
    description: Optional[str] | None = None
    icon_url: Optional[str] | None = None


class UserWorldsList(BaseModel):
    worlds: List[WorldResponse]