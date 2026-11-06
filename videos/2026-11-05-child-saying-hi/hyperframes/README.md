# HyperFrames build: "10 Steps Felt Like 10 Kilometers"

- Voice: ElevenLabs "Vestal - Calm & Grounded Male Narrator" (American), model eleven_v4, one MP3 per chapter. Flow: https://elevenlabs.io/app/flows/h9M2fARrxLYU5jbCIhOP
- `build/lines.py`: the 100 voiceover lines. `build/line_times.py`: where each line sits inside its chapter MP3 (from ElevenLabs Scribe word timestamps).
- `build/vo_from_chapters.py`: put the 9 chapter MP3s in `build/el/` (hook, relate, head, temp, liking, reject, self, parents, close) and run it. It cuts each chapter at the real pauses, joins them into `vo.wav` (-15 LUFS) and writes `vo_timing.json`.
- `build/build.py`: writes the HyperFrames project (100 scenes, captions, sound effects) from `rig.py`, `props.py` and `scenes1-5.py`.
- `project/`: the generated project. The voiceover audio is not committed; rebuild it with the steps above.
- Render: `npx hyperframes render --quality looks -o out.mp4` inside `project/`. Length: 7:31.
