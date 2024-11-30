from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.achievement import user_achievements

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    profile_pic_url = Column(String, default="https://i.pinimg.com/736x/09/7d/3c/097d3cf1d036e549d1caa10ad9268dfe.jpg")
    banner_url = Column(String, default="")
    bio = Column(String, default="")

    achievements = relationship(
        "Achievement",
        secondary=user_achievements,
        backref="users"
    )