"""
Main FastAPI application for TravelLangGraph API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config import settings

# Import controllers
from controllers.health_controller import router as health_router
from controllers.hello_controller import router as hello_router
from controllers.chat_controller import router as chat_router

# Create FastAPI app
app = FastAPI(
    title="TravelLangGraph API",
    description="A FastAPI backend for TravelLangGraph application",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router)
app.include_router(hello_router)
app.include_router(chat_router)

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to TravelLangGraph API!", "version": "0.1.0"}

def main():
    """Main function to run the API server."""
    uvicorn.run(
        "travelanggraph_api.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level="info"
    )

if __name__ == "__main__":
    main()
