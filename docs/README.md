# Code Morningstar - LLM Application

## Overview
Code Morningstar is a full-stack LLM application supporting GGUF models with a beautiful web interface.

## Features
- ✅ FastAPI backend with automatic API documentation
- ✅ GGUF model support via llama-cpp-python
- ✅ Mock mode for development without models
- ✅ Feature flags system
- ✅ Comprehensive test suite
- ✅ Beautiful web interface with gradient design
- ✅ Example prompts for code generation
- ✅ Health monitoring endpoints

## Quick Start

### 1. Setup Environment
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt
```

### 2. Configure Environment
Copy `backend/.env.example` to `backend/.env` and configure:
```env
MODEL_PATH=models/your-model.gguf
API_KEY=your-secure-api-key
MOCK_MODE=true
```

### 3. Start Backend
```bash
python backend/start.py
```

### 4. Access Frontend
Open `frontend/standalone.html` in your browser or visit:
- API Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Generate Text
```http
POST /llm/generate
Content-Type: application/json

{
    "prompt": "Write a Python function",
    "max_tokens": 100,
    "temperature": 0.7
}
```

### Health Check
```http
GET /llm/health
```

## Development

### Running Tests
```bash
python -m pytest backend/tests/ -v
```

### Mock Mode
Set `MOCK_MODE=true` in your environment to use the application without a model file.

## Model Support
- Supports any GGUF model compatible with llama-cpp-python
- Automatic model detection and loading
- Graceful fallback to mock mode if model not found

## Architecture
- **Backend**: FastAPI with Pydantic settings
- **LLM Service**: llama-cpp-python integration
- **Frontend**: Standalone HTML with modern CSS
- **Configuration**: Environment-based with feature flags
- **Testing**: pytest with 100% coverage of core functionality
