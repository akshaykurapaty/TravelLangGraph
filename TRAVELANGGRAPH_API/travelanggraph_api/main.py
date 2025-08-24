"""
Main FastAPI application for TravelLangGraph API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to TravelLangGraph API!"}

@app.get("/hello")
async def hello_world():
    """Hello World endpoint."""
    return {"message": "Hello, World!"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "TravelLangGraph API"}

def main():
    """Main function to run the API server."""
    uvicorn.run(
        "travelanggraph_api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
