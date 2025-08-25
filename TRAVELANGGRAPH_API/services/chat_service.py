"""
Chat service for TravelLangGraph API.
Contains business logic for chat operations using DeepSeek.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import logging
from clients.deepseek_client import DeepSeekClient

logger = logging.getLogger(__name__)

class ChatService:
    """Service class for chat-related operations."""
    
    def __init__(self):
        """Initialize chat service with DeepSeek client."""
        try:
            self.deepseek_client = DeepSeekClient()
            logger.info("Chat service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize chat service: {e}")
            raise
    
    async def send_message(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        model: str = "deepseek-chat",
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict[str, Any]:
        """
        Send a message and get AI response.
        
        Args:
            message: User message
            system_prompt: Optional system prompt
            model: Model to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            
        Returns:
            Response dictionary with AI reply and metadata
        """
        try:
            start_time = datetime.utcnow()
            
            # Get AI response
            ai_response = await self.deepseek_client.simple_chat(
                message=message,
                system_prompt=system_prompt
            )
            
            end_time = datetime.utcnow()
            processing_time = (end_time - start_time).total_seconds()
            
            return {
                "user_message": message,
                "ai_response": ai_response,
                "system_prompt": system_prompt,
                "model": model,
                "processing_time_seconds": processing_time,
                "timestamp": end_time.isoformat(),
                "status": "success"
            }
            
        except Exception as e:
            logger.error(f"Error in send_message: {e}")
            return {
                "user_message": message,
                "ai_response": None,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
                "status": "error"
            }
    
    async def chat_with_context(
        self,
        messages: List[Dict[str, str]],
        model: str = "deepseek-chat",
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict[str, Any]:
        """
        Send multiple messages with context and get AI response.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            
        Returns:
            Response dictionary with AI reply and metadata
        """
        try:
            start_time = datetime.utcnow()
            
            # Get AI response with context
            response = await self.deepseek_client.chat_completion(
                messages=messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            end_time = datetime.utcnow()
            processing_time = (end_time - start_time).total_seconds()
            
            ai_message = response["choices"][0]["message"]["content"]
            
            return {
                "conversation_history": messages,
                "ai_response": ai_message,
                "model": model,
                "processing_time_seconds": processing_time,
                "timestamp": end_time.isoformat(),
                "status": "success",
                "usage": response.get("usage", {})
            }
            
        except Exception as e:
            logger.error(f"Error in chat_with_context: {e}")
            return {
                "conversation_history": messages,
                "ai_response": None,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
                "status": "error"
            }
    
    def get_service_status(self) -> Dict[str, Any]:
        """
        Get chat service status and DeepSeek client health.
        
        Returns:
            Service status dictionary
        """
        try:
            deepseek_health = self.deepseek_client.health_check()
            
            return {
                "service": "ChatService",
                "status": "healthy",
                "deepseek_client": deepseek_health,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "service": "ChatService",
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
