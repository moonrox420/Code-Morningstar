# Code Morningstar

Enterprise-grade, multi-DB, privacy-first Python/FastAPI + Svelte stack with local LLM integration.

## Setup

Run the setup script to populate all project files:

```powershell
# PowerShell (Windows, macOS, Linux)
./setup.ps1
```

This will create the complete project structure with all necessary files.

## Features

- Strictly validated, immutable config (`backend/settings.py`)
- Multi-database support: Postgres, MySQL, MongoDB, Redis, SQLite, Cassandra, Neo4j, Elasticsearch
- Local GGUF LLM inference (via [llama-cpp-python](https://github.com/abetlen/llama-cpp-python))
- Feature flag management
- Production-ready CI/CD (GitHub Actions), K8s, Terraform
- Secure, dependency-injected, and testable architecture

## Quickstart

```sh
# 1. Run setup script first
./setup.ps1

# 2. Backend
cd backend
pip install -r requirements.txt
cp ../.env.example .env
# Edit .env with your configuration
uvicorn app.main:app --reload

# 3. Frontend
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

## Project Structure

The setup script creates:

- **backend/**: FastAPI application with multi-DB support
- **frontend/**: Svelte TypeScript UI
- **infra/**: Kubernetes and Terraform configurations
- **.github/workflows/**: CI/CD pipelines
- **ADRs/**: Architecture Decision Records