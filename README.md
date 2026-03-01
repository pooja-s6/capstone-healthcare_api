# Healthcare API

Microservices-based healthcare management system.

## Running the Application

Start all services:
```bash
docker-compose up --build
```

Stop services:
```bash
docker-compose down
```

## Services

- API Gateway: http://localhost:8000
- Auth Service: http://localhost:8001
- User Service: http://localhost:8002
- Appointment Service: http://localhost:8003
- Prescription Service: http://localhost:8004
- Database: PostgreSQL on port 5432

## API Access

All requests go through the API Gateway at port 8000.

Example:
- Register: POST http://localhost:8000/auth/register
- Login: POST http://localhost:8000/auth/login
- Get Doctors: GET http://localhost:8000/users/doctors
