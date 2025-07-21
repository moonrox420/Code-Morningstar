# API Reference - Code Morningstar

## Base URL
```
http://localhost:8000
```

## Authentication
Include API key in request headers:
```http
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### 1. Generate Text

Generate text using the loaded LLM model.

**Endpoint:** `POST /llm/generate`

**Request Body:**
```json
{
    "prompt": "string",           // Required: Text prompt for generation
    "max_tokens": 100,           // Optional: Maximum tokens to generate (default: 100)
    "temperature": 0.7,          // Optional: Sampling temperature (default: 0.7)
    "top_p": 0.9,               // Optional: Top-p sampling (default: 0.9)
    "frequency_penalty": 0.0,    // Optional: Frequency penalty (default: 0.0)
    "presence_penalty": 0.0,     // Optional: Presence penalty (default: 0.0)
    "stop": ["\\n"],            // Optional: Stop sequences (default: ["\\n"])
    "stream": false             // Optional: Stream response (default: false)
}
```

**Response:**
```json
{
    "response": "Generated text response...",
    "model_used": "mock" | "llama",
    "tokens_generated": 42,
    "processing_time": 0.123
}
```

**Example Request:**
```bash
curl -X POST "http://localhost:8000/llm/generate" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "prompt": "Write a Python function to calculate fibonacci numbers",
    "max_tokens": 150,
    "temperature": 0.7
  }'
```

**Example Response:**
```json
{
    "response": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
    "model_used": "mock",
    "tokens_generated": 25,
    "processing_time": 0.05
}
```

### 2. Health Check

Check the health and status of the LLM service.

**Endpoint:** `GET /llm/health`

**Response:**
```json
{
    "status": "healthy" | "degraded" | "unhealthy",
    "model_loaded": true | false,
    "model_path": "/path/to/model.gguf",
    "mock_mode": true | false,
    "uptime": 123.45,
    "version": "1.0.0",
    "timestamp": "2025-07-21T10:30:00Z"
}
```

**Example Request:**
```bash
curl "http://localhost:8000/llm/health"
```

**Example Response:**
```json
{
    "status": "healthy",
    "model_loaded": false,
    "model_path": "models/default.gguf",
    "mock_mode": true,
    "uptime": 300.12,
    "version": "1.0.0",
    "timestamp": "2025-07-21T10:30:00Z"
}
```

### 3. Model Information

Get information about the currently loaded model.

**Endpoint:** `GET /llm/model`

**Response:**
```json
{
    "model_path": "/path/to/model.gguf",
    "model_size": 1234567890,
    "model_type": "llama",
    "context_length": 2048,
    "vocab_size": 32000,
    "loaded": true | false,
    "load_time": 12.34
}
```

### 4. System Information

Get system information and configuration.

**Endpoint:** `GET /system/info`

**Response:**
```json
{
    "version": "1.0.0",
    "python_version": "3.11.9",
    "platform": "Windows-10",
    "memory_usage": {
        "rss": 123456789,
        "vms": 987654321
    },
    "cpu_usage": 15.2,
    "disk_usage": {
        "total": 1000000000000,
        "used": 500000000000,
        "free": 500000000000
    }
}
```

## Error Responses

All endpoints return consistent error responses:

```json
{
    "error": {
        "code": "ERROR_CODE",
        "message": "Human readable error message",
        "details": "Additional error details",
        "timestamp": "2025-07-21T10:30:00Z"
    }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_REQUEST` | 400 | Invalid request format or parameters |
| `UNAUTHORIZED` | 401 | Invalid or missing API key |
| `MODEL_NOT_LOADED` | 503 | LLM model is not loaded |
| `GENERATION_FAILED` | 500 | Text generation failed |
| `RATE_LIMITED` | 429 | Rate limit exceeded |
| `INTERNAL_ERROR` | 500 | Internal server error |

## Rate Limiting

Default rate limits:
- 60 requests per minute per API key
- 1000 requests per hour per API key

Rate limit headers included in responses:
```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
X-RateLimit-Reset: 1642781400
```

## WebSocket Support (Future)

Real-time streaming endpoint:
```
ws://localhost:8000/llm/stream
```

## SDK Examples

### Python
```python
import requests

class CodeMorningstarClient:
    def __init__(self, base_url="http://localhost:8000", api_key=None):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
    
    def generate(self, prompt, **kwargs):
        response = requests.post(
            f"{self.base_url}/llm/generate",
            json={"prompt": prompt, **kwargs},
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def health(self):
        response = requests.get(f"{self.base_url}/llm/health")
        response.raise_for_status()
        return response.json()

# Usage
client = CodeMorningstarClient(api_key="your-api-key")
result = client.generate("Write a hello world function")
print(result["response"])
```

### JavaScript
```javascript
class CodeMorningstarClient {
    constructor(baseUrl = "http://localhost:8000", apiKey = null) {
        this.baseUrl = baseUrl;
        this.headers = {"Content-Type": "application/json"};
        if (apiKey) {
            this.headers["Authorization"] = `Bearer ${apiKey}`;
        }
    }
    
    async generate(prompt, options = {}) {
        const response = await fetch(`${this.baseUrl}/llm/generate`, {
            method: "POST",
            headers: this.headers,
            body: JSON.stringify({prompt, ...options})
        });
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        return response.json();
    }
    
    async health() {
        const response = await fetch(`${this.baseUrl}/llm/health`);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    }
}

// Usage
const client = new CodeMorningstarClient("http://localhost:8000", "your-api-key");
client.generate("Write a hello world function")
    .then(result => console.log(result.response))
    .catch(error => console.error(error));
```

## OpenAPI Specification

The complete OpenAPI 3.0 specification is available at:
- JSON: `http://localhost:8000/openapi.json`
- Interactive docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
