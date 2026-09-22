from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from app.core.deps import get_current_user, get_db
from app.models.models import User
from app.services.export_service import build_csv, build_geojson

router = APIRouter()


@router.get("/parcels.geojson")
def export_geojson(project_id: int | None = None, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    return build_geojson(db, project_id)


@router.get("/parcels.csv")
def export_csv(project_id: int | None = None, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    return PlainTextResponse(content=build_csv(db, project_id), media_type="text/csv")
