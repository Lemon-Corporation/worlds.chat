from pydantic import BaseModel

class BotCreate(BaseModel):
    name: str
    prompt: str
    model: str

class BotResponse(BaseModel):
    id: int
    name: str
    prompt: str
    model: str

    class Config:
        from_attributes = True