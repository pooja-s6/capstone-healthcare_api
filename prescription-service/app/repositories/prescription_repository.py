from sqlalchemy.orm import Session
from app.models.prescription import Prescription

class PrescriptionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, prescription_data: dict):
        prescription = Prescription(**prescription_data)
        self.db.add(prescription)
        self.db.commit()
        self.db.refresh(prescription)
        return prescription

    def get_by_id(self, prescription_id: int):
        return self.db.query(Prescription).filter(Prescription.id == prescription_id).first()

    def get_all(self):
        return self.db.query(Prescription).all()

    def get_by_patient(self, patient_id: int):
        return self.db.query(Prescription).filter(Prescription.patient_id == patient_id).all()

    def get_by_doctor(self, doctor_id: int):
        return self.db.query(Prescription).filter(Prescription.doctor_id == doctor_id).all()

    def update(self, prescription_id: int, prescription_data: dict):
        prescription = self.get_by_id(prescription_id)
        if prescription:
            for key, value in prescription_data.items():
                if value is not None:
                    setattr(prescription, key, value)
            self.db.commit()
            self.db.refresh(prescription)
        return prescription

    def delete(self, prescription_id: int):
        prescription = self.get_by_id(prescription_id)
        if prescription:
            self.db.delete(prescription)
            self.db.commit()
        return prescription