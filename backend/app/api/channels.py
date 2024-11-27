from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.models.messages import Message
from app.core.security import get_current_user
from app.crud import channels as crud
from app.schemas.messages import MessageResponse, PaginatedMessagesResponse
from app.schemas.channels import (
    ChannelCreate, 
    ChannelResponse, 
    PaginatedChannelsResponse,
    ChannelDetailResponse,
    ChannelInfo,
    ErrorResponse
)
from app.models.channels import ChannelType

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
    
    if channel.type not in ChannelType.__members__.values():
        raise HTTPException(status_code=400, detail="Invalid channel type.")
    
    
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

@router.get("/{channel_id}/get_messages", response_model=PaginatedMessagesResponse)
def get_messages(
    channel_id: int,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, gt=0),
    db: Session = Depends(get_db),
):
    offset = (page - 1) * per_page

    total_messages = db.query(Message).filter(Message.channel_id == channel_id).count()

    messages = (
        db.query(Message)
        .filter(Message.channel_id == channel_id)
        .order_by(Message.created_at)
        .offset(offset)
        .limit(per_page)
        .all()
    )

    message_list = [
        MessageResponse(
            message_id=message.id,
            channel_id=message.channel_id,
            content=message.content,
            timestamp=message.created_at
        )
        for message in messages
    ]

    return PaginatedMessagesResponse(
        page=page,
        per_page=per_page,
        total=total_messages,
        messages=message_list
    )
