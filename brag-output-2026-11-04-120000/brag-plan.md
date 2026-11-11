# Brag Plan: SWYNEX Smart Task Parser

## What is this app?
A CLI that turns messy natural-language tasks into validated, structured to-dos with a category, priority, deadline, confidence, and ambiguity flag.

## The angle
Treat the parser like a tiny command-line translator: one sentence goes in, a trustworthy task object comes out. The joke is the contrast between human shorthand (“Finish the budget report by next Tuesday”) and the suspiciously tidy JSON that follows.

## Hook (first 2-3 seconds)
A stark terminal prompt types: `> Finish the budget report by next Tuesday` while the headline interrupts: `MESSY INPUT.` The cursor snaps to a clean parse.

## Key moments (the middle)
- The input line is “sent” through a compact inference rail labeled `GEMINI 2.5 FLASH`.
- The result resolves into the real schema fields: `category: Work`, `priority: High`, `deadline: next Tuesday`, `confidence: 0.94`.
- A validation stamp lands: `PYDANTIC VALIDATED`, with a small `is_ambiguous: false` confirmation.

## Outro / punchline
The structured output locks up beside the line: `Your to-do list just got a translator.` End on the product name and `natural language → actionable JSON`.

## User flow worth showing
Entry: a plain-text task string in the CLI. Key action: prompt assembly and Gemini inference. Result: a Pydantic-validated `Task` object with category, priority, deadline, confidence, and ambiguity state.

## Tone
- Preset: polished
- Creative direction: “A precise developer-tool launch film with a little terminal drama.”
- Interpretation: Dark, restrained, technical, and rhythmic; use crisp monospace UI and confident transitions rather than generic SaaS cards.

## Format: landscape — 1920x1080
## Duration: 20 seconds

## Visual identity (from the project)
- Background: no authored UI palette; use a dark ink field `#101820`
- Accent: validation green `#67E8A5` with warm amber for inference `#F6C453`
- Text: warm white `#F6F1E8`, muted slate `#AAB7C4`
- Display font: system sans fallback, bold
- Body font: monospace fallback for CLI/schema surfaces
- Strongest visual element: the actual CLI example and Pydantic `Task` schema fields

## Share copy (draft)
Natural language in. A clean, validated task object out. SWYNEX Smart Task Parser gives your to-do list a translator.

## Audio direction
- Role: warm bed with precise UI accents
- Music: `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3`
- Music treatment: start at 0.0s, restrained volume, subtle lift around the result reveal, fade under the final lockup.
- Music cue guidance: bundled preset `happy-beats-business-moves-vol-1-by-ende-dot-app.music-cues.md`; use beats around 3.02, 7.02, 11.02, 16.02, and 18.52s as optional reveal anchors.
- Audio-reactive treatment: subtle; let the amber inference rail and green validation glow breathe slightly, never pulse text.
- SFX posture: sparse and motion-matched: keyboard ticks, soft send, validation chime.
- Audio-coupled moments: typed input, inference handoff, schema fields resolving, validation stamp, final lockup.
- Restraint rule: no noisy hacker-terminal clichés, no waveform or equalizer visuals.

## Storyboard

### Scene 1 — Human shorthand — 3.2s
A dark terminal-like canvas. `SWYNEX / SMART TASK PARSER` sits small in the upper-left. The real README example types into a bordered prompt: `Finish the budget report by next Tuesday`. A large side label says `MESSY INPUT.`
Sequential/interaction: yes — type-on treatment, then a sharp cursor blink.
Transition: amber line sweeps right.
SFX: light key ticks.

### Scene 2 — Inference rail — 3.8s
The sentence compresses into a centered pipeline: `NATURAL LANGUAGE` → `GEMINI 2.5 FLASH` → `STRUCTURED TASK`. Amber signal travels through the middle node.
Sequential/interaction: yes — nodes resolve left to right.
Transition: signal becomes the top edge of the output panel.
SFX: soft send.

### Scene 3 — Schema resolves — 5.0s
A large JSON-like panel assembles field by field using actual model names: `task_description`, `category`, `priority`, `deadline`, `confidence`, `is_ambiguous`. Values settle in green, amber, and white.
Sequential/interaction: yes — fields stagger in.
Transition: panel lifts and the validation stamp enters.
SFX: small ticks per field, restrained.

### Scene 4 — Validated result — 4.0s
`PYDANTIC VALIDATED` stamps over the panel. A green check and `is_ambiguous: false` make the promise concrete. A thin footer calls out `schema-enforced JSON`.
Sequential/interaction: yes — stamp, then check, then footer.
Transition: clean horizontal wipe into the closing lockup.
SFX: validation chime.

### Scene 5 — Translator lockup — 4.0s
The output panel becomes a quiet hero object. Main line: `Your to-do list just got a translator.` Beneath: `SWYNEX SMART TASK PARSER` and `natural language → actionable JSON`.
Sequential/interaction: no — slow settle and hold.
SFX: none beyond music tail.

Total: 20.0s.
