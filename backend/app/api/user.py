from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.models.worlds import World
from app.models.members import WorldMember
from app.schemas.worlds import WorldResponse, UserWorldsList
from app.schemas.user import UserPublicInfoResponse, UserPrivateInfoResponse, UserUpdateRequest

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/me", response_model=UserPrivateInfoResponse)
def get_current_user_info(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    info: User = db \
        .query(User) \
        .filter(User.id == current_user.id) \
        .first()
    
    return UserPrivateInfoResponse(
        id=info.id,
        username=info.username,
        email=info.email,
        profile_pic_url=info.profile_pic_url,
        banner_url=info.banner_url,
        bio=info.bio
    )


@router.get("/worlds", response_model=UserWorldsList)
def get_participating_worlds(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    print(current_user)

    worlds = db \
        .query(World, WorldMember) \
        .join(WorldMember, WorldMember.world_id == World.id) \
        .filter(WorldMember.user_id == current_user.id) \
    
    world_responses = [
        WorldResponse(
            id=world.id,
            name=world.name,
            description=world.description,
            created_at=world.created_at,
            updated_at=world.updated_at,
            owner_id=world.owner_id,
            icon_url=world.icon_url,
            is_personal_chat=world.is_personal_chat,
            partner_id=world.partner_id,
            parent_world_id=world.parent_world_id,
        ) for world, _ in worlds
    ]

    for obj in world_responses:
        print(obj)

    return {"worlds": world_responses}


@router.get("/{user_id}", response_model=UserPublicInfoResponse)
def get_user_info_by_user_id(
    user_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user: User = db \
        .query(User) \
        .filter(User.id == current_user.id) \
        .first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User with such username not found.")
    
    return UserPublicInfoResponse(
        id=user.id,
        username=user.username,
        profile_pic_url=user.profile_pic_url,
        banner_url=user.banner_url,
        bio=user.bio
    )


@router.patch("/", status_code=status.HTTP_200_OK)
def update_user(
    update: UserUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user: User = db \
        .query(User) \
        .filter(User.id == current_user.id) \
        .first()
    
    for attr, value in vars(update).items():
        if attr == "email" and db.query(User).filter(User.email == update.email).first():
            raise HTTPException(status_code=400, detail="This email address is already in use.")

        if value is not None:
            setattr(user, attr, value)

    db.commit()
