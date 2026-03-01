from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.services.prescription_service import PrescriptionService
from app.schemas.prescription_schema import PrescriptionCreate, PrescriptionResponse
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=PrescriptionResponse, status_code=status.HTTP_201_CREATED)
def create_prescription(prescription_data: PrescriptionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    prescription_service = PrescriptionService(db)
    return prescription_service.create_prescription(prescription_data.model_dump(), current_user.id)

@router.get("/", response_model=List[PrescriptionResponse])
def get_prescriptions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    prescription_service = PrescriptionService(db)
    return prescription_service.get_user_prescriptions(current_user.id, current_user.role)

@router.get("/{prescription_id}", response_model=PrescriptionResponse)
def get_prescription(prescription_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    prescription_service = PrescriptionService(db)
    return prescription_service.get_prescription_by_id(prescription_id)

@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(prescription_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    prescription_service = PrescriptionService(db)
    prescription_service.delete_prescription(prescription_id, current_user.id)