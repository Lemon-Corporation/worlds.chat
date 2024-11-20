from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.core.security import get_current_user
from app.crud import channels as crud
from app.schemas.channels import (
    ChannelCreate, 
    ChannelResponse, 
    PaginatedChannelsResponse,
    ChannelDetailResponse,
    ChannelInfo,
    ErrorResponse
)

router = APIRouter(
    prefix="/channels",
    tags=["channels"]
)

@router.post("/create", response_model=ChannelResponse, responses={400: {"model": ErrorResponse}})
def create_channel(
    channel: ChannelCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not channel.name:
        raise HTTPException(status_code=400, detail="Channel name is required.")
    
    new_channel = crud.create_channel(db, channel)
    return new_channel

@router.get("/all", response_model=PaginatedChannelsResponse)
def get_channels(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total_channels = crud.get_total_channels_count(db)
    channels = crud.get_channels_by_page(db, page, per_page)

    return PaginatedChannelsResponse(
        page=page,
        per_page=per_page,
        total=total_channels,
        channels=[
        ChannelInfo(
            id=channel.id,  # было channel_id, стало id
            name=channel.name,
            type=channel.type,
            world_id=channel.world_id
        )
            for channel in channels
        ]
    )

@router.get("/{channel_id}", response_model=ChannelDetailResponse)
def get_channel(
    channel_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    channel = crud.get_channel(db, channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found.")
    
    return channel