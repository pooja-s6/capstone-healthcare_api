from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service", version="1.0.0")

app.include_router(user.router, prefix="", tags=["Users"])

@app.get("/")
def root():
    return {"message": "User Service is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}