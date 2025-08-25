"""
Health check controller for TravelLangGraph API.
"""

from fastapi import APIRouter
from datetime import datetime
from models.schemas import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        service="TravelLangGraph API",
        timestamp=datetime.utcnow()
    )

@router.get("/ping")
async def ping():
    """Simple ping endpoint."""
    return {"message": "pong", "timestamp": datetime.utcnow().isoformat()}
