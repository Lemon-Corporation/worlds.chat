from datetime import datetime
from pydantic import BaseModel

class MessageCreate(BaseModel):
    channel_id: int
    content: str

class MessageResponse(BaseModel):
    message_id: int
    channel_id: int
    content: str
    timestamp: datetime

class MessageUpdate(BaseModel):
    content: str
