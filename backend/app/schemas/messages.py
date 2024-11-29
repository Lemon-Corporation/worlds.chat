from datetime import datetime
from pydantic import BaseModel
from typing import List

class MessageCreate(BaseModel):
    user_id: int
    channel_id: int
    content: str

class MessageResponse(BaseModel):
    message_id: int
    channel_id: int
    user_id: int
    content: str
    timestamp: datetime

class MessageUpdate(BaseModel):
    content: str

class PaginatedMessagesResponse(BaseModel):
    page: int
    per_page: int
    total: int
    messages: List[MessageResponse]
