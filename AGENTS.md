# Agent Instructions

## First action: bootstrap
Read `STANDARD.md`, `project.yaml`, `PROJECT_STATUS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TEST_RESULTS.md`, and `HANDOFF.md` when present. Follow project-specific instructions too.

## Work rules
- Verify repository, branch, working directory, and available permissions before assuming access.
- Treat repository documentation as the durable source of truth; chat history is supplementary.
- Do not repeat completed work unless verification shows it is needed.
- Keep changes scoped to the current task and acceptance criteria.
- Do not overwrite user work or alter approved decisions without permission.
- Never expose or commit secrets or sensitive operational data.
- Run relevant tests. Record exact commands and outcomes; do not invent evidence.
- If blocked, explain the specific blocker and the smallest action needed to proceed.

## Before ending
Update `PROJECT_STATUS.md`, `TEST_RESULTS.md`, `CHANGELOG.md`, and `HANDOFF.md` as relevant. Clearly mark unverified items as `VERIFICATION_REQUIRED`. Report files changed, tests run, result, and next step.
