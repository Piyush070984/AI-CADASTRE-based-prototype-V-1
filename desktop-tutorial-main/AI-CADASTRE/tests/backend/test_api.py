import os
from pathlib import Path

from fastapi.testclient import TestClient

DB_PATH = Path("/tmp/aicadastre_test.db")
if DB_PATH.exists():
    DB_PATH.unlink()
os.environ["DATABASE_URL"] = f"sqlite:///{DB_PATH}"
os.environ["UPLOAD_DIR"] = "/tmp/aicadastre_uploads"

from app.main import app  # noqa: E402
from app.db.init_db import init_db, seed_db  # noqa: E402
from app.db.session import SessionLocal  # noqa: E402

init_db()
with SessionLocal() as session:
    seed_db(session)
client = TestClient(app)


def get_token(email: str, password: str) -> str:
    response = client.post("/api/v1/auth/login", json={"email": email, "password": password})
    assert response.status_code == 200
    return response.json()["access_token"]


def test_auth_me_and_projects_flow():
    token = get_token("admin@aicadastre.example.com", "Admin@123")
    headers = {"Authorization": "Bearer " + token}

    me = client.get("/api/v1/auth/me", headers=headers)
    assert me.status_code == 200
    assert me.json()["role"] == "admin"

    created = client.post("/api/v1/projects", headers=headers, json={"name": "T1", "location": "Nagpur"})
    assert created.status_code == 200
    listed = client.get("/api/v1/projects", headers=headers)
    assert listed.status_code == 200
    assert len(listed.json()) >= 1


def test_role_restriction_and_exports():
    surveyor_token = get_token("surveyor@aicadastre.example.com", "Surveyor@123")
    surveyor_headers = {"Authorization": "Bearer " + surveyor_token}

    blocked = client.get("/api/v1/users", headers=surveyor_headers)
    assert blocked.status_code == 403

    admin_token = get_token("admin@aicadastre.example.com", "Admin@123")
    admin_headers = {"Authorization": "Bearer " + admin_token}

    parcels = client.get("/api/v1/parcels", headers=admin_headers)
    assert parcels.status_code == 200
    parcel_id = parcels.json()[0]["id"]

    reviewed = client.post(
        f"/api/v1/parcels/{parcel_id}/review",
        headers=surveyor_headers,
        json={"decision": "accept", "comment": "checked"},
    )
    assert reviewed.status_code == 200

    geojson = client.get("/api/v1/exports/parcels.geojson", headers=admin_headers)
    assert geojson.status_code == 200
    assert geojson.json()["type"] == "FeatureCollection"

    csv_data = client.get("/api/v1/exports/parcels.csv", headers=admin_headers)
    assert csv_data.status_code == 200
    assert "id,project_id" in csv_data.text
