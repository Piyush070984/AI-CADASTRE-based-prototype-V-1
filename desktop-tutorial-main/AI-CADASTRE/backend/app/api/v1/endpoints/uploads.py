from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.deps import get_current_user, get_db
from app.models.models import Project, UploadedFile, User

router = APIRouter()
ALLOWED_EXTENSIONS = {".geojson", ".json", ".csv", ".tif", ".tiff", ".zip"}


@router.post("")
async def upload_file(
    project_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    content = await file.read()
    max_bytes = settings.max_upload_size_mb * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(status_code=400, detail=f"File too large (>{settings.max_upload_size_mb}MB)")

    settings.upload_path.mkdir(parents=True, exist_ok=True)
    destination = settings.upload_path / file.filename
    destination.write_bytes(content)

    record = UploadedFile(
        project_id=project_id,
        filename=file.filename or "uploaded_file",
        content_type=file.content_type or "application/octet-stream",
        size_bytes=len(content),
        path=str(destination),
        uploaded_by_id=user.id,
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return {"id": record.id, "filename": record.filename, "size_bytes": record.size_bytes, "status": "uploaded", "mode": "demo"}
