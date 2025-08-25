"""
DeepSeek API client for TravelLangGraph API.
"""

import os
import httpx
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class DeepSeekClient:
    """Client for interacting with DeepSeek API."""
    
    def __init__(self):
        """Initialize DeepSeek client with API key from environment."""
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.base_url = os.getenv("DEEPSEEK_API_BASE_URL", "https://api.deepseek.com/v1")
        
        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY environment variable is required")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        logger.info("DeepSeek client initialized successfully")
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "deepseek-chat",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        stream: bool = False
    ) -> Dict[str, Any]:
        """
        Send chat completion request to DeepSeek API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use for completion
            temperature: Sampling temperature (0.0 to 2.0)
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response
            
        Returns:
            API response dictionary
        """
        try:
            payload = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stream": stream
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json=payload,
                    timeout=30.0
                )
                
                response.raise_for_status()
                return response.json()
                
        except httpx.HTTPStatusError as e:
            logger.error(f"DeepSeek API HTTP error: {e.response.status_code} - {e.response.text}")
            raise
        except httpx.RequestError as e:
            logger.error(f"DeepSeek API request error: {e}")
            raise
        except Exception as e:
            logger.error(f"DeepSeek API unexpected error: {e}")
            raise
    
    async def simple_chat(self, message: str, system_prompt: Optional[str] = None) -> str:
        """
        Simple chat method for basic conversations.
        
        Args:
            message: User message
            system_prompt: Optional system prompt
            
        Returns:
            AI response text
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": message})
        
        try:
            response = await self.chat_completion(messages)
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            logger.error(f"Error in simple chat: {e}")
            raise
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check if DeepSeek client is properly configured.
        
        Returns:
            Health status dictionary
        """
        return {
            "status": "healthy" if self.api_key else "unhealthy",
            "api_key_configured": bool(self.api_key),
            "base_url": self.base_url,
            "timestamp": datetime.utcnow().isoformat()
        }
