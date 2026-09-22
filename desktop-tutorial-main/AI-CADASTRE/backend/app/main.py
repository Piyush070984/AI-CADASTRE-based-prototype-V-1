from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.db.init_db import init_db, seed_db
from app.db.session import SessionLocal

app = FastAPI(
    title=settings.app_name,
    description="AI-CADASTRE backend API. AI/GIS outputs are demo-mode unless explicitly replaced with trained and authorized pipelines.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()
    with SessionLocal() as db:
        seed_db(db)


@app.get("/")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "AI-CADASTRE API"}


app.include_router(api_router, prefix=settings.api_v1_prefix)
