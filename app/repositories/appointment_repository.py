from sqlalchemy.orm import Session
from app.models.appointment import Appointment, AppointmentStatus

class AppointmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, appointment_data: dict):
        appointment = Appointment(**appointment_data)
        self.db.add(appointment)
        self.db.commit()
        self.db.refresh(appointment)
        return appointment

    def get_by_id(self, appointment_id: int):
        return self.db.query(Appointment).filter(Appointment.id == appointment_id).first()

    def get_all(self):
        return self.db.query(Appointment).all()

    def get_by_doctor(self, doctor_id: int):
        return self.db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

    def get_by_patient(self, patient_id: int):
        return self.db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

    def update(self, appointment_id: int, appointment_data: dict):
        appointment = self.get_by_id(appointment_id)
        if appointment:
            for key, value in appointment_data.items():
                if value is not None:
                    setattr(appointment, key, value)
            self.db.commit()
            self.db.refresh(appointment)
        return appointment

    def delete(self, appointment_id: int):
        appointment = self.get_by_id(appointment_id)
        if appointment:
            self.db.delete(appointment)
            self.db.commit()
        return appointment