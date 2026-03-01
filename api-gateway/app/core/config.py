from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AUTH_SERVICE_URL: str
    USER_SERVICE_URL: str
    APPOINTMENT_SERVICE_URL: str
    PRESCRIPTION_SERVICE_URL: str

    class Config:
        env_file = ".env.docker"

settings = Settings()