# Cross-Agent Change Protocol v1.0

- **Status:** ADOPTED (decision D-010).
- **Date:** 2026-11-14
- **Scope:** How a change to this repository is prepared, applied, and verified when more than one AI agent works on the project.
- **Authority:** This protocol does not override `STANDARD.md`, `docs/DOLA_PRODUCTION_STANDARD_v1.md`, or `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md`. It only governs how changes reach `main`.

## 1. Principles

1. The repository on GitHub is the single source of truth. Local copies, chat history, and agent memory are not.
2. No claim without evidence: a change is "done" only after it has been read back from `main` and compared with what was intended.
3. Changes are small, exact, and checkable. Agents do not improvise merges or rewrite wording.

## 2. Roles (as of 2026-11-14; revisit when access changes)

| Role | Who | Can do | Cannot do |
|---|---|---|---|
| Owner | Project owner | Decides, approves, forwards packs | n/a |
| Writer | ChatGPT through its GitHub connector | Write commits to `main` | Run `scripts/validate_context.py` (no runtime) |
| Author and auditor | Claude in the free web chat | Read the public repo, build and test change packs on a clean clone, audit `main` after a commit | Write to GitHub (no credentials); read a private repo without pasted content |

If these capabilities change (for example an agent gains write access), update this table by decision before relying on the change.

## 3. Change flow

1. **Author** builds a change pack against a named base commit. The pack contains the instructions for the writer, any new files in full, FIND/REPLACE operations for existing files, a report format, and the expected SHA-256 of every changed file. The author tests the pack on a clean clone of `main` and states the base commit.
2. **Owner** forwards the single pack file to the writer with one sentence asking to follow it exactly.
3. **Writer** reads the latest `main`, confirms the base commit, applies the pack exactly, makes one commit, reads every changed file back from `main`, and sends the report. The writer never reports validator results it did not run.
4. **Auditor** reads `main`, compares each changed file with the expected SHA-256 and line counts, checks that the commit touched only the files named in the pack, and reports PASS, FAIL, or PARTIAL with specifics.
5. **Close-out:** the audit result is recorded in `TEST_RESULTS.md` by the next change pack. Until then the change is `VERIFICATION_REQUIRED`.

## 4. Pack rules

- Each FIND text must match **exactly once** in the target file. If any FIND does not match exactly once, the writer stops, changes nothing, and reports the file, the operation number, and the current text around the expected location.
- The writer changes nothing outside the pack: no rewording, renumbering, formatting cleanup, or status changes.
- One pack produces one commit. The commit message is given in the pack.
- If `main` has moved since the base commit and a FIND no longer matches, the author rebuilds the pack on the new `main`; the writer does not merge by hand.
- A blocked or preflight-only result is reported in chat, not committed. A commit that only records preflight moves `main` and invalidates the pack's base. Outcomes are recorded in the same commit that applies the pack, or by the next pack.

## 5. Evidence and honesty rules

- A validator result may be written only by the agent that ran it, with the command and output.
- Differences found in the audit (trailing newline, line endings, altered wording) are reported as differences, not silently accepted or corrected.
- Statuses follow the project vocabulary (`PASS` requires observable evidence; otherwise `VERIFICATION_REQUIRED`).

## 6. Secrets

Never put tokens, keys, or passwords in the repository, in a pack, or in chat. If an agent is ever given write access, use a single-repository token with a short expiry and revoke it after use.

## 7. Audit checklist

- [ ] The commit's parent is the base commit named in the pack (or the author was told otherwise).
- [ ] Only the files named in the pack changed.
- [ ] Each changed file matches the expected SHA-256 and line count, or each difference is listed.
- [ ] `DECISIONS.md` contains the decision named in the pack, and `CHANGELOG.md` starts with the pack's entry.
- [ ] Validator status is stated as run or not run, and by whom.

## 8. Limitations and open items

- The flow depends on the owner forwarding the pack; no agent can trigger another.
- If the repository becomes private, the auditor cannot read it without pasted content.
- Direct writes to `main` were chosen for speed. If conflicts recur, move to branch-per-change with the owner merging.
