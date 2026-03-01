from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.router import api_router
from app.middleware.cors import add_cors_middleware
from app.middleware.logging_middleware import log_requests

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Healthcare API", version="1.0.0")

add_cors_middleware(app)
app.middleware("http")(log_requests)

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Healthcare API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}