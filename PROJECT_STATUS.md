# Project Status

- **Project:** Project Context Standard
- **Overall status:** IN_PROGRESS
- **Last updated:** 2026-11-12
- **DOLA prompt disclosure:** Standard v1.1 requires the AI-character disclosure as the first text of every DOLA prompt, with an explicit exception/clarification for authentic real-animal and product footage.
- **Mandatory production rule:** DOLA Production Standard v1.0 is the parent, cross-niche rule for every DOLA project and content theme. See `docs/DOLA_PRODUCTION_STANDARD_v1.md` and decision D-003.

## Objective
Maintain reusable repository-first context and agent handoff standards.

## Verified state
- Tari Piring (30-second project, three 10-second generations): Clips 01 to 03 were generated and reviewed, and a raw 30.21 s assembly with voice-over exists. Working averages: Clip 01 v2 about 7.1, Clip 02 v2 about 7.4, Clip 03 v1 about 7.9 out of 10. The assembly scores about 6.2/10 on content structure (no hook text, label, subtitles, or CTA; one setting; average shot length about 6 to 10 s versus about 2.5 s in two reference videos). Clip 01 v3 was reported worse than v2 and not audited. DOLA prompt structure is v1.2 (D-011); the shot-variety analysis is recorded as hypotheses (D-012). Nothing is approved for publication by these records.
- DOLA prompt structure and beat rules v1.0 added (`docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md`, decision D-008) as a subordinate companion to the parent standard. Misi Mustahil Klip A (problem) and Klip B (solution) were generated as 10 s, 9:16 clips and reviewed: Klip A had a strong frame-one hook but a weak fit-failure beat and a 3 s static hold; Klip B had a legible loading sequence but about four cuts, a start state that did not match the continuity frame, a basket not seen in Klip A, and no end pose. Neither is approved; the 15-second edit is not yet assembled.
- Added an interim analysis checkpoint for four user-supplied reference videos at `docs/VIDEO_AI_REFERENCE_VIDEO_ANALYSIS_CHECKPOINT_v1.md`. It records visible formats, evidence limits on software attribution, the provisional hybrid workflow, format experiments, DOLA guardrails, and unresolved audio-analysis questions. This is EXPERIMENTAL, not a canonical creative or production decision.
- The four MP4s expose an FFmpeg/libavformat encoder tag (`Lavf62.3.103`), which does not identify the original creative applications. Audio streams exist, but full transcription and voice-delivery analysis were not completed.
- Revised DOLA Production Standard to v1.1: mandatory opening AI-character disclosure for fictional AI-generated human/animal characters, plus a truthful real-animal/product footage clarification where applicable. Updated `AGENTS.md`, DOLA project checkpoint, and Bandaro niche checkpoint. Decision D-004 records owner approval.
- Added mandatory cross-niche DOLA Production Standard v1.0. It requires actual image attachments and explicit reference mapping for applicable subject, object, environment, storyboard, and continuity roles; shot-by-shot prompts; continuity; and review gates. `AGENTS.md`, the DOLA working checkpoint, and the Bandaro niche checkpoint now explicitly point to this parent standard.
- The DOLA shot-controlled production checkpoint at `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md` records the second Misi Mustahil Klip 1 generation review (1280×720, 24 fps, approximately 10.04 seconds against a 6-second prompt). Review found the setting/character/vehicle/groceries and broad lift-lower action, but the rear-seat fit conflict and immediate hook were weak; a rear basket undermined the small-capacity premise; requested push-in was unclear; visible Dola AI watermark/text remained. Working editorial score: 6/10. Character/wardrobe likeness and exact prop matching against master references remain unverified.
- Repository: `Roughall/project-context-standard`
- Default branch: `main`
- A Video_AI retention and storytelling framework v2.0 has been committed under `docs/`.
- A Bandaro Betta content strategy checkpoint v1.0 has been committed under `docs/`; its concepts and content mix remain hypotheses pending pilot results.
- A channel pivot and niche separation checkpoint v1.0 has been committed under `docs/CHANNEL_PIVOT_AND_NICHE_SEPARATION_CHECKPOINT_v1.md`.
- A retention-first Indonesian Shorts formats checkpoint v1.0 has been committed under `docs/RETENTION_FIRST_INDONESIAN_SHORTS_FORMATS_CHECKPOINT_v1.md`.
- **New working niche decision:** Bandaro Betta.ID is positioned as general-audience Indonesian betta entertainment, mixed humor and casual Indonesian language, with 15-second short videos. Five recurring series and the first three pilots are documented in `docs/BANDARO_BETTA_INDONESIAN_15S_NICHE_CHECKPOINT_v1.md`. This is an approved working direction; performance remains unvalidated until published pilots are measured.
- **Bandaro Pilot 01 DOLA prompt pack:** Added `docs/BANDARO_PILOT01_DOLA_PROMPT_v1.md` with two AI-character shot prompts and one authentic Halfmoon footage insert. Prompt pack committed to `main`; generation is blocked pending actual reference assets and selected fish footage. See decision D-005.


- Added `docs/GORENGAN_VISUAL_EXPLAINER_DOLA_EXPERIMENT_CHECKPOINT_v1.md` (2026-11-13): Track A Visual Explainer, 20-second target, two 10-second DOLA generations, reference asset map, timed VO, audio/editing plan, and evaluation gates. Status is EXPERIMENTAL; actual reference assets, DOLA generation, review, and publication metrics are pending.

## Milestones
| Milestone | Status | Evidence / notes |
|---|---|---|
| Add Video_AI retention/storytelling guidance | PASS | Commit: 3fc6d1e578b2c454cec9b5195353e7e994f3fe17 |
| Add Bandaro Betta content strategy checkpoint | PASS | Commit: 3b6e7bf81f1b5ed832794fdd01d9716e775a80e2 |
| Add channel pivot and niche separation checkpoint | PASS | Commit: a72ef495336264c82117dda93223eaef8c3211a6 |
| Add retention-first Indonesian Shorts formats checkpoint | PASS | Commit: 450cbea64f15d723756eb9b351f4b1c674b41591 |
| Add DOLA shot-controlled production checkpoint | PASS | Commit: 105b780b2801d1704823493c777384f81a8e1afc |
| Set Bandaro Betta.ID Indonesian 15-second working niche | IN_PROGRESS | Checkpoint and decision recorded; pilot performance not yet validated |
| Establish mandatory cross-niche DOLA Production Standard v1.0 | PASS | Commit `158d09161f17367e803da78303c6450705fc98f0` |
| Add mandatory AI-character disclosure to DOLA Production Standard v1.1 | PASS | Commit `c76dad9b49152d9185e8620577a6dc20ea4e6660` |
| Add four-reference-video analysis checkpoint | PASS | Commit `d5ecd9b1540eb343dbaa3ee81b664a4124c0a79b`; experimental observations only |
| Adopt cross-agent change protocol v1.0 | PASS (document added) / VERIFICATION_REQUIRED (first use) | `docs/CROSS_AGENT_CHANGE_PROTOCOL_v1.md`, D-010; first pack not yet applied and audited |
| Revise DOLA prompt structure to v1.2 (rules R1 to R12, gate item 14) | PASS (document revised) / VERIFICATION_REQUIRED (effectiveness) | `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md`, D-009 and D-011; R7 untested, R8 downgraded, R9 to R12 rest on two observations |
| Review Tari Piring Clips 01 to 03 and the assembled video | VERIFICATION_REQUIRED | `docs/TARI_PIRING_DOLA_CHECKPOINT_v1.md`; none approved; assembly lacks hook text, label, subtitles, CTA |
| Record shot-variety analysis of two reference videos | VERIFICATION_REQUIRED | `docs/VIDEO_AI_SHOT_VARIETY_REFERENCE_ANALYSIS_v1.md`, D-012; hypotheses, no A/B test |
| Add DOLA prompt structure and beat rules v1.0 | PASS (document added) / VERIFICATION_REQUIRED (effectiveness) | `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md`, D-008; no clip generated from the new structure has been reviewed |
| Review Misi Mustahil Klip A and Klip B (9:16, 10 s) | VERIFICATION_REQUIRED | Reviewed from extracted frames; see `TEST_RESULTS.md`; not approved; reference likeness unverified |
| Validate DOLA Klip 1 prompt adherence (horizontal 16:9 iteration) | VERIFICATION_REQUIRED | Second generation reviewed; partial compliance only. Targeted regeneration still required |
| Validate revised DOLA workflow across the pilot | VERIFICATION_REQUIRED | Klip 1 is not approved; later shots and full-story payoff remain unverified |
| Run repository validator | PASS (basic) | `python scripts/validate_context.py` returned PASS on `main` at `ab933b1`; it checks only file presence and manifest top-level keys, and `project.yaml` still has placeholder values |

## Blockers
- Bandaro niche performance and sales impact are not yet validated by published pilots.
- Competitive uniqueness of prior Video_AI formats has not been established.
- Full repository validation remains unverified.
- The four reference videos' exact source applications and full audio/voice-over characteristics remain unverified.
- No format track has yet been selected as the next Video_AI experiment.

## Next action
Decide how to improve the Tari Piring assembly: re-edit with the shot-variety toolkit (punch-ins, inserts, captions, CTA, audio bed, loudness), approve or reject Mode M for new generations, or build a new format; test by A/B against the current version. Verify any cultural facts before captions or voice-over. Previous queue: For the reference-video study, complete audio transcription/voice-delivery analysis, then choose a format track or same-story A/B/C comparison and prepare a timed master script plus shot-by-shot storyboard before generating any DOLA prompts. For Bandaro, collect actual reference assets and real Halfmoon footage, then produce and publish the three pilots in `docs/BANDARO_BETTA_INDONESIAN_15S_NICHE_CHECKPOINT_v1.md`. Separately, continue the DOLA Klip 1 targeted regeneration and run `python scripts/validate_context.py` in a local checkout when available.
