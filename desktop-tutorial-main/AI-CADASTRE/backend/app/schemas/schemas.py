from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field

from app.models.models import ReviewDecision, UserRole


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8)
    role: UserRole


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True


class ProjectCreate(BaseModel):
    name: str
    location: str = "Nagpur"


class ProjectResponse(BaseModel):
    id: int
    name: str
    location: str
    status: str
    created_by_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProcessingStartRequest(BaseModel):
    project_id: int


class ParcelResponse(BaseModel):
    id: int
    project_id: int
    name: str
    geometry_geojson: str
    area_sq_m: float
    confidence: float
    verification_status: str
    is_demo: bool

    class Config:
        from_attributes = True


class ParcelReviewRequest(BaseModel):
    decision: ReviewDecision
    comment: str = ""


class GroundTaskCreate(BaseModel):
    project_id: int
    parcel_id: int | None = None
    surveyor_id: int
    status: Literal["open", "in_progress", "done"] = "open"
    notes: str = ""


class GroundTaskResponse(BaseModel):
    id: int
    project_id: int
    parcel_id: int | None
    surveyor_id: int
    status: str
    notes: str
    created_at: datetime

    class Config:
        from_attributes = True
