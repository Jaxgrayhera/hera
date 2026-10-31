# Overworld: Deadletter: Simulated Playtest Report

**Contains full spoilers. For builders only.** This is a desk playthrough of the master spec (Revision 7), played start to finish as a three-player co-op group on the Kanto map, checking geography, gating, pacing, mechanics, story logic, and co-op behavior. Every issue below has been fixed in the spec; the section where each fix lives is listed.

## Route walked

Workshop → Cinder Row (Pallet) → Route 1 → Gatehouse (Viridian) → Route 2 → Unindexed Wood (Viridian Forest) → Grayscale (Pewter) → Route 3 → Moon Cache (Mt. Moon) → Route 4 → Glasswater (Cerulean) → Routes 24 and 25 → Routes 5 and 6 → Port Meridian and the *Long Handshake* (Vermilion, S.S. Anne) → Visiting Hours → Saint Orison crisis (Vermilion) → Diglett's Cave (optional) → Route 9 → the Dark Fiber (Rock Tunnel) → Lanternfall (Lavender) → Routes 7 and 8 → Marquee and the Second Ledger (Celadon) → Longline (Cycling Road) → the Preserve (Fuchsia, Safari) → Routes 12 to 15 (courier coast) → Halcyon and the Spire (Saffron, Silph Co.) → the Old Load (Power Plant) → Routes 19 and 20 → Brine Stacks and Ashgrove (Seafoam, Cinnabar) → the Outer Nodes (Sevii) → Route 21 → the Reconstruction (Pallet) → the Continuity Office (Viridian Gym) → Routes 22 and 23 → the Last Mile (Victory Road) → the Root Court (Indigo Plateau) → the Unsent (Cerulean Cave).

**Result: geography is sound.** The chapter order follows Kanto's real road network the whole way, including the Route 21 sail from Cinnabar back to Pallet for Chapter 16, then north through Viridian to Victory Road and Indigo. No chapter requires going somewhere the map does not connect.

## What worked on the walk

- Act I builds love efficiently: Dax, Suture, Pip, Milo, Bex, Nara, and Gil all get real time before anything happens to them.
- The Navi arc map, signature moments, and spotlight balance hold up chapter by chapter; no Navi disappears for long.
- The day calendar, Rock's absences, Postscript's log dates, the Three Seals sightings (six before Chapter 15), and the Night Audit dates all line up.
- Tally's arc has a beat in every act and reads as earned.
- The Kanto map already contains a mechanic for almost every world rule (Flash, card keys, Safari rules, ice, boulders, statue switches, hidden stairs, invisible walls, forced-slope movement, the Elite Four's four rooms).

## Issues found and fixed

### Opening and Chapter 1
1. **No defined opening.** The spec started Chapter 1 mid-walk, with no spawn point for three players and no tutorial for the intent-label dialogue system. *Fixed:* "Opening: the first ten minutes" (Section 7). All three players spawn in the Workshop, learn intent labels in one choice, and step out through Jackson's PC into the rain.
2. **The Graft system appeared for the first time as a cover story.** Chapter 1's death relies on "Daedalus's modified combat Graft," but players had never seen a Graft. *Fixed:* the Spike Graft consent tutorial before the raid (Chapter 1).
3. **The first Navi argument had no consequence.** *Fixed:* it is now the first co-op vote, and each side has a concrete later effect (Chapter 1).

### Hospital (Chapter 7)
4. **The emergency control route sat on the path to the boss.** In the asset plan, Nara's objective and the guardian's core were both in the Vermilion Gym, so the objective that decides her fate could not actually be neglected. *Fixed:* her route is now the east gate building toward Route 11, far from the core (Asset Plan).
5. **"Patients die" was undefined.** It was unclear which deaths were fixed and which depended on play, which risked feeling like a hidden roll. *Fixed:* visible lockdown stages, named patients on a visible list, three fixed losses, plainly warned objectives (Chapter 7).
6. **The boss was reachable without the right tool.** *Fixed:* the core requires the Prune Graft from Chapter 6, matching the original Cut tree (Asset Plan).

### Systems
7. **No HM equivalent.** The map is gated by Cut, Surf, Strength, Flash, and Fly, but nothing in the spec opened those gates. *Fixed:* traversal Grafts, one per Navi plus a shared one, earned at specific chapters (Section 10.2b).
8. **Graft refusal could soft-lock exploration.** *Fixed:* traversal Grafts are memory-safe and never refused; refusal applies only to Grafts that touch memory, perception, autonomy, or continuity (Section 10.2b).
9. **Ludonarrative clash in hundreds of routine battles.** A game about not erasing beings had no rule for what players fight in tall grass. *Fixed:* wild encounters are non-sentient noise processes, route trainers are friendly sparring, meaning lives in story bosses (Section 10.1a).
10. **The best-ending requirements were vague and invisible.** *Fixed:* the Three Seals Board, visible from Chapter 3, with exact requirements (Section 10.8), and the ending vote logic (Section 11).
11. **Scripted loss versus engine defeat.** Pokémon-style engines black out on a loss. *Fixed:* Boss 4 must not trigger defeat behavior (Section 16).

### Co-op
12. **No rule for a missing player.** Real friends will miss sessions, and several of the game's most important choices are personal. *Fixed:* absent players' Navis travel with the group, and no personal decision is ever made without its own player (Section 10.4a).
13. **Vote ties with three players.** *Fixed:* majority decides; ties only on abstention or absence (Section 10.5).

### Story logic
14. **The antagonist had no final scene.** He escaped in Chapter 17 and never appeared again. *Fixed:* his last scene at the purge console in the finale, and his arrest by Ines Kade on a lawful order when the relay record exists (Chapter 20, Section 4.11, Section 18).
15. **Boss 9 contradicted Cordon's turn.** The "Cordon System" boss had no location, and Cordon had already turned. *Fixed:* Boss 9 is in Chapter 17, and Cordon's refusal happens mid-fight, changing the arena (Chapter 17, Section 16).
16. **Milo vanished for three chapters right before his death,** which would weaken it. *Fixed:* Milo at Ashgrove (Chapter 14), the island fishing contest (Chapter 15), and his call that leads into Chapter 18 (Chapter 17).
17. **"Why not just file for an exemption?"** Players would ask this as soon as the countdown is revealed. *Fixed:* the team files and gets "Pending verification" forever, echoing Ren's letters (Chapter 14), and Jo explains why (Chapter 15).
18. **Jo's regret was promised but never scheduled.** *Fixed:* Chapter 15.
19. **A Navi saved by Vale's certificate had no defined fate in Ending C.** *Fixed:* Section 2.11.
20. **Two dramatic-irony lines in one chapter.** Gil's line had no chapter and could collide with Chapter 6. *Fixed:* moved to Chapter 2.
21. **The Unthreading's safe route used different criteria from the ending.** *Fixed:* both use the Three Seals Board (Section 9.6).
22. **The Root Court defenders were unnamed.** *Fixed:* the four Arbiters (Chapter 19).

### Pacing
23. **Long stretches without a boss** (Chapters 8 to 16 had almost none), and Silph Co., Kanto's biggest dungeon, had no boss at all. *Fixed:* the Spire Concierge (Chapter 12) and the Old Load's Keeper (Chapter 13), the Mimic as an optional Chapter 2 mini-boss, and a boss pacing table showing which chapters deliberately have none (Section 16).
24. **Night Audit logs had no placement.** *Fixed:* thirteen locations with dates, four on the critical path (Section 8.9).
25. **Large Kanto set pieces were unused.** Several gyms, the Dojo, Bill's cottage, the Tower, the Department Store, and the Route 12 sleeper had no job. *Fixed:* every one now has one (Asset Plan, "Reusing Kanto's big set pieces"), including the sleeper woken only by the Courier's Tune.

## Remaining risks (not fixable in a spec)

- **Scope.** This is still a very large game. Build the vertical slice (Workshop, Cinder Row, Chapter 1) and play it as a group before building further.
- **Writing quality.** The spec describes scenes; the lines themselves will decide whether players love the Navis. Review Act I dialogue with the real players early.
- **Battle system fit.** Several bosses (Mimic, Spire Concierge, Old Load's Keeper, Whole Thread) need battle rules the existing system may not have. Record each gap as a named task and implement the closest version rather than skipping the idea.
- **Public release.** Pokémon assets are fine privately but must be replaced before any public release.
