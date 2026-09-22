from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, get_db
from app.models.models import Parcel, ParcelReview, User
from app.schemas.schemas import ParcelResponse, ParcelReviewRequest

router = APIRouter()


@router.get("", response_model=list[ParcelResponse])
def list_parcels(project_id: int | None = None, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    query = db.query(Parcel)
    if project_id:
        query = query.filter(Parcel.project_id == project_id)
    return query.all()


@router.get("/{parcel_id}", response_model=ParcelResponse)
def get_parcel(parcel_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    parcel = db.get(Parcel, parcel_id)
    if not parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return parcel


@router.post("/{parcel_id}/review")
def review_parcel(
    parcel_id: int,
    payload: ParcelReviewRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    parcel = db.get(Parcel, parcel_id)
    if not parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")

    review = ParcelReview(parcel_id=parcel_id, reviewer_id=user.id, decision=payload.decision, comment=payload.comment)
    parcel.verification_status = payload.decision.value
    db.add(review)
    db.commit()
    return {"status": "saved", "parcel_id": parcel_id, "decision": payload.decision, "mode": "demo"}
