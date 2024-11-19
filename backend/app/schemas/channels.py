from pydantic import BaseModel


class ChannelResponse(BaseModel):
    channel_id: int
    name: str
    type: str

    class Config:
        orm_mode = True
