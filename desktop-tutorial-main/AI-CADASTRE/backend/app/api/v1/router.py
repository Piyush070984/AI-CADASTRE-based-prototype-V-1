from fastapi import APIRouter

from app.api.v1.endpoints import auth, exports, ground_tasks, parcels, processing, projects, reports, uploads, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(uploads.router, prefix="/uploads", tags=["uploads"])
api_router.include_router(processing.router, prefix="/processing", tags=["processing"])
api_router.include_router(parcels.router, prefix="/parcels", tags=["parcels"])
api_router.include_router(ground_tasks.router, prefix="/ground-tasks", tags=["ground-tasks"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
api_router.include_router(exports.router, prefix="/exports", tags=["exports"])
