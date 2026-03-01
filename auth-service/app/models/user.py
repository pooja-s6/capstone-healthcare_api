from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from datetime import datetime
from app.core.database import Base

class UserRole(str, enum.Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    phone = Column(String)
    role = Column(Enum(UserRole), nullable=False)
    specialization = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)