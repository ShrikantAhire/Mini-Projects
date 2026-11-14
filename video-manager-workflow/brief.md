# Brief: "How 4 AI agents made this video"

Owner: Manager (Claude). Workers: worker-1, worker-2, worker-3.

## Goal
A 30-second vertical video that shows, step by step, the manager-worker workflow used to make it. Audience: LinkedIn and YouTube Shorts viewers who use Claude for work. They should understand the setup well enough to copy it.

## Format (non-negotiable)
- 1080x1920, 30 fps, H.264 (yuv420p), no audio track in scene clips.
- 12 scenes, each exactly 2.5 s (75 frames). Total 30.0 s.
- One file per scene: `clips/scene_NN.mp4` (NN = 01..12).
- Render only with the shared toolkit `assets/style.py`. Do not edit it. Scene scripts go in `assets/scenes/scene_NN.py`.

## Look
- Background `BG` (near black), text `INK` (off-white), accent `ACCENT` (warm orange), secondary `MUTED`. Use the toolkit constants only.
- Font: Inter (toolkit `font()`), monospace for file names and JSON (`mono()`).
- Every scene calls `chrome(img, scene_no, t)`: it draws the scene counter and the 30-second progress bar so the cut feels continuous.
- Headline: max 8 words, `font(96, "bold")` or smaller, left-aligned at `MARGIN`, top third of the frame.
- Minimum text size 30 px for anything a viewer should read (added after batch 1 review). Pass `accent_words` without punctuation ("Pass", not "Pass:"), because the toolkit strips punctuation before matching.
- One supporting visual per scene (file tree, cards, JSON, icons). Keep it in the middle third. Nothing inside 140 px of the bottom (platform UI).
- Motion: elements ease in during the first 0.6 s, hold still for at least 1.2 s so they can be read. No flashing, no spinning.

## Writing rules (on-screen text)
- Plain business English. One idea per scene.
- No em dashes, no emojis, no buzzwords (game-changer, unlock, supercharge, harness, revolutionary).
- No tee-ups ("here's the kicker", "the secret is"). State the point.

## Storyboard

| # | Worker | Headline (exact) | Visual |
|---|--------|------------------|--------|
| 01 | worker-1 | This video was made by 4 AI agents | 4 agent circles: 1 large "Manager" on top, 3 small "Worker 1/2/3" below, connected by lines |
| 02 | worker-1 | Step 1: the manager writes a brief | A document card titled `brief.md` with 4-5 lines filling in like typing (grey bars are fine) |
| 03 | worker-1 | Then it sets up a shared folder | File tree in mono: `project/`, `brief.md`, `status/`, `assets/`, `clips/`, rows appearing one by one |
| 04 | worker-1 | 12 scenes, split across 3 workers | Three columns: "Worker 1: scenes 1-4", "Worker 2: scenes 5-8", "Worker 3: scenes 9-12" |
| 05 | worker-2 | Each worker builds in batches of 2 | A row of 4 scene tiles grouped into 2 brackets labelled "Batch A" and "Batch B" |
| 06 | worker-2 | After every scene, it logs its status | JSON card in mono: `{"worker": 2, "scene": 6, "state": "done"}` |
| 07 | worker-2 | After each batch, it stops and waits | Worker circle with a pause symbol and the label "Waiting for review" |
| 08 | worker-2 | The manager checks the batch against the brief | Two cards side by side: "Brief" and "Batch", with a checklist ticking 3 items: Format, Look, Words |
| 09 | worker-3 | Pass: next batch starts. Fail: redo it. | Two outcome cards: green-ish check "Approved" and accent X "Redo" |
| 10 | worker-3 | Mistakes get caught after 2 scenes, not 12 | A bar of 12 tiles; first 2 highlighted with a check, remaining 10 dimmed |
| 11 | worker-3 | The manager stitches the final cut | 12 small tiles sliding together into one long bar labelled "final.mp4  0:30" |
| 12 | worker-3 | Try this setup in Claude Code | Subline: "Follow for practical Claude workflows". Accent underline under the headline |

## Process
1. Each worker gets a scene range split into batches of 2 scenes.
2. After every scene: render the clip, verify it with ffprobe (75 frames, 1080x1920), then update `status/worker-N.json`.
3. After each batch: stop and report. Do not start the next batch until the manager approves.
4. Manager reviews each batch (contact sheet + ffprobe) against this brief, then approves or sends fixes.
5. Manager stitches `clips/` into `final.mp4` and adds the music bed.

## Status file schema (`status/worker-N.json`)
```json
{
  "worker": 1,
  "scenes": [1, 2, 3, 4],
  "batches": [[1, 2], [3, 4]],
  "current_batch": 0,
  "state": "working | awaiting_review | approved | done",
  "scene_status": {"1": "pending | rendering | done | redo"},
  "notes": "free text, one line per update",
  "updated_at": "ISO 8601 timestamp"
}
```
