from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.appointment_repository import AppointmentRepository
from app.models.user import UserRole
from app.models.appointment import AppointmentStatus

class AppointmentService:
    def __init__(self, db: Session):
        self.db = db
        self.appointment_repo = AppointmentRepository(db)

    def create_appointment(self, appointment_data: dict, user_id: int):
        return self.appointment_repo.create(appointment_data)

    def get_appointment_by_id(self, appointment_id: int):
        appointment = self.appointment_repo.get_by_id(appointment_id)
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
        return appointment

    def get_user_appointments(self, user_id: int, role: UserRole):
        if role == UserRole.doctor:
            return self.appointment_repo.get_by_doctor(user_id)
        elif role == UserRole.patient:
            return self.appointment_repo.get_by_patient(user_id)
        else:
            return self.appointment_repo.get_all()

    def update_appointment(self, appointment_id: int, appointment_data: dict):
        appointment = self.appointment_repo.update(appointment_id, appointment_data)
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
        return appointment

    def cancel_appointment(self, appointment_id: int, user_id: int):
        appointment = self.get_appointment_by_id(appointment_id)
        appointment.status = AppointmentStatus.cancelled
        self.db.commit()
        return appointment