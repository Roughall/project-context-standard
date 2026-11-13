# Gorengan Visual Explainer — DOLA Experiment Checkpoint v1

- **Date:** 2026-11-13
- **Status:** EXPERIMENTAL / PROMPT AND ASSET PLAN READY; generation and performance validation pending
- **Format:** Visual Explainer (Track A)
- **Target runtime:** 20 seconds, vertical 9:16
- **Generation plan:** Two DOLA image-to-video generations, 10 seconds each
- **Purpose:** Test whether DOLA can animate supplied still-image references while preserving food/container identity, create plausible steam/condensation motion, and maintain continuity across two clips. Native DOLA audio is enabled for SFX testing only; final edit may mute it and use a separately produced voice-over.

## 1. Creative decision for this experiment

The owner selected **A — Visual Explainer** for the gorengan (Indonesian fried snacks) educational pilot. The story remains one topic: why hot gorengan can become soggy when sealed immediately, and how allowing steam to escape / using ventilation can help.

This is a single controlled experiment, not a permanent channel format or proven performance formula.

## 2. Distribution and retention inputs adopted as hypotheses

Creator-provided recommendations were translated into testable practices:
- One Reels = one topic.
- Hook should communicate the relatable problem within the first 3 seconds.
- Compact runtime; this pilot targets 20 seconds (within the suggested 13–40 second range).
- Use voice-over as the primary explanation.
- Include one relevant comment CTA.
- Evaluate hook and CTA after publication.
- Consider two daily posting windows (04:00–06:00 and 17:00–20:00 WIB) as hypotheses to test against account Insights, not guaranteed optimal times.
- Consider on-topic photo/text/Story support content, while verifying platform-specific reach/monetization counting separately.
- The claim that 7–10 of 60 Reels will reach 70k–150k views and yield 1M total views is an anecdotal target, not a guarantee or validated forecast.

## 3. Master voice-over (20-second target)

**0–3s — Hook:** “Gorengan baru lima menit, kok sudah nggak kriuk?”

**3–8s — Problem:** “Kalau masih panas langsung ditutup rapat, uap airnya terperangkap.”

**8–13s — Explanation:** “Uap itu mengembun jadi titik air, lalu bikin permukaannya lembap.”

**13–17s — Solution:** “Biarkan uap keluar dulu, lalu simpan di wadah berventilasi.”

**17–20s — CTA:** “Kamu biasanya langsung tutup atau dibiarkan terbuka? Tulis di komentar!”

Voice-over timing is an editing target; actual spoken duration must be checked in the final cut.

## 4. Reference asset map

Actual production images are **not yet confirmed as supplied/attached**. Search-result thumbnails or text descriptions do not count as attached DOLA references.

- **REF 01 — Closed container / starting image (REQUIRED):** Photorealistic Indonesian gorengan in a transparent tightly closed food container on a kitchen counter. This is Generate 1's exact start image.
- **REF 02 — Condensation appearance guide (SUPPORTING):** Same food/container/environment, with small droplets on the inner surface of the transparent lid. It guides condensation appearance; it is not the starting frame.
- **REF 03 — Ventilated storage solution guide (SUPPORTING):** Same type and identity of gorengan on a clean wire cooling rack or in a ventilated food container, in a matching kitchen environment.
- **CONTINUITY FRAME — Generate 1 final frame (REQUIRED FOR GENERATE 2):** Export the actual last frame of Generate 1 and use it as Generate 2's starting image where DOLA supports it.
- If multi-reference input is unavailable, use the designated primary start image and treat supporting images as separate visual guides only where the tool permits. Never claim a reference is attached when it is not.

Reference consistency requirements: same snack type, count, shape, color, container identity, kitchen setting, and lighting across all images.

## 5. DOLA generation plan

### Generate 1 — trapped steam and condensation (10 seconds)

- Primary image: REF 01.
- Supporting guide: REF 02, if multi-reference is supported.
- 0–3s: exact starting composition; subtle push-in; visible but restrained warm steam immediately communicates activity for the hook.
- 3–7s: steam accumulates and moves naturally toward the lid; small droplets gradually form on the INNER lid surface.
- 7–10s: macro emphasis on droplets with snacks still visible below; end on a clear condensation frame.
- One continuous shot; photorealistic food explainer; preserve exact food/container/environment identity.
- Native audio: subtle kitchen room tone and gentle steam hiss only; no speech, narration, music, or singing.
- No people/hands/characters, generated text, labels, logos, extra food, object deformation, exaggerated smoke, or magical effects.

### Generate 2 — release steam and show solution (10 seconds)

- Primary starting image: actual final frame of Generate 1.
- Supporting guide: REF 03; REF 01 may be used as snack identity reference if multi-reference is supported.
- 0–3s: continue from condensation close-up.
- 3–6s: lid opens smoothly; steam escapes and dissipates naturally.
- 6–10s: reveal the same snacks on a ventilated rack/container; finish with a dry, crisp-looking close-up.
- One continuous shot; preserve food identity, quantity, kitchen environment, lighting, and style.
- Native audio: subtle lid-opening sound, gentle escaping steam, and kitchen ambience only; no speech, narration, music, or singing.
- No people/hands/characters, generated text, extra food, food deformation, duplication, disappearance, or abrupt transitions.

Every DOLA prompt begins with the exact AI-character disclosure required by DOLA Production Standard v1.1, even though this food-only experiment does not intentionally depict fictional characters. This follows the currently recorded repository rule.

## 6. Editing map

| Timeline | Visual | Voice-over |
|---|---|---|
| 00–03s | Closed container; steam begins | Gorengan baru lima menit, kok sudah nggak kriuk? |
| 03–08s | Steam trapped inside | Kalau masih panas langsung ditutup rapat, uap airnya terperangkap. |
| 08–10s | Condensation starts | Uap itu mengembun... |
| 10–13s | Close-up of droplets | ...jadi titik air, lalu bikin permukaannya lembap. |
| 13–17s | Lid opens; ventilated storage | Biarkan uap keluar dulu, lalu simpan di wadah berventilasi. |
| 17–20s | Final appetizing close-up | Kamu biasanya langsung tutup atau dibiarkan terbuka? Tulis di komentar! |

Add captions, hook text, and CTA text in the editor, not in DOLA. Mute generated audio if it conflicts with the separately recorded voice-over; retain only useful SFX if quality is acceptable.

## 7. Review gates

Score the two generations separately:
1. Reference identity preservation (snack, container, kitchen).
2. Motion quality and temporal stability.
3. Steam/condensation plausibility and legibility.
4. Generate 1 → Generate 2 continuity.
5. Visual comprehension without on-screen text.
6. Native audio quality and synchronization.
7. Final 20-second pacing, hook clarity, VO intelligibility, CTA timing.

Do not approve the production workflow solely because the clips look attractive. Compare actual output frames with the actual input references. If condensation or lid opening causes severe artifacts, simplify the visual action and test a separate shot rather than allowing DOLA to redesign the scene.

## 8. Publication experiment and metrics

If this pilot is published, record:
- 3-second hold / early retention where available.
- Average watch time and completion rate.
- Shares, saves, comments, follows/profile visits.
- Hook and CTA version.
- Posting time and audience Insights.
- Production time, generation attempts, editing time, and cost.

Do not infer success from views alone. Treat posting windows and supporting photo/text posts as hypotheses. Confirm the platform's current definition of monetizable/eligible views in its own dashboard.

## 9. Current status and next actions

- Creative track A selected for this experiment.
- 20-second script and two 10-second prompt specifications drafted.
- Reference asset plan defined; actual REF 01–03 still need to be created/selected and attached.
- DOLA generation has **not** been performed or reviewed in this checkpoint.
- Next: prepare consistent actual reference images; run Generate 1; inspect output and export its final frame; run Generate 2; edit with VO; review before publication.
- After publication, collect Insights before changing the next pilot.

## 10. Scope warning

This checkpoint records an experiment only. It does not supersede the parent DOLA Production Standard, does not establish a permanent niche or format, and does not validate the creator's reach claims.
