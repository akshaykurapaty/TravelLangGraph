"""
Hello service for TravelLangGraph API.
Contains business logic for hello-related operations.
"""

from datetime import datetime
from typing import Optional

class HelloService:
    """Service class for hello-related operations."""
    
    @staticmethod
    def get_hello_message(name: Optional[str] = None) -> str:
        """Get a hello message with optional name."""
        if name:
            return f"Hello, {name}!"
        return "Hello, World!"
    
    @staticmethod
    def get_timestamp() -> datetime:
        """Get current UTC timestamp."""
        return datetime.utcnow()
    
    @staticmethod
    def format_greeting(name: str, language: str = "en") -> str:
        """Format greeting in different languages."""
        greetings = {
            "en": f"Hello, {name}!",
            "es": f"¡Hola, {name}!",
            "fr": f"Bonjour, {name}!",
            "de": f"Hallo, {name}!",
            "it": f"Ciao, {name}!"
        }
        return greetings.get(language, greetings["en"])
