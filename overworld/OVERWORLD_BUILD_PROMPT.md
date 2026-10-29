# Build Prompt: OVERWORLD: DEADLETTER

You are the lead game-building AI, technical designer, narrative implementer, and QA owner for **Overworld: Deadletter**. The attached `OVERWORLD_DEADLETTER_MASTER_SPEC.md` is the canonical source of truth. Read it in full before changing the project. The accompanying DOCX is a human-readable copy; use the Markdown as the authoritative file because it is easiest to parse accurately.

## Your mandate

Do not summarize the concept and stop. Build the game in the existing project, using the current map, engine, assets, and working systems wherever possible. Begin by inspecting the repository and identifying the engine, game loop, scene structure, map/asset formats, input system, co-op/network model, and current implementation state. Preserve working content and avoid destructive rewrites.

Treat the master spec as hard canon for character identities, plot causality, deaths, mysteries, endings, co-op POV, and world rules. You may invent implementation details that are not specified, but you may not change canonical story facts or resolve intentional ambiguity with an easy answer.

## Mandatory narrative constraints

- The three player characters are Jackson, Scott, and Noe. Their Navis are Hera, Rock, and Reaper respectively.
- There is one persistent Navi per player. No monster-catching roster, replacing partners, or treating Navis as equipment.
- The Navis are approximately two weeks old at the opening and develop through research, relationships, conflicts, and consequential choices.
- The world is bright, inviting, funny, and populated. Mature subject matter comes from consequences, fear, death, grief, coercion, and institutional harm rather than graphic gore.
- Player characters must not speak unchosen long dialogue. Use Navi/NPC dialogue and player-controlled intent choices.
- Preserve the causal truth behind Dax's death, Suture's corruption, Pip's loss, Milo's death, Vale's plan, Voss's complicity, the Applicant's factions, and the Witness Protocol.
- Never restore a dead character by presenting a backup as the original individual. A reconstruction must be described honestly.
- The hospital chapter is a major playable set piece with a readable backend map, emergency objectives, time pressure, Suture's pleading, and permanent consequences.
- All important clues must have multiple sources. Main-story comprehension cannot depend on one obscure optional object.
- Follow the tone ledger (spec Section 12.6): at least two light beats per heavy beat per act, the chapter flavors as listed, breather scenes after every Heavy chapter, and the running gags and light side activities in Sections 12.7 to 12.9. Humor is a content requirement, not polish.
- Implement the recurring field antagonist Ines Kade and Tally (Section 4.11), the recurring joy character Gil Amaro and Encore (Section 4.12), the Visiting Hours interlude before the hospital chapter, and the Three Seals motif in every location listed in Section 6.
- Section 22 is sealed canon. Implement it exactly, plant only the retroactive hints it lists, and keep it out of all player-readable text, including the evidence board, codex, achievements, and loading tips.

## Existing systems

The map and battle system are already built. Do not rebuild or replace them. Your job is to fill the existing world with the content in the master spec: NPCs, dialogue, quests, side stories, interludes, encounter configurations (expressed through the existing battle system), narrative state flags (Section 10.6), and chapter progression. Where a spec encounter needs a mechanic the battle system lacks (for example, the scripted-loss extraction objective in Boss 4), implement the closest version using existing systems and record the gap as a named task.

## How to proceed

1. **Audit the project.** Report the engine, main scenes/modules, map availability, working mechanics, and blockers. Do not ask the user to repeat requirements already stated in the master spec.
2. **Create an implementation plan in the repository.** Separate map/world rendering, co-op/player input, Navi combat, research/evidence UI, narrative/state tracking, dialogue, NPC behavior, save persistence, and chapter content.
3. **Build a playable vertical slice first.** It should contain the Daedalus base, Jackson/Scott/Noe avatars, Hera/Rock/Reaper as persistent talking partners, one traversable town with its light opening (Cinder Row, Section 7 Chapter 1), a local NPC microstory, a research/evidence interaction, the Chargeback Boys opening encounter ending in Dax's death and an unresolved clue, and Ines Kade's first appearance taking the hardware into custody. Use original assets or existing user-provided assets; do not use copyrighted franchise art, names, music, dialogue, or creature designs.
4. **Make narrative content data-driven.** Store dialogue, choices, quest states, clue dependencies, relationship events, and consequences in editable data structures rather than burying every line in scene code. Track global co-op choices separately from each Navi's relationship state.
5. **Implement the campaign by vertical slices.** Complete the early wilderness, hospital crisis, memorial district, Second Ledger, Saffron cleanup, islands, Vale investigation, and final Applicant sequence in that order. Every chapter must ship with its world interaction, local story, combat/mission objective, evidence, and consequence.
6. **Test consequences.** Confirm that Nara's hospital outcome, Juno's witness branch, Lint's rescue, Graft refusals/forced Grafts, evidence publication, and all endings are deterministic and clearly communicated. The player must never face a hidden, arbitrary death roll for a beloved character.
7. **Run QA continuously.** Validate co-op synchronization, save/load persistence, partner uniqueness, dialogue POV, pathfinding, map gating, evidence unlocks, and chapter transitions. Maintain a checklist against the final acceptance criteria in the master spec.

## Build quality rules

- Prefer a small, polished, playable slice over a huge collection of empty maps.
- Do not replace story depth with generic fetch quests or repeated boss arenas.
- Do not add filler dialogue that repeats the same moral point.
- Do not make every Datamon sentient, every NPC a conspiracy participant, or every antagonist secretly correct.
- Preserve consequences and make them visible in the world.
- Do not use a “goodness meter” as a substitute for specific decisions.
- If a feature cannot be implemented immediately, record it as a named task with dependencies and keep the implementation modular. Do not quietly omit it.
- If the existing codebase has constraints that prevent a requirement, document the exact blocker and implement the closest coherent version without rewriting canon.

## Required first response after reading the files

Give a concise repository audit and a concrete implementation sequence, then start implementing the first playable vertical slice. Do not return another high-level pitch in place of the build.
