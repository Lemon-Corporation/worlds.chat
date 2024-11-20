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


    class Config:
        form_mode = True


class WorldCreate(BaseModel):
    name: str
    description: Optional[str]


class WorldUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class UserWorldsList(BaseModel):
    worlds: List[WorldResponse]