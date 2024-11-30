from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.worlds import World
from app.schemas.worlds import WorldCreate, WorldUpdate, WorldResponse
from app.db.database import get_db
from app.core.security import oauth2_scheme, get_current_user
from app.models.user import User
from app.models.members import WorldMember

router = APIRouter(
    prefix="/worlds",
    tags=["worlds"]
)

@router.post("/", response_model=WorldResponse, status_code=201)
def create_world(
    world: WorldCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  
):
    if not world.name:
        raise HTTPException(status_code=400, detail="World name is required.")
    
    # Если создаётся личный чат, проверяем наличие партнёра
    partner = None

    if world.is_personal_chat:
        if not world.partner_id:
            raise HTTPException(status_code=400, detail="To create a personal chat you need an ID of your partner.")

        partner = db.query(User).filter(User.id == world.partner_id).first()
        if not partner:
            raise HTTPException(status_code=403, details="Provided partner does not exist.")
        
    #Добавлена логика для родительского мира
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
    # Добавляем partner_id в объект World
    db_world = World(
        name=world.name, 
        description=world.description,
        owner_id=current_user.id,
        icon_url=world.icon_url,
        is_personal_chat=world.is_personal_chat,
        parent_world_id=world.parent_world_id, #Добавлен parent_world_id
        partner_id=world.partner_id,  # Добавлено partner_id
    )

    db.add(db_world)
    db.commit()
    db.refresh(db_world)

    # Создатель мира автоматически становится его участником
    membership = WorldMember(
        world_id=db_world.id,
        user_id=current_user.id,
        role="owner"
    )
    db.add(membership)

    # Если есть партнёр, добавляем его в мир
    if partner:
        partner_membership = WorldMember(
            world_id=db_world.id,
            user_id=partner.id,
            role="owner"
        )
        db.add(partner_membership)

    # Если этот мир является подмиром, нужно добавить всех существующих
    # членов мира в этот новый подмир.
    print(world.parent_world_id)
    if world.parent_world_id:
        print("Copying over users from parent world...")
        for member in db.query(WorldMember).filter(WorldMember.world_id == world.parent_world_id):
            if member.user_id != current_user.id:
                membership = WorldMember(
                    world_id=db_world.id,
                    user_id=member.user_id,
                    role="member"
                )
                db.add(membership)

    db.commit()

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

    stack = [db_world]
    while stack:
        current_world = stack.pop()
        children = db.query(World).filter(World.parent_world_id == current_world.id).all()
        stack.extend(children)
        db.delete(current_world)

    db.commit()
    return None


@router.patch("/{world_id}", response_model=WorldResponse)
def update_world(
    world_id: int, 
    update_data: WorldUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_world: World = db.query(World).filter(World.id == world_id).first()
    if not db_world:
        raise HTTPException(status_code=404, detail="World not found.")

    if db_world.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    if update_data.name is not None:
        db_world.name = update_data.name
    if update_data.description is not None:
        db_world.description = update_data.description
    if update_data.icon_url is not None:
        db_world.icon_url = update_data.icon_url

    db.commit()
    db.refresh(db_world)
    return db_world