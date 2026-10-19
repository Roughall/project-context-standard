# Project Context Standard v1.0

## Purpose
Make any project resumable by a new ChatGPT conversation or another authorized agent without relying on old chat history. Repository documentation is the source of truth; the AI workspace is the entry point.

## Required files in each project
- `AGENTS.md` — operating rules for AI agents.
- `project.yaml` — machine-readable project identity and key paths.
- `PROJECT_STATUS.md` — current milestone, verified status, blockers, next action.
- `ARCHITECTURE.md` — system structure and important boundaries.
- `DECISIONS.md` — approved decisions and rationale.
- `TEST_RESULTS.md` — verification evidence.
- `CHANGELOG.md` — meaningful changes.
- `HANDOFF.md` — precise continuation instructions for the next session.

Projects may add `docs/`, `modules/`, `evidence/`, `runbooks/`, `agents/`, or `prompts/` without restructuring existing project folders.

## Status vocabulary
Use only: `PLANNED`, `IN_PROGRESS`, `BLOCKED`, `VERIFICATION_REQUIRED`, `PASS`, `FAIL`, `DEFERRED`.

A `PASS` must point to observable evidence (test output, command result, screenshot reference, commit, or reproducible manual verification). If evidence is absent or stale, use `VERIFICATION_REQUIRED`.

## Operating protocol
1. Discover the active repository/work directory and available tools. Never assume access.
2. Read project instructions and the required context files before acting.
3. Inspect only the live state relevant to the next task; compare it with documented state.
4. State the next action and acceptance criteria, then execute within approved scope.
5. Run appropriate tests and record actual results, including failures.
6. Update status, changelog, and handoff before ending.
7. Report changes, verification, blockers, and the next concrete action.

## Safety and integrity
- Never put passwords, tokens, private keys, session cookies, patient data, or other secrets in repository context.
- Use least privilege and avoid production-impacting actions without explicit approval.
- Do not silently change approved architecture, scope, or acceptance criteria.
- Do not claim a command, test, commit, push, or external action succeeded unless its result was observed.
- Separate facts, assumptions, and unverified claims.
- Preserve existing project layout; add context files without unrelated refactors.
- Ask a focused question only when a missing decision genuinely blocks safe progress.

## Completion criteria
A handoff is complete when another agent can identify: current objective, verified state, relevant files, exact next step, acceptance criteria, known risks/blockers, and required approvals.
