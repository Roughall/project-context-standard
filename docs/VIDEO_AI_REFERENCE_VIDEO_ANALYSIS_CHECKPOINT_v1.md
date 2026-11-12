# Video_AI Reference Video Analysis Checkpoint v1.0

- **Date:** 2026-11-12
- **Status:** WORKING ANALYSIS / EXPERIMENTAL
- **Scope:** Review of four user-supplied reference videos and the resulting production-workflow discussion.
- **Authority:** This checkpoint records observations and hypotheses only. It does not promote a new channel niche, story format, app stack, or DOLA rule to CANONICAL status.

## 1. Purpose

Preserve the interim findings from reviewing four example videos so the next session can continue from the same evidence, without treating guessed software attribution or unverified audio details as facts.

## 2. Reference files reviewed

Four MP4s supplied in the conversation were inspected for duration, dimensions, frame rate, visible content, captions, and container metadata.

| Reference | Duration | Frame / orientation | Visible format |
|---|---:|---|---|
| 01 | ~59.8 s | 360×640, 30 fps, vertical | 3D stylized character/tutorial with alternating screen/UI visuals |
| 02 | ~103.9 s | 360×640, 30 fps, vertical | Timeline-led illustrated explainer with cards, labels, symbolic scenes, and documentary-style visual elements |
| 03 | ~74.5 s | 360×640, 30 fps, vertical | Low-poly/isometric cause-and-effect explainer about a floating/raised house and flood systems |
| 04 | ~430.8 s | 640×360, 30 fps, horizontal | 2D illustrated comic/storytelling with recurring human characters and sequential locations |

The files contain AAC audio streams. Visible captions and visual sequences were inspected. A full audio transcription and detailed prosody/intonation analysis were **not** completed in this review; do not claim otherwise.

## 3. Software attribution — evidence limit

- The MP4 container metadata includes the encoder tag `Lavf62.3.103`.
- This identifies an FFmpeg/libavformat encoding or muxing layer, not the original creative application.
- The source files do not provide reliable evidence identifying which image generator, video generator, voice service, or editor created the videos.
- Product/tool names visible inside a video (for example, a tutorial discussing Codex or showing a design interface) are part of the video content and are not proof of the tools used to produce that video.

**Rule:** Keep exact app attribution marked UNKNOWN unless supported by creator disclosure, project files, source assets, or other verifiable provenance.

## 4. Observed creative/production patterns

### Reference 01 — character-led tutorial
- Alternates a stylized character world with screen/UI demonstrations.
- Uses on-screen text to reinforce the tutorial's sequence and practical takeaway.
- The character animation is not required to carry every informational detail; the screen/UI insert carries task-specific evidence.

### Reference 02 — timeline / illustrated explainer
- Organizes a complex subject into named entities, dated beats, visual links, and symbolic transitions.
- Relies on graphic composition, labels, cards, and editorial sequencing more than continuous character animation.
- Factual allegations or political claims depicted in the video were not independently verified in this review.

### Reference 03 — visual cause-and-effect explainer
- Each major narration idea has a corresponding visual demonstration: water level, house movement, pump, pipes/cables, and hose arrangement.
- Abstract or technical relationships become easier to follow when represented as visible physical states and transitions.
- This format is a strong candidate for controlled diagrams, 2D/3D motion graphics, or a hybrid of still renders and limited animation.

### Reference 04 — illustrated narrative
- Uses sequential illustrated scenes, recurring characters, and location changes to sustain a longer story.
- The format can be produced from a locked storyboard/illustration set with camera moves and selective animation; it does not require every frame to be generated as full-motion video.
- The complete spoken story and detailed plot beats were not transcribed in this review.

## 5. Interim production diagnosis

The working diagnosis is that weak or confusing outputs are not necessarily caused by prompt wording alone. A single generative-video prompt is being asked to solve several distinct jobs at once:

1. Story design — premise, hook, conflict, escalation, payoff, CTA.
2. Script and narration — wording, timing, emotional delivery, and information order.
3. Visual direction — shot purpose, composition, staging, references, and continuity.
4. Motion generation — physically plausible movement within the model's limits.
5. Editing — pacing, captions, inserts, sound design, transitions, and final payoff.

These jobs should be separated. A video model such as DOLA should be treated as a shot-level motion-generation component, not assumed to be the sole writer, director, animator, voice artist, and editor.

## 6. Proposed experimental hybrid workflow

This is a proposed workflow to test, not yet a canonical project-wide rule:

1. **Story engine:** define audience promise, hook, central question/conflict, escalation, payoff, and CTA.
2. **Master script:** write narration/dialogue and map each sentence to a visible action or graphic.
3. **Voice-over first:** record or synthesize the narration separately; use it as the timing spine.
4. **Storyboard:** define shot duration, visual purpose, camera, character/prop state, and transitions.
5. **Asset lock:** prepare and attach actual character, object, and environment references; maintain a reference map.
6. **Choose production method per shot:**
   - DOLA / video generation for short, achievable motion shots.
   - Still-image generation plus camera movement for illustrated storytelling.
   - Motion graphics for timelines, labels, diagrams, and infographic sequences.
   - Blender or other controllable 3D workflow for precise spatial/physical cause-and-effect.
   - Authentic screen recordings for software demonstrations.
7. **Edit:** assemble VO, visuals, captions, music/SFX, transitions, and pacing in a dedicated editor.
8. **QC:** verify hook clarity, visual/narration synchronization, continuity, factual accuracy, payoff, CTA, and final runtime.

Do not assume that a suggested tool was used in the reference videos. Tools previously discussed as possible components include ElevenLabs, Kling AI, Blender, CapCut, and DaVinci Resolve; these are options for future testing, not verified source-app attribution.

## 7. Format experiments proposed

| Track | Format | Best-fit use |
|---|---|---|
| A | Visual explainer | Systems, mechanisms, practical concepts, cause-and-effect |
| B | Illustrated storytelling | Longer narrative, recurring characters, emotional arc |
| C | Character-led tutorial/story | Character personality plus practical demonstration |
| D | Controlled comparison | Test the same story premise in A/B/C to isolate format effects |

No format has been selected as the permanent direction yet. The prior interactive selection offered a default of Track B, 60–90 seconds, natural voice-over, but this is not an owner-approved production decision unless explicitly confirmed.

## 8. DOLA-specific guardrails

- Continue to follow the mandatory parent standard in `docs/DOLA_PRODUCTION_STANDARD_v1.md`; this checkpoint does not override it.
- Use DOLA for one clearly defined shot/action at a time, within its tested duration and reference constraints.
- Avoid asking one generation to communicate multiple unrelated story beats or complex physical interactions.
- Where exact object placement, mechanical logic, diagrams, UI, or multi-character continuity is essential, prefer a controllable method or split the shot into simpler elements.
- Keep voice-over, captions, music, and sound effects in the post-production workflow when the chosen DOLA task is motion-only.
- Review generated clips against the storyboard; regenerate only the failed shot/element where practical.

## 9. Open questions / evidence gaps

- Transcribe and listen to all four audio tracks to assess script structure, voice delivery, pacing, pauses, emphasis, and CTA wording.
- Determine whether captions are burned-in subtitles or manually added in editing; current inspection does not establish the authoring workflow.
- Obtain creator disclosures or source project files if exact app attribution is required.
- Select one pilot story and test a controlled A/B/C format comparison.
- Record generation attempts, prompt versions, editing time, cost, and retention metrics before adopting a workflow.

## 10. Next session handoff

1. Confirm which format track to test first (or explicitly choose the same-story A/B/C comparison).
2. Choose a concrete subject/story with a clear audience payoff.
3. Produce a complete timed script and shot-by-shot storyboard before writing DOLA prompts.
4. Decide which shots need DOLA and which should use stills, motion graphics, 3D, or screen recording.
5. Complete audio transcription/analysis of the four references if voice-over quality is a key comparison criterion.

## 11. Governance note

The uploaded `Video_AI_SSOT_Draft_AudioManager.docx` is a separate document marked DRAFT — NEEDS VALIDATION. It was not used to alter canonical DNA, Story Engine, Master Script, DOLA, Visual Consistency, or Shorts rules in this checkpoint. Its [VERIFY] sections must be validated against their latest canonical sources before any promotion to CANONICAL.
