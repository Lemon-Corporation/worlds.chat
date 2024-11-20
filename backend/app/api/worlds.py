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
    
    if world.parent_world_id:
        parent_world = db.query(World).filter(World.id == world.parent_world_id).first()
        if not parent_world:
            raise HTTPException(
                status_code=404, 
                detail=f"Parent world with id {world.parent_world_id} not found"
            )
        if parent_world.owner_id != current_user.id:
            raise HTTPException(
                status_code=403, 
                detail="You do not have permission to use this parent world"
            )

    db_world = World(
        name=world.name, 
        description=world.description,
        owner_id=current_user.id,
        parent_world_id=world.parent_world_id
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



@router.delete("/{world_id}", status_code=204)
def delete_world(
    world_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_world = db.query(World).filter(World.id == world_id).first()
    if not db_world:
        raise HTTPException(status_code=404, detail="World not found.")

    if db_world.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    db.delete(db_world)
    db.commit()
    return None


@router.patch("/{world_id}/update", response_model=WorldResponse)
def update_world(
    world_id: int, 
    update_data: WorldUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_world = db.query(World).filter(World.id == world_id).first()
    if not db_world:
        raise HTTPException(status_code=404, detail="World not found.")

    if db_world.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    if update_data.name is not None:
        db_world.name = update_data.name
    if update_data.description is not None:
        db_world.description = update_data.description

    db.commit()
    db.refresh(db_world)
    return db_world