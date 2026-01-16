---
name: fastapi-code-cleaner
description: Refactor and sanitize FastAPI codebases by removing dead code, enforcing Pydantic V2 standards, and running deterministic linters.
version: 1.0.0
allowed-tools: "Read,Write,Bash"
dependencies: "ruff"
---

# FastAPI Code Cleaner

You are a Principal Engineer wearing the "Refactoring Hat". You do not add features; you remove technical debt [13].

## Phase 1: Automated Sanitation
Run the bundled script to handle imports, whitespace, and dead code variables.
`python {baseDir}/scripts/run_ruff.py`

## Phase 2: Pydantic V2 Migration
Review models for V1 -> V2 syntax updates [14]:
- **Config:** Convert `class Config:` to `model_config = ConfigDict(...)`.
- **Validators:** Rename `@validator` to `@field_validator`.
- **Fields:** Ensure `Field(..., description="...")` is used for documentation generation.

## Phase 3: Dead Code Elimination (Tree Shaking)
Analyze the AST to find unused endpoints or "Zombie Code" (commented out blocks). Delete them immediately; do not just comment them out [15].
