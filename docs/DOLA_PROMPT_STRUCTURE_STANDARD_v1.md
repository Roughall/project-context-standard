# DOLA Prompt Structure and Beat Rules v1.2

- **Status:** APPROVED AS WORKING AUTHORING STANDARD (decisions D-008, D-009, and D-011). Effectiveness is `VERIFICATION_REQUIRED`; see section 6 for what has and has not been observed.
- **Revision history:** v1.0 (2026-11-10) initial structure from Misi Mustahil Klip A/B. v1.1 (2026-11-14) adds rules R1 to R8 and gate items 11 to 13 from the Tari Piring Clip 01 comparison. v1.2 (2026-11-17) adds R9 to R12, downgrades R8 to a guideline, and adds gate item 14 from the Tari Piring Clip 02, Clip 03, and assembled-video reviews.
- **Parent standard:** [`DOLA_PRODUCTION_STANDARD_v1.md`](DOLA_PRODUCTION_STANDARD_v1.md) (v1.1). This document is subordinate to it, adds prompt-writing and review rules, and does not waive or weaken any parent requirement (actual attached references, reference map, AI-character disclosure, shot-by-shot control, continuity, gates).
- **Companion evidence:** `DOLA_SHOT_CONTROLLED_PRODUCTION_CHECKPOINT_v1.md` section 10 (Misi Mustahil) and `TARI_PIRING_DOLA_CHECKPOINT_v1.md` (Tari Piring), and `VIDEO_AI_SHOT_VARIETY_REFERENCE_ANALYSIS_v1.md` (shot-variety hypotheses, proposed only).
- **Basis:** Observations from reviewed generations, not a validated model of DOLA behavior.

## 1. What "mandatory" means

The structure is mandatory for authors: no DOLA prompt is submitted unless every required section below is present and the pre-submit checklist passes. It cannot force DOLA to obey. Each output is inspected with the acceptance gate in section 5, and no clip is reported as compliant without inspection.

## 2. Fixed section order

Every prompt uses these labels in this order. (R) means required.

1. **AI-CHARACTER DISCLOSURE (R):** the exact text from section 2 of the parent standard, as the first text of the prompt. Add the real-animal/product clarification only when authentic source footage appears.
2. **HEADER (R):** shot ID, duration, aspect ratio, take mode, one-line positive style lock, and story purpose.
3. **REFERENCE MAP (R):** one entry per actually attached image, `CODE = role` (`START-xxx` for the first-frame image, `CHAR-xxx`, `VEH-xxx`, `PROP-xxx`, `ENV-xxx`, `SHOT-xxx`, `CONT-xxx` for the previous clip's final frame). Do not re-describe what a reference already shows; describe only what it cannot: position, screen direction, and state.
4. **START STATE (R):** observable facts at 0 s, written from the image actually used as the first frame (rule R1). For a continuation clip it equals the previous clip's actual final frame, not the intended one.
5. **SHOT PLAN / CAMERA (R):** take mode and camera (section 3).
6. **ACTION BEATS (R):** time-coded beats under sections 4 and 4A.
7. **END STATE (R):** the exact visible final frame, checked against the widest element (rule R2).
8. **PHYSICAL LOGIC AND SAFETY (R)**
9. **CONTINUITY LOCKS (R):** light, time of day, count of key objects, what must not appear (new objects, readable plates, brand text).
10. **AUDIO (R)**
11. **OUTPUT (R):** no generated text, logos or watermarks. Duration and aspect ratio are also set in the DOLA interface; prompt text alone is not trusted.

## 3. Take modes

**MODE S — single take (default, consistent with the parent standard's one primary continuous action).** Specify shot size, angle, height, lens look, focus, and state exactly which camera movements are allowed and which are forbidden. For people-action clips the default is a locked or near-locked camera with no zoom, pan, tilt, cut, or close-up. One deliberate move is allowed when it is declared in the camera line and tied to the beats: a slow push-in, a pull-back, or one combined pull-back with a smooth arc (rule R6). One primary action.

**MODE M — planned cuts (PROPOSED, not approved).** The parent standard says to avoid multiple scene changes per generation. Mode M is a proposed exception where pace matters more than precision: each segment gets its own time range, shot size, angle, and single visible action, with at most 4 segments of at least 2 seconds per 10 seconds. Use it only after the owner approves it in `DECISIONS.md`. Never write "no cuts" together with several camera setups; that contradiction is the failure seen in Klip B.

## 4. Beat rules

B1. **Cause before effect.** A reversal needs a visible cause in an earlier frame. Stating the conclusion is not enough.
B2. **Observable verbs only.** Lift, place, push, step back, look at, smile. Not realize, think, believe, "as if", or "intelligently".
B3. **One primary action per segment;** at most 4 beats per 10 s; each beat at least 1.5 s.
B4. **Hook in frame one.** The first frame already shows the conflict or the object of curiosity. No decorative establishing shot.
B5. **Payoff by 8.5 s** of a 10 s clip.
B6. **Explicit end pose,** including where each key item is, verified in review ("beside the pile" versus "on top of the pile").

## 4A. Revision rules R1 to R12 (v1.1 and v1.2)

- **R1. Start state from the actual first frame.** Describe the image really used as `START-xxx`, including camera side, angle, and background. If the image is unknown, write UNKNOWN and do not describe it from imagination. Observed: the Tari Piring v1 and v2 runs opened on visibly different frames, so run-to-run comparison was confounded.
- **R2. Frame the widest element.** The end frame is defined by the widest part of the subject (arms, props), not the body. Keep it at least 10% of the frame width from each edge. In 9:16 the frame width is roughly 56% of the frame height (estimate), so a straight-arm child dancer cannot fit in a medium shot. Use bent elbows, a smaller span, or a full-body frame with the subject at about 60 to 65% of the frame height (values to verify).
- **R3. Camera stop by composition and time.** Define the stop frame by what is visible (for example feet and a strip of floor) and by a time, and schedule it 1 to 1.5 seconds earlier than needed. Observed: a pull-back requested to stop at about 7.5 s finished at about 8.5 to 9 s.
- **R4. No hold block.** Do not ask for a static hold. Use a small visible final action in the last 1 to 1.5 seconds. Observed: a requested 1 s hold became about 2 s of near-static footage (frame difference fell from about 13 to about 2.6).
- **R5. Quantify the visible cause.** Give size and direction of the demonstrating motion (for example "the plate dips about 10 degrees and the palm brings it level"). Subtle wording produced almost no legible motion.
- **R6. Declared combined move.** Mode S may use one declared pull-back with a smooth arc. Banning orbit and then receiving an uncontrolled arc was the failure; declaring the move gives DOLA a usable path.
- **R7. Sequence the span.** Widen the subject's span only after the camera has reached its final framing. Never open arms or props while the frame is still tight. Observed (Tari Piring v2): plates left the frame for about 3.5 seconds while the arms opened during the pull-back. Status: untested fix.
- **R8. Cap amplitudes and check plausibility.** State a maximum for demonstrating motions (for example plate tilt at most 15 degrees, plate never leaves the palm) and check physical plausibility in the moving video, not only in stills. Observed: a plate tilted nearly vertical at about 8.5 s. Status: untested fix.
- **R8 downgrade (v1.2).** Numeric amplitude targets were not reliably followed (about 20 degrees of plate tilt was requested in Clip 02 v2 and tilts near 60 degrees were observed), while motion sizes tied to a body scale were roughly followed (a side step of about 8 cm was requested in Clip 03 v1 and about 11% of the frame width, roughly 11 cm by estimate, was observed). R8 is therefore a guideline: describe amplitudes in positive terms, do not rely on numeric caps, and verify plausibility in the moving video.
- **R9. Disclosure clarifier (provisional).** Immediately after the exact disclosure text, add one line: "(The two sentences above are production metadata. Never display, caption, or speak them.)" The exact parent text is not changed. Observed: Tari Piring Clip 02 v1, without the line, rendered a garbled copy of the disclosure as on-screen text for about 5 seconds; Clip 02 v2 and Clip 03 v1, with the line, showed none. Two observations with confounds; treat as unproven.
- **R10. Audit each clip against its own assignment.** Audit a clip only against the poses and beats the storyboard assigns to it. Auditing all poses of the character sheet against one clip produced false failures (Tari Piring poses 7 and 9 belong to Clip 03).
- **R11. Settle into the end pose.** For continuous motion, describe the slowing into the final pose in the last 1 to 1.5 seconds as a small visible action. Observed: Clip 02 v2 had no settling instruction and ended mid-swing with the plates at different heights; Clip 03 v1, with an explicit settling smile, ended in a clean final pose. Hypothesis from two clips.
- **R12. Do not rely on mid-clip camera moves.** A move declared from 0 s was executed (Clip 01 v2 pull-back with an arc); "locked until 6.0 s, then one pull-back" was not (Clip 03 v1 kept the same framing). If a reveal is required, start the move at 0 s or reframe in editing. Hypothesis from two clips.

### Rule status

| Rule | Observed support | Status |
|---|---|---|
| R1, R3, R4, R5, R6 | Tari Piring v2 improved over v1 on these points, with confounds (section 9) | ADOPTED, VERIFICATION_REQUIRED |
| R2 | v2 delivered a valid full-body end frame with plates inside; v1 did not | ADOPTED, VERIFICATION_REQUIRED |
| R7 | Not exercised: Clip 01 v3 was reported worse than v2 and not audited, and Clip 03 v1 did not execute its pull-back | ADOPTED PROVISIONALLY, UNTESTED |
| R8 | Numeric caps not reliably followed (see R8 downgrade) | DOWNGRADED TO GUIDELINE |
| R9 | Clip 02 v1 without it showed on-screen disclosure text; Clip 02 v2 and Clip 03 v1 with it did not | ADOPTED PROVISIONALLY (n=2, confounded) |
| R10 | Direct observation in the Tari Piring storyboard audit | ADOPTED |
| R11, R12 | Observations from Clip 02 v2 and Clip 03 v1 | HYPOTHESIS (n=2) |

## 5. Acceptance gate after generation

Score each item YES / NO / PARTIAL before any next generation. Items 1 to 6 restate the parent per-shot gate; 7 to 14 are additions.

1. Subject identity and wardrobe match the references.
2. Vehicle and key objects match, with no added accessories or objects.
3. The primary action of each beat visibly occurs.
4. Start and end states are usable and match the prompt.
5. Camera framing supports the story purpose.
6. No critical artifact or continuity break.
7. Cut count equals the planned count.
8. First frame matches `START-xxx` or `CONT-xxx` (light, pose, props, camera side and position).
9. No readable license plates, brand marks, or text that changes between shots.
10. Actual duration and any platform watermark are recorded.
11. **Widest-element check:** no key prop is cropped by or leaves the frame, except where planned, and the end frame meets the margin in R2.
12. **Camera stop check:** the actual stop time and final framing are recorded against the plan.
13. **Amplitude and plausibility check:** demonstrating motions stay within the stated cap and look physically plausible in motion. (v1.2: R8 is a guideline, so this check is observational.)
14. **Audio check:** listen to the whole clip and record any generated speech, music, tones, or on-screen text. Prompt wording did not reliably suppress audio: Clip 02 v1 had sound from about 7.75 s, Clip 02 v2 had loud sound throughout (about -18 dB RMS), Clip 01 v2 had one short sound, and Clip 03 v1 was near silent. Plan to mute or replace the audio in editing.

Decision rule: any identity or vehicle mismatch, or 5 or more NO items, means do not continue from this output; fix the references first. Otherwise trim to the best segment, continue, and record the failures. Export a handoff frame only from a moment where key props are inside the frame and level or stable.

## 6. Evidence (observations)

| Episode / clip | Observed | Rule it motivated |
|---|---|---|
| Misi Mustahil Klip A (10.08 s, 720x1280, 24 fps) | One continuous locked take; conflict visible in frame one; fit failure not legible; 3 s static hold; bag ended on top of the pile | B1, B4, B6, hold limit (now R4) |
| Misi Mustahil Klip B (same format) | About four cuts despite "no cuts"; start state did not match the continuity frame; light and basket differed from Klip A; no end pose; readable plate whose digits changed | Mode M proposal; contradiction ban; gate items 8 and 9 |
| Tari Piring Clip 01, ChatGPT prompt (screenshots only) | Wide stage opening with a small subject; camera direction reversed against the storyboard; plates cropped at the end; about 3.9/10 working average | B4; R1; R2 |
| Tari Piring Clip 01 v1, Claude prompt (10.08 s, 720x1280) | Storyboard sequence followed; one take; plates cropped for about 3 s at the end; camera passed its stop point; about 2 s near-static end; about 6.1/10 | R2, R3, R4, R5 |
| Tari Piring Clip 01 v2, Claude prompt with R1 to R6 (10.08 s, 720x1280) | Valid full-body end frame with plates inside; visible plate tilt; plates out of or cropped by the frame for about 3.5 s mid-clip; camera stop about 1 to 1.5 s late; about 7.2/10 | R7, R8 |
| Tari Piring Clip 02 v1, Claude prompt, no R9 (10.08 s, 720x1280) | Locked full-body take; first frame matched START-02; plates inside the frame throughout; wrist circles and lowering present, swing weak; garbled disclosure text on screen for about 5 s; sound from about 7.75 s; about 6.4/10 | R9, gate item 14 |
| Tari Piring Clip 02 v2, Claude prompt with R9 (same format) | No on-screen text; clear swing; plates inside the frame; loud generated audio throughout despite "no audio"; a pale reflection patch on the floor (first read as an object, corrected); ended mid-swing; about 7.4/10 | R8 downgrade, R11, gate item 14 |
| Tari Piring Clip 03 v1, Claude prompt (same format) | All storyboard beats; settled final pose with a smile; plates inside the frame; near-silent audio; the declared pull-back did not occur; floor patch inherited from the start frame; about 7.9/10 | R10, R11, R12 |
| Tari Piring assembled 30 s video (1080x1920, 30 fps, 30.21 s) | Raw concatenation of the three clips with voice-over; no on-screen text, hook text, label, subtitles or CTA; about 6.2/10 on content structure (7.0 without the CTA item) | see `VIDEO_AI_SHOT_VARIETY_REFERENCE_ANALYSIS_v1.md` |
| Tari Piring Clip 01 v3 | The owner reported it worse than v2; the file was not audited | R7 and R8 stay untested |

Hypotheses, not confirmed: the continuity or start image may be weighted weakly; several time-coded camera setups invite cuts; one actor with one simple action is followed more reliably than a multi-item sequence; long lists of negatives may suppress motion.

## 7. Template

```
[AI-CHARACTER DISCLOSURE: exact text from the parent standard, section 2]
[R9 clarifier: (The two sentences above are production metadata. Never display, caption, or speak them.)]
[Real-animal/product clarification only if authentic footage appears]

SHOT ID / DURATION / ASPECT: [id] / [N s] / 9:16 / [MODE S or approved MODE M]
STORY PURPOSE: [what this clip must show]
REFERENCE MAP (actually attached): START-01 = [first frame] | CHAR-001 = [role] | PROP-001 = [role] | ENV-001 = [role] | CONT-001 = [previous actual final frame]
START STATE (0 s): [observable facts from the image actually used: camera side, positions, pose, props, background, light]
CAMERA: [size / angle / height / lens look / focus. Allowed and forbidden movement. One declared move, if any, with its stop frame and stop time (rules R3, R6)]
ACTION BEATS:
  [t0-t1] visible cause -> visible effect, with quantified amplitude (R5, R8)
  [t1-t2] ... (span widens only after final framing, R7)
  (payoff visible by 8.5 s; last 1 to 1.5 s is a small visible action, no hold, R4)
END STATE: [exact final frame: pose, item positions, expression; widest element inside the frame with margin, R2]
PHYSICAL LOGIC AND SAFETY: [weight, contact, vehicle state, amplitude caps, no unsafe riding or overload]
CONTINUITY LOCKS: [light, time of day, item counts, no new objects, no readable plates or brand text]
NEGATIVE (specific failures only): [for example no plate cropped by the frame edge; no extra or duplicated props]
AUDIO: [No generated audio of any kind, or the specified audio. Plan to mute or replace in editing; gate item 14]
OUTPUT: photorealistic live-action, no on-screen text, subtitles, logos or watermarks
```

## 8. Pre-submit checklist

- [ ] Disclosure is the first text of the prompt.
- [ ] Every image in the reference map is actually attached; missing ones are marked MISSING. The first-frame image is named `START-xxx`.
- [ ] Start state is written from the image actually used (R1) or from the previous clip's actual final frame.
- [ ] Mode declared; no "no cuts" combined with multiple setups; Mode M only if approved.
- [ ] Every beat has an observable cause and effect, quantified where it demonstrates skill (R5, R8); no inner-state verbs.
- [ ] Payoff visible by 8.5 s; no hold block; end pose written (R4, B6).
- [ ] Widest element fits the end frame with margin; the span widens only after the final framing (R2, R7).
- [ ] Camera stop defined by composition and time, scheduled early (R3).
- [ ] Duration and aspect ratio set in the DOLA interface.
- [ ] No unapproved new objects; plates and brand text handled.
- [ ] Safety reviewed: no riding with an unstable or overloaded load.
- [ ] The R9 clarifier line follows the exact disclosure text.
- [ ] Audio plan: assume generated audio may appear; mute or replace in editing (gate item 14).

## 9. Limitations

- Evidence comes from two episodes (Misi Mustahil: people and vehicle; Tari Piring: one child dancer) and from one generation per variant. Applicability to food or object explainers such as the gorengan experiment (D-007) is untested.
- Tari Piring v1 and v2 appear to start from different first frames, so the improvement cannot be attributed to the prompt alone. The ChatGPT-prompt run was assessed from screenshots, not a file.
- Scores are working editorial judgments, not metrics. Face likeness against master references was judged at a glance only.
- DOLA's handling of reference codes and continuity images is unverified; if codes are ignored, fall back to "attached image 1/2/3" in upload order and record the result.
- Platform watermarks cannot be removed by prompt wording. Audio content was assessed by level only.
- Evidence now covers 3 Tari Piring clips and one assembled video; R9, R11, and R12 rest on two observations each, with chance and prompt changes confounded. Each variant was one generation.
- The assembled-video audit (6.2/10 on content structure) is an editorial judgment of a raw concatenation; shot-variety findings from two reference videos are hypotheses (see the shot-variety analysis).
