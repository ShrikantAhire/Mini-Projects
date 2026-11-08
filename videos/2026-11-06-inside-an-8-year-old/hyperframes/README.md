# HyperFrames build: Episode 1 "Am I Good Enough?"

- Voice: Kokoro `am_fenrir`, made by `../build/ep1_vo.py` into `../voiceover/ep1-voiceover.mp3`, with sentence timings in `../voiceover/ep1-vo-timing.json`.
- `build/rig.py`: stickman rig. Leo (amber T-shirt, hair tuft, missing tooth, chest feelings meter), girls with hair and dresses, kids with caps.
- `build/props.py`, `build/frame.py`: props, backgrounds and the scene/tween helper. `build/epc.py`: the cast (Leo, Mason, Maya, Ava, Ethan, Noah, Ms. Carter, Mom, Dad) and the big meter.
- `build/scenes_a.py` (lines 1-37) and `build/scenes_b.py` (lines 38-82): one scene per voiceover line, keyed to the line's real start time.
- `build/build_ep1.py`: writes the HyperFrames project (8 chapter compositions, captions, sound effects, index). Paths at the top point at the cloud session's scratchpad; change PROJ and SFXDIR to rebuild elsewhere.
- Render: `npx hyperframes render --quality looks -o out.mp4` inside the project. Length: 8:02.
