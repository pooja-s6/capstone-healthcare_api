import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db
from app.models.user import UserRole

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

@pytest.fixture
def test_patient_data():
    return {
        "email": "patient@test.com",
        "password": "password123",
        "full_name": "Test Patient",
        "phone": "1234567890",
        "role": UserRole.patient.value
    }

@pytest.fixture
def test_doctor_data():
    return {
        "email": "doctor@test.com",
        "password": "password123",
        "full_name": "Test Doctor",
        "phone": "0987654321",
        "role": UserRole.doctor.value,
        "specialization": "Cardiology"
    }

@pytest.fixture
def test_admin_data():
    return {
        "email": "admin@test.com",
        "password": "password123",
        "full_name": "Test Admin",
        "role": UserRole.admin.value
    }

@pytest.fixture
def auth_token(client, test_patient_data):
    # Register and login to get token
    client.post("/api/auth/register", json=test_patient_data)
    response = client.post("/api/auth/login", data={
        "username": test_patient_data["email"],
        "password": test_patient_data["password"]
    })
    return response.json()["access_token"]

@pytest.fixture
def doctor_token(client, test_doctor_data):
    # Register and login to get token
    client.post("/api/auth/register", json=test_doctor_data)
    response = client.post("/api/auth/login", data={
        "username": test_doctor_data["email"],
        "password": test_doctor_data["password"]
    })
    return response.json()["access_token"]
