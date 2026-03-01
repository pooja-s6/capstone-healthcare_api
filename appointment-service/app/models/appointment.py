from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
import enum
from datetime import datetime
from app.core.database import Base

class AppointmentStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, nullable=False)
    doctor_id = Column(Integer, nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    status = Column(Enum(AppointmentStatus), default=AppointmentStatus.pending)
    reason = Column(String)
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)