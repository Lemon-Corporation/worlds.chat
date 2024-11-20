from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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

    parent_world_id = Column(Integer, ForeignKey('worlds.id'), nullable=True)
    subworlds = relationship("World", backref="parent_world", remote_side=[id], cascade="all, delete-orphan", single_parent=True)


    # Используем строку вместо прямой ссылки на класс
    channels = relationship("Channel", back_populates="world", cascade="all, delete-orphan")