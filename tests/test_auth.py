import pytest
from fastapi import status

class TestAuth:
    """Test authentication endpoints"""
    
    def test_register_patient_success(self, client, test_patient_data):
        """Test successful patient registration"""
        response = client.post("/api/auth/register", json=test_patient_data)
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_register_duplicate_email(self, client, test_patient_data):
        """Test registration with duplicate email"""
        client.post("/api/auth/register", json=test_patient_data)
        response = client.post("/api/auth/register", json=test_patient_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_register_invalid_email(self, client, test_patient_data):
        """Test registration with invalid email"""
        test_patient_data["email"] = "invalid-email"
        response = client.post("/api/auth/register", json=test_patient_data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_login_success(self, client, test_patient_data):
        """Test successful login"""
        client.post("/api/auth/register", json=test_patient_data)
        response = client.post("/api/auth/login", data={
            "username": test_patient_data["email"],
            "password": test_patient_data["password"]
        })
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    
    def test_login_wrong_password(self, client, test_patient_data):
        """Test login with wrong password"""
        client.post("/api/auth/register", json=test_patient_data)
        response = client.post("/api/auth/login", data={
            "username": test_patient_data["email"],
            "password": "wrongpassword"
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
