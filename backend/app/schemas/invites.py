from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class InviteCreate(BaseModel):
    world_id: int
    lifespan: int  # in seconds
    invited_users: Optional[List[int]] = []


class InviteResponse(BaseModel):
    invite_token: str
    expiration_date: datetime
