# Project Context Standard

Reusable repository-first context and agent handoff standard. The repository is the durable source of truth; the AI workspace is the entry point.

## Quick start
1. Copy `AGENTS.md`, `project.yaml`, `PROJECT_STATUS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TEST_RESULTS.md`, `CHANGELOG.md`, and `HANDOFF.md` into a project repository.
2. Edit `project.yaml` and the project-specific context files to reflect verified reality.
3. Keep the existing project folder layout; add these files at the repository root.
4. Start new AI sessions with `prompts/bootstrap.md`.
5. Run `python scripts/validate_context.py` from this repository to validate required files and manifest structure.

See `STANDARD.md` for the full operating rules.
