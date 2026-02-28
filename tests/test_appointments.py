import pytest
from fastapi import status
from datetime import datetime, timedelta

class TestAppointments:
    """Test appointment endpoints"""
    
    def test_create_appointment_unauthenticated(self, client):
        """Test creating appointment without authentication"""
        appointment_data = {
            "doctor_id": 1,
            "patient_id": 2,
            "appointment_datetime": datetime.now().isoformat(),
            "reason": "Checkup"
        }
        response = client.post("/api/appointments/", json=appointment_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_appointments_unauthenticated(self, client):
        """Test getting appointments without authentication"""
        response = client.get("/api/appointments/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_nonexistent_appointment(self, client, auth_token):
        """Test getting a nonexistent appointment"""
        response = client.get(
            "/api/appointments/99999",
            headers={"Authorization": f"Bearer {auth_token}"}
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
