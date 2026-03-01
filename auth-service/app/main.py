from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Service", version="1.0.0")

app.include_router(auth.router, prefix="", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "Auth Service is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}