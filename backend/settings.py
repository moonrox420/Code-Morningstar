from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr, AnyUrl
from pathlib import Path

class Settings(BaseSettings):
    APP_ENV: str = Field(default="development", description="Application environment (development|staging|production)")
    SECRET_KEY: SecretStr = Field(default="changeme-supersecret", description="Cryptographic secret")
    ALLOWED_HOSTS: List[str] = Field(default_factory=lambda: ["localhost"])
    FEATURE_FLAGS_PATH: Path = Field(default="/tmp/flags.yaml", description="Absolute path to feature flags YAML")

    POSTGRES_HOST: str = Field(default="localhost")
    POSTGRES_PORT: int = Field(default=5432)
    POSTGRES_USER: str = Field(default="postgres")
    POSTGRES_PASSWORD: SecretStr = Field(default="postgres")
    POSTGRES_DB: str = Field(default="code_morningstar")

    MYSQL_HOST: str = Field(default="localhost")
    MYSQL_PORT: int = Field(default=3306)
    MYSQL_USER: str = Field(default="root")
    MYSQL_PASSWORD: SecretStr = Field(default="root")
    MYSQL_DB: str = Field(default="code_morningstar")

    MONGODB_URI: AnyUrl = Field(default="mongodb://localhost:27017")
    REDIS_HOST: str = Field(default="localhost")
    REDIS_PORT: int = Field(default=6379)
    SQLITE_PATH: Path = Field(default="/tmp/code_morningstar.sqlite3")
    CASSANDRA_HOST: str = Field(default="localhost")
    CASSANDRA_PORT: int = Field(default=9042)
    NEO4J_URI: AnyUrl = Field(default="bolt://localhost:7687")
    NEO4J_USER: str = Field(default="neo4j")
    NEO4J_PASSWORD: SecretStr = Field(default="neo4j")
    ELASTICSEARCH_HOST: str = Field(default="localhost")
    ELASTICSEARCH_PORT: int = Field(default=9200)

    LLM_MODEL_PATH: Path = Field(default="/tmp/model.gguf", description="Absolute path to GGUF model file")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()