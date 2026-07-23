from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, EmailStr


class ApplicationStatus(str, Enum):
    applied = "Applied"
    interviewing = "Interviewing"
    offer = "Offer"
    rejected = "Rejected"
    closed = "Closed"


class ApplicationBase(BaseModel):
    company_id: str
    position: str
    source: str = Field(default="Online")
    status: ApplicationStatus = ApplicationStatus.applied
    deadline: datetime | None = None
    notes: str | None = None
    recruiter_email: EmailStr | None = None
    recruiter_phone: str | None = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    status: ApplicationStatus | None = None
    deadline: datetime | None = None
    notes: str | None = None
    recruiter_email: EmailStr | None = None
    recruiter_phone: str | None = None


class ApplicationResponse(ApplicationBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        orm_mode = True
