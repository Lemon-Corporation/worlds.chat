from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.worlds import World
from app.models.members import WorldMember
from app.models.user import User
from app.models.invites import Invite
from app.schemas.invites import InviteCreate, InviteResponse
from datetime import datetime, timedelta
from app.core.deps import get_current_user
import random
import string

router = APIRouter(
    prefix="/invites", 
    tags=["invites"]
)


def generate_invite_code(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@router.post("/", response_model=InviteResponse)
def create_invite(
    invite: InviteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check if the world exists
    world = db.query(World).filter(World.id == invite.world_id).first()
    if not world:
        raise HTTPException(status_code=404, detail="This world does not exist.")
    if world.parent_world_id:
        raise HTTPException(status_code=403, detail="Cannot create an invite for a subworld.")

    # Generate invite code and expiration date
    invite_code = generate_invite_code()
    expiration_date = datetime.utcnow() + timedelta(seconds=invite.lifespan)

    if not invite.invited_users:
        # Create a single open invitation
        db_invite = Invite(
            invite_code=invite_code,
            world_id=invite.world_id,
            expiration_date=expiration_date,
            creator_id=current_user.id,
            invited_user_id=0,
        )
        db.add(db_invite)
    else:
        # Create multiple invites for specific users
        for user_id in invite.invited_users:
            db_invite = Invite(
                invite_code=invite_code,
                world_id=invite.world_id,
                expiration_date=expiration_date,
                creator_id=current_user.id,
                invited_user_id=user_id,
            )
            db.add(db_invite)

    db.commit()

    return {"invite_token": invite_code, "expiration_date": expiration_date}


@router.get("/{invite_code}")
def get_invite(
    invite_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check if the invite exists
    invite = db.query(Invite).filter(Invite.invite_code == invite_code).first()
    if not invite:
        raise HTTPException(status_code=404, detail="The invitation is invalid.")

    # Remove expired invites
    if invite.expiration_date < datetime.utcnow():
        db.delete(invite)
        db.commit()
        raise HTTPException(status_code=404, detail="The invitation is invalid.")

    return {
        "world_id": invite.world_id,
        "expiration_date": invite.expiration_date,
    }


@router.post("/{invite_code}/accept")
def accept_invite(
    invite_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check if the invite exists
    invite = db.query(Invite).filter(Invite.invite_code == invite_code).first()
    if not invite:
        raise HTTPException(status_code=404, detail="The invitation is invalid.")

    # Remove expired invites
    if invite.expiration_date < datetime.utcnow():
        db.delete(invite)
        db.commit()
        raise HTTPException(status_code=404, detail="The invitation is invalid.")

    # Validate user
    if invite.invited_user_id not in (0, current_user.id):
        raise HTTPException(status_code=403, detail="The invitation is invalid.")
    
    # Check if the user is already in the world
    membership = db.query(WorldMember).filter(WorldMember.user_id == current_user.id).first()
    if membership:
        raise HTTPException(status_code=403, detail="The user is already a member of the world.")

    # Prevent creators from accepting their own invites
    if invite.creator_id == current_user.id:
        raise HTTPException(status_code=403, detail="The invitation is invalid.")

    # Add the user to the world members table
    world_member = WorldMember(world_id=invite.world_id, user_id=current_user.id)
    db.add(world_member)

    # If there are subworlds, add the user to them as well:
    for subworld in db.query(World).filter(World.parent_world_id == invite.world_id):
        membership = WorldMember(world_id=subworld.id, user_id=current_user.id)
        db.add(membership)

    db.commit()

    return {"message": "Invitation accepted."}


@router.delete("/{invite_code}")
def delete_invite(
    invite_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check if the invite exists
    invite = db.query(Invite).filter(Invite.invite_code == invite_code).first()
    if not invite:
        raise HTTPException(status_code=404, detail="The invitation is invalid.")

    # Only the creator can delete the invite
    if invite.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="You cannot revoke this invitation.")

    db.delete(invite)
    db.commit()

    return {"message": "Invitation deleted."}
