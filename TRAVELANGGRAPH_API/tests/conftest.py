"""
Pytest configuration and fixtures for TravelLangGraph API tests.
"""

import pytest
from fastapi.testclient import TestClient
from travelanggraph_api.main import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

@pytest.fixture
def app_instance():
    """Get the FastAPI app instance."""
    return app
