from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class AppointmentStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    completed = "completed"
    cancelled = "cancelled"

class Appointment(BaseModel):
    __tablename__ = "appointments"
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    appointment_datetime = Column(DateTime, nullable=False)
    reason = Column(String)
    status = Column(Enum(AppointmentStatus), default=AppointmentStatus.pending)
    
    doctor = relationship("User", foreign_keys=[doctor_id], back_populates="appointments_as_doctor")
    patient = relationship("User", foreign_keys=[patient_id], back_populates="appointments_as_patient")
    prescriptions = relationship("Prescription", back_populates="appointment")