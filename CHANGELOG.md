## 2026-11-21 — Update DOLA prompt structure to v1.3 and record Healing Murah source audit
- Added the exact owner-requested final line `it's not contain copyrighted or policy-violating content` to the DOLA prompt template and pre-submit checklist; recorded D-014.
- Updated the Bandaro Idea 02 checkpoint with the Test03.mp4 source-clip review and marked the assembled 15-second edit and cut-point verification as pending.
- The Test03 source was generated before this v1.3 footer change; no claim is made that the footer was used in that generation.
- Recorded the source audit and kept the final edit and Mode M effectiveness unverified; see `TEST_RESULTS.md`.

## 2026-11-21 — Record Bandaro Idea 02 “Healing Murah Meriah” DOLA test prompt
- Added `docs/BANDARO_IDEA02_HEALING_DOLA_TEST_CHECKPOINT_v1.md` with the prompt retained by the owner, a four-shot/three-cut camera plan, the 10-second-source to 15-second-edit map, VO/CTA, and missing-asset gates.
- Recorded D-013 approving Mode M for this one test only; the general Mode M status and DOLA prompt standard remain unchanged.
- DOLA generation and output review remain `VERIFICATION_REQUIRED`; no successful generation or performance result is claimed.
- Validator `python scripts/validate_context.py` was not run in this GitHub-connector workflow; see `TEST_RESULTS.md`.

## 2026-11-17 — Apply DOLA prompt structure v1.2, Tari Piring checkpoint, shot-variety analysis, and cross-agent protocol (content dated 2026-11-14 to 2026-11-17)
- Added `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md` (v1.2): fixed prompt section order, rules R1 to R12 (R8 downgraded to a guideline), acceptance-gate items 1 to 14, template, checklist, and evidence rows. Planned-cut Mode M remains proposed only.
- Added `docs/TARI_PIRING_DOLA_CHECKPOINT_v1.md`: Tari Piring Clips 01 to 03, the assembled-video audit, working scores, and the prompts as run; Clip 01 v3 recorded as owner-reported and not audited.
- Added `docs/VIDEO_AI_SHOT_VARIETY_REFERENCE_ANALYSIS_v1.md`: two reference videos analyzed for shot variety, the gap against the assembly, and a proposed (not adopted) standard.
- Added `docs/CROSS_AGENT_CHANGE_PROTOCOL_v1.md` and a pointer in `AGENTS.md`. Recorded decisions D-008 to D-012, the reviews and audit results in `TEST_RESULTS.md`, and updated project status and handoff.
- Verification: see `TEST_RESULTS.md`. Effectiveness of the rules is untested; the change pack is not closed until Claude's audit of `main` is recorded.

## 2026-11-15 — Record CHATGPT_UPDATE_PACK v2 preflight
- Recorded that all 11 exact FIND targets in the rebuilt v2 pack matched `main` exactly once at `ec00ef7`.
- The pack itself was not applied: no new files or replacements were written, and no pack commit, post-change read-back, or validator run is claimed.
- See `TEST_RESULTS.md` for the precise preflight result. The DOLA prompt-structure/Tari Piring/cross-agent pack remains pending application.

## 2026-11-10 — Revise DOLA Production Standard to v1.1: mandatory AI-character disclosure
- Added an exact AI-character disclosure as the first text in every DOLA prompt, covering fictional human and animal characters.
- Added a required clarification for authentic real-animal/product footage so real fish or sale products are never falsely labelled AI-generated or replaced by generated substitutes.
- Updated `AGENTS.md`, the DOLA working checkpoint, and the Bandaro niche checkpoint; recorded decision D-004.
- GitHub writes and read-back verification recorded in `TEST_RESULTS.md`.

## 2026-11-10 — Establish mandatory cross-niche DOLA Production Standard v1.0
- Added `docs/DOLA_PRODUCTION_STANDARD_v1.md` as the parent production standard for every DOLA project, niche, theme, and channel.
- Made actual attached image references and explicit reference mapping mandatory for applicable subject, object, environment, storyboard, and continuity roles; asset names or text descriptions alone do not qualify.
- Added mandatory shot-by-shot prompt structure, continuity protocol, pre-generation/per-shot/publication gates, and a formal versioning rule so niche changes cannot silently weaken production requirements.
- Updated `AGENTS.md`, the DOLA shot-controlled checkpoint, and the Bandaro niche checkpoint to link to and enforce the parent standard.
- Recorded decision D-003. GitHub writes completed; read-back verification and repository validator status are recorded in `TEST_RESULTS.md`.

## 2026-11-10 — Set Bandaro Betta.ID Indonesian 15-second working niche
- Added `docs/BANDARO_BETTA_INDONESIAN_15S_NICHE_CHECKPOINT_v1.md`.
- Recorded the approved working niche: “CUPANG, TINGKAH, & TINGKAT KEHALUAN” / “Ikannya cupang. Kelakuannya orang kita.”
- Defined five recurring short-video series: DOMPET VS CUPANG, TINGKAH ORANG + TINGKAH CUPANG, PILIHAN WARGA, CUPANG SOK SULTAN, and LAH, KOK BAGUS BANGET?
- Set general Indonesian audience, mixed humor, casual Indonesian language, and a 15-second target structure.
- Added three first pilots, inventory alignment, direct-DM sales path, measurement criteria, and animal/product-representation guardrails.
- Recorded decision D-002 and updated project status and handoff. This is a working niche hypothesis; no pilot performance is claimed.

## 2026-11-10 — Record Misi Mustahil Klip 1 horizontal 16:9 test
- Updated `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md` with the second Klip 1 generation review (1280×720, 24 fps, approximately 10.04 seconds versus 6 seconds requested).
- Recorded strengths, concrete prompt mismatches, a working editorial score of 6/10, and targeted corrections: immediate hook, smaller scooter without a large rear basket, explicit rear-seat fit attempt, continuous composition, and actual-duration inspection.
- Character/wardrobe likeness and exact prop-reference matching remain unverified; Klip 1 remains unapproved and must be regenerated before Klip 2.
- Verification: video reviewed; repository validator remains `VERIFICATION_REQUIRED`.

# Changelog

## 2026-11-09 — Add retention-first Indonesian Shorts formats checkpoint v1.0
- Added `docs/RETENTION_FIRST_INDONESIAN_SHORTS_FORMATS_CHECKPOINT_v1.md`.
- Captured five repeatable formats: Sidang Warga, Misi Mustahil Orang Indonesia, Tebak Sebelum Terungkap, 1 Benda 5 Bencana, and Pilihan yang Salah.
- Recommended Sidang Warga as the first pilot candidate, subject to competitor review and pilot validation.
- Verification: file creation committed; later read-back confirmed.

## 2026-11-06 — Add channel pivot and niche separation checkpoint v1.0
- Added `docs/CHANNEL_PIVOT_AND_NICHE_SEPARATION_CHECKPOINT_v1.md`.
- Recorded the recommendation to preserve the existing Video_AI channel and create a separate Bandaro Betta channel when audience promises remain materially different.
- Verification: file created and fetched back successfully; commit `a72ef495336264c82117dda93223eaef8c3211a6`.

## 2026-11-06 — Add Bandaro Betta content strategy checkpoint v1.0
- Added `docs/BANDARO_BETTA_CONTENT_STRATEGY_CHECKPOINT_v1.md` with proposed content concepts, pilot priorities, a proposed content mix, Betta Identity Card concept, measurement plan, and editorial guardrails.
- Verification: file creation committed successfully; commit `3b6e7bf81f1b5ed832794fdd01d9716e775a80e2`.

## 2026-11-10 — Add DOLA shot-controlled production checkpoint v1.0
- Added `docs/DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md` after reviewing the first Misi Mustahil pilot draft.
- Established actual subject/object/environment references, shot-by-shot prompts, continuity handoff, and acceptance gates.
- Verification: GitHub create-file operation returned commit `105b780b2801d1704823493c777384f81a8e1afc`; checkpoint and updated context files fetched successfully.

## 2026-11-06 — Add Video_AI retention and storytelling framework v2.0
- Added `docs/VIDEO_AI_RETENTION_STORYTELLING_FRAMEWORK_v2.md` covering hook, curiosity, payoff, retention-graph interpretation, evaluation, experimentation, and Bobo application.
- Verification: framework committed; full repository validator remains `VERIFICATION_REQUIRED`.



## 2026-11-10 — Add Bandaro Pilot 01 shot-by-shot DOLA prompt pack
- Added `docs/BANDARO_PILOT01_DOLA_PROMPT_v1.md` for “Tanggal Tua, Jangan Buka Marketplace.”
- Recreated the 15-second episode as two separately generated fictional-human shots plus one authentic Halfmoon footage insert; placed the mandatory disclosures at the beginning of each DOLA generation prompt and real-footage clarification at the actual fish insert.
- Recorded required asset gaps and blocked generation until actual references and fish footage are supplied; no DOLA execution is claimed.
- Linked the prompt pack from the Bandaro niche checkpoint and recorded decision D-005.
