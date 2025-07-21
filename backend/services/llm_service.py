from pathlib import Path
from typing import Optional, Union, Any
import os

try:
    from llama_cpp import Llama
    LLAMA_CPP_AVAILABLE = True
except ImportError:
    LLAMA_CPP_AVAILABLE = False
    Llama = None

class LLMService:
    """
    Local GGUF LLM inference service for Code Morningstar.
    """
    def __init__(self, model_path: str, n_ctx: int = 2048, n_threads: int = -1):
        self.model_path = Path(model_path)
        self.n_ctx = n_ctx
        self.n_threads = n_threads if n_threads > 0 else os.cpu_count()
        self._llm: Optional[Any] = self._load_model()

    def _load_model(self) -> Optional[Any]:
        if not LLAMA_CPP_AVAILABLE or Llama is None:
            print("Warning: llama-cpp-python not available. Using mock responses.")
            return None
            
        if not self.model_path.exists():
            print(f"Warning: Model file not found: {self.model_path}. Using mock responses.")
            return None
            
        try:
            return Llama(
                model_path=str(self.model_path),
                n_ctx=self.n_ctx,
                n_threads=self.n_threads,
                verbose=False
            )
        except Exception as e:
            print(f"Error loading model: {e}. Using mock responses.")
            return None

    def generate(self, prompt: str, max_tokens: int = 256, temperature: float = 0.7) -> str:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")
            
        # If no model loaded, return mock response
        if self._llm is None:
            return f"[MOCK] Generated response for: {prompt[:50]}..."
            
        try:
            response = self._llm(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                stop=["Human:", "Assistant:", "\n\n"],
                echo=False
            )
            return response['choices'][0]['text'].strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return f"[ERROR] Could not generate response: {str(e)}"

    def is_model_loaded(self) -> bool:
        """Check if a model is successfully loaded."""
        return self._llm is not None