from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, get_db
from app.models.models import ProcessingJob, Project, User
from app.schemas.schemas import ProcessingStartRequest
from app.services.processing_service import start_demo_processing

router = APIRouter()


@router.post("/start")
def start_processing(payload: ProcessingStartRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    project = db.get(Project, payload.project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    job = start_demo_processing(db, payload.project_id, user.id)
    return {
        "id": job.id,
        "project_id": job.project_id,
        "status": job.status,
        "pipeline_type": job.pipeline_type,
        "metadata": job.metadata_json,
    }


@router.get("/{processing_id}")
def get_processing(processing_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    job = db.get(ProcessingJob, processing_id)
    if not job:
        raise HTTPException(status_code=404, detail="Processing job not found")
    return {
        "id": job.id,
        "project_id": job.project_id,
        "status": job.status,
        "pipeline_type": job.pipeline_type,
        "metadata": job.metadata_json,
    }
