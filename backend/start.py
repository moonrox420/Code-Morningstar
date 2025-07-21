"""
Code Morningstar - Startup Script
Handles application initialization and model setup
"""
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent  # Go up to Code-Morningstar root
sys.path.insert(0, str(project_root))

def setup_environment():
    """Set up environment variables and paths."""
    backend_root = Path(__file__).parent
    env_file = backend_root / ".env"
    if not env_file.exists():
        print("Warning: .env file not found. Creating from .env.example...")
        example_file = backend_root / ".env.example"
        if example_file.exists():
            import shutil
            shutil.copy(example_file, env_file)
            print("Created .env file from .env.example")
        else:
            print("Error: .env.example not found!")
            return False
    return True

def check_model():
    """Check if GGUF model exists."""
    from backend.settings import settings
    model_path = settings.LLM_MODEL_PATH
    
    if not model_path.exists():
        print(f"Warning: GGUF model not found at {model_path}")
        print("The application will run in mock mode.")
        print("\nTo download a model:")
        print("1. Visit https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF")
        print("2. Download a .gguf file (e.g., codellama-7b-instruct.Q4_K_M.gguf)")
        print(f"3. Place it at: {model_path}")
        return False
    else:
        print(f"✓ Model found: {model_path}")
        return True

def main():
    """Main startup function."""
    print("🌟 Starting Code Morningstar...")
    
    # Setup environment
    if not setup_environment():
        sys.exit(1)
    
    # Check model
    model_available = check_model()
    
    # Import and start the app
    try:
        from backend.app.main import app
        import uvicorn
        
        print("\n🚀 Starting FastAPI server...")
        print("📖 API Documentation: http://localhost:8000/docs")
        print("🔄 ReDoc: http://localhost:8000/redoc")
        if model_available:
            print("🤖 LLM Model: Loaded")
        else:
            print("🤖 LLM Model: Mock mode (no model file)")
        print("\n" + "="*50)
        
        uvicorn.run(
            "backend.app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
