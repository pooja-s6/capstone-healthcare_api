from fastapi import APIRouter, Request
import httpx
from app.core.config import settings

router = APIRouter()

SERVICE_MAP = {
    "auth": settings.AUTH_SERVICE_URL,
    "users": settings.USER_SERVICE_URL,
    "appointments": settings.APPOINTMENT_SERVICE_URL,
    "prescriptions": settings.PRESCRIPTION_SERVICE_URL,
}

@router.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):
    if service not in SERVICE_MAP:
        return {"error": "Service not found"}

    target_url = f"{SERVICE_MAP[service]}/{path}"
    
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=request.headers.raw,
            content=await request.body()
        )

    return response.json()