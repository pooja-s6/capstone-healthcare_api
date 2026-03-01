from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.prescription_repository import PrescriptionRepository
from app.schemas.prescription_schema import PrescriptionCreate, PrescriptionUpdate

class PrescriptionService:
    def __init__(self, db: Session):
        self.db = db
        self.prescription_repo = PrescriptionRepository(db)

    def create_prescription(self, prescription_data: PrescriptionCreate):
        prescription_dict = prescription_data.model_dump()
        return self.prescription_repo.create(prescription_dict)

    def get_prescription(self, prescription_id: int):
        prescription = self.prescription_repo.get_by_id(prescription_id)
        if not prescription:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescription not found")
        return prescription

    def get_all_prescriptions(self):
        return self.prescription_repo.get_all()

    def get_patient_prescriptions(self, patient_id: int):
        return self.prescription_repo.get_by_patient(patient_id)

    def get_doctor_prescriptions(self, doctor_id: int):
        return self.prescription_repo.get_by_doctor(doctor_id)

    def update_prescription(self, prescription_id: int, prescription_data: PrescriptionUpdate):
        prescription = self.prescription_repo.update(prescription_id, prescription_data.model_dump(exclude_unset=True))
        if not prescription:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescription not found")
        return prescription

    def delete_prescription(self, prescription_id: int):
        prescription = self.prescription_repo.delete(prescription_id)
        if not prescription:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescription not found")
        return {"message": "Prescription deleted successfully"}