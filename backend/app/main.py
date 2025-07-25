from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api_router import api_router

def get_application() -> FastAPI:
    app = FastAPI(
        title="Code Morningstar API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify exact origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(api_router)
    return app

app = get_application()