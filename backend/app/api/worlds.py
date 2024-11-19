from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.worlds import World
from app.schemas.worlds import WorldCreate, WorldUpdate, WorldResponse
from app.db.database import get_db
from app.core.security import oauth2_scheme, get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/worlds",
    tags=["worlds"]
)

@router.post("/create", response_model=WorldResponse, status_code=201)
def create_world(
    world: WorldCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  
):
    if not world.name:
        raise HTTPException(status_code=400, detail="World name is required.")

    db_world = World(
        name=world.name, 
        description=world.description,
        owner_id=current_user.id  
    )
    db.add(db_world)
    db.commit()
    db.refresh(db_world)

    return db_world

@router.get("/{world_id}", response_model=WorldResponse)
def get_world(
    world_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_world = db.query(World).filter(World.id == world_id).first()
    if not db_world:
        raise HTTPException(
            status_code=404, 
            detail="World not found"
        )
    return db_world