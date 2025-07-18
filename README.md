# Code Morningstar

Enterprise-grade, multi-DB, privacy-first Python/FastAPI + Svelte stack with local LLM integration.

## Features

- Strictly validated, immutable config (`backend/settings.py`)
- Multi-database support: Postgres, MySQL, MongoDB, Redis, SQLite, Cassandra, Neo4j, Elasticsearch
- Local GGUF LLM inference (via [llama-cpp-python](https://github.com/abetlen/llama-cpp-python))
- Feature flag management
- Production-ready CI/CD (GitHub Actions), K8s, Terraform
- Secure, dependency-injected, and testable architecture

## Quickstart

```sh
# Backend
cd backend
pip install -r requirements.txt
cp ../.env.example .env
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## LLM Model
Download your GGUF model (e.g., CodeLlama) and set `LLM_MODEL_PATH` in `.env`.

## Tests

```sh
cd backend
pytest
```