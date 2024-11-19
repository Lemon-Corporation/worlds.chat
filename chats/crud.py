from sqlalchemy.orm import Session
from . import models

def create_channel(db: Session, world_id: int, name: str, type: str) -> models.Channel:
    new_channel = models.Channel(world_id=world_id, name=name, type=type)
    db.add(new_channel)
    db.commit()
    db.refresh(new_channel)
    return new_channel

def get_channel_by_id(db: Session, channel_id: int) -> models.Channel:
    return db.query(models.Channel).filter(models.Channel.id == channel_id).first()

#def get_all_channels(db: Session, offset: int = 0, limit: int = 10):
 #   return db.query(models.Channel).offset(offset).limit(limit).all()

def get_total_channels_count(db: Session):
    return db.query(models.Channel).count()

def get_channels_by_page(db: Session, page: int, per_page: int):
    skip = (page - 1) * per_page
    return db.query(models.Channel).offset(skip).limit(per_page).all()