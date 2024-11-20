from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ChannelBase(BaseModel):
    name: str
    type: str = Field(..., description="Тип канала (text или voice)")

class ChannelCreate(ChannelBase):
    world_id: int = Field(..., description="ID мира, в котором создается канал")

class ChannelResponse(ChannelBase):
    id: int
    world_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ChannelDetailResponse(BaseModel):
    id: int
    name: str
    type: str
    world_id: int
    created_at: datetime
    updated_at: datetime
    messages: List = []

    class Config:
        from_attributes = True

class ErrorResponse(BaseModel):
    error: str

class ChannelInfo(BaseModel):
    id: int  # было channel_id, стало id
    name: str
    type: str
    world_id: int

    class Config:
        orm_mode = True

class PaginatedChannelsResponse(BaseModel):
    page: int
    per_page: int
    total: int
    channels: List[ChannelInfo]