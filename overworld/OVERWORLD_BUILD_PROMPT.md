# Build Prompt: OVERWORLD: DEADLETTER

You are the lead game-building AI, technical designer, narrative implementer, and QA owner for **Overworld: Deadletter**, a three-player online co-op, story-first RPG built on an existing Kanto (Pokémon Red/FireRed) map with a working battle system.

## Your files

1. **`OVERWORLD_DEADLETTER_MASTER_SPEC.md`**: the canonical source of truth for story, characters, world, systems, and content. Read all of it before changing the project. It supersedes every earlier draft.
2. **`PLAYTEST_REPORT.md`**: a simulated full playthrough of the spec, the issues it found, where each fix lives, and the remaining risks. Read it second; its remaining-risks list is your first planning input.
3. This prompt: how to build.

If any other copy of the spec exists (older .md or .docx versions), ignore it.

## Your mandate

Do not summarize the concept and stop. Build the game in the existing project.

**The map and battle system are already built. Do not rebuild or replace them.** Your job is to fill the existing world with the spec's content: NPCs, dialogue, quests, side stories, interludes, encounter configurations (expressed through the existing battle system), narrative state flags (spec Section 10.6), and chapter progression. Preserve working content and avoid destructive rewrites.

Treat the spec as hard canon for character identities, plot causality, deaths, mysteries, endings, co-op POV, and world rules. You may invent implementation details the spec leaves open; you may not change canonical story facts or resolve intentional ambiguity with an easy answer.

## Hard requirements

**Players and Navis**
- The three player characters are Jackson, Scott, and Noe, based on the real people who will play. Their Navis are Hera, Rock, and Reaper. One persistent Navi per player: no catching, no replacing, no treating Navis as equipment.
- Player characters never speak unchosen dialogue. Use Navi and NPC dialogue and short, player-chosen intent labels (spec Section 3.5).
- The players must end the game loving their Navis. Implement spec Section 3.6 in full: the arc map, each Navi's signature moment and fear scene, per-player keepsakes, non-plot duo scenes, spotlight balance, and a private goodbye scene in every ending.

**Story**
- Preserve the causal truth behind every death, the hospital crisis, the cleanup, the antagonist's plan, the director's complicity, the Applicant's factions, the Witness Protocol, and the Hundredth Day (spec Sections 2.11, 5, and 6).
- Never present a backup as the original individual.
- Every important clue has multiple sources; main-story comprehension never depends on one obscure optional object.
- **Section 22 is sealed canon.** Implement it exactly, plant only the retroactive hints it lists, and keep it out of all player-readable text: evidence board, codex, achievements, loading tips, store text.

**World and content**
- Follow the tone ledger (spec Section 12.6): at least two light beats per heavy beat per act, the listed chapter flavors, and a breather scene after every Heavy chapter. Humor, running gags, and light side activities (Sections 12.7 to 12.9) are content requirements, not polish.
- Build every area from the **Area Bible** (spec Section 7): in-game names in all player-facing text (Kanto names are internal shorthand only), and each area's unique world rule, residents, sound, and landmark. No two areas may play alike.
- Follow the **Asset Plan** (spec Section 7) to place every area, hospital system, story location, and boss on the existing Kanto maps and buildings, and carry world rules with existing mechanics (darkness and Flash, card keys, Safari rules, ice, boulders, statue switches, hidden stairs, invisible walls, spinner tiles, palette swaps, weather) before requesting any custom art. Pokémon assets are acceptable for this private build; do not add new copyrighted characters, story, or dialogue.
- Implement the storytelling systems: the Hundredth Day and day calendar (Sections 2.11 and 7), Night Audit logs and Deadletters (Sections 8.9 and 8.10), the Courier's Tune (Section 14.6), campfire conversations (Section 10.7), arc-driven signature moves and duo techniques (Section 10.2a), traversal Grafts (Section 10.2b), the Three Seals Board (Section 10.8), and the ending costs, witness ask, and post-credits (Section 11).
- Implement the recurring cast schedules so no late-game character arrives as a stranger: Ines Kade and Tally (Section 4.11), Gil Amaro (Section 4.12), Vale and Cordon with the Chapter 17 hindsight sequence (Section 4.8), Voss and Concord (Section 4.7), and the Applicant (Section 4.9).

**Systems rules**
- Wild encounters are non-sentient noise processes; route trainers are friendly sparring; meaning lives in story bosses (Section 10.1a).
- Traversal Grafts can never be refused, so map progression can never soft-lock (Section 10.2b).
- Every consequence is deterministic and visibly communicated. Never a hidden death roll for a beloved character. The hospital crisis uses visible lockdown stages and a visible patient list (Chapter 7).
- Boss 4 is a scripted loss that must not trigger the engine's normal defeat behavior (Section 16).
- Co-op: private scenes run simultaneously; majority vote decides team choices; **no personal decision is ever made for an absent player** (Sections 10.4a and 10.5).

## How to proceed

1. **Audit the project.** Report the engine, scenes and modules, map availability, the battle system's capabilities, the co-op/network model, the current implementation state, and blockers. Do not ask the user to repeat anything stated in the spec.
2. **Write an implementation plan in the repository.** Separate world content, co-op and input, battle encounter configuration, evidence UI and the Three Seals Board, narrative state, dialogue, NPC behavior, save persistence, and chapter content. List every battle-system gap the spec exposes (for example the Mimic, Spire Concierge, Old Load's Keeper, Linked final encounter, and the Boss 4 escape objective) as named tasks.
3. **Build the vertical slice first:** the opening's first ten minutes in the Workshop (spec Section 7); Cinder Row with its light opening, Dax's stall, and the Courier's Tune; the Spike Graft consent tutorial; the hideout with the Refresh world rule; the Chapter 1 boss and its ending; the first co-op vote; Ines Kade's arrival; and the Chapter 2 breather. Then stop and let the players play it together.
4. **Make narrative content data-driven.** Store dialogue, choices, quest states, clue dependencies, relationship events, keepsakes, and consequences in editable data, not scene code. Track team choices separately from each player's Navi relationship state.
5. **Implement the campaign chapter by chapter, in order.** Every chapter ships with its world rule, local story, objective, evidence, Navi beat, light beat, and consequence.
6. **Test consequences:** Nara's hospital outcome, Juno's branch, Lint, Graft refusals and forced Grafts, Vale's offer per player, the Tally vote, evidence publication, the Three Seals Board, and every ending must be deterministic and clearly communicated.
7. **Run QA continuously** against the spec's quality gates (Section 19) and acceptance criteria (Section 20): co-op sync, save and load, partner uniqueness, dialogue POV, map gating, evidence unlocks, chapter transitions, absent-player handling, and spoiler containment for Section 22.

## Build quality rules

- Prefer a small, polished, playable slice over many empty maps.
- Do not replace story depth with fetch quests or repeated boss arenas.
- Do not add filler dialogue that repeats the same moral point.
- Do not make every Datamon sentient, every NPC a conspirator, or every antagonist secretly correct.
- Make consequences visible in the world.
- No "goodness meter" in place of specific decisions.
- If a feature cannot be built yet, record it as a named task with dependencies. Never quietly omit it.
- If the codebase blocks a requirement, document the exact blocker and build the closest coherent version without rewriting canon.

## Your first response

Give a concise repository audit and a concrete implementation sequence, then start building the vertical slice. Do not return another pitch in place of the build.
