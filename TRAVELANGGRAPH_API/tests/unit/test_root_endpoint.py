"""
Unit tests for root endpoint.
"""

import pytest
from fastapi.testclient import TestClient

def test_root_endpoint_returns_data(client: TestClient):
    """Test that root endpoint returns data."""
    response = client.get("/")
    
    # Check if response is successful
    assert response.status_code == 200
    
    # Check if response contains data
    data = response.json()
    assert data is not None
    assert isinstance(data, dict)
    
    # Check required fields
    assert "message" in data
    assert "version" in data
    
    # Check field values
    assert data["message"] == "Welcome to TravelLangGraph API!"
    assert data["version"] == "0.1.0"

def test_root_endpoint_returns_json(client: TestClient):
    """Test that root endpoint returns JSON content type."""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

def test_root_endpoint_structure(client: TestClient):
    """Test that root endpoint has correct structure."""
    response = client.get("/")
    data = response.json()
    
    # Check data types
    assert isinstance(data["message"], str)
    assert isinstance(data["version"], str)
    
    # Check message length
    assert len(data["message"]) > 0
    assert len(data["version"]) > 0
