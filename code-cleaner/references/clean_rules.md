# Deep Cleaning Rules

## 1. Dead Code Elimination (Tree Shaking)
- **Zombie Code:** Delete commented-out code blocks immediately. Git history is for recovery; the codebase is for the present.
- **Unused Endpoints:** In FastAPI, remove `@router` definitions that are not included in the main `app` or `include_router` calls.
- **ES Modules (JS/TS):** Ensure `import` is used over `require` to allow bundlers to perform tree shaking [9].

## 2. Anti-Pattern Remediation
- **Shotgun Surgery:** If a single change requires editing many different classes, refactor to move that logic into a single cohesive module (e.g., `Combine Functions into Class`) [14], [15].
- **Primitive Obsession:** Replace loose primitives (e.g., `email: str`) with Value Objects (e.g., `class Email`) to encapsulate validation logic [16].

## 3. Safety Protocol
- **Pre-Refactoring Check:** Before applying changes, ask: "Do you have a passing test suite?"
- **Atomic Commits:** Do not combine cleanup (renaming variables) with logic changes.
