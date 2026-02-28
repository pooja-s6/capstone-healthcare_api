import pytest
from fastapi import status

class TestPatients:
    """Test patient endpoints"""
    
    def test_get_all_patients_unauthenticated(self, client):
        """Test getting all patients without authentication"""
        response = client.get("/api/patients/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_nonexistent_patient(self, client, auth_token):
        """Test getting a nonexistent patient"""
        response = client.get(
            "/api/patients/99999",
            headers={"Authorization": f"Bearer {auth_token}"}
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_update_patient_unauthenticated(self, client):
        """Test updating patient without authentication"""
        update_data = {"full_name": "Updated Name"}
        response = client.put("/api/patients/1", json=update_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
