"""
Pydantic schemas for TravelLangGraph API.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    service: str
    timestamp: Optional[datetime] = None

class HelloResponse(BaseModel):
    """Hello world response model."""
    message: str
    timestamp: Optional[datetime] = None

class RootResponse(BaseModel):
    """Root endpoint response model."""
    message: str
    version: str
    timestamp: Optional[datetime] = None
