import json

from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.db.base import Base
from app.db.session import engine
from app.models.models import Parcel, Project, User, UserRole


NAGPUR_DEMO_POLYGONS = [
    {
        "name": "Parcel-A",
        "area_sq_m": 812.4,
        "confidence": 0.86,
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[79.0888, 21.1457], [79.0893, 21.1457], [79.0893, 21.1462], [79.0888, 21.1462], [79.0888, 21.1457]]],
        },
    },
    {
        "name": "Parcel-B",
        "area_sq_m": 674.0,
        "confidence": 0.82,
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[79.0895, 21.1454], [79.0900, 21.1454], [79.0900, 21.1459], [79.0895, 21.1459], [79.0895, 21.1454]]],
        },
    },
]


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def seed_db(db: Session) -> None:
    if db.query(User).count() > 0:
        return

    admin = User(
        name="Admin User",
        email="admin@aicadastre.example.com",
        password_hash=hash_password("Admin@123"),
        role=UserRole.admin,
    )
    surveyor = User(
        name="Surveyor User",
        email="surveyor@aicadastre.example.com",
        password_hash=hash_password("Surveyor@123"),
        role=UserRole.surveyor,
    )
    db.add_all([admin, surveyor])
    db.flush()

    project = Project(name="Nagpur Demo Project", location="Nagpur Ward Demo Area", status="active", created_by_id=admin.id)
    db.add(project)
    db.flush()

    for item in NAGPUR_DEMO_POLYGONS:
        db.add(
            Parcel(
                project_id=project.id,
                name=item["name"],
                geometry_geojson=json.dumps(item["geometry"]),
                area_sq_m=item["area_sq_m"],
                confidence=item["confidence"],
                verification_status="pending",
                is_demo=True,
            )
        )

    db.commit()
