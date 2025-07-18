from typing import List, Optional
from pydantic import BaseSettings, Field, SecretStr, AnyUrl, PostgresDsn, MySQLDsn
from pathlib import Path

class Settings(BaseSettings):
    APP_ENV: str = Field(..., description="Application environment (development|staging|production)")
    SECRET_KEY: SecretStr = Field(..., description="Cryptographic secret")
    ALLOWED_HOSTS: List[str] = Field(default_factory=lambda: ["localhost"])
    FEATURE_FLAGS_PATH: Path = Field(..., description="Absolute path to feature flags YAML")

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str
    POSTGRES_DSN: Optional[PostgresDsn] = None

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: SecretStr
    MYSQL_DB: str
    MYSQL_DSN: Optional[MySQLDsn] = None

    MONGODB_URI: AnyUrl
    REDIS_HOST: str
    REDIS_PORT: int
    SQLITE_PATH: Path
    CASSANDRA_HOST: str
    CASSANDRA_PORT: int
    NEO4J_URI: AnyUrl
    NEO4J_USER: str
    NEO4J_PASSWORD: SecretStr
    ELASTICSEARCH_HOST: str
    ELASTICSEARCH_PORT: int

    LLM_MODEL_PATH: Path = Field(..., description="Absolute path to GGUF model file")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        frozen = True

settings = Settings()
