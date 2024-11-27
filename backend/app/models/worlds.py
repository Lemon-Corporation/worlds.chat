from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class World(Base):
    __tablename__ = "worlds"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'))
    is_personal_chat = Column(Boolean, default=False)
    icon_url = Column(String, default="")
    partner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    

    parent_world_id = Column(Integer, 
                             ForeignKey('worlds.id', ondelete="CASCADE"), 
                             nullable=True
                             )
    subworlds = relationship("World", 
                             backref="parent_world", 
                             remote_side=[id], 
                             cascade="all, delete-orphan", 
                             passive_deletes=True, 
                             single_parent=True
                             )

    # Используем строку вместо прямой ссылки на класс
    channels = relationship("Channel", back_populates="world", cascade="all, delete-orphan")