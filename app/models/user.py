from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class UserRole(str, enum.Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

class User(BaseModel):
    __tablename__ = "users"
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    phone = Column(String)
    role = Column(Enum(UserRole), nullable=False)
    specialization = Column(String)
    
    appointments_as_doctor = relationship("Appointment", foreign_keys="Appointment.doctor_id", back_populates="doctor")
    appointments_as_patient = relationship("Appointment", foreign_keys="Appointment.patient_id", back_populates="patient")
    prescriptions_as_doctor = relationship("Prescription", foreign_keys="Prescription.doctor_id", back_populates="doctor")
    prescriptions_as_patient = relationship("Prescription", foreign_keys="Prescription.patient_id", back_populates="patient")