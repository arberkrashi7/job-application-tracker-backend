from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, Field


class ApplicationCreate(BaseModel):
    company: str = Field(min_length=1, max_length=200)
    role: str = Field(min_length=1, max_length=200)
    status: str = Field(default="applied", max_length=50)
    applied_date: date | None = None


class ApplicationRead(BaseModel):
    id: UUID
    user_id: UUID
    company: str
    role: str
    status: str
    applied_date: date | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
