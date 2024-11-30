import uuid
import string
import random

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.schemas.voice import VoiceChannelData
from app.models.voice import VoicePeer, ActiveRoom
from app.db.database import get_db
from app.core.security import oauth2_scheme, get_current_user
from app.models.user import User
from app.models.channels import Channel, ChannelType

router = APIRouter(
    prefix="/voice",
    tags=["voice-chats"]
)


def generate_random_password(length=32):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@router.post("/{channel_id}/join", response_model=VoiceChannelData)
def join_voice_channel(
    channel_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    channel: Channel = db.query(Channel).filter(Channel.id == channel_id).first()

    if not channel:
        raise HTTPException(404, detail="Channel not found.")
    
    if channel.type not in [ChannelType.voice, ChannelType.video]:
        raise HTTPException(403, "Channel not of type 'voice' or 'video'.")

    room: ActiveRoom = db.query(ActiveRoom).filter(ActiveRoom.channel_id == channel_id).first()    
    if not room:
        print("No users found. Creating the room...")
        room = ActiveRoom(
            channel_id=channel.id,
            room_id=str(uuid.uuid4()),
            password=generate_random_password()
        )
        db.add(room)

    # Create a record that a new user just joined
    participant = VoicePeer(
        channel_id=channel_id,
        user_id=current_user.id
    )
    if not db.query(VoicePeer).filter(VoicePeer.user_id == current_user.id).first():
        db.add(participant)
    
    db.commit()

    return VoiceChannelData(
        room_id=room.room_id,
        password=room.password
    )


@router.post("/{channel_id}/leave", status_code=200)
def join_voice_channel(
    channel_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    participant: VoicePeer = db \
        .query(VoicePeer) \
        .filter(
            VoicePeer.channel_id == channel_id,
            VoicePeer.user_id == current_user.id
        ).first()

    if not participant:
        raise HTTPException(404, detail="User not active in that room.")

    db.delete(participant)
    db.commit()

    if not db.query(VoicePeer).first():
        room: ActiveRoom = db \
            .query(ActiveRoom) \
            .filter(
                ActiveRoom.channel_id == channel_id
            ).first()
        
        db.delete(room)
        db.commit()

    raise HTTPException(status_code=200)