from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.services.prescription_service import PrescriptionService
from app.schemas.prescription_schema import PrescriptionCreate, PrescriptionUpdate, PrescriptionResponse

router = APIRouter()

@router.post("/prescriptions", response_model=PrescriptionResponse, status_code=status.HTTP_201_CREATED)
def create_prescription(prescription_data: PrescriptionCreate, db: Session = Depends(get_db)):
    prescription_service = PrescriptionService(db)
    return prescription_service.create_prescription(prescription_data)

@router.get("/prescriptions/{prescription_id}", response_model=PrescriptionResponse)
def get_prescription(prescription_id: int, db: Session = Depends(get_db)):
    prescription_service = PrescriptionService(db)
    return prescription_service.get_prescription(prescription_id)

@router.get("/prescriptions", response_model=List[PrescriptionResponse])
def get_all_prescriptions(db: Session = Depends(get_db)):
    prescription_service = PrescriptionService(db)
    return prescription_service.get_all_prescriptions()

@router.get("/prescriptions/patient/{patient_id}", response_model=List[PrescriptionResponse])
def get_patient_prescriptions(patient_id: int, db: Session = Depends(get_db)):
    prescription_service = PrescriptionService(db)
    return prescription_service.get_patient_prescriptions(patient_id)

@router.get("/prescriptions/doctor/{doctor_id}", response_model=List[PrescriptionResponse])
def get_doctor_prescriptions(doctor_id: int, db: Session = Depends(get_db)):
    prescription_service = PrescriptionService(db)
    return prescription_service.get_doctor_prescriptions(doctor_id)

@router.put("/prescriptions/{prescription_id}", response_model=PrescriptionResponse)
def update_prescription(prescription_id: int, prescription_data: PrescriptionUpdate, db: Session = Depends(get_db)):
    prescription_service = PrescriptionService(db)
    return prescription_service.update_prescription(prescription_id, prescription_data)

@router.delete("/prescriptions/{prescription_id}")
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    prescription_service = PrescriptionService(db)
    return prescription_service.delete_prescription(prescription_id)