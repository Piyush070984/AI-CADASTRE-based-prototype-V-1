from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, get_db
from app.models.models import Parcel, ProcessingJob, Project, User

router = APIRouter()


@router.get("/summary")
def report_summary(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    total_projects = db.query(func.count(Project.id)).scalar() or 0
    total_jobs = db.query(func.count(ProcessingJob.id)).scalar() or 0
    total_parcels = db.query(func.count(Parcel.id)).scalar() or 0
    verified = db.query(func.count(Parcel.id)).filter(Parcel.verification_status != "pending").scalar() or 0

    return {
        "mode": "demo",
        "warning": "Statistics are based on demo data until authorized datasets and trained models are integrated.",
        "total_projects": total_projects,
        "total_processing_jobs": total_jobs,
        "total_parcels": total_parcels,
        "verified_parcels": verified,
    }
