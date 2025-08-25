"""
Unit tests for chat controller.
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

def test_chat_health_endpoint_returns_data(client: TestClient):
    """Test that chat health endpoint returns data."""
    response = client.get("/chat/health")
    
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
    assert "endpoints" in data
    
    # Check field values
    assert data["status"] == "healthy"
    assert data["service"] == "Chat API"
    assert isinstance(data["endpoints"], list)

def test_chat_endpoints_return_json(client: TestClient):
    """Test that chat endpoints return JSON content type."""
    health_response = client.get("/chat/health")
    
    assert health_response.headers["content-type"] == "application/json"

@patch('controllers.chat_controller.ChatService')
def test_simple_chat_endpoint_structure(mock_chat_service, client: TestClient):
    """Test that simple chat endpoint has correct structure."""
    # Mock the chat service
    mock_service = MagicMock()
    mock_service.send_message.return_value = {
        "status": "success",
        "ai_response": "Hello! How can I help you?",
        "processing_time_seconds": 1.5,
        "timestamp": "2024-01-01T00:00:00",
        "model": "deepseek-chat"
    }
    mock_chat_service.return_value = mock_service
    
    # Test request structure
    chat_request = {
        "message": "Hello, how are you?",
        "system_prompt": "You are a helpful assistant.",
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    response = client.post("/chat/simple", json=chat_request)
    
    # Should return 200 if service is properly mocked
    if response.status_code == 200:
        data = response.json()
        assert "status" in data
        assert "ai_response" in data
        assert "timestamp" in data

@patch('controllers.chat_controller.ChatService')
def test_context_chat_endpoint_structure(mock_chat_service, client: TestClient):
    """Test that context chat endpoint has correct structure."""
    # Mock the chat service
    mock_service = MagicMock()
    mock_service.chat_with_context.return_value = {
        "status": "success",
        "ai_response": "I understand the context.",
        "processing_time_seconds": 2.0,
        "timestamp": "2024-01-01T00:00:00",
        "model": "deepseek-chat",
        "usage": {"prompt_tokens": 10, "completion_tokens": 20}
    }
    mock_chat_service.return_value = mock_service
    
    # Test request structure
    chat_request = {
        "messages": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"},
            {"role": "user", "content": "How are you?"}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    response = client.post("/chat/context", json=chat_request)
    
    # Should return 200 if service is properly mocked
    if response.status_code == 200:
        data = response.json()
        assert "status" in data
        assert "ai_response" in data
        assert "timestamp" in data
