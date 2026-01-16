---
name: fastapi-code-structure
description: Enforce enterprise-grade project structure (Dispatch style), dependency injection patterns, and async concurrency rules for FastAPI.
version: 2.0.0
allowed-tools: "Read,Write"
---

# FastAPI Enterprise Standards

## 1. Directory Structure
Do not structure by file type (`routers/`, `models/`). Structure by **Domain Component**.
Refer to the standard layout: `Read({baseDir}/assets/project_layout.txt)` [9].

## 2. Concurrency Rules
- **Async Safety:** Never put blocking I/O (synchronous DB calls, heavy calculation) inside `async def` routes. This blocks the event loop [10].
- **Remediation:** If blocking code is necessary, define the route as `def` (sync) so FastAPI runs it in a threadpool [11].

## 3. Dependency Injection
Use dependencies for data validation against the DB, not just Pydantic validation. Decouple dependencies to maximize caching within the request scope [12].
File: assets/project_layout.txt
src/
  auth/               # Domain Component
    router.py         # Endpoints
    service.py        # Business Logic
    models.py         # SQLAlchemy Models
    schemas.py        # Pydantic Models
    dependencies.py   # Component-specific DI
  billing/            # Domain Component
    router.py
    service.py
  config.py           # Split BaseSettings
  main.py             # App Factory

--------------------------------------------------------------------------------

