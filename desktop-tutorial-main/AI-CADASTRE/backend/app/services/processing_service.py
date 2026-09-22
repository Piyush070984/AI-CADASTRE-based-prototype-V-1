from sqlalchemy.orm import Session

from app.models.models import Parcel, ProcessingJob


def start_demo_processing(db: Session, project_id: int, user_id: int) -> ProcessingJob:
    parcels = db.query(Parcel).filter(Parcel.project_id == project_id).all()
    reviewed_count = sum(1 for parcel in parcels if parcel.verification_status != "pending")
    metadata = {
        "mode": "demo",
        "note": "Deterministic demo processing. Replace with authorized AI/GIS worker pipeline for real outputs.",
        "parcel_count": len(parcels),
        "reviewed_count": reviewed_count,
    }
    job = ProcessingJob(
        project_id=project_id,
        created_by_id=user_id,
        status="demo_complete",
        pipeline_type="deterministic_demo_pipeline",
        metadata_json=metadata,
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
