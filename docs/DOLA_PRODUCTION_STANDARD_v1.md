# DOLA Production Standard v1.0

- **Status:** APPROVED — MANDATORY CROSS-NICHE STANDARD
- **Date:** 2026-11-10
- **Scope:** Every DOLA-assisted video project, channel, niche, genre, subject, object, and environment in this workspace.
- **Authority:** This is the parent production standard. Niche/content checkpoints define creative strategy; they do not override this standard unless a formally approved revision is recorded.

## 1. Non-negotiable principle

**A new niche, theme, story, character, product, or channel does not reset or replace the production standard.** Creative content may change; the production workflow remains in force.

Before writing any DOLA prompt, the agent must consult this file and the relevant project-specific DOLA checkpoint. Do not ask the owner to repeat an already approved rule.

## 2. Mandatory visual-reference workflow

For every shot, identify which visual elements must remain consistent and prepare actual image files for the relevant DOLA reference inputs, where supported:

- **Subject reference:** the approved person, character, animal, or other main subject; include identity, appearance, wardrobe, proportions, and defining features as applicable.
- **Object reference:** every continuity-critical product, prop, vehicle, tool, costume detail, or other object.
- **Environment reference:** the actual location or approved set, including architecture, layout, surfaces, background, and lighting context.
- **Storyboard / composition reference:** framing, camera position, screen direction, relative placement, and composition.
- **Continuity reference:** the approved final frame or still from the preceding shot whenever the next shot continues the same action, pose, or scene state.

A category is required whenever it materially affects the shot. If a category is genuinely irrelevant, state why in the shot brief.

### Reference rules

1. Actual image files must be attached through DOLA's relevant reference inputs when supported. A written description, filename, asset ID, URL, or label alone is not an attached reference.
2. Every prompt must include a **reference map** naming each attached image and its exact role. Never imply an attachment exists if it has not been supplied.
3. Prepare and approve missing master references before generation. Do not invent unapproved visual details to fill a missing reference.
4. A storyboard image controls composition only unless explicitly approved for another role; it does not automatically establish subject identity, object design, or environment.
5. Use references consistent with the target visual style. For photorealistic output, use photorealistic appearance references.
6. Master references preserve identity/design. Continuity references preserve the state at a particular moment. Do not confuse their functions.
7. If DOLA/model UI does not support a required reference type, explicitly record the limitation, select a tested alternative, and mark the reference requirement as not fully satisfied. Never claim unsupported reference use.
8. If the user has not supplied a required image, provide a reference checklist or request the missing image. Do not silently replace it with a text-only description.
9. For real sale products, actual product footage/photos are the source of truth. Do not generate a substitute product or materially alter its appearance, condition, dimensions, or behavior.

## 3. Required pre-prompt asset map

Before drafting prompts, create an asset map:

| Asset role | Approved image/file | Applies to shot(s) | Status |
|---|---|---|---|
| Subject | Exact supplied/approved file | Shot IDs | READY / MISSING / NOT APPLICABLE |
| Object | Exact supplied/approved file | Shot IDs | READY / MISSING / NOT APPLICABLE |
| Environment | Exact supplied/approved file | Shot IDs | READY / MISSING / NOT APPLICABLE |
| Storyboard | Exact supplied/approved file | Shot IDs | READY / MISSING / NOT APPLICABLE |
| Continuity | Approved preceding final frame | Shot IDs | READY / MISSING / NOT APPLICABLE |

Never mark an asset READY until the actual file is available and intended for attachment.

## 4. Shot-controlled prompt contract

Direct DOLA shot by shot, not with a whole-story prompt that expects autonomous film direction. Each generation should normally contain one primary continuous action.

Every shot prompt must specify:

1. Shot ID, target duration, and story purpose.
2. Actual attached references and an explicit reference map.
3. Starting state: subject/object positions, pose, prop count, screen direction, and environment state.
4. One observable primary action in chronological order.
5. Ending state: exact visible state at the final frame.
6. Camera: shot size, angle, movement or static framing, and elements that must remain visible.
7. Physical logic and safety.
8. Continuity locks: what must not change, disappear, duplicate, teleport, or switch sides.
9. Relevant negative constraints: e.g. no cut, montage, extra subject, object substitution, unapproved text, or visual redesign.
10. Output style, aspect ratio, and frame orientation.

Do not overload a short clip with unrelated actions, multiple scene changes, or unnecessary camera moves. Text that requires exact spelling, price, stock ID, or typography should normally be added in editing.

## 5. Story gate

Before generation, define the episode's hook, central question/conflict, progression, escalation, and visible payoff. The first frame must communicate the premise; decorative establishing shots must not delay the hook. Every shot must advance the story or reveal product information relevant to the premise.

## 6. Continuity and approval gates

For sequential shots:
1. Generate and review one shot at a time.
2. Approve the preceding shot before generating the next.
3. Use the actual approved final frame as a continuity reference when the next shot continues that scene.
4. Specify matching start/end states and preserve identity, wardrobe, object count/position, environment, lighting, and screen direction.
5. Inspect the assembled seam; text descriptions alone do not prove continuity.

### Pre-generation gate
- [ ] Hook, conflict, progression, and payoff are defined.
- [ ] Storyboard and shot IDs/timecodes are prepared.
- [ ] Every shot has one primary action, starting state, and ending state.
- [ ] Subject/object/environment reference assets are mapped and actual files are attached where applicable.
- [ ] Storyboard and continuity references are attached where needed.
- [ ] Missing or unsupported reference categories are disclosed.
- [ ] Visual style, physical logic, and safety are specified.

### Per-shot review gate
- [ ] Subject identity/design matches its approved reference.
- [ ] Objects and their count/design/positions match references.
- [ ] Environment matches the approved reference.
- [ ] Primary action occurs as requested.
- [ ] Starting and ending states are usable.
- [ ] Camera supports the story purpose.
- [ ] No critical artifact or continuity break.

### Publication gate
- [ ] Opening communicates the premise immediately.
- [ ] Story progression and payoff are complete.
- [ ] Product claims and real-product footage are accurate.
- [ ] IDs, prices, availability, and CTA are current and legible.
- [ ] Assembled continuity and final export are inspected.

## 7. How this standard relates to changing niches

- **This standard stays stable** when a project changes niche, genre, channel, audience, or content theme.
- **A content checkpoint may change** the story, subject, objects, location, tone, runtime, platform, and creative objective.
- The new content checkpoint must link to this standard and state that it remains mandatory.
- A niche change is not permission to skip image references, shot control, continuity, or review.
- To change this standard, create a deliberate versioned revision, document the rationale and approval in `DECISIONS.md`, update related checkpoints, and record the change in the changelog. Never weaken it implicitly inside a content brainstorm.

## 8. Prompt template

- **SHOT ID / TARGET DURATION:**
- **STORY PURPOSE:**
- **ACTUAL ATTACHED REFERENCES:** subject / object / environment / storyboard / continuity; name each actual file and role
- **STARTING STATE:**
- **ONE PRIMARY ACTION (chronological):**
- **ENDING STATE:**
- **CAMERA:** shot size / angle / movement / framing constraints
- **PHYSICAL LOGIC & SAFETY:**
- **CONTINUITY LOCKS:**
- **NEGATIVE CONSTRAINTS:**
- **OUTPUT STYLE / ASPECT RATIO:**

## 9. Limits and evidence

Prompt instructions do not guarantee model compliance. Record actual output properties and inspect each generation against its references and shot contract. Mark untested behavior as `VERIFICATION_REQUIRED`; never report a prompt as successfully executed in DOLA unless generation actually occurred and was reviewed.
