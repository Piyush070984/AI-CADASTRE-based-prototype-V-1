from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_role
from app.core.security import hash_password
from app.models.models import User, UserRole
from app.schemas.schemas import UserCreate, UserResponse

router = APIRouter()


@router.get("", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.admin))):
    return db.query(User).all()


@router.post("", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.admin))):
    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
