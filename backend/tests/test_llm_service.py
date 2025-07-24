import pytest
import sys
import os
from pathlib import Path

# Add the project root to Python path  
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.services.llm_service import LLMService
import tempfile

@pytest.fixture
def mock_model_file():
    """Create a temporary mock GGUF file for testing."""
    with tempfile.NamedTemporaryFile(suffix=".gguf", delete=False) as f:
        f.write(b"mock model data")
        yield f.name
    Path(f.name).unlink()

@pytest.fixture
def nonexistent_model():
    """Return path to a non-existent model file."""
    return "/nonexistent/path/model.gguf"

def test_llm_service_initialization(mock_model_file):
    """Test LLM service initializes correctly with valid model path."""
    service = LLMService(mock_model_file)
    assert service.model_path == Path(mock_model_file)

def test_llm_service_initialization_nonexistent_model(nonexistent_model):
    """Test LLM service handles non-existent model gracefully."""
    service = LLMService(nonexistent_model)
    assert service.model_path == Path(nonexistent_model)
    assert not service.is_model_loaded()

def test_llm_service_generate_with_mock(nonexistent_model):
    """Test generation works in mock mode when no model is available."""
    service = LLMService(nonexistent_model)
    result = service.generate("test prompt")
    assert "[MOCK]" in result
    assert "test prompt" in result
    assert isinstance(result, str)

def test_llm_service_generate_empty_prompt(nonexistent_model):
    """Test that empty prompt raises ValueError."""
    service = LLMService(nonexistent_model)
    with pytest.raises(ValueError, match="Prompt cannot be empty"):
        service.generate("")

def test_llm_service_generate_with_parameters(nonexistent_model):
    """Test generation with custom parameters."""
    service = LLMService(nonexistent_model)
    result = service.generate("test prompt", max_tokens=100, temperature=0.5)
    assert isinstance(result, str)
    assert len(result) > 0

def test_llm_service_model_loaded_status(nonexistent_model):
    """Test model loaded status check."""
    service = LLMService(nonexistent_model)
    assert isinstance(service.is_model_loaded(), bool)
    assert not service.is_model_loaded()  # Should be False for nonexistent model