from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Prescription(BaseModel):
    __tablename__ = "prescriptions"
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    medication = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    duration = Column(String)
    notes = Column(Text)
    
    doctor = relationship("User", foreign_keys=[doctor_id], back_populates="prescriptions_as_doctor")
    patient = relationship("User", foreign_keys=[patient_id], back_populates="prescriptions_as_patient")
    appointment = relationship("Appointment", back_populates="prescriptions")