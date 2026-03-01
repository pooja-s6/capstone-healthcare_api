from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import appointment

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appointment Service", version="1.0.0")

app.include_router(appointment.router, prefix="", tags=["Appointments"])

@app.get("/")
def root():
    return {"message": "Appointment Service is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}