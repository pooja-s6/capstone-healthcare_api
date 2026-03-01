from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import prescription

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Prescription Service", version="1.0.0")

app.include_router(prescription.router, prefix="", tags=["Prescriptions"])

@app.get("/")
def root():
    return {"message": "Prescription Service is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}