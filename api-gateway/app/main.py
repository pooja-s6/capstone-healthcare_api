from fastapi import FastAPI
from app.routers import proxy

app = FastAPI(title="Healthcare API Gateway", version="1.0.0")

app.include_router(proxy.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Healthcare API Gateway is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}