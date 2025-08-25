"""
Chat controller for TravelLangGraph API.
Contains chat-related API endpoints.
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["chat"])

# Request/Response Models
class ChatMessage(BaseModel):
    """Individual chat message model."""
    role: str = Field(..., description="Role of the message sender (user, assistant, system)")
    content: str = Field(..., description="Content of the message")

class SimpleChatRequest(BaseModel):
    """Simple chat request model."""
    message: str = Field(..., description="User message to send")
    system_prompt: Optional[str] = Field(None, description="Optional system prompt")
    model: str = Field("deepseek-chat", description="Model to use for chat")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Sampling temperature")
    max_tokens: int = Field(1000, ge=1, le=4000, description="Maximum tokens to generate")

class ContextChatRequest(BaseModel):
    """Context chat request model."""
    messages: List[ChatMessage] = Field(..., description="List of conversation messages")
    model: str = Field("deepseek-chat", description="Model to use for chat")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Sampling temperature")
    max_tokens: int = Field(1000, ge=1, le=4000, description="Maximum tokens to generate")

class ChatResponse(BaseModel):
    """Chat response model."""
    status: str
    ai_response: Optional[str] = None
    error: Optional[str] = None
    processing_time_seconds: Optional[float] = None
    timestamp: str
    model: Optional[str] = None
    usage: Optional[dict] = None

# Dependency to get chat service
def get_chat_service() -> ChatService:
    """Get chat service instance."""
    return ChatService()

@router.post("/simple", response_model=ChatResponse)
async def simple_chat(
    request: SimpleChatRequest,
    chat_service: ChatService = Depends(get_chat_service)
):
    """
    Send a simple message and get AI response.
    """
    try:
        result = await chat_service.send_message(
            message=request.message,
            system_prompt=request.system_prompt,
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        return ChatResponse(
            status=result["status"],
            ai_response=result.get("ai_response"),
            error=result.get("error"),
            processing_time_seconds=result.get("processing_time_seconds"),
            timestamp=result["timestamp"],
            model=result.get("model")
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat service error: {str(e)}")

@router.post("/context", response_model=ChatResponse)
async def context_chat(
    request: ContextChatRequest,
    chat_service: ChatService = Depends(get_chat_service)
):
    """
    Send multiple messages with context and get AI response.
    """
    try:
        # Convert Pydantic models to dictionaries
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        result = await chat_service.chat_with_context(
            messages=messages,
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        return ChatResponse(
            status=result["status"],
            ai_response=result.get("ai_response"),
            error=result.get("error"),
            processing_time_seconds=result.get("processing_time_seconds"),
            timestamp=result["timestamp"],
            model=result.get("model"),
            usage=result.get("usage")
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat service error: {str(e)}")

@router.get("/status")
async def chat_status(chat_service: ChatService = Depends(get_chat_service)):
    """
    Get chat service status and DeepSeek client health.
    """
    try:
        return chat_service.get_service_status()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Status check error: {str(e)}")

@router.get("/health")
async def chat_health():
    """
    Simple health check for chat endpoints.
    """
    return {
        "status": "healthy",
        "service": "Chat API",
        "timestamp": datetime.utcnow().isoformat(),
        "endpoints": ["/chat/simple", "/chat/context", "/chat/status", "/chat/health"]
    }
