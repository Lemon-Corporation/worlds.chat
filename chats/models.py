from sqlalchemy import Column, Integer, String
from .database import Base

class Channel(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
