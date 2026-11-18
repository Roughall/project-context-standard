# Handoff

## Mandatory DOLA production rule
- Every DOLA prompt in every niche/theme must follow `docs/DOLA_PRODUCTION_STANDARD_v1.md` (parent standard). Niche/content checkpoints can change creative material but cannot waive actual image references, reference mapping, shot-by-shot prompts, continuity, or review gates.
- Before drafting prompts, inspect the asset map and attach actual files through supported DOLA reference inputs. Never treat labels, filenames, or text descriptions as attached images. Mark missing assets MISSING and request/prepare them before generation.
- Every prompt must begin with the exact AI-character disclosure in Section 2 of the standard. For authentic real-animal/product footage, add the required clarification that the footage is real and must not be replaced by AI-generated imagery.
- `AGENTS.md` enforces this rule. Changing the standard requires a versioned decision, not a niche pivot.

## Current objective
Maintain repository-first project context and continue the Video_AI reference-video study while keeping the separate Bandaro Betta.ID pilot and DOLA video-production work resumable.

## Current state
- `CHATGPT_UPDATE_PACK.md` v3 was applied to `main` in a single commit (the commit that adds `docs/CROSS_AGENT_CHANGE_PROTOCOL_v1.md`). It is not closed until Claude's audit of `main` is recorded; the earlier preflight-only records in `TEST_RESULTS.md` remain as history.
- Repository: `Roughall/project-context-standard`
- Branch: `main`
- Latest interim checkpoint: `docs/VIDEO_AI_REFERENCE_VIDEO_ANALYSIS_CHECKPOINT_v1.md` (2026-11-12).
- Four user-supplied MP4 references were visually/structurally inspected: character-led tutorial, timeline/illustrated explainer, low-poly cause-and-effect explainer, and longer 2D illustrated narrative.
- Exact source apps are UNKNOWN. `Lavf62.3.103` is an FFmpeg/libavformat encoder tag, not proof of the original production app.
- Audio streams exist, but full audio transcription and detailed voice delivery analysis remain outstanding.
- The hybrid workflow proposed in the checkpoint is EXPERIMENTAL; no permanent format or app stack has been selected.
- Bandaro Betta.ID remains positioned as general-audience Indonesian betta entertainment, mixed humor, casual Indonesian language, 15-second vertical videos. This is a working creative direction; performance is not yet validated.
- DOLA Klip 1 remains unapproved after the second horizontal 16:9 test; see `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md`.

## Gorengan Visual Explainer experiment — current working task
- Checkpoint: `docs/GORENGAN_VISUAL_EXPLAINER_DOLA_EXPERIMENT_CHECKPOINT_v1.md`.
- Owner selected Track A — Visual Explainer for a 20-second gorengan education Reel, split into two 10-second DOLA generations.
- Prepare three consistent actual image references: REF 01 closed transparent container (Generate 1 start), REF 02 inner-lid condensation guide, REF 03 ventilated rack/container solution guide. Actual files are not yet confirmed as prepared or attached.
- Generate 1 uses REF 01 and should end on a clear condensation frame. Export its actual final frame and use it as Generate 2's start image; use REF 03 as the solution visual guide if supported.
- Master VO includes a 3-second relatable hook, one explanation, practical solution, and a comment CTA. Add captions/CTA text in editing, not DOLA.
- Enable DOLA native audio only to test synchronized subtle SFX; no generated speech/music. Mute/replace with master VO in editing as needed.
- No generation or output review has occurred yet. Do not mark this experiment complete until both clips are reviewed against the actual references.

## Misi Mustahil update (Klip A and Klip B) and prompt structure
- Klip A (problem) and Klip B (solution) were generated as 10 s, 9:16 clips on separate accounts and reviewed (section 10 of `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md`). Neither is approved. Older Klip 1 items under "DOLA project — next actions" predate these clips and are superseded here.
- Decision D-008 adopts `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md` (subordinate to the parent standard): disclosure first, actual attached references, start state from the previous clip's actual final frame, Mode S by default, observable-cause beats, hold at most 1 s, explicit end pose, 10-point acceptance gate. Use it when writing the gorengan Generate 1 and Generate 2 prompts as well.
- Next for Misi Mustahil: assemble and review the 15-second edit (Klip A 0-6.5 s plus Klip B about 0-8.5 s): trim the static hold, match color, blur or cover the license plate, add hook, strategy, and CTA overlays. Do not show an overloaded vehicle being ridden; a Part 2 should end at arrival.

## Cross-agent workflow
- Changes now follow `docs/CROSS_AGENT_CHANGE_PROTOCOL_v1.md` (D-010): Claude builds and tests a change pack and audits `main` afterwards; ChatGPT applies the pack exactly and reports a read-back; the owner forwards one file. The first use is the DOLA prompt structure v1.1 and Tari Piring checkpoint pack; it is not closed until Claude's audit of `main` is recorded. The first attempt halted at preflight (see `TEST_RESULTS.md`); the pack was rebuilt on `ec00ef7`.
- Known formatting defect (not fixed in this pack): in the Relevant files section the first two bullets of the previous update are joined by a literal backslash-n instead of a line break. Fix it in a separate, deliberate change.

## Tari Piring (30-second project)
- Checkpoint: `docs/TARI_PIRING_DOLA_CHECKPOINT_v1.md`. Clips 01 to 03 were generated and reviewed; a raw 30.21 s assembly with voice-over exists. Working averages: Clip 01 v2 about 7.1, Clip 02 v2 about 7.4, Clip 03 v1 about 7.9 out of 10; the assembly about 6.2/10 on content structure. Clip 01 v3 was reported worse than v2 and not audited. Nothing is approved for publication by these records.
- Prompt rules are v1.2 (D-011): R9 to R12, R8 downgraded, gate item 14 (audio check) in `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md`. Generated audio appeared in two of four clips despite instructions, so always plan to mute or replace it in editing.
- Shot-variety analysis (D-012): `docs/VIDEO_AI_SHOT_VARIETY_REFERENCE_ANALYSIS_v1.md`. Two reference videos averaged about 2.5 s per shot with 14 to 17 shots, word-by-word captions, a keyword CTA, and an audio bed; the assembly has 3 clips and a 6 to 10 s average. Findings are hypotheses; test by A/B.
- Next: owner decision on re-edit versus new production and on Mode M; then audit the result.

## Video_AI reference-study next actions
1. Transcribe and listen to all four reference audio tracks to assess hook, script structure, voice delivery, pacing, emphasis, and CTA wording.
2. Choose a first experiment track (A visual explainer, B illustrated storytelling, C character-led tutorial/story) or explicitly run a same-story A/B/C comparison.
3. Select one concrete subject/story with a clear audience payoff.
4. Build a timed master script and shot-by-shot storyboard before drafting generation prompts.
5. Assign each shot to the most controllable method: DOLA/video generation, still illustration plus camera movement, motion graphics, controlled 3D, or authentic screen recording.
6. Track prompt versions, attempts, editing time, cost, final runtime, and retention metrics.

## Bandaro Betta — next actions
1. Select actual available fish for three pilots: Halfmoon for “Tanggal tua, jangan buka marketplace”; Crowntail Black Orchid for “Anak sultan masuk tongkrongan”; and three actual fish for “Dikasih gratis, pilih satu!”.
2. Replace placeholder IDs with live inventory IDs; confirm current availability, price, and shipping information before publication.
3. Batch-record real fish footage in one session. Keep colors, fin shape, size, and condition accurate; do not use generated fish as product evidence.
4. Edit each as a simple vertical short with a target duration of 15 seconds, one clear premise, casual Indonesian text, and a single primary CTA.
5. Publish the three pilots and record retention, profile visits, qualified DMs, completed orders, and production time by series.
6. Review results before promoting any series to a permanent high-volume pillar or changing the niche.

## DOLA project — next actions
1. For the Bandaro pilot, build the actual asset map and collect/attach the real Halfmoon product footage plus applicable subject, object, and environment references before DOLA generation. The fish product shot itself should use actual footage in the edit, not an AI-generated substitute.
2. Regenerate Misi Mustahil Klip 1 only, applying the latest checkpoint corrections: immediate hook from frame one; small scooter without a large rear basket; clear attempt to position the oversized bag on the rear seat and lower it when it does not fit; one continuous medium-wide three-quarter composition; retain a six-second target but inspect actual duration.
3. Attach actual approved subject, vehicle, environment, and grocery reference images. Verify face/wardrobe and prop matching against those references.
4. Review the regenerated clip against the per-shot acceptance gate. Do not proceed to Klip 2 until Klip 1 is approved.

## Relevant files
- `docs/CROSS_AGENT_CHANGE_PROTOCOL_v1.md` — roles, change-pack flow, audit checklist for multi-agent updates.
- `docs/TARI_PIRING_DOLA_CHECKPOINT_v1.md` — Tari Piring Clips 01 to 03, the assembled video audit, scores, and the prompts as run.
- `docs/VIDEO_AI_SHOT_VARIETY_REFERENCE_ANALYSIS_v1.md` — shot-variety analysis of two reference videos (hypotheses) and the gap against the Tari Piring assembly.
- `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md` — fixed DOLA prompt section order, beat rules, acceptance gate, template, checklist (subordinate to the parent standard).
- `docs/VIDEO_AI_REFERENCE_VIDEO_ANALYSIS_CHECKPOINT_v1.md` — four reference-video observations, attribution limits, proposed hybrid workflow, and next experiments.\n- `docs/GORENGAN_VISUAL_EXPLAINER_DOLA_EXPERIMENT_CHECKPOINT_v1.md` — 20-second two-generation gorengan Visual Explainer experiment, reference map, timed VO, prompts' shot plan, and review gates.
- `docs/DOLA_PRODUCTION_STANDARD_v1.md` — mandatory parent DOLA production rules across all niches and themes.
- `docs/BANDARO_BETTA_INDONESIAN_15S_NICHE_CHECKPOINT_v1.md` — latest working niche, five series, pilot scripts, inventory alignment, conversion path, and measurement.
- `docs/BANDARO_PILOT01_DOLA_PROMPT_v1.md` — shot-by-shot prompt pack for Bandaro Pilot 01.
- `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md` — DOLA shot-control and pilot review.
- `PROJECT_STATUS.md` — milestones, verification state, and next actions.
- `DECISIONS.md` — approved decisions and experimental records.
- `TEST_RESULTS.md` — actual checks and evidence.

## Blockers, risks, and approvals
- Bandaro niche performance and sales conversion remain unverified until pilots are published and measured.
- Placeholder fish IDs must not be published; replace them with real inventory identifiers.
- Competitor uniqueness of previous Video_AI formats has not been established.
- DOLA Klip 1 still requires targeted regeneration and reference matching.
- Exact source applications and full voice-over characteristics of the four reference videos remain unknown pending further evidence.
- Full repository validation remains pending.

## Tests
- Reference-video checkpoint committed and read-back verification pending.
- Bandaro niche decision and checkpoint documented; repository commit/read-back verification to be recorded after each repository write.
- `python scripts/validate_context.py` remains `VERIFICATION_REQUIRED` until run in a local checkout.

## Bandaro Pilot 01 — prompt pack ready, assets pending
- Use `docs/BANDARO_PILOT01_DOLA_PROMPT_v1.md` for “Tanggal Tua, Jangan Buka Marketplace.” It contains Shot 01 and Shot 03 DOLA generation prompts, plus Shot 02 instructions for inserting authentic Halfmoon footage.
- Every generated shot begins with the exact AI-character disclosure. The real fish insert must be identified as authentic footage and must not be replaced or materially altered by AI.
- **Do not generate yet:** actual fictional talent, wallet, smartphone, and environment references plus the selected available Halfmoon video are MISSING. Attach actual files in the DOLA workflow before generation. Replace stock-ID placeholder only with a verified live inventory ID.
- DOLA is not connected to this workspace; no generation or output review has occurred. Keep status as pending until the owner/operator runs and reviews the shots.
