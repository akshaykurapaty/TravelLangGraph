"""
Unit tests for hello controller.
"""

import pytest
from fastapi.testclient import TestClient

def test_hello_world_endpoint_returns_data(client: TestClient):
    """Test that hello world endpoint returns data."""
    response = client.get("/hello/")
    
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
    assert data["message"] == "Hello, World!"
    assert data["timestamp"] is not None

def test_hello_name_endpoint_returns_data(client: TestClient):
    """Test that hello name endpoint returns data."""
    test_name = "John"
    response = client.get(f"/hello/{test_name}")
    
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
    assert data["message"] == f"Hello, {test_name}!"
    assert data["timestamp"] is not None

def test_hello_endpoints_return_json(client: TestClient):
    """Test that hello endpoints return JSON content type."""
    hello_response = client.get("/hello/")
    name_response = client.get("/hello/TestUser")
    
    assert hello_response.headers["content-type"] == "application/json"
    assert name_response.headers["content-type"] == "application/json"

def test_hello_name_with_different_names(client: TestClient):
    """Test hello name endpoint with various names."""
    test_names = ["Alice", "Bob", "Charlie", "123"]
    
    for name in test_names:
        response = client.get(f"/hello/{name}")
        assert response.status_code == 200
        
        data = response.json()
        assert data["message"] == f"Hello, {name}!"
        assert data["timestamp"] is not None
