# Hyperframes Composition Brief: SWYNEX Smart Task Parser

## Objective
Create a 20-second polished launch-style brag video for the SWYNEX Smart Task Parser CLI.

## Output
- Composition directory: `brag-output-2026-11-04-120000/composition/`
- Rendered video: `brag-output-2026-11-04-120000/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 20 seconds

## Source Material
- Project root: `D:/SWYNEX-Internship/smart-todo-categoriser`
- Primary files read: `README.md`, `categoriser.py`, `models.py`, `cli.py`, `.docs/project_flow.md`
- Product name: SWYNEX Smart Task Parser
- Tagline / strongest claim: natural language in, schema-enforced JSON out
- Key UI or visual moment to recreate: CLI task input followed by a validated Task model result
- Copy that must appear verbatim:
  - `Finish the budget report by next Tuesday`
  - `category: Work`
  - `priority: High`
  - `deadline: next Tuesday`
  - `confidence: 0.94`
  - `is_ambiguous: false`
  - `PYDANTIC VALIDATED`

## Creative Direction
- Tone preset: polished
- Creative direction: A precise developer-tool launch film with a little terminal drama.
- Interpretation: dark ink canvas, warm-white typography, amber inference, green validation, crisp monospace surfaces, restrained motion.
- Angle: one human sentence becomes a trustworthy structured task object.
- Hook: type the real budget-report example into a terminal-like prompt and label it `MESSY INPUT.`
- Outro / punchline: `Your to-do list just got a translator.`
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign
  - Hacker-terminal clichés and waveform graphics

## Visual Identity
- Background: `#101820`
- Text: `#F6F1E8`
- Accent: `#67E8A5` validation green; `#F6C453` inference amber
- Display font: system sans fallback
- Body font: monospace fallback
- Visual references from the project: CLI interface, actual README example, Pydantic Task schema, project flow diagram

## Storyboard
Use `brag-plan.md` as the creative contract.

Scene summary:
1. Human shorthand — 3.2s — typed actual task string and `MESSY INPUT.`
2. Inference rail — 3.8s — natural language → Gemini 2.5 Flash → structured task
3. Schema resolves — 5.0s — actual Task fields assemble one by one
4. Validated result — 4.0s — `PYDANTIC VALIDATED`, check, ambiguity false
5. Translator lockup — 4.0s — product name and final line

## Audio
- Audio role: warm bed with sparse professional accents
- Audio arc: restrained opening, slightly brighter result reveal, quiet tail
- Music: `composition/assets/music.mp3`
- Music treatment: low bed from 0s, fade under final lockup
- Music cue guidance: `happy-beats-business-moves-vol-1-by-ende-dot-app.music-cues.md`; optional beat anchors at 3.02, 7.02, 11.02, 16.02, 18.52s
- Audio-reactive treatment: subtle; amber rail and green validation glow breathe with music energy, no text pulsing
- Audio-coupled moments:
  - Scene 1 — typing
  - Scene 2 — signal send
  - Scene 3 — field sequence
  - Scene 4 — validation chime
  - Scene 5 — final logo hold
- SFX selection guidance: use low-volume keyboard, soft send, and restrained validation sounds matched to entrances
- Exact SFX choice: choose based on implemented animation; keep density sparse
- Audio files: `composition/assets/music.mp3`

## Hyperframes Instructions
Use one standalone HTML composition with one paused GSAP timeline registered as `window.__timelines["main"]`. Keep all motion deterministic and use compositor-safe transforms/opacity. Use actual product copy and readable holds. Run `npx hyperframes check` before preview or render.
