from typing import List
from datetime import datetime
from pydantic import BaseModel

class Subscriber(BaseModel):
    user_id: int
    username: str
    subscribed_at: datetime

class SubscriberListResponse(BaseModel):
    world_id: int
    subscribers: List[Subscriber]