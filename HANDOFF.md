# Handoff

## Mandatory DOLA production rule
- Every DOLA prompt in every niche/theme must follow `docs/DOLA_PRODUCTION_STANDARD_v1.md` (parent standard). Niche/content checkpoints can change creative material but cannot waive actual image references, reference mapping, shot-by-shot prompts, continuity, or review gates.
- Before drafting prompts, inspect the asset map and attach actual files through supported DOLA reference inputs. Never treat labels, filenames, or text descriptions as attached images. Mark missing assets MISSING and request/prepare them before generation.
- Every prompt must begin with the exact AI-character disclosure in Section 2 of the standard. For authentic real-animal/product footage, add the required clarification that the footage is real and must not be replaced by AI-generated imagery.
- `AGENTS.md` enforces this rule. Changing the standard requires a versioned decision, not a niche pivot.

## Current objective
Maintain repository-first project context and continue the Video_AI reference-video study while keeping the separate Bandaro Betta.ID pilot and DOLA video-production work resumable.

## Current state
- Repository: `Roughall/project-context-standard`
- Branch: `main`
- Latest interim checkpoint: `docs/VIDEO_AI_REFERENCE_VIDEO_ANALYSIS_CHECKPOINT_v1.md` (2026-11-12).
- Four user-supplied MP4 references were visually/structurally inspected: character-led tutorial, timeline/illustrated explainer, low-poly cause-and-effect explainer, and longer 2D illustrated narrative.
- Exact source apps are UNKNOWN. `Lavf62.3.103` is an FFmpeg/libavformat encoder tag, not proof of the original production app.
- Audio streams exist, but full audio transcription and detailed voice delivery analysis remain outstanding.
- The hybrid workflow proposed in the checkpoint is EXPERIMENTAL; no permanent format or app stack has been selected.
- Bandaro Betta.ID remains positioned as general-audience Indonesian betta entertainment, mixed humor, casual Indonesian language, 15-second vertical videos. This is a working creative direction; performance is not yet validated.
- DOLA Klip 1 remains unapproved after the second horizontal 16:9 test; see `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md`.

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
- `docs/VIDEO_AI_REFERENCE_VIDEO_ANALYSIS_CHECKPOINT_v1.md` — four reference-video observations, attribution limits, proposed hybrid workflow, and next experiments.
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
