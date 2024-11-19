from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

# Ручка для создания канала
@router.post("/create", response_model=schemas.ChannelResponse, responses={400: {"model": schemas.ErrorResponse}})
def create_channel(channel: schemas.ChannelCreate, db: Session = Depends(database.get_db)):
    if not channel.name:
        raise HTTPException(status_code=400, detail="Channel name is required.")
    new_channel = crud.create_channel(db, channel.world_id, channel.name, channel.type)
    return schemas.ChannelResponse(
        channel_id=new_channel.id,
        name=new_channel.name,
        type=new_channel.type,
        world_id=new_channel.world_id
    )

# Ручка для получения всех каналов с пагинацией

@router.get("/all", response_model=schemas.PaginatedChannelsResponse)
def get_channels(
    page: int = Query(1, ge=1),  # Параметр страницы, по умолчанию 1
    per_page: int = Query(10, gt=0),  # Параметр количества на странице, по умолчанию 10
    db: Session = Depends(database.get_db)
):
    total_channels = crud.get_total_channels_count(db)
    channels = crud.get_channels_by_page(db, page, per_page)

    return schemas.PaginatedChannelsResponse(
        page=page,
        per_page=per_page,
        total=total_channels,
        channels=[
            schemas.ChannelInfo(
                channel_id=channel.id,
                name=channel.name,
                type=channel.type,
                world_id=channel.world_id
            )
            for channel in channels
        ]
    )


# Ручка для получения канала по ID
@router.get("/{channel_id}", response_model=schemas.ChannelDetailResponse, responses={404: {"model": schemas.ErrorResponse}})
def get_channel(channel_id: int, db: Session = Depends(database.get_db)):
    channel = crud.get_channel_by_id(db, channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found.")
    return schemas.ChannelDetailResponse(
        channel_id=channel.id,
        name=channel.name,
        type=channel.type,
        world_id=channel.world_id,
        messages=[]
    )

