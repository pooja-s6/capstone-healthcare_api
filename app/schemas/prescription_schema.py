from pydantic import BaseModel
from datetime import datetime

class PrescriptionBase(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_id: int = None
    medication: str
    dosage: str
    duration: str = None
    notes: str = None

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionResponse(PrescriptionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True