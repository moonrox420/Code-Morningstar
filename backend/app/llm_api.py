from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, constr
from backend.services.llm_service import LLMService
from backend.settings import settings

router = APIRouter()

class LLMRequest(BaseModel):
    prompt: constr(min_length=1, max_length=4096)

def get_llm_service() -> LLMService:
    return LLMService(str(settings.LLM_MODEL_PATH))

@router.post("/generate")
def generate_text(request: LLMRequest, llm: LLMService = Depends(get_llm_service)):
    try:
        result = llm.generate(request.prompt)
        return {"result": result}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
