from pydantic import BaseModel

class AchievementBase(BaseModel):
    title: str
    description: str
    icon_url: str

class AchievementCreate(AchievementBase):
    pass

class AchievementResponse(AchievementBase):
    id: int

    class Config:
        from_attributes = True
