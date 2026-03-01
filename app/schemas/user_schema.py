from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.models.user import UserRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone: str = None
    role: UserRole
    specialization: str = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: str = None
    phone: str = None
    specialization: str = None

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True