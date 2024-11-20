from sqlalchemy.orm import Session
from app.models.channels import Channel
from app.schemas.channels import ChannelCreate

def create_channel(db: Session, channel: ChannelCreate) -> Channel:
    db_channel = Channel(
        world_id=channel.world_id,
        name=channel.name,
        type=channel.type
    )
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel

def get_channel(db: Session, channel_id: int) -> Channel:
    return db.query(Channel).filter(Channel.id == channel_id).first()

def get_channels_by_world(db: Session, world_id: int, skip: int = 0, limit: int = 100):
    return db.query(Channel)\
        .filter(Channel.world_id == world_id)\
        .offset(skip)\
        .limit(limit)\
        .all()

def get_total_channels_count(db: Session, world_id: int = None):
    query = db.query(Channel)
    if world_id:
        query = query.filter(Channel.world_id == world_id)
    return query.count()

def get_channels_by_page(db: Session, page: int, per_page: int):
    skip = (page - 1) * per_page
    return db.query(Channel)\
        .offset(skip)\
        .limit(per_page)\
        .all()