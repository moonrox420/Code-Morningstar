import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.services.llm_service import LLMService
import tempfile
from pathlib import Path

@pytest.fixture
def mock_model_file():
    with tempfile.NamedTemporaryFile(suffix=".gguf", delete=False) as f:
        f.write(b"mock model data")
        yield f.name
    Path(f.name).unlink()

def test_llm_service_initialization(mock_model_file):
    service = LLMService(mock_model_file)
    assert service.model_path == Path(mock_model_file)

def test_llm_service_generate(mock_model_file):
    service = LLMService(mock_model_file)
    result = service.generate("test prompt")
    assert "test prompt" in result
    assert isinstance(result, str)