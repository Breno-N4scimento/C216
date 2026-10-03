from fastapi import APIRouter
from app.schemas.health import HealthResponse
from app.services.health import get_health_status

router = APIRouter()


@router.get("/", response_model=HealthResponse)
def health_check():
    return get_health_status()