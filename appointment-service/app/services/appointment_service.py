from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.appointment_repository import AppointmentRepository
from app.schemas.appointment_schema import AppointmentCreate, AppointmentUpdate

class AppointmentService:
    def __init__(self, db: Session):
        self.db = db
        self.appointment_repo = AppointmentRepository(db)

    def create_appointment(self, appointment_data: AppointmentCreate):
        appointment_dict = appointment_data.model_dump()
        return self.appointment_repo.create(appointment_dict)

    def get_appointment(self, appointment_id: int):
        appointment = self.appointment_repo.get_by_id(appointment_id)
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
        return appointment

    def get_all_appointments(self):
        return self.appointment_repo.get_all()

    def get_patient_appointments(self, patient_id: int):
        return self.appointment_repo.get_by_patient(patient_id)

    def get_doctor_appointments(self, doctor_id: int):
        return self.appointment_repo.get_by_doctor(doctor_id)

    def update_appointment(self, appointment_id: int, appointment_data: AppointmentUpdate):
        appointment = self.appointment_repo.update(appointment_id, appointment_data.model_dump(exclude_unset=True))
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
        return appointment

    def delete_appointment(self, appointment_id: int):
        appointment = self.appointment_repo.delete(appointment_id)
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
        return {"message": "Appointment deleted successfully"}