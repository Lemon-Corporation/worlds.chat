from typing import List
from pydantic import BaseModel

class Permission(BaseModel):
    name: str
    description: str

class Role(BaseModel):
    role: str
    permissions: List[str]

class RoleListResponse(BaseModel):
    roles: List[Role]