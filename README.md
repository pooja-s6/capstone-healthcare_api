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

## Database Migrations

This project uses Alembic for database migrations.

### Setup

Alembic is already configured. The configuration file is `alembic.ini` and the database URL is set to use the `healthcare_db` database.

### Common Migration Commands

1. **Create a new migration after model changes:**
   ```bash
   alembic revision --autogenerate -m "description of changes"
   ```

2. **Apply all pending migrations:**
   ```bash
   alembic upgrade head
   ```

3. **Rollback the last migration:**
   ```bash
   alembic downgrade -1
   ```

4. **View migration history:**
   ```bash
   alembic history
   ```

5. **Check current migration version:**
   ```bash
   alembic current
   ```

### Migration Workflow

1. Make changes to your models in `app/models/`
2. Generate a migration: `alembic revision --autogenerate -m "Add new field to User table"`
3. Review the generated migration file in `alembic/versions/`
4. Apply the migration: `alembic upgrade head`

**Note:** The database URL is configured in `alembic.ini` but will be overridden by the `DATABASE_URL` environment variable from `.env` if present.
