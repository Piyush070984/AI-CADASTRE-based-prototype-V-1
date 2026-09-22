# AI-CADASTRE (Foundation Full-Stack Implementation)

This repository now contains a runnable first implementation of the AI-CADASTRE web application with:
- React + TypeScript + Vite frontend
- FastAPI backend
- SQLAlchemy models (PostgreSQL/PostGIS target, SQLite default fallback)
- JWT login and role-based access for admin/surveyor
- Demo Nagpur-centered map/data flow with clear demo labeling

> ⚠️ AI and GIS processing outputs are deterministic demo placeholders in this version. They are **not trained-model predictions** and must not be treated as official cadastral outputs.

## Folder structure

```text
AI-CADASTRE/
├── frontend/
├── backend/
├── ai_model/
├── gis_processing/
├── database/
├── prototype/
├── tests/
├── docs/
├── scripts/
├── storage/
├── .github/workflows/
├── docker-compose.yml
├── .env.example
├── .gitignore
├── Makefile
└── README.md
```

## Demo accounts (local development only)
- Admin: `admin@aicadastre.example.com` / `Admin@123`
- Surveyor: `surveyor@aicadastre.example.com` / `Surveyor@123`

## Local setup

### 1) Backend
```bash
cd AI-CADASTRE/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2) Frontend
```bash
cd AI-CADASTRE/frontend
npm install
npm run dev
```

Frontend defaults to `http://localhost:5173`, backend to `http://localhost:8000`.

## Docker setup
```bash
cd AI-CADASTRE
docker compose up --build
```

## Tests
```bash
pytest AI-CADASTRE/tests/backend -q
cd AI-CADASTRE/frontend && npm run test
```

## API quick usage
- `POST /api/v1/auth/login`
- Use returned bearer token for protected endpoints.
- OpenAPI docs available at `http://localhost:8000/docs`.

## Data and license caveat
Demo GeoJSON is intentionally small and synthetic near Nagpur for development/testing UX only. Replace with authorized datasets and track licensing/permissions before production use.

## Replacing demo GIS/AI
1. Ingest authorized raster/vector data.
2. Implement real worker queue (Celery/RQ) in processing service.
3. Wire `ai_model` training/inference outputs into `gis_processing` modules.
4. Remove demo labels only after measured evaluation and verified legal data usage.
