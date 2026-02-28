import pytest
from fastapi import status

class TestDoctors:
    """Test doctor endpoints"""
    
    def test_get_all_doctors_unauthenticated(self, client):
        """Test getting all doctors without authentication"""
        response = client.get("/api/doctors/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_nonexistent_doctor(self, client, auth_token):
        """Test getting a nonexistent doctor"""
        response = client.get(
            "/api/doctors/99999",
            headers={"Authorization": f"Bearer {auth_token}"}
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
