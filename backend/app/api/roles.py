from fastapi import APIRouter, Depends
from app.schemas.roles import RoleListResponse
from app.core.deps import get_current_user

router = APIRouter()

@router.get("/{world_id}/roles", response_model=RoleListResponse)
def get_roles(world_id: int, current_user = Depends(get_current_user)):
    return {
        "roles": [
            {
                "role": "owner",
                "permissions": ["create_channel", "delete_world", "update_settings", "manage_roles"]
            },
            {
                "role": "moderator",
                "permissions": ["kick_member", "manage_channels", "manage_messages"]
            },
            {
                "role": "member",
                "permissions": ["send_message", "join_channel", "read_messages"]
            }
        ]
    }