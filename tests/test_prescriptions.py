import pytest
from fastapi import status

class TestPrescriptions:
    """Test prescription endpoints"""
    
    def test_create_prescription_unauthenticated(self, client):
        """Test creating prescription without authentication"""
        prescription_data = {
            "doctor_id": 1,
            "patient_id": 2,
            "medication": "Test Med",
            "dosage": "100mg"
        }
        response = client.post("/api/prescriptions/", json=prescription_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_prescriptions_unauthenticated(self, client):
        """Test getting prescriptions without authentication"""
        response = client.get("/api/prescriptions/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
