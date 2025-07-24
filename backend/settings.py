from typing import List, Optional, Union
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr, field_validator
from pathlib import Path

class Settings(BaseSettings):
    APP_ENV: str = Field(default="development", description="Application environment (development|staging|production)")
    SECRET_KEY: SecretStr = Field(default=SecretStr("local-fastapi-dev-key"), description="Cryptographic secret")
    ALLOWED_HOSTS: Union[str, List[str]] = Field(default="localhost", description="Allowed hosts (comma-separated)")
    FEATURE_FLAGS_PATH: Path = Field(default=Path(__file__).parent / "feature_flags" / "flags.yaml", description="Path to feature flags YAML")

    # Database configurations
    DATABASE_URL: str = Field(default="sqlite:///./code_morningstar.db", description="Database URL")
    
    # API Configuration
    API_HOST: str = Field(default="0.0.0.0", description="API host")
    API_PORT: int = Field(default=8000, description="API port")

    # LLM Configuration
    LLM_MODEL_PATH: Path = Field(default=Path(__file__).parent.parent / "models" / "codellama-7b-instruct.Q4_K_M.gguf", description="Path to GGUF model file")

    @field_validator('ALLOWED_HOSTS', mode='before')
    @classmethod
    def parse_hosts(cls, v):
        if isinstance(v, str):
            return [host.strip() for host in v.split(',') if host.strip()]
        return v if isinstance(v, list) else [v]
    
    @property 
    def allowed_hosts_list(self) -> List[str]:
        if isinstance(self.ALLOWED_HOSTS, str):
            return [host.strip() for host in self.ALLOWED_HOSTS.split(',') if host.strip()]
        return self.ALLOWED_HOSTS

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()