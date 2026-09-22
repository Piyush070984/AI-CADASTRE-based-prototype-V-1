import csv
import io
import json

from sqlalchemy.orm import Session

from app.models.models import Parcel


def build_geojson(db: Session, project_id: int | None = None) -> dict:
    query = db.query(Parcel)
    if project_id:
        query = query.filter(Parcel.project_id == project_id)

    features = []
    for parcel in query.all():
        features.append(
            {
                "type": "Feature",
                "geometry": json.loads(parcel.geometry_geojson),
                "properties": {
                    "id": parcel.id,
                    "project_id": parcel.project_id,
                    "name": parcel.name,
                    "area_sq_m": parcel.area_sq_m,
                    "confidence": parcel.confidence,
                    "verification_status": parcel.verification_status,
                    "is_demo": parcel.is_demo,
                },
            }
        )

    return {
        "type": "FeatureCollection",
        "metadata": {
            "mode": "demo",
            "warning": "Demo parcel geometries only. Not official cadastral output.",
        },
        "features": features,
    }


def build_csv(db: Session, project_id: int | None = None) -> str:
    query = db.query(Parcel)
    if project_id:
        query = query.filter(Parcel.project_id == project_id)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "project_id", "name", "area_sq_m", "confidence", "verification_status", "is_demo"])
    for parcel in query.all():
        writer.writerow(
            [parcel.id, parcel.project_id, parcel.name, parcel.area_sq_m, parcel.confidence, parcel.verification_status, parcel.is_demo]
        )
    return output.getvalue()
