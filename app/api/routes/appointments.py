from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.services.appointment_service import AppointmentService
from app.schemas.appointment_schema import AppointmentCreate, AppointmentResponse, AppointmentUpdate
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(appointment_data: AppointmentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment_service = AppointmentService(db)
    return appointment_service.create_appointment(appointment_data.model_dump(), current_user.id)

@router.get("/", response_model=List[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment_service = AppointmentService(db)
    return appointment_service.get_user_appointments(current_user.id, current_user.role)

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment_service = AppointmentService(db)
    return appointment_service.get_appointment_by_id(appointment_id)

@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(appointment_id: int, appointment_data: AppointmentUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment_service = AppointmentService(db)
    return appointment_service.update_appointment(appointment_id, appointment_data.model_dump(exclude_unset=True))

@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_appointment(appointment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment_service = AppointmentService(db)
    appointment_service.cancel_appointment(appointment_id, current_user.id)