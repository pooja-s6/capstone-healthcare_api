from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.prescription_repository import PrescriptionRepository
from app.models.user import UserRole

class PrescriptionService:
    def __init__(self, db: Session):
        self.db = db
        self.prescription_repo = PrescriptionRepository(db)

    def create_prescription(self, prescription_data: dict, doctor_id: int):
        return self.prescription_repo.create(prescription_data)

    def get_prescription_by_id(self, prescription_id: int):
        prescription = self.prescription_repo.get_by_id(prescription_id)
        if not prescription:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescription not found")
        return prescription

    def get_user_prescriptions(self, user_id: int, role: UserRole):
        if role == UserRole.doctor:
            return self.prescription_repo.get_by_doctor(user_id)
        elif role == UserRole.patient:
            return self.prescription_repo.get_by_patient(user_id)
        else:
            return self.prescription_repo.get_all()

    def delete_prescription(self, prescription_id: int, doctor_id: int):
        prescription = self.prescription_repo.delete(prescription_id)
        if not prescription:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescription not found")
        return prescription