"""
Integration tests for TravelLangGraph API.
"""

import pytest
from fastapi.testclient import TestClient

def test_api_health_flow(client: TestClient):
    """Test the complete health check flow."""
    # Test ping first
    ping_response = client.get("/health/ping")
    assert ping_response.status_code == 200
    assert ping_response.json()["message"] == "pong"
    
    # Test full health check
    health_response = client.get("/health/")
    assert health_response.status_code == 200
    assert health_response.json()["status"] == "healthy"

def test_api_hello_flow(client: TestClient):
    """Test the complete hello flow."""
    # Test basic hello
    hello_response = client.get("/hello/")
    assert hello_response.status_code == 200
    assert hello_response.json()["message"] == "Hello, World!"
    
    # Test personalized hello
    name_response = client.get("/hello/IntegrationTest")
    assert name_response.status_code == 200
    assert name_response.json()["message"] == "Hello, IntegrationTest!"

def test_api_complete_flow(client: TestClient):
    """Test the complete API flow from root to all endpoints."""
    # Start with root
    root_response = client.get("/")
    assert root_response.status_code == 200
    assert "TravelLangGraph API" in root_response.json()["message"]
    
    # Check health
    health_response = client.get("/health/")
    assert health_response.status_code == 200
    assert health_response.json()["status"] == "healthy"
    
    # Check hello
    hello_response = client.get("/hello/")
    assert hello_response.status_code == 200
    assert hello_response.json()["message"] == "Hello, World!"

def test_api_response_consistency(client: TestClient):
    """Test that API responses are consistent across calls."""
    # Make multiple calls to same endpoints
    responses = []
    for _ in range(3):
        response = client.get("/health/")
        responses.append(response.json())
    
    # All responses should have same structure
    for response in responses:
        assert "status" in response
        assert "service" in response
        assert "timestamp" in response
        assert response["status"] == "healthy"
        assert response["service"] == "TravelLangGraph API"
