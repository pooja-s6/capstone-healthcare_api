from pydantic import BaseModel
from datetime import datetime
from app.models.appointment import AppointmentStatus

class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_datetime: datetime
    reason: str = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    appointment_datetime: datetime = None
    reason: str = None
    status: AppointmentStatus = None

class AppointmentResponse(AppointmentBase):
    id: int
    status: AppointmentStatus
    created_at: datetime

    class Config:
        from_attributes = True