# ADR 0001: Enterprise Architecture for Code Morningstar

## Context

- Must support multiple databases for migration and data sovereignty.
- LLMs must run locally for privacy and security.
- Strict config, feature flags, and ironclad error handling are non-negotiable.

## Decision

- Backend: Python, FastAPI, Pydantic, SQLAlchemy, dependency injection.
- Frontend: Svelte with strict TypeScript.
- Infrastructure: Docker, K8s manifests, Terraform for provisioning, GitHub Actions CI.

## Consequences

- Upfront complexity for maintainability and security.
- All code validated, strictly typed, and covered by tests/CI.
