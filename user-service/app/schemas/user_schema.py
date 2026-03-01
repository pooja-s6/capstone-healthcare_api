from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.models.user import UserRole

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    phone: str = None
    role: UserRole
    specialization: str = None
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: str = None
    phone: str = None
    specialization: str = None