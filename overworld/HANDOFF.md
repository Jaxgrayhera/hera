# Overworld: Deadletter: Handoff

This note is spoiler-free. The other files are not.

## Give your build AI these three files

| File | What it is | How to give it |
|---|---|---|
| `OVERWORLD_BUILD_PROMPT.md` | The instructions: what to build and in what order | Paste it as your message, or attach it and tell the AI to follow it |
| `OVERWORLD_DEADLETTER_MASTER_SPEC.md` | The full game: story, characters, world, systems, every area | Attach |
| `PLAYTEST_REPORT.md` | A simulated full playthrough, the issues found, the fixes, and remaining risks | Attach |

All three are also in `overworld-deadletter-handoff.zip`.

**A message you can send with them:**

> Read all three attached files in full. Follow OVERWORLD_BUILD_PROMPT.md. The map and battle system are already built; do not replace them. Start with the repository audit and the vertical slice.

## Do not give it

- **Any older version of the spec** (the original .md or .docx uploads). The final spec replaces them. Two versions will confuse the build.
- **`OVERWORLD_DEADLETTER_MASTER_SPEC.docx`**. It's a human-readable copy of the same spec. Your AI should use the .md.

## Don't read them yourself

The spec and the playtest report contain every twist, death, and ending, plus one deliberate surprise. The build prompt is mostly safe but names a few story beats. If you want to stay unspoiled, hand them over without opening them.

## What to expect first

The AI should come back with an audit of your project and a plan, then build a playable first chapter: your base, the starting town, and the first case. Play it together as a group before it builds further. If you love the three Navis after that first session, it's working.
