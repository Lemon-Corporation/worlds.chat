from pydantic import BaseModel, Field
from typing import List

class ChannelCreate(BaseModel):
    world_id: int = Field(..., description="ID мира, в котором создается канал")
    name: str = Field(..., description="Имя канала")
    type: str = Field(..., description="Тип канала (например, text или voice)")

class ChannelResponse(BaseModel):
    channel_id: int
    name: str
    type: str
    world_id: int

class ChannelDetailResponse(ChannelResponse):
    messages: list = []

class ErrorResponse(BaseModel):
    error: str

class ChannelInfo(BaseModel):
    channel_id: int
    name: str
    type: str
    world_id: int

class PaginatedChannelsResponse(BaseModel):
    page: int
    per_page: int
    total: int
    channels: List[ChannelInfo]