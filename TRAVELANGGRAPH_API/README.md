# TravelLangGraph API

A FastAPI backend for the TravelLangGraph application.

## Installation

### Using Conda

```bash
conda create -n travelanggraph python=3.11
conda activate travelanggraph
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
```

## Running the API

```bash
# Using the entry point
travelanggraph-api

# Or directly with uvicorn
uvicorn travelanggraph_api.main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

```bash
# Run tests
pytest

# Format code
black .

# Lint code
flake8

# Type checking
mypy .
```
