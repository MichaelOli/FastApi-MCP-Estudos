# FastAPI + MCP Coding Test

Minimal FastAPI training project: CRUD items in memory, plus room for async demos and a small MCP interface later.

## Stack

- **Python + uv** — fast local setup and dependency management
- **FastAPI** — REST API with validation and OpenAPI (`/docs`)
- **Pydantic** — request/response schemas (`ItemCreate` / `Item`)
- **Uvicorn** — ASGI server for local run
- **MCP SDK** — official Python SDK for the Model Context Protocol
- **Ruff** — linting and formatting

## How to run

```bash
git clone https://github.com/MichaelOli/FastApi-MCP-Estudos.git
cd FastApi-MCP-Estudos
uv sync #Install dependencies
uv run uvicorn app.main:app --reload

```

Open http://localhost:8000/docs or http://localhost:8000/health

## Project structure
- `app/routers/` - HTTP routes (status code, `HTTPException`)
- `app/services/` - business logic and in-memory store (no FastAPI)
- `app/schemas.py` - Pydantic models for input/output
- `app/mcp_server/` - MCP layer (next)

## Design decisions

- **`ItemCreate` vs `Item`** - clients don't send `id`; the server assigns it. Keeps POST body clean and OpenAPI accurate.
- **Service without `HTTPException`** - domain returns `None` / `False` ; the router maps that to 404. Same service can be reused by MCP or tests.
- **In-memory dict** - enough for a coding exercise; no DB noise while learning layers and async.

## Roadmap

- [x] Project setup (`uv`, folders)
- [x] Health check + empty items router
- [x] Async vs Sync sleep experiment
- [x] In-memory items service
- [x] CRUD router(201,200,204,404,422)
- [ ] Middleware
- [ ] Minimal MCP interface
- [ ] Tests