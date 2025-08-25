"""
Health service for TravelLangGraph API.
Contains business logic for health-related operations.
"""

from datetime import datetime
import psutil
import os

class HealthService:
    """Service class for health-related operations."""
    
    @staticmethod
    def get_system_health() -> dict:
        """Get comprehensive system health information."""
        return {
            "status": "healthy",
            "service": "TravelLangGraph API",
            "timestamp": datetime.utcnow(),
            "system": {
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent
            },
            "process": {
                "pid": os.getpid(),
                "memory_info": psutil.Process().memory_info()._asdict()
            }
        }
    
    @staticmethod
    def is_healthy() -> bool:
        """Check if the service is healthy."""
        try:
            # Basic health checks
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            
            # Consider healthy if CPU < 90% and memory < 90%
            return cpu_usage < 90 and memory_usage < 90
        except Exception:
            return False
    
    @staticmethod
    def get_uptime() -> float:
        """Get system uptime in seconds."""
        return psutil.boot_time()
