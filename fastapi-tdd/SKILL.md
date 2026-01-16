---
name: fastapi-tdd
description: Expert guide for Test-Driven Development in FastAPI, focusing on the "Quads" strategy and async testing patterns.
version: 1.0.0
allowed-tools: "Read,Write,Bash"
---

# FastAPI TDD Standards

## 1. The Strategy: Testing by Layer (The Quads)
Do not write generic tests. Identify the layer and apply the specific strategy:
`Read({baseDir}/references/quad_strategy.md)`

## 2. Async Testing Rules
- **Client:** Use `httpx.AsyncClient` with `ASGILifespan`.
- **Event Loop:** Never use `TestClient` (sync) for async database routes to avoid event loop conflicts [16].
- **Overrides:** Use `app.dependency_overrides` to mock Infrastructure layers when testing Presentation layers [17].

## 3. Scaffolding
To generate a test file structure that mirrors the source code, run:
`python {baseDir}/scripts/scaffold_test.py <path_to_source_file>`
