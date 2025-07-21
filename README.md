# 🌟 Code Morningstar

A beautiful, full-stack LLM application with GGUF model support and modern web interface.

## ✨ Features

- 🚀 **FastAPI Backend** - High-performance API with automatic documentation
- 🧠 **GGUF Model Support** - Compatible with llama-cpp-python models
- 🎭 **Mock Mode** - Development-friendly mode without requiring models
- 🎨 **Beautiful UI** - Modern gradient design with responsive layout
- 🔧 **Easy Setup** - One-command deployment with cross-platform scripts
- 📊 **Health Monitoring** - Built-in health checks and status endpoints
- 🧪 **Comprehensive Tests** - 100% coverage of core functionality
- 📚 **Rich Documentation** - API docs, development guides, and examples

## 🚀 Quick Start

### Windows
```cmd
deploy.bat
```

### Unix/Linux/macOS
```bash
chmod +x deploy.sh
./deploy.sh
```

### Manual Setup
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Unix

# Install dependencies
pip install -r backend/requirements.txt

# Configure environment
cp backend/.env.example backend/.env

# Start application
python backend/start.py
```

## 🌐 Access Points

- **Frontend**: Open `frontend/standalone.html` in your browser
- **API Documentation**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/llm/health

## 📖 Documentation

- [Development Guide](docs/DEVELOPMENT.md) - Detailed development information
- [API Reference](docs/API.md) - Complete API documentation
- [Changelog](CHANGELOG.md) - Version history and updates

## 🔧 Configuration

Edit `backend/.env` to configure:
```env
MODEL_PATH=models/your-model.gguf
API_KEY=your-secure-api-key
MOCK_MODE=true
PORT=8000
HOST=0.0.0.0
```

## 🧪 Testing

```bash
python -m pytest backend/tests/ -v
```

## 📝 Example Usage

### API Call
```bash
curl -X POST "http://localhost:8000/llm/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a Python hello world function", "max_tokens": 100}'
```

### Python Client
```python
import requests

response = requests.post(
    "http://localhost:8000/llm/generate",
    json={"prompt": "Write a Python function", "max_tokens": 100}
)
print(response.json()["response"])
```

## 🏗️ Architecture

- **Backend**: FastAPI + uvicorn + llama-cpp-python
- **Frontend**: Standalone HTML with modern CSS/JavaScript
- **Configuration**: Pydantic Settings + YAML feature flags
- **Testing**: pytest with comprehensive coverage
- **Documentation**: OpenAPI 3.0 + ReDoc + Swagger UI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python -m pytest backend/tests/ -v`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Support

If you find this project helpful, please give it a star on GitHub!
