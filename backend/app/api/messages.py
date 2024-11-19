from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageResponse
from app.core.security import oauth2_scheme
from jose import jwt
from app.core.config import settings

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/send", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def send_message(
    message: MessageCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    
    if not message.content.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Message content is required."
        )

   
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_email = payload.get("sub")
        user = db.query(User).filter(User.email == user_email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

    
    new_message = Message(
        channel_id=message.channel_id,
        user_id=user.id,
        content=message.content
    )
    
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    
    return {
        "message_id": new_message.id,
        "channel_id": new_message.channel_id,
        "content": new_message.content,
        "timestamp": new_message.timestamp
    }