from pathlib import Path
from llama_cpp import Llama, LlamaError
from typing import Optional

class LLMService:
    """
    Local GGUF LLM inference service for Code Morningstar.
    """
    def __init__(self, model_path: str):
        self.model_path = Path(model_path)
        self._llm = self._load_model()

    def _load_model(self) -> Optional[Llama]:
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        try:
            return Llama(
                model_path=str(self.model_path),
                n_ctx=4096,
                n_threads=8,
            )
        except LlamaError as ex:
            raise RuntimeError(f"Failed to load Llama model: {ex}")

    def generate(self, prompt: str, max_tokens: int = 256, temperature: float = 0.7) -> str:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")
        try:
            completion = self._llm(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                stop=["</s>"],
            )
            return completion["choices"][0]["text"].strip()
        except Exception as ex:
            raise RuntimeError(f"LLM inference failed: {ex}")