from pydantic import BaseModel, EmailStr
from app.models.user import UserRole

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    phone: str = None
    role: UserRole
    specialization: str = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str