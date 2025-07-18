from fastapi import APIRouter
from backend.app.llm_api import router as llm_router

api_router = APIRouter()
api_router.include_router(llm_router, prefix="/llm", tags=["llm"])