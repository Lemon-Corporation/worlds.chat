from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base
import enum

class ChannelType(enum.Enum):
    text = "text"
    voice = "voice"
    video = "video"
    todo = "todo"

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    type = Column(Enum(ChannelType), nullable=False)
    world_id = Column(Integer, ForeignKey("worlds.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Используем строку вместо прямой ссылки на класс
    world = relationship("World", back_populates="channels")