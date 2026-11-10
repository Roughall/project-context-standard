# Handoff

## Mandatory DOLA production rule
- Every DOLA prompt in every niche/theme must follow `docs/DOLA_PRODUCTION_STANDARD_v1.md` (parent standard). Niche/content checkpoints can change creative material but cannot waive actual image references, reference mapping, shot-by-shot prompts, continuity, or review gates.
- Before drafting prompts, inspect the asset map and attach actual files through supported DOLA reference inputs. Never treat labels, filenames, or text descriptions as attached images. Mark missing assets MISSING and request/prepare them before generation.
- `AGENTS.md` enforces this rule. Changing the standard requires a versioned decision, not a niche pivot.

## Current objective
Maintain repository-first project context and execute the current Bandaro Betta.ID content niche pilot while keeping the separate DOLA video-production work resumable.

## Current state
- Repository: `Roughall/project-context-standard`
- Branch: `main`
- Latest documented Bandaro working niche decision (2026-11-10): general-audience Indonesian betta entertainment, mixed humor, casual Indonesian language, 15-second vertical videos.
- Bandaro series identity: **CUPANG, TINGKAH, & TINGKAT KEHALUAN**; tagline **“Ikannya cupang. Kelakuannya orang kita.”**
- Five recurring series are documented in `docs/BANDARO_BETTA_INDONESIAN_15S_NICHE_CHECKPOINT_v1.md`.
- This is a working creative direction, not validated performance. No published pilot results are recorded yet.
- DOLA Klip 1 remains unapproved after the second horizontal 16:9 test; see `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md`.

## Bandaro Betta — next actions
1. Select actual available fish for three pilots: Halfmoon for “Tanggal tua, jangan buka marketplace”; Crowntail Black Orchid for “Anak sultan masuk tongkrongan”; and three actual fish for “Dikasih gratis, pilih satu!”.
2. Replace placeholder IDs with live inventory IDs; confirm current availability, price, and shipping information before publication.
3. Batch-record real fish footage in one session. Keep colors, fin shape, size, and condition accurate; do not use generated fish as product evidence.
4. Edit each as a simple vertical short with a target duration of 15 seconds, one clear premise, casual Indonesian text, and a single primary CTA.
5. Publish the three pilots and record retention, profile visits, qualified DMs, completed orders, and production time by series.
6. Review results before promoting any series to a permanent high-volume pillar or changing the niche.

## Bandaro creative guardrails
- Broad Indonesian audience; humor should be instantly understandable and not require betta expertise.
- Mix relatable/receh humor, light satire, and absurdity; avoid heavy themes, overly complex plots, and formal narration.
- Real fish footage is the source of truth for sale inventory.
- No false scarcity, misleading stock status, unsupported biological claims, or fish-stressing stunts.
- Halfmoon is the main inventory exposure (reported ~70%); Plakat ~25%; Crowntail ~5%. Black Orchid can be a distinctive feature but should not dominate inventory exposure.

## DOLA project — next actions
1. For the Bandaro pilot, build the actual asset map and collect/attach the real Halfmoon product footage plus applicable subject, object, and environment references before DOLA generation. The fish product shot itself should use actual footage in the edit, not an AI-generated substitute.
2. Regenerate Misi Mustahil Klip 1 only, applying the latest checkpoint corrections: immediate hook from frame one; small scooter without a large rear basket; clear attempt to position the oversized bag on the rear seat and lower it when it does not fit; one continuous medium-wide three-quarter composition; retain a six-second target but inspect actual duration.
3. Attach actual approved subject, vehicle, environment, and grocery reference images. Verify face/wardrobe and prop matching against those references.
4. Review the regenerated clip against the per-shot acceptance gate. Do not proceed to Klip 2 until Klip 1 is approved.

## Relevant files
- `docs/DOLA_PRODUCTION_STANDARD_v1.md` — mandatory parent DOLA production rules across all niches and themes.
- `docs/BANDARO_BETTA_INDONESIAN_15S_NICHE_CHECKPOINT_v1.md` — latest working niche, five series, pilot scripts, inventory alignment, conversion path, and measurement.
- `docs/BANDARO_BETTA_CONTENT_STRATEGY_CHECKPOINT_v1.md` — earlier broader Bandaro strategy; superseded in creative direction where it conflicts with the newer niche checkpoint.
- `docs/CHANNEL_PIVOT_AND_NICHE_SEPARATION_CHECKPOINT_v1.md` — channel preservation and niche separation.
- `docs/RETENTION_FIRST_INDONESIAN_SHORTS_FORMATS_CHECKPOINT_v1.md` — Indonesian entertainment-format research hypotheses for the separate Video_AI work.
- `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md` — DOLA shot-control and pilot review.
- `PROJECT_STATUS.md` — milestones, verification state, and next actions.
- `TEST_RESULTS.md` — actual checks and evidence.

## Blockers, risks, and approvals
- Bandaro niche performance and sales conversion remain unverified until pilots are published and measured.
- Placeholder fish IDs must not be published; replace them with real inventory identifiers.
- Competitor uniqueness of previous Video_AI formats has not been established.
- DOLA Klip 1 still requires targeted regeneration and reference matching.
- Full repository validation remains pending.

## Tests
- Bandaro niche decision and checkpoint documented; GitHub commit/read-back verification to be recorded after repository write.
- `python scripts/validate_context.py` remains `VERIFICATION_REQUIRED` until run in a local checkout.
