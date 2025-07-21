# Code Morningstar Development Guide

## Project Structure
```
Code-Morningstar/
├── backend/                 # FastAPI backend
│   ├── app/                # FastAPI application
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI app instance
│   │   ├── api_router.py   # API route definitions
│   │   └── llm_api.py      # LLM-specific endpoints
│   ├── services/           # Business logic
│   │   ├── __init__.py
│   │   └── llm_service.py  # LLM integration service
│   ├── tests/              # Test suite
│   │   └── test_llm_service.py
│   ├── feature_flags/      # Feature toggles
│   │   └── flags.yaml
│   ├── models/             # Data models (Pydantic)
│   ├── logs/               # Application logs
│   ├── requirements.txt    # Python dependencies
│   ├── settings.py         # Configuration management
│   ├── start.py           # Application entry point
│   └── .env.example       # Environment template
├── frontend/               # Web interface
│   ├── standalone.html     # Main frontend (no build required)
│   ├── src/               # Svelte source (optional)
│   │   ├── App.svelte
│   │   ├── main.ts
│   │   └── lib/
│   │       ├── Message.svelte
│   │       └── prompts.ts
│   └── package.json       # Frontend dependencies
├── docs/                  # Documentation
├── models/                # ML model storage
├── logs/                  # Application logs
├── deploy.py              # Cross-platform deployment
├── deploy.bat             # Windows deployment
├── deploy.sh              # Unix deployment
└── package.json           # Workspace configuration
```

## Backend Architecture

### Settings Management
The application uses Pydantic Settings for configuration:

```python
from pydantic_settings import BaseSettings
from pydantic import SecretStr
from pathlib import Path

class Settings(BaseSettings):
    model_path: Path = Path("models/default.gguf")
    api_key: SecretStr = SecretStr("default-key")
    mock_mode: bool = True
    
    class Config:
        env_file = ".env"
```

### LLM Service
Core service for model interaction:

```python
from llama_cpp import Llama

class LLMService:
    def __init__(self, model_path: Path, mock_mode: bool = False):
        self.mock_mode = mock_mode
        if not mock_mode and model_path.exists():
            self.llm = Llama(model_path=str(model_path))
        else:
            self.llm = None
            
    def generate(self, prompt: str, **kwargs) -> str:
        if self.mock_mode or self.llm is None:
            return f"[MOCK] Generated response for: {prompt[:50]}..."
        return self.llm(prompt, **kwargs)
```

### API Endpoints
RESTful API with automatic documentation:

```python
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.7

@router.post("/generate")
async def generate_text(request: GenerateRequest):
    response = llm_service.generate(
        prompt=request.prompt,
        max_tokens=request.max_tokens,
        temperature=request.temperature
    )
    return {"response": response}
```

## Frontend Architecture

### Standalone HTML
The main frontend is a single HTML file with embedded CSS and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Code Morningstar</title>
    <style>
        /* Modern gradient design */
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- UI elements -->
    </div>
    
    <script>
        // API integration
        async function generateText(prompt) {
            const response = await fetch('http://localhost:8000/llm/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt })
            });
            return response.json();
        }
    </script>
</body>
</html>
```

## Development Workflow

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Unix

# Install dependencies
pip install -r backend/requirements.txt
```

### 2. Configuration
```bash
# Copy environment template
cp backend/.env.example backend/.env

# Edit configuration
# Set MODEL_PATH, API_KEY, MOCK_MODE, etc.
```

### 3. Development Server
```bash
# Start backend
python backend/start.py

# Access frontend
# Open frontend/standalone.html in browser
```

### 4. Testing
```bash
# Run all tests
python -m pytest backend/tests/ -v

# Run specific test
python -m pytest backend/tests/test_llm_service.py::test_llm_service_generate_with_mock -v
```

## Feature Flags

Configure features via `backend/feature_flags/flags.yaml`:

```yaml
llm:
  enabled: true
  mock_mode: true
  
api:
  rate_limiting: false
  cors_enabled: true
  
frontend:
  debug_mode: false
  example_prompts: true
```

## API Documentation

### Automatic Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Manual Testing
```bash
# Health check
curl http://localhost:8000/llm/health

# Generate text
curl -X POST http://localhost:8000/llm/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a Python function", "max_tokens": 100}'
```

## Deployment Options

### Local Development
```bash
python deploy.py
```

### Docker (Future Enhancement)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
EXPOSE 8000
CMD ["python", "start.py"]
```

### Production Considerations
- Use proper secret management for API keys
- Configure reverse proxy (nginx/Apache)
- Set up SSL/TLS certificates
- Monitor logs and performance
- Scale with multiple workers

## Troubleshooting

### Common Issues

1. **Model Not Found**
   - Check MODEL_PATH in .env
   - Ensure model file exists
   - Use MOCK_MODE=true for development

2. **Port Already in Use**
   - Change PORT in settings.py
   - Kill existing processes: `netstat -ano | findstr :8000`

3. **Frontend CORS Issues**
   - Ensure CORS is enabled in FastAPI
   - Use same origin for API calls
   - Check browser developer console

4. **Import Errors**
   - Verify virtual environment is activated
   - Install missing dependencies
   - Check Python path configuration
