"""
Hello world controller for TravelLangGraph API.
"""

from fastapi import APIRouter
from datetime import datetime
from models.schemas import HelloResponse

router = APIRouter(prefix="/hello", tags=["hello"])

@router.get("/", response_model=HelloResponse)
async def hello_world():
    """Hello World endpoint."""
    return HelloResponse(
        message="Hello, World!",
        timestamp=datetime.utcnow()
    )

@router.get("/{name}")
async def hello_name(name: str):
    """Hello with custom name endpoint."""
    return HelloResponse(
        message=f"Hello, {name}!",
        timestamp=datetime.utcnow()
    )
