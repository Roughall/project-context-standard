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

## DOLA production rule — mandatory across niches
- Before drafting any DOLA prompt, read `docs/DOLA_PRODUCTION_STANDARD_v1.md` and the relevant project-specific DOLA checkpoint.
- Begin every DOLA prompt with the exact AI-character disclosure in Section 2 of the parent standard. Apply it to fictional AI-generated human and animal characters; when authentic real-animal/product footage appears, append the required clarification so the real footage is never falsely labelled AI-created.
- The DOLA Production Standard is the parent, cross-niche production rule. A new niche, theme, story, character, product, or channel does not reset or override it.
- For each shot, map actual subject, object, environment, storyboard, and continuity image files as applicable. A filename, asset ID, description, or URL in prompt text is not a substitute for attaching the actual image through the supported DOLA reference input.
- Never claim a reference is attached or ready unless the actual file is available. If a required image is missing, list it as MISSING and request/prepare it before generation.
- Direct DOLA shot by shot; include starting state, one primary action, ending state, camera, continuity locks, and relevant negatives.
- Preserve actual sale-product footage as the source of truth; do not generate a replacement that misrepresents the product.
- Content checkpoints may change creative strategy, but may not silently weaken production requirements. Only a deliberate, documented standard revision can do that.

## Before ending
Update `PROJECT_STATUS.md`, `TEST_RESULTS.md`, `CHANGELOG.md`, and `HANDOFF.md` as relevant. Clearly mark unverified items as `VERIFICATION_REQUIRED`. Report files changed, tests run, result, and next step.
