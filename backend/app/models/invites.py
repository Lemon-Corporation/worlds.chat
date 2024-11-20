from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base


class Invite(Base):
    __tablename__ = "invites"

    db_id = Column(Integer, primary_key=True, index=True)
    invite_code = Column(String(8), index=True, unique=True)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    expiration_date = Column(DateTime)
    creator_id = Column(Integer, ForeignKey("users.id"))
    invited_user_id = Column(Integer, default=0)  # 0 means open invitation

    creator = relationship("User", backref="created_invites")