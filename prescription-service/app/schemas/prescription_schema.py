from pydantic import BaseModel
from datetime import datetime

class PrescriptionCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_id: int = None
    medication: str
    dosage: str
    frequency: str
    duration: str
    instructions: str = None

class PrescriptionUpdate(BaseModel):
    medication: str = None
    dosage: str = None
    frequency: str = None
    duration: str = None
    instructions: str = None

class PrescriptionResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_id: int = None
    medication: str
    dosage: str
    frequency: str
    duration: str
    instructions: str = None
    created_at: datetime

    class Config:
        from_attributes = True