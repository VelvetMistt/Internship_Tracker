from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from app.schemas.auth import Role


class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: Role = Role.student
    verified: bool = False


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
