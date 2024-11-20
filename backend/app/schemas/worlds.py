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
    parent_world_id: Optional[int] = None


    class Config:
        orm_mode = True


class WorldCreate(BaseModel):
    name: str
    description: Optional[str]
    parent_world_id: Optional[int] = None


class WorldUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    parent_world_id: Optional[int]
