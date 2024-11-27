from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    profile_pic_url: str

    class Config:
        from_attributes = True

class UserPublicInfoResponse(BaseModel):
    id: int
    username: str
    profile_pic_url: Optional[str]
    banner_url: Optional[str]
    bio: str

class UserPrivateInfoResponse(UserPublicInfoResponse):
    email: Optional[str]

class UserUpdateRequest(BaseModel):
    email: Optional[str] = None
    profile_pic_url: Optional[str] = None
    banner_url: Optional[str] = None
    bio: Optional[str] = None