# Video_AI — DOLA Shot-Controlled Production Checkpoint v1.0

> **Parent standard:** This project-specific checkpoint supplements and does not override the mandatory cross-niche rules in [`DOLA_PRODUCTION_STANDARD_v1.md`](DOLA_PRODUCTION_STANDARD_v1.md). All DOLA work must follow that standard, regardless of niche or theme.

- **Status:** APPROVED AS WORKING PRODUCTION GUARDRAIL
- **Date:** 2026-11-10
- **Scope:** DOLA-based live-action / photorealistic short-form video generation.
- **Trigger:** Review of the first three generated clips for "Misi Mustahil Orang Indonesia — Belanjaan dari Pasar ke Rumah". The combined result showed weak opening intent, repetitive loading actions, insufficient escalation, no completed payoff, and weak control over requested actions and continuity.
- **Basis and limitation:** This checkpoint records observed production failures and corrective workflow decisions. It does not claim that prompt wording can guarantee exact model compliance; each generation must be inspected.

## 1. Core rule

**Do not prompt DOLA with a whole story and expect it to autonomously direct a coherent short film. Direct it shot by shot.**

The story defines why a shot exists. The shot specification defines exactly what must happen. References define what things look like. The generated result must be checked before it becomes an input to the next shot.

## 2. Mandatory pre-generation references

Every generation must receive actual image files through the relevant DOLA reference inputs when those features are supported. Internal asset IDs (for example, CHAR-001 or ENV-001) are labels for our production organization; they are not substitutes for attaching the images.

Required reference categories, as applicable:
- **Subject reference:** approved character/person/animal identity and wardrobe.
- **Object reference:** vehicle, product, prop, costume detail, and other continuity-critical objects.
- **Environment reference:** the actual location, architecture, street, interior, and lighting context.
- **Storyboard / shot reference:** framing, camera position, composition, screen direction, and subject placement.
- **Continuity reference:** approved final frame or still from the preceding shot when the next shot continues the same action or state.

Rules:
1. Prepare and approve missing master references before generation; do not invent their appearance in a production prompt.
2. Explicitly map each attached image to its role in the prompt.
3. Use a storyboard image for composition only; do not assume it automatically establishes identity or environment.
4. For photorealistic/live-action output, use photorealistic references. Do not use stylized/illustrated storyboard art as the sole appearance reference.
5. If the DOLA interface or selected model does not support a required reference category, record the limitation and use a tested alternative; do not claim the reference was applied.
6. Preserve approved subject, object, wardrobe, and environment designs unless a change is explicitly approved.

## 3. Shot-controlled prompt contract

Each generated clip should normally contain **one primary continuous action**. A clip may contain small subordinate movements only when they are part of that same action.

Every prompt must specify:

1. **Shot ID and story purpose:** what this shot contributes to hook, conflict, escalation, transition, or payoff.
2. **Reference map:** which actual attached image is the subject, object, environment, storyboard, and continuity reference.
3. **Starting state:** exact positions, poses, props, cargo state, screen direction, and environment state at the first frame.
4. **Single primary action:** observable action in chronological order; avoid long lists of unrelated actions.
5. **Ending state:** exact visible state that should exist at the final frame.
6. **Camera instruction:** shot size, angle, movement (or static), lens/DOF intention where useful, and what must remain in frame.
7. **Physical logic:** plausible weight, contact, object handling, vehicle operation, and safety.
8. **Continuity constraints:** what must not change, disappear, duplicate, teleport, or switch sides.
9. **Negative constraints:** only the relevant failure modes for that shot (e.g. no cut, no montage, no extra people, no object substitution).

Prefer one shot and one continuous take when precise action compliance matters. Use multiple cuts only when separately planned and generated as distinct shots. Do not overload a short generation with many actions, camera changes, or scene transitions.

## 4. Story and retention gate before prompting

A technically attractive clip is not necessarily a story. Before generation, the episode must define:
- **Hook:** an immediately legible unusual situation, problem, or stake that gives a reason to keep watching.
- **Central question / mission:** what the viewer is waiting to see answered.
- **Progression:** each beat changes the situation, adds information, increases stakes, or reveals a strategy.
- **Escalation:** avoid repeating the same action (for example, repeatedly lifting and placing groceries) without a new consequence.
- **Payoff:** a visible ending that answers the opening promise.
- **Story completion:** do not end on a travel or process shot when the promised outcome is arrival/success at the destination.

The hook must not be replaced by a decorative establishing shot. Establishing shots are allowed only when they also communicate the premise or are brief enough not to delay it.

## 5. Continuity protocol between clips

For sequential generations:
1. Approve the preceding clip before generating the next one.
2. Export/select its actual final frame (or a representative approved continuity still).
3. Attach that still as a continuity reference to the next generation when supported.
4. Explicitly state what must carry over: character pose/location, screen direction, prop count and positions, cargo arrangement, vehicle state, wardrobe, lighting, and time of day.
5. Specify the next shot's starting state so it matches the previous ending state.
6. Inspect the seam in the assembled edit; do not assume matching text descriptions guarantee matching frames.

Master references preserve identity; continuity frames preserve the current scene state. They serve different purposes.

## 6. Production gates

### Pre-production — must pass before generation
- [ ] Episode has a clear hook, central question, escalation, and payoff.
- [ ] Storyboard is broken into numbered shots with timecodes and a defined purpose per shot.
- [ ] Each shot has one primary action, a starting state, and an ending state.
- [ ] Actual subject, object, and environment reference images are prepared and attached.
- [ ] Storyboard and continuity references are prepared where needed.
- [ ] Visual style is explicit and consistent (e.g. photorealistic live-action, not animation).
- [ ] Physical logic and safety have been reviewed.

### Per-shot review — must pass before next generation
- [ ] Correct subject identity and wardrobe.
- [ ] Correct objects, count, appearance, and positions.
- [ ] Correct environment and visual style.
- [ ] Requested primary action actually occurs.
- [ ] Starting and ending states are usable.
- [ ] Camera framing supports the story purpose.
- [ ] No critical generation artifact or continuity break.

### Final edit — must pass before publication
- [ ] First frame communicates the premise and creates curiosity.
- [ ] Every shot adds story information or changes the situation.
- [ ] No repetitive filler or decorative shots that delay the story.
- [ ] Escalation is understandable without relying on explanatory text alone.
- [ ] Central promise receives a visible payoff.
- [ ] Final shot completes the story rather than stopping mid-journey.
- [ ] Character, prop, environment, screen direction, and action continuity have been checked in the assembled video.
- [ ] Text overlays and captions are added in editing when exact typography matters.

## 7. Case study: Misi Mustahil — groceries from Jakarta market to home

Observed problems in the first assembled three-clip draft:
- Opening aerial/market footage established location but did not immediately show the challenge.
- Character reactions (looking, smiling, thinking) did not create meaningful story progression.
- Grocery loading repeated similar actions without a new obstacle, failed attempt, or strategic change.
- The journey began, but the draft ended before arrival and therefore did not deliver the promised success payoff.
- Prompt instructions combined too many actions and camera changes within short generations.
- Asset labels in text were not sufficient evidence that corresponding image files had actually been attached and used.
- No approved final-frame handoff was defined between generations.

Corrective direction:
- Open on the visual contradiction: a modest motorcycle beside a clearly excessive but physically plausible grocery load, with the mission immediately legible.
- Make the viewer's question explicit through the image/action: can all groceries reach home in one trip?
- Show one meaningful failed arrangement or constraint, followed by a visible, plausible strategy.
- Show safe departure and a concise journey only if it advances the mission.
- End at the home with an unmistakable check that all groceries arrived intact.
- Keep the challenge entertaining without depicting unsafe riding or exceeding the vehicle's rated capacity.

## 8. Prompt acceptance template

Use this structure for every DOLA generation:

- **SHOT ID / duration:**
- **STORY PURPOSE:**
- **ACTUAL ATTACHED REFERENCES:** subject / object / environment / storyboard / continuity
- **STARTING STATE:**
- **ONE PRIMARY ACTION (chronological):**
- **ENDING STATE:**
- **CAMERA:** shot size / angle / movement / framing constraints
- **PHYSICAL LOGIC & SAFETY:**
- **CONTINUITY LOCKS:**
- **NEGATIVE CONSTRAINTS:**
- **OUTPUT STYLE / ASPECT RATIO:**

## 9. Case study update: Misi Mustahil — Klip 1, horizontal 16:9 test (2026-11-10)

A second Klip 1 generation was reviewed after changing the output canvas to horizontal 16:9. The observed file properties were 1280×720, 24 fps, and approximately 10.04 seconds, although the prompt requested 6 seconds.

### Observed strengths
- Traditional-market context, Bambang, scooter, and grocery pile were visible together.
- The clip contained one broad action sequence: lifting a grocery bag and lowering it again.
- The scooter remained stationary; the groceries remained present.
- The horizontal composition provided room to see the character, vehicle, and groceries together.

### Observed gaps against the prompt
- The action did not clearly show Bambang attempting to place the bag onto the rear seat and discovering that the available space was insufficient. It read more like lifting/moving the bag.
- The visual contradiction between the bag size and available scooter capacity was not strong enough.
- The opening held a relatively passive standing beat before the action began, delaying the hook.
- The requested slow push-in was not clearly expressed.
- Actual duration exceeded the requested six seconds.
- A visible Dola AI watermark/text was present, despite the no-watermark instruction.
- The scooter appeared to have a rear basket/carrying structure that weakened the intended small-capacity visual premise.

### Evaluation and next-generation corrections
- Working review score: 6/10; this is an editorial assessment, not a measured model metric.
- Keep 16:9 as a valid test format; the aspect ratio itself was not identified as the cause of the action-compliance gaps.
- Start with the challenge already legible in frame one; remove the passive opening hold.
- Use a small, simple scooter without a large pre-fitted rear basket or preloaded cargo that undermines the limited-capacity premise.
- Make the primary action explicit and observable: Bambang brings the oversized grocery bag toward the rear seat, makes a clear but safe attempt to position it, recognizes that it does not fit, and lowers it back to the ground.
- Keep Bambang, the rear seat, the bag, and the grocery pile in one continuous medium-wide three-quarter composition so the spatial conflict can be read.
- Keep the six-second target in the next prompt, but treat actual generated duration as an independently checked result rather than an assumed guarantee.
- Regenerate only Klip 1 with these targeted changes, then compare it against this test.

### Verification limits
Character likeness/wardrobe and exact grocery matching against the approved master references were not conclusively verified in this review. The next test must compare the actual attached references with the generated output. The 16:9 test does not validate the entire DOLA workflow or later story beats.

## 10. Status and limitations

This checkpoint is an approved working production guardrail based on one reviewed pilot draft. It is not evidence that the revised prompts will achieve perfect DOLA adherence. DOLA behavior, reference controls, and model limits must be verified in actual generations. Record failures and revise one major variable at a time.
