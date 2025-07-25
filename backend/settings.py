from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr
from pathlib import Path
import os

def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent

class Settings(BaseSettings):
    APP_ENV: str = Field(default="development", description="Application environment (development|staging|production)")
    SECRET_KEY: SecretStr = Field(default=SecretStr("local-fastapi-dev-key"), description="Cryptographic secret")
    ALLOWED_HOSTS: List[str] = Field(default_factory=lambda: ["localhost"])
    FEATURE_FLAGS_PATH: Path = Field(default=get_project_root() / "backend" / "feature_flags" / "flags.yaml", description="Path to feature flags YAML")

    # Database configurations
    DATABASE_URL: str = Field(default="sqlite:///./code_morningstar.db", description="Database URL")
    
    # API Configuration
    API_HOST: str = Field(default="0.0.0.0", description="API host")
    API_PORT: int = Field(default=8000, description="API port")

    # LLM Configuration
    LLM_MODEL_PATH: Path = Field(default=get_project_root() / "models" / "codellama-7b-instruct.Q4_K_M.gguf", description="Path to GGUF model file")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()