from pydantic import BaseModel

class VoiceChannelData(BaseModel):
    room_id: str
    password: str