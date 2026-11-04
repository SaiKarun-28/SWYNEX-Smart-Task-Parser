# Reconnaissance: Smart To-do Categoriser

## Repository
- Name: `smart-todo-categoriser`
- Root: `D:\SWYNEX-Internship\smart-todo-categoriser`
- Commit: `ec3bf697c8121bac4334771ef46a8fb7b480f708`
- Worktree: Clean

## Scope & Surface
- **CLI Entry**: `cli.py` (Parses user task string, calls `categoriser.py`).
- **Core Logic**: `categoriser.py` (Constructs prompts, interacts with Google Gemini 2.5 Flash via `google-genai` SDK, validates output).
- **Data Contract**: `models.py` (Pydantic schema, enums).
- **Security Boundaries**:
    - Input Boundary: User task string from `cli.py` -> `categoriser.py` (`cli` arg -> `categorise()` function).
    - Authentication Boundary: `GOOGLE_API_KEY` environment variable accessed in `categoriser.py`.
    - Inference Boundary: Call to `gemini-2.5-flash` API.

## Plan & Coverage Units
1. **cli-input**: Validating input handling and argument parsing in `cli.py`.
2. **api-auth**: Ensuring API key access and usage in `categoriser.py`.
3. **inference-payload**: Validating prompt construction, schema enforcement, and input sanitization in `categoriser.py`.
4. **model-validation**: Pydantic schema validation in `models.py`.
