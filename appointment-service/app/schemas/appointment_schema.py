from pydantic import BaseModel
from datetime import datetime
from app.models.appointment import AppointmentStatus

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    reason: str = None
    notes: str = None

class AppointmentUpdate(BaseModel):
    appointment_date: datetime = None
    status: AppointmentStatus = None
    reason: str = None
    notes: str = None

class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    status: AppointmentStatus
    reason: str = None
    notes: str = None
    created_at: datetime

    class Config:
        from_attributes = True