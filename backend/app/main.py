from fastapi import FastAPI
from backend.app.api_router import api_router

def get_application() -> FastAPI:
    app = FastAPI(
        title="Code Morningstar API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    app.include_router(api_router)
    return app

app = get_application()
