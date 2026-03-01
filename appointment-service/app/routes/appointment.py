from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.services.appointment_service import AppointmentService
from app.schemas.appointment_schema import AppointmentCreate, AppointmentUpdate, AppointmentResponse

router = APIRouter()

@router.post("/appointments", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(appointment_data: AppointmentCreate, db: Session = Depends(get_db)):
    appointment_service = AppointmentService(db)
    return appointment_service.create_appointment(appointment_data)

@router.get("/appointments/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment_service = AppointmentService(db)
    return appointment_service.get_appointment(appointment_id)

@router.get("/appointments", response_model=List[AppointmentResponse])
def get_all_appointments(db: Session = Depends(get_db)):
    appointment_service = AppointmentService(db)
    return appointment_service.get_all_appointments()

@router.get("/appointments/patient/{patient_id}", response_model=List[AppointmentResponse])
def get_patient_appointments(patient_id: int, db: Session = Depends(get_db)):
    appointment_service = AppointmentService(db)
    return appointment_service.get_patient_appointments(patient_id)

@router.get("/appointments/doctor/{doctor_id}", response_model=List[AppointmentResponse])
def get_doctor_appointments(doctor_id: int, db: Session = Depends(get_db)):
    appointment_service = AppointmentService(db)
    return appointment_service.get_doctor_appointments(doctor_id)

@router.put("/appointments/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(appointment_id: int, appointment_data: AppointmentUpdate, db: Session = Depends(get_db)):
    appointment_service = AppointmentService(db)
    return appointment_service.update_appointment(appointment_id, appointment_data)

@router.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment_service = AppointmentService(db)
    return appointment_service.delete_appointment(appointment_id)