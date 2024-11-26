from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.database import Base

class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    prompt = Column(Text)
    model = Column(String)  # название модели AI