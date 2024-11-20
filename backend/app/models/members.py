from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class WorldMember(Base):
    __tablename__ = "world_members"

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String, default="member")  # owner, moderator, member
    joined_at = Column(DateTime, default=datetime.utcnow)

    # Отношения
    user = relationship("User", backref="world_memberships")
    world = relationship("World", backref="members")