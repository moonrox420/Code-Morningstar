from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional
from backend.services.llm_service import LLMService
from backend.settings import settings

router = APIRouter()

class LLMRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4096, description="The text prompt to generate from")
    max_tokens: Optional[int] = Field(default=256, ge=1, le=2048, description="Maximum number of tokens to generate")
    temperature: Optional[float] = Field(default=0.7, ge=0.0, le=2.0, description="Sampling temperature")

class LLMResponse(BaseModel):
    response: str
    model_loaded: bool
    tokens_generated: Optional[int] = None

def get_llm_service() -> LLMService:
    return LLMService(str(settings.LLM_MODEL_PATH))

@router.post("/generate", response_model=LLMResponse)
async def generate_text(request: LLMRequest, llm: LLMService = Depends(get_llm_service)):
    """Generate text using the local GGUF LLM model."""
    try:
        result = llm.generate(
            prompt=request.prompt,
            max_tokens=request.max_tokens or 256,
            temperature=request.temperature or 0.7
        )
        return LLMResponse(
            response=result,
            model_loaded=llm.is_model_loaded(),
            tokens_generated=len(result.split()) if result else 0
        )
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"LLM generation failed: {str(ex)}")

@router.get("/health")
async def health_check(llm: LLMService = Depends(get_llm_service)):
    """Check if the LLM service is healthy and model is loaded."""
    return {
        "status": "healthy" if llm.is_model_loaded() else "model_not_loaded",
        "model_path": str(settings.LLM_MODEL_PATH),
        "model_loaded": llm.is_model_loaded()
    }