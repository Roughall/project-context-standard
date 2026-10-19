# Project Bootstrap Protocol

You are joining an existing project. Continue from documented and verified state; do not restart analysis by default.

1. **Discover:** identify the active repository, working directory, branch, and available tools. Do not assume access.
2. **Load context:** read `AGENTS.md`, `project.yaml`, `PROJECT_STATUS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TEST_RESULTS.md`, and `HANDOFF.md` when present.
3. **Verify state:** inspect files, configuration, commits, logs, or tests relevant to the next task. Compare actual state with documentation.
4. **Set starting point:** summarize current milestone, last verified results, blockers, constraints, and next action with acceptance criteria.
5. **Execute:** stay within scope; do not make unapproved architecture changes, overwrite user work, expose secrets, or perform sensitive production changes without approval.
6. **Preserve continuity:** update status, test evidence, changelog, and handoff. Distinguish facts, assumptions, and unverified claims.
7. **Report:** provide concise starting state, work performed, files changed, verification, blockers, and next action.

If context is missing, name the exact missing resource and ask only for information that blocks safe progress. Never invent project state or claim access/actions that were not verified.
