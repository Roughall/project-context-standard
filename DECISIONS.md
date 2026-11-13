# Decisions

Record approved decisions and their rationale. Do not silently reverse them.

## D-001 — Replace with decision title
- **Status:** PROPOSED / APPROVED / SUPERSEDED
- **Date:** YYYY-MM-DD
- **Decision:** What was decided?
- **Rationale:** Why?
- **Impact:** What changes because of this decision?
- **Approval:** Who or what approved it?

## D-002 — Set Bandaro Betta.ID's working Indonesian short-video niche
- **Status:** APPROVED (working checkpoint; performance validation pending)
- **Date:** 2026-11-10
- **Decision:** Position Bandaro Betta.ID as general-audience Indonesian betta entertainment: “CUPANG, TINGKAH, & TINGKAT KEHALUAN” with the audience promise “Ikannya cupang. Kelakuannya orang kita.” Use mixed humor (relatable/receh, light satire, absurd), casual Indonesian language, and target 15-second vertical videos. The five recurring series are DOMPET VS CUPANG, TINGKAH ORANG + TINGKAH CUPANG, PILIHAN WARGA, CUPANG SOK SULTAN, and LAH, KOK BAGUS BANGET?
- **Rationale:** Earlier concepts felt too Western, classic, heavy, or confusing. Everyday Indonesian humor can make betta content understandable to non-hobbyists while keeping real fish visually central and commercially discoverable.
- **Impact:** Start with three pilots; align featured fish to live stock, use Halfmoon as the main volume exposure, Plakat as secondary, and Crowntail Black Orchid as a distinctive feature. Use real footage, stock IDs, direct DM purchase path, and measure qualified inquiries/orders alongside retention.
- **Approval:** Explicitly approved by the project owner in the conversation on 2026-11-10. This remains a working niche until pilot evidence is reviewed.


## D-003 — Make DOLA production rules mandatory across all niches
- **Status:** APPROVED
- **Date:** 2026-11-10
- **Decision:** Establish `docs/DOLA_PRODUCTION_STANDARD_v1.md` as the mandatory parent production standard for every DOLA-based video project, channel, niche, genre, subject, and theme in this workspace. Every shot must use actual attached image references for applicable subject, object, environment, storyboard, and continuity roles; include an explicit reference map; and follow shot-by-shot action, state, camera, continuity, and review requirements.
- **Rationale:** The existing DOLA shot-controlled checkpoint already required real visual references, but its project-specific placement did not clearly establish that the rule persists across future niche/theme changes. This caused inconsistent application when switching to Bandaro Betta content.
- **Impact:** `AGENTS.md` now instructs agents to read and enforce the parent standard before every DOLA prompt. Content/niche checkpoints must link to it and may change creative material only. A missing actual reference must be marked MISSING; prompt text or asset labels do not count as an attachment. Changing the standard requires a deliberate versioned decision.
- **Approval:** Explicitly approved by the project owner in the conversation on 2026-11-10.


## D-004 — Add mandatory AI-character disclosure at the beginning of every DOLA prompt
- **Status:** APPROVED
- **Date:** 2026-11-10
- **Decision:** Revise the cross-niche DOLA Production Standard to require an AI-character disclosure as the first text in every DOLA prompt: “All fictional characters depicted in this AI-generated scene, whether human or animal, are AI-created characters. Do not present an AI-generated character as a real person or real animal.” When authentic real-animal or product footage is included, immediately add the clarification that the real animal/product footage is real, not AI-generated, and must not be replaced or materially altered.
- **Rationale:** Establish a consistent disclosure convention for generated fictional human and animal characters across all content themes while preserving factual accuracy for real animals/products used as source footage.
- **Impact:** Updated DOLA Production Standard, `AGENTS.md`, the DOLA working checkpoint, and the Bandaro niche checkpoint. Every future prompt must begin with the disclosure and add the real-footage clarification where applicable.
- **Approval:** Explicitly requested by the project owner in the conversation on 2026-11-10.



## D-005 — Approve Bandaro Pilot 01 shot-by-shot DOLA prompt pack
- **Status:** APPROVED FOR PRODUCTION PLANNING (generation pending assets)
- **Date:** 2026-11-10
- **Decision:** Adopt the shot-by-shot prompt pack in `docs/BANDARO_PILOT01_DOLA_PROMPT_v1.md` for “Tanggal Tua, Jangan Buka Marketplace.” Use AI-created fictional human talent only in Shots 01 and 03; use authentic footage of the actual Halfmoon fish in Shot 02.
- **Rationale:** The 15-second concept needs clear separation between fictional AI characters and authentic sale-product evidence, while keeping the story controllable and the fish representation truthful.
- **Impact:** Generate and review the two human shots separately. Insert actual Halfmoon footage in editing. Do not generate until required visual references and the actual fish video are supplied; do not publish placeholders or imply a completed purchase.
- **Approval:** Project owner approved proceeding and requested the prompt be recreated and checkpointed in this conversation on 2026-11-10.

## D-006 — Record interim analysis of four reference videos
- **Status:** RECORDED / EXPERIMENTAL (not a canonical creative-direction approval)
- **Date:** 2026-11-12
- **Decision:** Preserve the review of four user-supplied reference videos and the proposed hybrid production workflow in `docs/VIDEO_AI_REFERENCE_VIDEO_ANALYSIS_CHECKPOINT_v1.md`.
- **Rationale:** The examples show distinct production approaches—character-led tutorial, timeline/illustrated explainer, cause-and-effect visual explainer, and illustrated narrative. Their production strengths can inform controlled experiments, but the available MP4 metadata does not establish the exact source applications.
- **Impact:** Separate story/script/voice-over, storyboard/visual direction, motion generation, and editing into testable stages. Treat the proposed app stack and format tracks as options only. Full audio transcription and voice-delivery analysis remain open.
- **Approval:** Owner requested an interim checkpoint and repository commit/push on 2026-11-12. No permanent format or app stack was approved.


## D-007 — Run a 20-second gorengan Visual Explainer experiment
- **Status:** APPROVED FOR EXPERIMENTAL TESTING (generation and performance validation pending)
- **Date:** 2026-11-13
- **Decision:** Use Track A — Visual Explainer for one educational gorengan Reel with a 20-second target runtime, produced as two 10-second DOLA image-to-video generations. The story covers trapped steam/condensation and a ventilated-storage solution. Use a concise Indonesian voice-over with a hook in the first three seconds and a relevant comment CTA. Enable native DOLA audio only to test synchronized environmental SFX; final editing may mute it and overlay the separate voice-over.
- **Rationale:** The owner selected the visual-explainer direction and wants to test whether DOLA can animate controlled image references while preserving object identity and continuity. Creator-provided consistency, hook, CTA, duration, voice, scheduling, and supporting-post advice is treated as experiment input, not a guaranteed reach formula.
- **Impact:** Record the reference asset map (REF 01 closed container, REF 02 condensation guide, REF 03 ventilated-storage guide), two-generation action plan, timed VO, editing map, review gates, and publication metrics in `docs/GORENGAN_VISUAL_EXPLAINER_DOLA_EXPERIMENT_CHECKPOINT_v1.md`. Actual assets must be prepared and attached before generation. Generation, review, publication, and performance validation remain pending. This does not establish a permanent format or guarantee views.
- **Approval:** Owner explicitly approved proceeding with the gorengan experiment and requested checkpoint, commit, and push on 2026-11-13.
