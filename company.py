from datetime import datetime
from pydantic import BaseModel, EmailStr


class CompanyBase(BaseModel):
    name: str
    website: str | None = None
    industry: str | None = None
    recruiter_email: EmailStr | None = None
    notes: str | None = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    website: str | None = None
    industry: str | None = None
    recruiter_email: EmailStr | None = None
    notes: str | None = None


class CompanyResponse(CompanyBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        orm_mode = True
