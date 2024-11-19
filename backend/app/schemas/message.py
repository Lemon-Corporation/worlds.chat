from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    channel_id: int
    content: str

class MessageResponse(BaseModel):
    message_id: int
    channel_id: int
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True