from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    world_id = Column(Integer, ForeignKey("worlds.world_id"))

    #world = relationship("World", back_populates="channels")