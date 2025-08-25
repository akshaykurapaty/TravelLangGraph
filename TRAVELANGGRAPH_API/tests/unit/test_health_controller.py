"""
Unit tests for health controller.
"""

import pytest
from fastapi.testclient import TestClient
from datetime import datetime

def test_health_check_endpoint_returns_data(client: TestClient):
    """Test that health check endpoint returns data."""
    response = client.get("/health/")
    
    # Check if response is successful
    assert response.status_code == 200
    
    # Check if response contains data
    data = response.json()
    assert data is not None
    assert isinstance(data, dict)
    
    # Check required fields
    assert "status" in data
    assert "service" in data
    assert "timestamp" in data
    
    # Check field types and values
    assert data["status"] == "healthy"
    assert data["service"] == "TravelLangGraph API"
    assert data["timestamp"] is not None

def test_health_ping_endpoint_returns_data(client: TestClient):
    """Test that health ping endpoint returns data."""
    response = client.get("/health/ping")
    
    # Check if response is successful
    assert response.status_code == 200
    
    # Check if response contains data
    data = response.json()
    assert data is not None
    assert isinstance(data, dict)
    
    # Check required fields
    assert "message" in data
    assert "timestamp" in data
    
    # Check field values
    assert data["message"] == "pong"
    assert data["timestamp"] is not None

def test_health_endpoints_return_json(client: TestClient):
    """Test that health endpoints return JSON content type."""
    health_response = client.get("/health/")
    ping_response = client.get("/health/ping")
    
    assert health_response.headers["content-type"] == "application/json"
    assert ping_response.headers["content-type"] == "application/json"
