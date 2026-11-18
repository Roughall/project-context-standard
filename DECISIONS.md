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


## D-008 — Adopt the fixed DOLA prompt structure and beat rules
- **Status:** APPROVED (Mode M planned cuts is PROPOSED and not approved)
- **Date:** 2026-11-14
- **Decision:** Adopt `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md` as a subordinate companion to the parent DOLA Production Standard v1.1. Every DOLA prompt follows its fixed section order (starting with the mandatory AI-character disclosure), its beat rules, and its pre-submit checklist; every output is inspected with its acceptance gate. Single-take Mode S is the default. Mode M (planned cuts) is recorded as a proposal and must not be used until separately approved.
- **Rationale:** Credits are scarce (one generation per account per clip), and the Misi Mustahil Klip A and Klip B reviews (2026-11-10) showed avoidable failures: a no-cut instruction contradicted by several camera setups, reversals without a visible cause, a long static hold, a missing end pose, and a start state that did not match the continuity frame.
- **Impact:** The structure binds authors; it does not guarantee DOLA compliance. It adds rules without waiving any parent requirement and applies to the gorengan experiment prompts (D-007) as well, where its fit for food and object explainers is untested. Effectiveness stays `VERIFICATION_REQUIRED` until a clip generated from this structure is reviewed.
- **Approval:** Owner requested a prompt structure that DOLA must follow and replied "Setuju" to commit and push; Mode M has not been explicitly approved.


## D-009 — Revise the DOLA prompt structure to v1.1 and record the Tari Piring Clip 01 experiment
- **Status:** APPROVED AS WORKING RULES (R1 to R6 have partial observed support; R7 and R8 are provisional and untested). Mode M planned cuts remains PROPOSED and not approved.
- **Date:** 2026-11-14
- **Decision:** Update `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md` to v1.1 with rules R1 to R8 (start state from the actual first frame; frame the widest element; camera stop by composition and time; no hold block; quantified visible cause; declared combined move; sequence the subject's span after final framing; amplitude caps and plausibility check) and acceptance-gate items 11 to 13. Record the Tari Piring Clip 01 comparison and the pending v3 prompt in `docs/TARI_PIRING_DOLA_CHECKPOINT_v1.md`.
- **Rationale:** In the Tari Piring comparison the Claude-structured prompt v2 scored about 7.2/10 against about 6.1 for v1 and about 3.9 for the ChatGPT-written prompt (working editorial scores), but was not highest on every criterion: plates left the frame for about 3.5 s mid-clip and voice-over alignment was lower than v1.
- **Impact:** All DOLA prompts follow v1.1 and its checklist. The rules bind authors; they do not guarantee DOLA compliance. The v1 and v2 runs used visibly different first frames, so improvement cannot be attributed to the prompt alone. Effectiveness stays `VERIFICATION_REQUIRED` until Clip 01 v3 is generated and reviewed.
- **Approval:** The owner had set a condition that the Claude prompt must score highest on every criterion; that condition was not met, and the owner then explicitly requested the checkpoint and rules update with commit and push on 2026-11-14 while testing v3.


## D-010 — Adopt the cross-agent change protocol
- **Status:** APPROVED
- **Date:** 2026-11-14
- **Decision:** Adopt `docs/CROSS_AGENT_CHANGE_PROTOCOL_v1.md`: Claude authors and tests change packs on a clean clone and audits `main` after the commit; ChatGPT, which has GitHub write access through its connector, applies each pack exactly and reports a read-back; the owner forwards a single pack file. A change is closed only after the audit.
- **Rationale:** Two agents writing to the same `main` already produced conflicts (`main` advanced by 35 commits while a change was being prepared), and Claude in the free web chat cannot write to GitHub or share a local repository with ChatGPT. The owner's daily usage is limited, so the flow minimizes manual steps to one forwarded file.
- **Impact:** Writer-side validator claims are limited to what the writer ran. A blocked or preflight-only result is reported in chat without a commit, because such commits move the base (observed twice on 2026-11-15). Direct writes to `main` are used for now; branch-per-change is the fallback if conflicts recur. The roles table is revisited when agent capabilities change.
- **Approval:** The owner agreed to the proposed protocol on 2026-11-14 ("ok mari kita lakukan"). The owner did not explicitly choose between direct-to-main and branch-per-change; direct-to-main was the recommendation and is adopted until the owner says otherwise.


## D-011 — Revise the DOLA prompt structure to v1.2
- **Status:** APPROVED AS WORKING RULES (R9 and R10 adopted provisionally; R11 and R12 are hypotheses; R8 downgraded to a guideline). Mode M planned cuts remains PROPOSED and not approved.
- **Date:** 2026-11-17
- **Decision:** Update `docs/DOLA_PROMPT_STRUCTURE_STANDARD_v1.md` to v1.2: add R9 (disclosure clarifier line), R10 (audit each clip against its own storyboard assignment), R11 (settle into the end pose), R12 (do not rely on mid-clip camera moves), downgrade R8, and add acceptance-gate item 14 (audio check). Record the Tari Piring Clip 02, Clip 03, and assembled-video reviews in `docs/TARI_PIRING_DOLA_CHECKPOINT_v1.md`.
- **Rationale:** Across Clip 02 v1, Clip 02 v2, and Clip 03 v1 (working averages about 6.4, 7.4, and 7.9 out of 10), on-screen disclosure text appeared once without R9 and not in two runs with it; generated audio appeared in two of four clips despite instructions; a declared mid-clip pull-back did not occur; numeric tilt targets were not followed.
- **Impact:** R9 to R12 rest on two observations each with confounds, and each variant was one generation. Effectiveness stays `VERIFICATION_REQUIRED`. No parent requirement is waived.
- **Approval:** The owner asked on 2026-11-17 to update the checkpoint and push ("update ke checkpoint, lalu commit dan push") after the reviews were presented.

## D-012 — Record the shot-variety reference analysis (hypotheses only)
- **Status:** RECORDED (EXPERIMENTAL). No new standard is adopted. Mode M remains not approved.
- **Date:** 2026-11-17
- **Decision:** Record the analysis of two reference videos and the gap against the Tari Piring assembly in `docs/VIDEO_AI_SHOT_VARIETY_REFERENCE_ANALYSIS_v1.md`, with a proposed standard (S1 to S8) marked PROPOSED. The proposed thresholds are to be tested by A/B before any adoption.
- **Rationale:** The owner observed that the assembled video lacks the multiple backgrounds and camera techniques seen in successful references. Measurement confirmed it: about 3 to 5 camera views and a 6 to 10 s average shot length versus 14 to 17 shots at about 2.5 s.
- **Impact:** The references come from one creator and one niche; no performance data exists for them. Whether to re-edit with the toolkit, approve Mode M, or build a new format is an open owner decision.
- **Approval:** The owner asked to study the references and apply them to later ideas, then to record the result in the checkpoint on 2026-11-17.
