"""
Configuration module for TravelLangGraph API.
Loads environment variables and provides configuration settings.
"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings loaded from environment variables."""
    
    # DeepSeek API Configuration
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_API_BASE_URL: str = os.getenv("DEEPSEEK_API_BASE_URL", "https://api.deepseek.com/v1")
    
    # API Configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Validation
    def validate(self) -> bool:
        """Validate that required environment variables are set."""
        if not self.DEEPSEEK_API_KEY:
            print("WARNING: DEEPSEEK_API_KEY is not set. Chat functionality will not work.")
            return False
        return True

# Create global settings instance
settings = Settings()

# Validate settings on import
settings.validate()
