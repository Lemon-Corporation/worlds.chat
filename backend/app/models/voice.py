from sqlalchemy import Column, String, Integer, ForeignKey
from app.db.database import Base

class VoicePeer(Base):
    __tablename__ = "voice_room_peers"

    record_id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)


class ActiveRoom(Base):
    __tablename__ = "active_voice_rooms"

    channel_id = Column(Integer, ForeignKey("channels.id"), primary_key=True, index=True)
    room_id = Column(String)
    password = Column(String)
