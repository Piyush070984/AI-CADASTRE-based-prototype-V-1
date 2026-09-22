from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, get_db
from app.models.models import GroundTask, User
from app.schemas.schemas import GroundTaskCreate, GroundTaskResponse

router = APIRouter()


@router.post("", response_model=GroundTaskResponse)
def create_ground_task(payload: GroundTaskCreate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    task = GroundTask(
        project_id=payload.project_id,
        parcel_id=payload.parcel_id,
        surveyor_id=payload.surveyor_id,
        status=payload.status,
        notes=payload.notes,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
