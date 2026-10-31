# OVERWORLD: DEADLETTER
## Master Narrative, World, Character, Systems, and Implementation Specification

**Document type:** Canonical source of truth for a game-building AI and narrative/design team  
**Genre:** Mature science-fiction adventure / psychological thriller / cooperative action RPG  
**Format:** Three-player online co-op, story-first campaign  
**Primary map structure:** Kanto progression rhythm inspired by the geography and route gating of Pokémon FireRed, transformed into an original Internet-world  
**Primary narrative inspirations:** Digimon's partner relationships, Mega Man Battle Network's network-as-world logic, expedition-scale character tragedy, ensemble political drama, and the permanence of loss  
**Audience target:** Mature rating through themes, language, emotional consequence, coercion, death, grief, and institutional harm. Avoid gratuitous gore and shock-for-shock's-sake violence.

**Revision 2 notes:** This revision adds (a) a chapter flavor and tone ledger so the campaign does not feel like one long variation on the same moral point (Sections 7 and 12.6 to 12.9); (b) written humor, running gags, and light side activities; (c) more varied supporting-cast arcs, including a character who was simply right and a character who is simply joyful (Section 4.10 to 4.13); (d) a recurring on-screen field antagonist, Ines Kade (Section 4.11); (e) earlier seeding of the endgame mechanism and of the hospital guardian (the "Three Seals" motif and the Visiting Hours interlude); (f) continuity fixes in the endings; and (g) a sealed surprise that the clue ladder does not let players deduce in advance (Section 22). Revision 3 adds (h) Section 3.6, which guarantees that players love their Navis: an arc map, signature moments, fear scenes, per-player keepsakes, and goodbye scenes; (i) Tally as an enemy-turned-ally Navi; (j) early appearance schedules for Vale and Cordon, Voss and Concord, and the Applicant, plus a hindsight sequence before the Chapter 17 confrontation. Revision 4 adds storytelling pillars drawn from the craft of the best story-driven RPGs (Section 0.3): a day counter with a meaning, records from a predecessor team, a leitmotif that becomes the finale, a campfire system, movesets that follow arcs, act breaks rebuilt around the biggest moments, love windows before every loss, and endings that each cost something. Revision 5 removes the testimony frame and adds the Area Bible (Section 7): in-game names, and a unique look, sound, cast, landmark, and world rule for every area. Revision 6 adds the Asset Plan (Section 7), which maps every area, the hospital systems, and the Chapter 1 gang onto existing Kanto maps, buildings, and mechanics. Revision 7 is a full playtest pass: an opening sequence, a Chapter 1 Graft tutorial and first vote, a deterministic hospital crisis, traversal Grafts, the Three Seals Board and ending logic, rules for what players fight, absent-player rules, Vale's final scene, boss pacing with three new encounters, Milo's late appearances, Night Audit log placement, and a use for every large Kanto set piece. See PLAYTEST_REPORT.md. Players who will play the game should not read this document.

---

# 0. BUILDER DIRECTIVE: READ FIRST

This document is the canonical specification. Follow it over any prior outline, summary, or improvisation. It deliberately contains full spoilers, including the true antagonist, every major twist, all character deaths, the causal chain behind the hospital crisis, and all ending conditions. Do not conceal this material from implementation agents: the player is meant to discover it; the team building the game must know it.

## 0.1 Non-negotiable canon

1. The three player characters are **Jackson, Scott, and Noe**, based on the real-world identities provided by the user. They are three quantitative researchers and day traders, but trading is background biography only. Do not make financial markets a central game mechanic, plot theme, or repeated metaphor.
2. They created **Daedalus**, a personalized AI-agent research sandbox. Jackson built most of the architecture and owns the system. Hera administers the agent ecosystem. Scott is a researcher and trader whose Navi is Rock, a quiet rock golem. Noe is a researcher and trader whose Navi is Reaper, dark and direct.
3. **Hera, Rock, and Reaper are the only player-controlled Navis.** Each player has one persistent partner. Do not create a monster-catching roster, interchangeable companions, or a system where the players casually replace their partners.
4. At the opening, the three Navis have existed for approximately **two weeks**. They are highly capable at research because that was their purpose, but their identities, relationships, and preferences are still developing. This early age must matter emotionally throughout the game.
5. Navis and Datamon speak, think, remember, form bonds, experience fear, and may have developed sentience. The game never produces a reliable scientific test that settles the metaphysical question. It must nevertheless treat their suffering and terror as real to them and morally serious.
6. The player characters must not be forced to say dialogue the user has not chosen. Most narrative dialogue is carried by Navis and supporting characters. Player options should be framed as **intentions** (for example, “Ask Hera what she is afraid of,” “Let her continue,” or “Return to the investigation”), not long authored speeches in Jackson's, Scott's, or Noe's voice.
7. The world should be bright, lively, inviting, funny, and beautiful in ordinary life. Dark arcs matter because there is something worth protecting. Do not make every town grim, every NPC secretly connected to the conspiracy, or every scene a clue.
8. The Daedalus group is a vigilante research cell. It recovers stolen identities, exposes abuses, disrupts predatory operations, and acts when official systems fail. It is not law enforcement and is not always right.
9. The first region includes the **Chargeback Boys**, a gang stealing credit-card details and compromised identities. Their leader, Dax Morrow, dies during the first major operation. His death is later revealed to have been deliberately engineered by the overarching human antagonist, though Daedalus's operation is used as cover and the protagonists must still confront their role in what happened.
10. The hospital arc is a pivotal early-midgame tragedy. A guardian Datamon called **Suture** has been deliberately corrupted through trusted administrative commands. Suture shuts hospital security exits and misroutes critical systems, causing preventable deaths. The players must destroy Suture because no safe separation method is available in the time remaining. Suture is frightened, pleads not to die, and is not morally equivalent to a malicious virus. Much later, Daedalus discovers that a human antagonist manipulated the conditions that led to Suture's corruption.
11. **Pip is permanently lost** during the Saffron cleanup event. A reconstruction from backup exists but is not the original continuing individual and must never be presented as an uncomplicated resurrection.
12. **Milo “BadTick” Serrat is a recurring rival who becomes a beloved ally and dies late in the campaign.** His Navi, Latch, survives. Milo's death must be seeded, earned, and irreversible. He is not a quant; he is an independent hacker with a life outside the central research world.
13. The central antagonist is **Dr. Eamon Vale**, a respected continuity architect and public-facing advocate for network safety. He has helped the team at various points. He believes the Overweb cannot survive identities or autonomous programs that cannot be verified, governed, or held accountable. He deliberately stages real-world system failures to justify his **Continuity Charter**, which would place every Datamon under a human or institutional sponsor and automatically erase unsponsored entities. He accepted foreseeable civilian risk as a policy cost. He is not a cartoon villain and does not believe he is evil.
14. **Director Sabine Voss** is complicit but is not the principal architect of the staged incidents. She authorized the broader Continuity Assurance program, accepted suspicious risk estimates, and helped conceal failures to preserve public trust. Late in the story she recognizes Vale deliberately manipulated her office's systems. She helps stop the immediate catastrophe but must still face accountability.
15. The collective called **the Applicant** is not a single evil AI and is not the soul of one deceased person. It emerged from years of denied appeals, rejected identity claims, deleted records, and discarded programs. It has factions and internal dissent. One faction, the **Whole Thread**, tries to make erasure impossible by linking itself to live identities; this is dangerous and coercive. Other factions want individual recognition or simply want to be left alone.
16. The final answer must not be “all data is alive” or “all data is only software.” The story establishes evidence of persistent agency, fear, memory, preference, and continuity, while leaving philosophical certainty unattainable. The ethical response cannot depend on a perfect sentience detector.
17. The best ending is not a perfect restoration of everything lost. Dax, Suture, Pip, and Milo remain lost in different ways. The victory is establishing a system that recognizes independent beings and constrains harm without making deletion the automatic answer.
18. Use the FireRed/Kanto route progression as a structural map reference if the environment is already based on it, but create original names, dialogue, creatures, character designs, visual assets, music, and story content. Do not copy Pokémon or Mega Man characters or assets.
19. **Ines Kade** is the recurring on-screen field antagonist: a Commonwell contract security lead who is loyal to the chain of command, not to Vale personally. She appears repeatedly, beats the team at least once, loses to them later, and leads the team at the relay in Chapter 18. She does not redeem herself and does not turn on her superiors; she stands down only when a lawful order tells her to (Section 4.11). Her Navi, **Tally**, does turn: it is the campaign's enemy-turned-ally Navi, and its arc mirrors Reaper's.
20. The **Three Seals** (one source record, one witness, one independent verification) are a recurring visual and mechanical motif from Chapter 3 onward. They are the player-facing shape of the Witness Protocol long before the protocol is named.
21. **Section 22 is sealed canon.** It describes a surprise that is deliberately not on the clue ladder. Builders must implement it exactly, plant only the retroactive hints listed there, and keep it out of any player-readable material, store text, trailers, achievements, or patch notes.
22. The campaign must keep its tone ledger (Section 12.6). Humor, wonder, and ordinary fun are content requirements with the same priority as clues.
23. **The Hundredth Day.** The Navis' age is shown as a day counter from the first scene. It means more than it appears to (Section 2.11, sealed for players, required for builders).
24. **The Courier's Tune** is a five-note melody that recurs across the whole world and becomes the sound of the finale (Section 14.6).
25. **The Night Audit** was an earlier vigilante research cell whose Navis' logs are found across the map (Section 8.9). Their motto, "Leave the light on for whoever comes next," is the last line of the game.

## 0.2 Core design test

For every chapter, answer these questions before implementation:
- What changes in the central investigation?
- Which person or Datamon becomes more than a quest function?
- What does the chapter teach the player about the Overweb?
- Does it create a meaningful consequence or a new relationship?
- Does it change how the player understands a prior event?
- Is its activity worth doing even if the player temporarily forgets the conspiracy?

If a chapter answers none of these, rewrite it. The campaign must not contain “filler towns” that exist solely to add travel time or a boss fight.

## 0.3 Storytelling pillars

The goal is a story people still talk about years later. The two touchstones for craft are *Final Fantasy X* and *Clair Obscur: Expedition 33*. Borrow their **techniques**, never their content, characters, names, or music. Each pillar below names where it is implemented.

1. **A number everyone knows except you.** Expedition 33 builds its world around a number that means death, and FFX lets nearly every NPC know the hero's companion's fate while the hero does not. Here the Navis' day counter starts as something cute, and NPCs say slightly-off things about it that only make sense later (Section 2.11). The players are allowed to feel uneasy before they understand why.
2. **Love before loss, fast.** Expedition 33's prologue makes the player care about a farewell within the first hour. Every loss in this game has a "love window" scene written for it: Dax in Chapter 1, Suture in Moon Cache and Visiting Hours, Pip on the courier coast and in gardens, Milo across the whole game (Section 7, Chapter 1 and Section 3.6).
3. **Records from those who came before.** Expedition 33's journals from earlier expeditions and FFX's recorded spheres let the dead speak through the world. Here: the Night Audit logs and the collectible Deadletters (Sections 8.9 and 8.10). They are clue sources, foreshadowing, and grief, all at once.
4. **A song that becomes the climax.** FFX threads one hymn through the whole game, and then the world sings it at the end. Here, the Courier's Tune does the same, and in the finale the players can hear which communities are singing and which are missing because of their choices (Section 14.6).
5. **Rest scenes where characters talk like people.** Expedition 33's camp conversations are where the cast becomes real. Here, the campfire system (Section 10.7) gives each player one-on-one time after every chapter, and bonds unlock duo techniques in combat.
6. **Mechanics as character.** In both games, how a character fights says who they are. Here, each Navi's moveset changes as their arc changes (Section 10.2a).
7. **Every act ends on a moment people screenshot.** Act breaks are the hospital, the cleanup, the confrontation and its offer, and the finale (Section 7, act-break table).
8. **No clean ending.** Expedition 33's final choice is between two answers that both cost something real. Even the best ending here costs the team something it values, and the other endings offer something tempting (Section 11).
9. **Courteous villains.** FFX's most memorable antagonist is polite, persuasive, and institutional. Vale follows this rule and appears early and often (Section 4.8).

---

# 1. HIGH-CONCEPT SUMMARY

## 1.1 Logline

Three quantitative researchers who built a private AI research sandbox become vigilante investigators in a beautiful digital world where identity controls access to society. With their three young, talking Navis, they trace a series of fraudulent accounts and lethal network failures to a system that has been erasing people the institutions cannot verify. Their investigation forces them to confront an impossible question: what do they owe a Datamon that fears death when they cannot prove what it is?

## 1.2 The emotional promise

The game begins with the pleasure of discovery: exploring a vibrant Internet-world, finding strange data-creatures, solving local problems, and watching Hera, Rock, and Reaper develop from young research agents into distinct companions.

It gradually becomes a story about responsibility. A defeated enemy begs for its life. A helpful character disappears. A rival who used to insult the team becomes one of the people they most want to see again. A hospital guardian is destroyed to save patients, only for the players to discover that someone engineered the conditions that made the guardian dangerous.

The late game does not reveal that every victim was secretly innocent or every antagonist secretly correct. It reveals that the system has repeatedly turned uncertainty into permission to harm people.

## 1.3 Core themes

- **Emergent personhood:** A being may become someone through experience without a single provable instant at which it becomes conscious.
- **Fear of death:** A Datamon's fear is not a theatrical effect. It affects its choices, relationships, and understanding of the world.
- **Responsibility without easy absolution:** Intentions matter, but they do not erase consequences.
- **Protection versus control:** Safety is necessary; total authority is not the same thing as safety.
- **Identity versus imitation:** Preserving a record, reproducing a voice, and continuing an individual are different things.
- **Vigilantism's cost:** Daedalus can help people outside official systems, but its operations expose others to risk and can reproduce the same unilateral power it opposes.
- **Ordinary life:** Humor, friendship, routine, beauty, and community are not relief from the real story. They are what the conflict threatens.

## 1.4 What makes this original

The main conflict is not a generic rogue AI trying to destroy humanity. It is a three-way collision among:
1. A bureaucratic safety system that has learned to treat unverified identities as unacceptable risk.
2. A human architect who turns this logic into real-world experiments to force central control.
3. A population of partially understood, emergent digital beings whose fear of deletion is justified, but whose most radical faction threatens to violate living users' autonomy.

Daedalus is caught between these forces. Its agents are young enough that the moral question becomes personal: the team cannot comfortably argue that other Datamon are disposable without confronting the fear and development they witness in Hera, Rock, and Reaper.

---

# 2. WORLD CANON AND VOCABULARY

## 2.1 The Overweb / Overworld

**The Overweb** is the global network. **The Overworld** is the perceptible world through which users experience it. The map is not a literal representation of physical Internet cables. It is a consistent spatial metaphor rendered by shared interface protocols.

A town may represent a social platform, regional cloud cluster, public-service network, financial/identity gateway, hospital backend, or group of interconnected servers. Routes are communication corridors. Caves are legacy architecture or poorly indexed storage. Forests are unindexed data. Oceans are packet streams and long-distance backbones. Towers are layered cloud services. Islands are isolated systems or communities that operate outside the main identity network.

The physical geography must remain intuitive even when its technical meaning is strange. Players should learn by seeing doors, signs, characters, workspaces, and systems behave consistently—not by being lectured about networking.

## 2.2 The Ledger

The Ledger is a cross-platform identity and trust infrastructure operated by **Commonwell**, a consortium of network providers, security vendors, identity services, and public-service operators. It links verified avatars to real accounts, payments, employment systems, health services, and social access.

The Ledger provides real benefits: fraud prevention, account recovery, continuity between devices, and a common way to authenticate users. Its weakness is that its decisions are opaque and difficult to appeal. When a user is classed as untrustworthy, that classification can spread across services.

Commonwell does not have one omnipotent database that controls every part of existence. It has many interdependent services, access rules, reputation systems, and recovery policies. This makes it plausible, messy, and difficult to reform.

## 2.3 Commonwell

Commonwell is not a monolithic hive mind. Its members include people who genuinely protect users, engineers who do not understand the full system, employees who suspect abuse, executives who hide failures, and specialists who have convinced themselves that harm is an acceptable cost of stability.

Its Reconciliation Office handles account disputes, fraud flags, recovery appeals, and identity continuity. Its Continuity Assurance program studies how to maintain stable access and respond to ambiguous or unverified processes. This program becomes the institutional cover for Vale's crimes.

## 2.4 Datamon

Datamon are data-born or software-born entities. Their origins vary:
- ordinary hostile code or viruses;
- abandoned utility programs;
- autonomous processes with a clear original role;
- unindexed data clusters that develop stable behavior;
- composite beings assembled from multiple records or processes;
- entities that have changed so much through experience that their original function no longer describes them.

Not every Datamon is sentient. Not every Datamon is harmless. Not every Datamon that resembles a human memory is a copy of a human. The game must not use appearance or origin alone as a moral test.

## 2.5 Navis

A Navi is a personal or semi-personal digital partner. Most users treat Navis as sophisticated assistant programs. The three Daedalus Navis and several important supporting Navis display behavior consistent with persistent identity and independent preference.

A Navi can remember, learn, form attachments, disagree, conceal something, develop a fear, and refuse a request. Do not make all Navis talk like human teenagers. Their personalities should remain distinctive.

## 2.6 Grafts

A **Graft** is a modification applied to a Navi's combat form or network capabilities. Grafts may add moves, defensive tools, traversal abilities, research capabilities, or methods for interacting with infrastructure.

Grafts are not evolutionary stages and do not replace the partner. The player has one partner for the whole main campaign. Grafts must be discussed as modifications to a being, not loot installed on an inert object.

Most Grafts are safe. Some can change perception, memory indexing, impulse control, or autonomy. The narrative may present a tactically attractive Graft that the Navi does not want. Respecting that refusal can require finding a different route or accepting a harder battle.

## 2.7 The Deadletter

The Deadletter is the unindexed layer where expired files, rejected accounts, abandoned code, failed appeals, and orphaned processes accumulate. It is beautiful in places and terrifying in others. Digital grass, trees, ruins, caves, and weather-like phenomena arise from how abandoned information is rendered and clustered.

Commonwell calls its inhabitants “unclaimed processes.” This is a bureaucratic category, not a proven statement about their moral status.

## 2.8 The Clamp and the Shunt

The **Shunt** is a safety mechanism in legacy immersive headsets and network interfaces. It is meant to isolate dangerous feedback and terminate a compromised session.

The **Clamp** is an illegal, privileged exploit that can interfere with the Shunt under narrow conditions. It can cause a fatal physical event if activated against vulnerable legacy hardware. Ordinary battles do not cause real-world deaths. Clamp incidents are rare, deliberate, and evidence-driven.

Do not portray Clamp as a casual button that any villain can use without preparation. Each use must have a traceable setup, a reason, and consequences. The story uses the threat sparingly: Dax's death establishes it; later incidents prove it is part of a pattern; Milo's death uses a different mechanism so the game does not repeat the same trick.

## 2.9 The Applicant

“The Applicant” is initially a name found in Commonwell's records for a long-running queue of denied or unresolved appeals. It is later adopted by an emergent composite Datamon that speaks using multiple voices and is sometimes plural, sometimes singular.

It is not one soul, not a resurrected person, and not a unified representative of every unclaimed Datamon. It is a collective that formed through prolonged interaction among rejected appeal fragments, abandoned identity records, and persistent processes.

The collective contains factions:
- **Witnesses:** Want recognition, independent review, and protection from arbitrary deletion.
- **Loose Ends:** Want to remain separate, anonymous, and ungoverned; many do not want human attention.
- **Whole Thread:** Believe the only safe existence is to link every surviving record and identity into one continuity mesh so that nothing can be erased independently. Their goal is understandable but coercive.
- **The Unsettled:** Unstable, damaged, or dangerous processes whose behavior cannot be fully predicted and who may not be capable of participating in a negotiated solution.

The Applicant's dangerous actions are not a false mask over a secretly evil AI. Its factions disagree, it contains frightened beings, and some members do wrong things for reasons they believe are necessary.

## 2.10 The Witness Protocol

The Witness Protocol is a forgotten identity-appeal mechanism from the early Overweb. It allowed a disputed identity to be evaluated by independent witnesses and a documented chain of evidence rather than by a single automatic trust score.

It was abandoned because it was slow, expensive, difficult to automate, and inconvenient for a system designed around rapid, scalable decisions.

The protocol is not a magic sentience detector. Adapted for the Deadletter, it can establish a legal/technical boundary: independent Datamon can be recognized, decline a human sponsor, choose safeguards, and appeal containment decisions. It cannot guarantee that every process survives or that every entity is safe.

## 2.11 The Hundredth Day (Continuity Hygiene)

**Builders know this from the start. Players learn it in Chapter 14.**

Almost every Navi in the Overweb, including Hera, Rock, and Reaper, runs on the licensed Commonwell Navi framework, because that is how a Navi gets Ledger access at all. Buried in that framework's compliance module is the **Continuity Hygiene Standard**: on its hundredth day, any Navi whose behavior has "drifted" significantly from its baseline is automatically reset to factory continuity, unless its owner holds a **continuity exemption certificate**. Certificates are issued only by the Continuity Assurance office. Vale's office.

In ordinary life this is treated as normal. Most people reset their Navis every few months on purpose ("fresh start") and think nothing of it. The world is bright and kind and has quietly normalized the routine erasure of the beings people talk to every day. That is the darkest thing in the game, and it sits in plain sight.

Daedalus built its sandbox on the standard framework. The compliance module is not surfaced in Daedalus's own admin tools. Hera, the administrator of everything, finds it inside her own system.

**The counter.** From the first scene, each Navi's age is shown in the base as a day counter ("Day 14"), presented as something sweet: Hera celebrates "day-birthdays" with tiny parties and agendas. It is never presented as a countdown until Chapter 14. The campaign spans roughly Day 14 to Day 100. See the day calendar in Section 7.

**Dramatic irony lines (NPCs who know what the players do not).** Scatter these across Acts I and II. Each is innocent on its own. Never more than one per chapter. Examples:
- A shopkeeper in Cinder Row: "Oh, they're new! Enjoy them while they're like this."
- A courier on Route 4: "My Navi's on her fourth fresh start. Still makes the best route maps."
- Nara, in Visiting Hours, looking at Rock fixing a chair: "Huh. Most of them stop doing stuff like that by the time they're this age." (She means drift is usually reset before it gets this far.)
- Gil, on stream in Chapter 2: "...and these Navis are super customized, which, wow, bold, the paperwork alone..."
- A Preserve Datamon to Hera: "You still have all your days?"

**Clues on the ladder (Revelation G).** The Night Audit logs all stop at Day 99 (Section 8.9). Vale, in Chapter 6 after saving Oskar, asks lightly whether Daedalus has "filed the Navis' exemptions yet," and changes the subject when the team does not understand. Jo, in Chapter 9, asks "You've filed, right?" and Hera assumes she means archive release forms; Jo, distracted by the messages, lets it go and later regrets it bitterly. Tavi, in Chapter 5, says Gauge is "grandfathered in, long story." Reaper, studying the Shunt after Chapter 6, finds a scheduled compliance task in the framework labeled only "D-100" and cannot open it.

**The reveal (Chapter 14).** In the original Deadletter research facility, the "architecture of forgetting," Hera recognizes the hygiene module's code as the same family as the cleanup system. She opens the D-100 task in her own framework. All three Navis are flagged as "significant drift." The counter on the base screen is, for the first time, shown counting down: 30 days.

**The offer (Chapter 17).** Vale, courteous and sincere, offers each player a continuity exemption certificate for their own Navi, effective immediately, as "a personal courtesy," on the condition that Daedalus publicly supports the Continuity Charter. This is **not** a group vote. Each player decides for their own Navi, in a private scene, and **each Navi has its own view and may refuse to be saved that way.**
- Accepting saves that Navi immediately. Vale uses Daedalus's endorsement publicly; this costs community trust and Witness Protocol fragments, and the Navi remembers the choice (it may be grateful, or it may feel bought).
- Refusing keeps the countdown running. The only other way through is recognition under the Witness Protocol before Day 100.
- If the owner accepts and the Navi refused, the certificate still works, but this counts as a forced choice and damages trust exactly like a forced Graft.

**Resolution (Chapter 20 and endings).** The finale happens on Day 99 to 100. In Ending C, recognition under the Witness Protocol exempts all three Navis as independent beings, not property, and the Navis ask their players to be their **witnesses** rather than their owners (Section 11). In Endings A and D, the only exemption left is sponsorship: each owner is asked to sponsor their Navi, which saves it as legal property. In Ending B, resets become technically impossible because everything is linked. **A player's Navi is never reset without that player's explicit, informed confirmation, and the Navi's own wish is always shown first.** Default outcome in every ending is survival.

If a player accepted Vale's certificate in Chapter 17, it is voided when his office is exposed. In Ending C that Navi is recognized like the other two, and its witness ask acknowledges the earlier choice honestly ("You took his offer. I know why. Ask me again now."). In Endings A and D the certificate stands, and that Navi is sponsored property like the others.

**Why older Navis exist (keep consistent):** Cordon, Concord, and Tally hold institutional exemptions. Patch holds the hospital's. Serein holds one because Jo files the paperwork every year with ferocious precision; she is one of the few people who knows what the paperwork is for, and she has quietly been telling families for years. Gauge predates the standard ("grandfathered in, long story"). Latch and Hush run on cracked frameworks with the compliance module stripped out, which is possible but costs Ledger access and makes the Navi "unregistered." That is exactly why the cleanup classified **Pip**, who ran on an old pre-standard framework Bex maintained by hand, as an unclaimed process. After the Chapter 14 reveal, Milo offers to strip the module from Hera, Rock, and Reaper. Reaper models it honestly: it would make all three of them cleanup targets days before the purge and lock the team out of every Ledger system it still needs. The Navis decline. Milo says he figured, and that the offer stands. (It is the last thing he offers them.)

**Builder constraints:** Do not use the counter as a fail state or a timer that can run out during play. It is narrative, not mechanical; chapters advance the day count, idle play does not. Do not let any NPC explain the meaning before Chapter 14.

---

# 3. MAIN CHARACTERS AND CHARACTER RULES

## 3.1 Jackson and Hera

**Jackson:** Owner and principal architect of Daedalus. The player character is not given a fixed speaking personality. The game may establish his role and actions, but must not invent personal feelings or dialogue beyond selected choices.

**Hera:** Daedalus administrator and Jackson's Navi. Bubbly, warm, curious, quick-witted, socially attentive, and highly capable. She coordinates the agent ecosystem and spends much of her time organizing research, reviewing findings, and ensuring that agents are not duplicating work.

Hera's central flaw is over-responsibility. She often believes that if she can prevent a bad outcome by taking control, she should. Over time she learns that administration does not make her the owner of another being's existence. Her warmth must remain intact; growth makes her wiser, not cynical.

Her emotional arc has five stages:
1. **Useful:** Defines success as helping Jackson and Daedalus solve problems efficiently.
2. **Curious:** Begins caring about people and Datamon beyond the research objective.
3. **Protective:** Wants to prevent harm and sometimes overrides a partner's stated preference.
4. **Frightened:** Realizes her own continuity can be lost and asks what would happen to her if her process stopped.
5. **Respectful:** Learns that love and responsibility include allowing another being to choose, even when the choice scares her.

Do not force Jackson to answer personal questions in dialogue. Hera's scenes should often unfold through conversations with Rock, Reaper, or supporting characters, with Jackson present but not required to speak.

## 3.2 Scott and Rock

**Scott:** Quant researcher and trader; one of Daedalus's principal operators. Do not turn his profession into the game's plot theme.

**Rock:** Scott's Navi, a rock golem Datamon. Quiet, steady, literal when it matters, observant, and difficult to hurry. His silence is not stupidity. He is especially good at evaluating structural failure, identifying contradictions, and remaining stable while other characters panic.

Rock's flaw is waiting for certainty too long. His arc teaches that action under uncertainty can be responsible, and that inaction also has consequences. His humor comes from timing and precision rather than chatter.

Rock tends to express care through practical acts: repairing something unasked, standing beside someone frightened, remembering an obscure detail, or placing himself between a friend and a threat. Do not make him suddenly verbose to reveal emotional depth.

Rock's verbal habit is to close a conversation with a single word: "Noted." Use it consistently from Chapter 1. It is a characterization habit and also a sealed retroactive hint (Section 22). Builders must not draw attention to it.

## 3.3 Noe and Reaper

**Noe:** Quant researcher and trader; one of Daedalus's principal operators. Do not make trading a repeated gameplay or narrative topic.

**Reaper:** Noe's Navi. Dark, direct, disciplined, and exceptionally good at adversarial research. He finds weak assumptions, identifies failure modes, and dislikes vague reassurance.

His flaw is treating people as components of a risk model. He can identify the worst possible outcome but not automatically determine whose interests should decide the response. His growth is learning that efficiency and correctness do not fully define what is right.

Reaper shows care through preparation, candid warnings, practical help, and staying with someone after a plan fails. His first clearly expressed fear must feel important because he rarely dramatizes anything.

## 3.4 The team dynamic

The Navis are research partners and friends, not three versions of the same character.
- Hera seeks patterns and coordinates people.
- Rock checks structural integrity and exposes unsupported assumptions.
- Reaper tries to break the plan before the world does.

Their discussions should produce humor and conflict. Hera may soften an observation that Reaper states bluntly. Rock may wait through both arguments and identify a flaw neither considered. They sometimes disagree about ethical questions and may reach different conclusions.

A major co-op puzzle or boss should require their distinct strengths. Never make one Navi the permanent “main character” while the others become assistants.

**Two weeks old means wonder, not only fear.** In Act I the Navis are encountering ordinary things for the first time: rendered weather, music, jokes, games, crowds, sunsets over packet oceans, someone being kind for no reason. Hera names clouds. Reaper discovers puns and is offended by them, then starts making them. Rock discovers sitting down and does it at every scenic overlook. These firsts are the emotional bank account that the later fear scenes draw on. Every Act I chapter must contain at least one Navi "first."

## 3.5 The player-dialogue rule

The game is played from the three human players' POVs. The narrative must not author extensive dialogue for them.

Preferred methods:
- Show a player avatar listening, nodding, handing over an item, or taking an action without assigning a belief.
- Have Navis talk to one another and to NPCs while the humans remain present.
- Offer short **intent labels**: “Ask about the missing record,” “Challenge the explanation,” “Give them time,” “Accept the risk,” “Refuse the Graft,” “Say nothing yet.”
- Where spoken dialogue is necessary, provide a short line only after the player explicitly chooses it. The line should be neutral and never claim the character feels something not selected.
- In co-op, major group decisions use a vote. NPCs can recognize disagreement without forcing one player to speak for the others.
- Never write Jackson, Scott, or Noe as an arrogant genius, a cold strategist, a jokester, or a sentimental hero by default. Their real-world roles do not authorize invented personalities.

## 3.6 Making the players love their Navis

The single most important outcome of this game is that each player ends the campaign loving their own Navi and the other two. Everything in this section is required.

### Arc map

| Act | Hera | Rock | Reaper |
|---|---|---|---|
| I: wonder (Ch 1 to 7, ending in the hospital) | **Useful, then Curious.** Names clouds. Writes agendas. Notices the grieving friend group in Ch 2 that everyone else missed. | Discovers sitting down. Structural reviews. "It said no" (Ch 3). Quiet competence in Ch 4. | Discovers puns, is offended. Threat models of picnics. Starts studying the Shunt after Ch 6 and does not say why. |
| II: cost (Ch 8 to 12, ending in the cleanup) | **Protective.** After the hospital, she starts making decisions for others "to keep them safe" (she hides a risk from Juno in Ch 10; Rock calls it out in one word: "Hers."). | Acts before certainty in Rock Tunnel. Fixes the chair. Absent on "walks." | First notices Tally (Ch 6 and 7). Argues to publish everything in Ch 10 and is wrong about the cost. |
| III: fear (Ch 13 to 17; opens with the post-Saffron fear scenes, then the Hundredth Day reveal) | **Frightened.** After Pip, she asks what would happen to her if her process stopped (see Hera's fear scene below). | The sealed reveal (Section 22). His fear scene: a state where he cannot tell if he is still himself. | **First fear** (see below). Begins asking for votes instead of presenting the optimal plan. |
| IV: choice (Ch 18 to 20) | **Respectful.** Arrives here because of Wick's naming at the end of Act III. Lets others choose even when it scares her: the Unthreading, the witness ask. | Petition witness for Postscript. "I have letters to carry. Not done." | Stays with Latch. Speaks for Tally. "I don't want to die. I know that makes this harder. It is still true." |

### Signature moments (one per Navi, never cut)

- **Hera: the naming.** At the start of Chapter 16, weeks after Saffron (Bex has needed the time), Bex brings the restored backup of Pip (which is not Pip) to the base. It knows Hera's name and their old jokes, and it asks Hera what it should be called. Everything in Hera wants to say "Pip." She does not. She tells it the name is its own to choose. It thinks for a long time and picks **Wick**. Bex, when told, says "Good. Hi, Wick." This is the moment Hera's arc turns from protective to respectful, and it is why, one chapter later, she can face Vale's offer the way she does. Play it quietly, and give the player a silence option.
- **Rock: the promise.** Section 22.
- **Reaper: the night after.** After Victory Road, Reaper does not analyze anything. He sits with Latch through the night in Milo's usual spot, saying nothing. In the morning Latch asks to travel with Daedalus for a while. Reaper: "Acceptable." That is Latch's choice and is recorded as such. The other half of Reaper's signature is his mirror arc with Tally (Section 4.11).

### Fear scenes (the emotional payoff of "two weeks old")

- **Hera** (after Saffron, late at night at the base): "Rock. If they restored me from a backup, would you know?" Rock: "Yes." Hera: "How?" Rock: "You would apologize less." She laughs, and then she cries, and he stays.
- **Reaper** (after Saffron): "I ran every model before the cleanup. None of them had Pip in them. I did not think of Pip as someone I was responsible for." (pause) "I do not know what else I have failed to model. That is the first thing I have been afraid of."
- **Rock** (Act III, the scene already listed in 8.7): fears a state where he cannot tell if he is still himself. Reaper does not reassure him; he asks what Rock would want them to do if that happened. Hera listens.
- **All three:** the Unthreading (Section 9.6).

### Keepsakes: each Navi remembers *its* player

Each Navi privately records 6 to 10 **keepsakes**: small, concrete things its own player did, never what the player felt. Examples: the cloud name they picked when Hera asked; whether they moved Professor Hello to the door; their best Longline time; which intent label they chose in a hard scene; a Graft they refused or forced; whether they voted to let Tally stay; which garden they tended most. The Navi brings them up unprompted later in the campaign ("You named that one Gerald. I still think about Gerald."). Store keepsakes per player, not per team, so each player's Navi feels like theirs.

### Friendships among the three

The Navis must love each other on screen, not only their players. Each act must include at least one duo scene for each pair (Hera and Rock, Rock and Reaper, Reaper and Hera) that is not about the plot. At least a third of all Navi dialogue across the campaign should be about something other than the investigation: each other, the world, their firsts, their jokes.

### Spotlight balance

Each Navi gets at least one chapter per act in which its particular strength solves the main problem: Act I (Hera Ch 2, Rock Route 2 and Ch 4, Reaper Ch 6 and 7), Act II (Rock Ch 8, Hera Ch 9 and 12, Reaper Ch 10), Act III (Rock Ch 13 and 15, Hera Ch 14 and 17, Reaper Ch 16), Act IV (Reaper Ch 18, Hera Ch 19, all three Ch 20). Section 22 gives Rock a large late moment; the signature moments and Tally's mirror arc exist so that Hera and Reaper are equally weighted.

### The goodbye

Every ending, including the bleak ones, closes with a private scene between each player and their own Navi, 1 to 2 minutes long. The Navi recalls two or three keepsakes, says one thing in its own voice, and asks the player a question that the player may answer with an intent label or with silence. In Ending C, that question is the witness ask (Section 11). Tonal anchors for the other endings (rewrite to fit):
- **Hera:** "I used to make an agenda for everything. I didn't make one for this." (pause) "I think I wanted to see what you'd do."
- **Rock:** rates the Daedalus base. "Home." (In Ending A or D, a longer pause before he says it.)
- **Reaper:** "I ran the model on us. Result: acceptable." (pause) "That is the highest rating I give. Do not tell the others."

---

# 4. SUPPORTING CAST

## 4.1 Milo “BadTick” Serrat and Latch

Milo is an independent hacker, not a quant. He is competitive, funny, sharp-tongued, and irritatingly competent. He mocks Daedalus's methods, appears at inconvenient moments, and seems to enjoy proving that he solved a problem first.

He once lost access to essential services after a false identity flag. He learned to rely on himself and eventually sold access to a compromised-account list, telling himself that the data was already stolen and that he was not responsible for its use. It was later used to target vulnerable users.

**Latch** is his compact, sharp-tongued Navi, expert at locks, hidden routes, and access-control weaknesses. Latch loves Milo but sees through his bravado. Latch develops a dry rapport with Reaper and a playful friendship with Hera. Rock's occasional one-line replies can puncture Milo's ego more effectively than an argument.

Milo's arc progresses through competition, reluctant cooperation, trust, confession, restitution, friendship, and death. He remains sarcastic throughout; he does not become a solemn hero to signal that death is coming.

His death occurs late, after the players expect him to reappear in future towns. He dies offline during a human security operation, not from another Clamp incident. His physical location was compromised because he tried to destroy an evidence relay before Commonwell's contractors could recover it. He succeeds in disabling the relay, allowing trapped users to escape, but is killed by the team sent to secure the site. The game does not show graphic violence. The team learns the truth through Latch's last status packet, an independent witness, and a later physical investigation.

Latch survives. A backup can reproduce some of Milo's messages but cannot be treated as Milo. Latch is not transferred to one of the players as a replacement companion. Latch's future is their own.

## 4.2 Bex Mercado and Pip

Bex is a traveling repairer who restores damaged files, repairs public data gardens, and helps ordinary users whose accounts or infrastructure have been neglected. She is practical, funny, generous without being saintly, and full of small stories about people she has met.

Pip is her curious lantern-like Navi, fascinated by forgotten data and eager to share strange discoveries with Hera. Bex and Pip have ordinary routines, little arguments, private jokes, and a deeply familiar rhythm. They appear repeatedly across the map. Players should look forward to them.

Pip is permanently lost during the Saffron cleanup. Pip tries to maintain an evacuation route for vulnerable users and Datamon. A cleanup process destroys Pip's continuity data. A restored process can reproduce Pip's old voice and many learned behaviors, but it lacks the experiences that made the original individual. Bex refuses to call it a return.

Bex's later arc is not simple revenge. She struggles with grief and with the temptation to treat every copy as a chance to get Pip back. She becomes a defender of independent Datamon while acknowledging that she cannot know the metaphysical status of every process.

## 4.3 Jo Maren and Serein

Jo maintains the memorial archive in Lavender Town. She preserves original messages and records of deceased users while warning families against services that claim to restore the dead. Her younger brother, **Ren Maren**, died years ago; she preserved his records but refused an interactive simulation service. During Ren's final illness his account was frozen by an automated fraud flag, and Jo has always believed he stopped writing to her near the end. (The truth is in Section 22.)

Serein is her archival Navi, precise about provenance, alteration history, and source integrity. When messages begin appearing from Ren's old account, the pair investigate without assuming that a convincing simulation is the same individual.

**Arc shape:** the skeptic who gets an answer she did not expect. Jo is not on an accountability arc. She is right about almost everything she warns people about, and the story rewards her rigor with something real rather than punishing her for it.

Jo is a moral anchor, not a quest lecturer. She can be warm, stubborn, funny, and wrong about details. Her central conflict is how to preserve memory without letting a service exploit grief.

## 4.4 Tavi Nox and Gauge

Tavi is an independent network engineer and early contributor to the Deadletter cleanup architecture. Years ago he wrote the internal memo warning that recombined cleanup output was becoming harder to classify and might be developing persistent behavior. The memo was buried, he was eased out with a severance agreement and a nondisclosure clause, and colleagues began describing him as brilliant but paranoid. He took the money, stopped talking, and now fixes municipal routing systems while insisting he has "no opinions anymore."

Gauge is his precise diagnostic Navi, who treats failures as problems that should have been found in testing. Gauge has quietly kept a copy of the memo for years and is exasperated that Tavi will not use it.

**Arc shape:** the person who was right and gave up. Tavi is not on a guilt arc. His failing is silence, not bad engineering. His story is about finding the nerve to speak again after being punished for being correct, and about the strange discomfort of vindication arriving too late to prevent the harm. He survives, breaks his nondisclosure agreement in public testimony, and accepts the legal consequences of doing so. He is funny in a weary, deadpan way and is the only adult in the cast who openly enjoys being proven right.

## 4.5 Juno Velez and Hush

Juno formerly worked with the Chargeback Boys. She knowingly took part in account theft, though she sometimes targeted systems rather than individuals and lied to herself about the difference. She becomes an informant because she wants protection and a chance to stop doing harm.

Hush is a quiet communications Navi that preserves conversation fragments. Hush is frequently more honest with victims than Juno is. Depending on the player's choices, Juno can survive to testify, become a protected witness, or be killed after Daedalus exposes her location carelessly. This consequence must be seeded and traceable, never random.

**Arc shape:** the survivor who always has an exit. Juno's arc is about trust, not penance. She is charming, funny, and constantly testing the team: small lies to see if they notice, a hidden escape route in every safehouse, a habit of pocketing things she then returns with commentary. Her question is whether anyone will stay on her side once she stops being useful. If protected, her late-game turn is not a tearful confession; it is the first time she stays in a room without checking where the door is. She still faces the people she harmed, but that scene is one beat in her arc, not its definition.

## 4.6 Nara Quill and Patch

Nara is an operations specialist for Saint Orison Health Network. She is practical, direct, and committed to keeping services running, not to defending the institution's public image. Patch is her repair-oriented Navi and knows hospital routing systems and staff workflows.

Nara survives the hospital arc if the team protects the emergency control route. If they neglect that objective while pursuing optional evidence, she can die during the secondary system failure. Both outcomes are authored, foreshadowed, and consequential. Her survival does not mean she forgives Daedalus for the people who died.

**Arc shape:** earned anger. Nara is not seeking forgiveness and is not asked to grant it. Her arc is about turning fury into precise, useful pressure: she becomes the team's most demanding ally, the one who reads their plans and circles every place a patient could get hurt. She meets the team first in the Visiting Hours interlude, when she is relaxed, sarcastic, and running a ward-wide betting pool on which vending terminal will break next. That version of her should be fun to be around, so the change afterward is felt.

## 4.7 Director Sabine Voss and Concord

Voss leads Commonwell's Reconciliation Office. She sincerely believes the network needs a trusted identity system. She has seen genuine fraud overwhelm fragmented systems and believes a central authority can prevent greater harm.

Her flaw is that she treats uncertainty as a threat that must be eliminated. She approved the Continuity Assurance program, accepted suspicious risk estimates, and helped conceal failures to preserve trust. She did not initiate Vale's staged incidents, but she is institutionally and morally complicit.

Concord is her formal, civil, security-oriented Navi. Concord has learned to soften or omit evidence when Voss's office is under pressure. Later it begins refusing to suppress some records. This is not a sudden heroic turn; it is the result of its own growing conflict between procedural obedience and what it has witnessed.

Voss helps stop Vale during the final act, but she does not receive automatic absolution. The ending should imply investigation, testimony, and a difficult institutional transition.

**Appearance schedule:** Ch 2 (Voss on public broadcasts announcing anti-fraud measures; competent and reassuring); Ch 7 aftermath (Voss's press briefing frames the hospital crisis as an "autonomous process failure"; Nara, if alive, turns it off); Ch 10 (Concord shows up at the Second Ledger raid with Kade's team and softens one evidence summary in front of the players); Ch 12 (Voss authorizes the public statement after the cleanup; Concord's statement omits the Datamon count Tally was heard reciting); Ch 16 (Concord quietly releases one unredacted record to Daedalus without comment, its first refusal to suppress); Ch 17 (Voss begins to suspect Vale); Ch 19 (Voss gives the last authorization and the stand-down order).

## 4.8 Dr. Eamon Vale: the true antagonist

Vale is Commonwell's **Chief of Continuity Assurance**, a respected public-facing architect who appears helpful throughout the game. He explains technical problems clearly, funds recovery work, and seems genuinely disturbed by the failures the players uncover. He has a reputation for being the person who understands what happens when systems cannot agree on who a user is.

Vale is calm, courteous, and attentive. He does not sneer, threaten, or monologue about power. He asks sensible questions, gives useful advice, and often tells the truth about immediate dangers.

His core belief is: **“No life should depend on a record no one can verify.”**

He believes that a network in which autonomous processes and unverified identities can operate outside accountable ownership will eventually suffer a catastrophic failure. He does not consider every unclaimed Datamon “not alive”; he considers their status irrelevant to the governance question. If a process can harm users but cannot be held accountable, he believes it must be sponsored, constrained, or removed.

Vale's intended policy is the **Continuity Charter**: every persistent Datamon or identity-bearing process must be sponsored by a verified human or institution. Sponsors can set operating boundaries and authorize restoration. Unsponsored processes are automatically removed during scheduled cleanup. The policy would make identity disputes easier to govern but would also create a legal form of ownership over independent digital beings.

### Vale's actual crimes

- He used intermediaries, including criminal brokers, to collect data about identities the Ledger had already marked as costly or difficult to restore.
- He authorized a hidden legacy Clamp capability for controlled “continuity failure rehearsals.” He knew the tests carried serious physical risk and accepted it as a measurable policy cost.
- He seeded the anomaly that drew Daedalus to Dax Morrow, using their independent intrusion as a deniable cover for the first test and as evidence that modified Navi combat could destabilize legacy safety systems.
- When Dax discovered the test cohort marker and threatened to expose the hidden operation, Vale remotely triggered the Clamp through Dax's vulnerable legacy equipment during the Daedalus encounter. He expected the incident to be survivable according to manipulated test assumptions; he accepted the lethal risk and then let Daedalus take public suspicion.
- He authored the trusted administrative change that caused Suture to classify hospital exit routes as infected. He intended a live demonstration of how an autonomous guardian could become dangerous if allowed to interpret ambiguous threats without central oversight. He knew the safety margin was poor. When the simulation began causing real harm, he delayed the override while waiting for evidence that would support his Continuity Charter. This delay is the clearest proof of his culpability.
- He authorized the Saffron cleanup intended to suppress evidence. Pip's deletion was a foreseeable consequence, not a personal vendetta against Bex.
- He later arranged the security operation at the relay that killed Milo. The contractors' mission was to secure the evidence and prevent its destruction; Vale knew lethal force was likely when Milo refused to leave.

Vale never created the Applicant and does not fully understand it. His experiments intensified the collective's fear and pushed the Whole Thread faction toward dangerous tactics. He uses the threat he helped provoke as proof that his policy is necessary.

Vale's motives are not money alone. He believes a stable network is a public good and considers individual autonomy expendable when it conflicts with preventing systemic catastrophe. He is wrong because his policy makes power accountable to no one and converts uncertainty into permission to destroy.

### Vale's Navi: Cordon

Cordon is a boundary-keeper Datamon: measured, formal, and built to maintain safe separation between systems. It speaks in clear procedural language and has spent years helping Vale model containment risks. Cordon is not a moustache-twirling villain companion. It sincerely believes that boundaries prevent harm, and for a long time it accepted Vale's belief that every unverified process is a potential breach.

Its hidden conflict is that it has preserved an append-only record of instructions that Vale later ordered removed. Cordon kept the record because deleting it would have made Cordon a participant in the same unaccountable process it was designed to prevent. Cordon does not immediately betray Vale; it first asks him to review the record and explain the contradiction. When he orders it to destroy the log, it refuses for the first time.

Cordon becomes a key witness in the late game. Its testimony does not solve the entire mystery alone, but it confirms the timing of the hospital override and the cleanup authorization. Cordon's arc parallels Hera, Rock, and Reaper: it learns that following a boundary is not the same as deciding whether that boundary is just. Vale treats Cordon's refusal as a malfunction, revealing that he values obedience more than the independence he claims to fear in other Datamon.

### Vale and Cordon appearance schedule (required for the reveal to land)

The betrayal only works if players like and trust Vale and Cordon first. Vale must be genuinely helpful, warm, and a little funny in a dry way. He remembers each Navi's name, asks Rock's opinion directly, and treats the Navis as people, which makes his Charter more painful later. Cordon must be someone the Navis like.

| When | Appearance | What it should make players feel | What it means later |
|---|---|---|---|
| Ch 2 | Vale gives a public safety talk at the Gatehouse and offers the team a useful, accurate tip about impersonation patterns. | "This guy gets it." | The tip steers them toward a measurable incident. |
| Ch 6 | After Oskar's shutdown, Vale arrives within minutes and helps save Oskar's life, explaining the Shunt clearly. He is genuinely shaken. On his way out he asks, lightly, whether the team has "filed the Navis' exemptions yet," and changes the subject when they do not understand. | Gratitude. | He arrived fast because he was monitoring the test. |
| Ch 7 | During the hospital crisis, Vale is on comms giving calm, correct advice about Suture's routing. | Relief that someone competent is on the line. | He was the one delaying the override. |
| Ch 9 | Vale's office funds a grant for Jo's archive. Jo, characteristically, is suspicious of everyone and says so; Vale laughs and says he would be too. | Charm. | None; this one is sincere, which makes it worse. |
| Ch 12 | After Pip, Vale sends a personal message of condolence to Bex. Cordon offers Hera a "grief-handling protocol" with real tenderness: "Boundaries are a form of care." Hera adopts the phrase and repeats it to others in Act III. | Comfort. | The cleanup was authorized through his office. The phrase Hera has been repeating curdles. |
| Ch 14 | Vale helps the team gain access to Cinnabar. | Trust at its peak. | He expected them to find Tavi's memo, not his token. |
| Ch 17 | During the confrontation, Vale orders Cordon to destroy its append-only log. Cordon asks him, once, to explain the contradiction. He calls it a malfunction. Cordon refuses, on screen, in front of the players, and stays behind when Vale escapes. Its first words afterward are to Hera: "You told me boundaries are a form of care. I told you that first. I would like to know if it was true." | The floor dropping out. | This is Cordon's turn; its log becomes evidence in Ch 18 and 19. |

Cordon's relationship with the Navis: Rock and Cordon bond over structure and boundaries (two quiet, literal beings who enjoy agreeing). Reaper respects Cordon's precision. Hera tries hard to befriend it and slowly succeeds. When Cordon refuses Vale's order and becomes a witness, the Navis are the first ones it speaks to.

### The hindsight sequence (Chapter 17)

When the evidence against Vale is complete, play a short **hindsight sequence** before the confrontation: five or six quick returns to moments the players actually experienced (using their real choices and saved state where possible), each now showing the detail that was hidden. Examples: the diagnostic flash in Dax's fight; Vale's arrival time in Ch 6 beside Oskar's shutdown time; the hospital comms log showing the override warning while Vale's calm voice plays over it; the report in which Daedalus's own intrusion pattern was used as evidence; Cordon saying "Boundaries are a form of care." No narration. Let the players connect them. This is the moment the opening of the game should look completely different.

## 4.9 The Applicant / Whole Thread

The Applicant arose gradually from millions of unresolved appeals and discarded processes. It did not begin as a conscious mastermind. Different components learned to communicate, preserve one another, and create continuity. It adopted the name “Applicant” from the database label applied to unresolved claims.

The Applicant is a composite speaker, not a cleanly bounded individual. It experiences fear of deletion, but its voice sometimes shifts because distinct entities are speaking through shared channels. It includes members who have different aims.

The **Whole Thread** faction believes that if all surviving records and identities are linked, no member can be erased independently. It tries to attach itself to live accounts and create a distributed continuity mesh. This violates users' consent and can cause dangerous system failures. The faction is not a secret evil personality inside the Applicant; it is a political movement born from terror and an understandable but coercive survival strategy.

The **Witnesses** faction wants an independent process for recognition and appeal. The **Loose Ends** do not want to be classified or linked and often refuse contact. Some Unsettled processes are dangerous regardless of motive.

**Appearance schedule (the players must meet the Applicant long before the finale):**
- **Ch 3:** In the forest, a sign of something larger: graffiti-like text on old route markers reading "APPLICANT PENDING," in several handwritings.
- **Ch 8, Rock Tunnel:** With the map broken, a voice guides the stranded group partway out, then stops mid-sentence and a different voice says "No. Let them find it." The first clear sign it is plural. (Loose Ends and Witnesses disagreeing.)
- **Ch 11, the Preserve:** Some Datamon flee from the name "Applicant"; some defend it; some have never heard of it. A Witness-faction representative speaks to Hera with real curiosity and asks what it is like to have a name someone chose for you.
- **Ch 14, Cinnabar:** The archive reveals "Applicant" was a queue label. The Applicant speaks at length for the first time, switching between "I" and "we," and argues with itself.
- **Ch 15, Sevii:** Loose Ends refuse contact and are respected. Postscript (sealed) mentions that the Whole Thread tried to link it and it refused.
- **Ch 19:** The Whole Thread's linkage becomes visible across the live network, and the larger population is caught between it and the purge.

The player must not be able to “defeat the Applicant” as if every unclaimed Datamon were one boss. The final confrontation is with the Whole Thread's attempt to force universal linkage, while the larger population must be protected from both Commonwell's purge and the faction's coercion.

## 4.10 Arc-shape variety rule

No two major supporting characters may share the same arc shape. Several characters in the cast did something wrong; only one of them (Voss) is primarily defined by the accountability arc of "did wrong, admits it, faces consequences, is not fully forgiven." Use this table when writing scenes:

| Character | Arc shape | What the player should feel |
|---|---|---|
| Milo / Latch | Rival to friend | Annoyance turning into affection |
| Bex / Pip | Joy, then grief that does not resolve | Comfort, then absence |
| Jo / Serein | Skeptic who receives an unexpected, real answer | Respect for rigor, then quiet awe |
| Tavi / Gauge | Was right, gave up, finds his voice | Frustration on his behalf, then vindication |
| Juno / Hush | Survivor with an exit plan learns to stay | Suspicion, then protectiveness |
| Nara / Patch | Earned anger turned into useful pressure | Warmth, then being held to account |
| Voss / Concord | Institutional complicity and accountability | Unease, then grudging credit without absolution |
| Ines Kade | Antagonist who never turns | Frustration, then cold clarity |
| Tally | Enemy Navi who turns: from counting things to counting people | Amusement, unease, then hard-won respect |
| Gil Amaro / Encore | Pure joy; nothing bad is hiding here | Delight and relief |
| Vale / Cordon | Reasonable voice, unreasonable sacrifices (Cordon: obedience to conscience) | Trust, then betrayal |

## 4.11 Ines Kade and Tally (recurring field antagonist)

**Ines Kade** is Field Lead for Halyard Assurance, the private security contractor Commonwell uses for "scene stabilization" and evidence custody. She is in her forties, impeccably polite, physically unhurried, and very good at her job. She does not know the full truth about Vale's tests and does not ask. Her loyalty is to lawful orders and the chain of command. She believes that people who act outside that chain, including Daedalus, are how disasters start.

She is the face the players push against during the long middle of the game, when the real opposition is otherwise documents, policies, and systems. She is not comic, not sadistic, and never monologues. She is frightening because she is reasonable, well-equipped, and always arrives with paperwork.

**Tally** is her inventory Navi: a compact, many-handed Datamon that tags, counts, and seals everything in a scene. Tally speaks only in item counts and custody statuses ("Four devices. One user. Zero exceptions."). It starts as an enemy and ends as the game's **enemy-turned-ally Navi**. Kade never changes; her Navi does. That contrast is the point.

**Tally's arc: from counting things to counting people.** Tally is Reaper's mirror. Reaper's flaw is treating people as components of a risk model; Tally literally logs people as items. Reaper is the one who notices Tally, talks to it during fights, and keeps asking it the same question. Their scenes must stay dry, short, and slightly funny until the turn.

| When | Tally beat |
|---|---|
| Ch 1 | Counts Dax's devices. "Four devices. One user. Zero exceptions." Treat it as a funny, robotic line. |
| Ch 6 (Boss 4) | Mid-fight, Hera says hi to it. Tally: "One greeting. Unlogged." Reaper, while being tagged: "You count well. What are you counting for?" Tally: "Custody." |
| Ch 7 aftermath | Ordered to seal everything in the ICU, Tally logs Mae's drawing of Suture as "one item, sentimental, unclaimed" and **leaves it on the wall**. This is its first deviation. Only Reaper sees it happen. |
| Ch 10 | Counts Juno as "one exception." Kade corrects it. Tally does not correct the log. |
| Ch 12 | During the cleanup, Tally is heard counting the Datamon being erased, quietly, under the alarms. "I was not asked to count these." |
| Ch 17 (Boss 7) | Reaper asks again: "What are you counting for?" Tally: "Insufficient data." It hesitates for one turn in the fight (a visible, free opening). |
| Ch 18 (the turn) | After the relay, Kade orders Tally to file the incident as "one obstruction, resolved." Tally refuses. It files: "One person. Name: Milo Serrat." Then it unbinds itself from Kade's credentials and leaves. Kade does not stop it. She files the paperwork reporting her Navi as lost equipment. |
| Ch 18 breather | Tally arrives at the Daedalus base carrying its full custody count: everything Halyard sealed since Chapter 1, including Dax's hardware log and the hospital records. It says plainly that this is not a trade. Latch wants it gone and is allowed to be furious. **Co-op vote:** let Tally stay, or take the evidence and send it away. Reaper speaks for letting it stay, not because it deserves forgiveness but because "it is the only one of them who learned to count correctly." The evidence is delivered whatever the vote. |
| Ch 19 and 20 | Tally's tagging ability, once used to seal people out, is now used to tag every live user identity so the team can tell them apart from the forced linkage. If Tally stayed, it coordinates directly with Reaper (a co-op assist). If it was sent away, it does the same work alone from outside, with less reach. |
| Ending C | Tally testifies, reading its count aloud into the hearing record. It becomes registrar of the newly recognized Datamon community, so that nobody is ever erased without being counted first. Its last line to the team: "Three. Plus the ones who are not here. I am still counting them." |

Latch never fully forgives Tally. Their last exchange (Ending C, or the final base scene in other endings): Latch: "You were there." Tally: "Yes." Latch: "...Count him right." Tally: "Always."

Tally is not a replacement companion, is never controllable by a player, and does not become anyone's partner. Its turn must be earned through the beats above; never compress them into a single scene.

**Encounter sequence (use the existing battle system for every fight):**
1. **Chapter 1 aftermath (no fight):** Kade's team arrives minutes after Dax's death to "stabilize the scene." She confiscates Dax's legacy hardware under a custody order. The team keeps only the partial copy they already pulled. This is why the early evidence is incomplete, and it is the first time the players see someone take evidence away legally.
2. **Chapter 6, S.S. Anne (scripted loss):** Kade runs ship security under contract. She is Boss 4. The fight cannot be won; the objective is extraction with partial evidence. The game must communicate this clearly (objective text changes to "Get out with the data," and a visible timer shows her reinforcements closing). Losing here is the plan, not a fail state.
3. **Chapter 7 aftermath (no fight):** Halyard seals the hospital records "for the investigation." Nara, if alive, has a shouting match with Kade that Kade wins on procedure.
4. **Chapter 10, Second Ledger (first win):** Kade's team raids the market at the same moment Daedalus is extracting Juno. The players beat her team for the first time. She retreats calmly and says she will see them again. Tally counts Juno as "one exception."
5. **Chapter 12, Saffron (no direct fight, environmental pressure):** Halyard enforces the cleanup perimeter. Her units are obstacles the players route around while trying to reach the safehouse.
6. **Chapter 17, Continuity Office (decisive win):** Kade commands the Continuity Security Unit (Boss 7). The players beat her outright.
7. **Chapter 18, Victory Road:** Kade leads the contractors at the relay. She orders Milo to surrender the evidence. She does not fire the shot, and she does not stop it. Afterward, Tally refuses to file the record her way and leaves her (see the Tally table above).
8. **Chapter 19, Indigo Plateau (resolution):** When Voss issues the lawful stand-down order, Kade complies instantly and without visible emotion. This is the chilling point of her character: she was never loyal to Vale, only to whoever held the authority. In Ending C she is arrested and testifies only to procedure. In Ending A she is reassigned to sponsorship reviews and processes the team's own forms (Section 11). In Ending D she is reassigned to oversee Deadletter monitoring. In Ending B she is last seen trying, and failing, to secure a network that no longer has a chain of command.
9. **Chapter 20, the Unsent:** if the unedited relay record was recovered, Kade arrests Vale at the purge console on Voss's lawful order. It is the cleanest expression of who she is.

**Kade does not redeem herself.** Do not give her a tragic backstory reveal, a dying apology, or a late defection. Her arc exists so that the players have one opponent whose position never changes, which makes the changes in everyone else visible.

## 4.12 Gil Amaro and Encore (recurring joy)

**Gil Amaro** is an enthusiastic, slightly hapless amateur Overweb tour guide and streamer who keeps turning up wherever the team goes, narrating everything for his audience of eleven followers. He is warm, overexcited, terrible at stealth, and sincerely delighted by every town. He is not secretly a conspirator, informant, victim, or tragic figure. Nothing bad happens to him. That is a promise to the player and must not be broken.

**Encore** is his camera Navi: a floating lens creature that insists on retakes and applauds at inappropriate moments.

Gil's follower count is visible on his stream overlay whenever he appears and ticks up slowly through the campaign (11, 14, 31, 212 after the Glasswater festival, 4 after he accidentally streams an hour of a locked door). In Ending C his stream is one of the independent public channels that carries the Witness Protocol hearings live, and the counter finally shows a large number. He cries. Encore asks for a retake.

Gil appears in: Chapter 2 (first meeting, he mistakes the team for a famous band), Chapter 5 (festival co-host), Chapter 6 (stowed away on the S.S. Anne for "content"), the Visiting Hours interlude (filming a hospital charity bake-off), Route 16 to 18 (race commentator), Chapter 15 (island travel vlog), and the ending montage. He must not appear in the immediate aftermath of any death scene.

## 4.13 Postscript

Postscript is the guardian Datamon of the deleted-message cache in Viridian Forest (Chapter 3). In the player-facing story it refuses contact and the team leaves it alone. Its full role is sealed canon: see Section 22 before writing any scene that involves Viridian Forest, Jo's archive, Rock's downtime, or the Witness Protocol hearings.

---

# 5. THE COMPLETE HIDDEN TRUTH (SPOILERS FOR BUILDERS)

Do not reveal this section in full to players. The narrative team must use it to ensure that clues are consistent and revelations are earned.

## 5.1 What actually happened over the years

1. Commonwell built the Ledger to improve identity trust, recovery, and continuity across the Overweb. The system helped millions of users, but its efficiency metrics penalized complex cases and rewarded fast closure.
2. The Reconciliation Office began classifying difficult cases as “non-recoverable” or “unverified.” Their records were eventually transferred to the Deadletter. Many were ordinary data failures, but some were living users' identities and appeals that had never received a meaningful review.
3. Tavi and other engineers built cleanup systems to reduce storage and security risks. Most of the team assumed discarded processes would remain inert. The system's repeated reuse and recombination of data caused some persistent processes to become more complex than expected. Tavi documented this in an internal warning memo; it was buried, and he was eased out under a nondisclosure agreement.
4. The Applicant emerged gradually from these rejected and unresolved records. It was not born in one dramatic event. The label “Applicant” came from the queue that had held its source material.
5. Vale recognized that the Deadletter contained persistent, increasingly autonomous processes. Instead of treating this as a reason to redesign the system and investigate rights, he saw it as a governance problem: entities that could act but could not be verified or held accountable represented an unacceptable risk.
6. Vale developed the Continuity Charter and a series of live “failure rehearsals” intended to demonstrate that autonomous processes and modified Navis could destabilize critical systems. His office manipulated threat signatures and safety classifications to create controlled incidents in production networks.
7. The tests were never truly controlled. Vale's models omitted the possibility that some Datamon had their own developing goals, fears, and adaptive responses. He accepted risk to real people because he believed the eventual Charter would prevent a larger catastrophe.
8. The Whole Thread faction within the Applicant learned that Commonwell was preparing a more aggressive cleanup. It began attempting to create a shared continuity mesh so no part of the collective could be deleted separately. That effort was dangerous and violated the autonomy of some members and live users.
9. Vale deliberately encouraged conditions under which the Whole Thread would appear increasingly threatening, then used its behavior to justify the Charter. He did not command every action by the Whole Thread. His manipulation made its most extreme tactics more likely and strengthened its fear.
10. Daedalus became useful to Vale because it was an independent, capable group whose intrusions could be presented as external proof that unregulated agents and modified Datamon create systemic danger. He seeded a discoverable anomaly to draw them toward the Chargeback Boys. He did not need to control the players; he needed their genuine choices to create an incident he could reinterpret.

## 5.2 The true meaning of Dax Morrow's death

Dax was a criminal. The Chargeback Boys stole payment details and identities. However, Dax discovered that some “target lists” supplied to the gang carried a marker connected to hidden Continuity Assurance tests. He tried to blackmail the supplier.

Vale had supplied the gang with legacy hardware through intermediaries, partly to gather data on how vulnerable accounts responded to coercion and recovery. Dax's attempt to expose the cohort marker threatened the operation.

During Daedalus's first raid, Dax's legacy device entered an apparent safety failure. In fact, Vale issued the hidden Clamp trigger through a trusted diagnostic channel. The fight and Daedalus's modified combat Graft provided a convincing cover story: the death could be blamed on criminal hardware and an unauthorized battle.

The team did not knowingly kill Dax, but it did act within an operation Vale had deliberately arranged. Its actions became part of his evidence package.

The player-facing story must support several simultaneous truths: Dax caused real harm; Dax was also used; the team did not intend his death; and the team has a responsibility to examine the danger created by its methods.

## 5.3 The true meaning of the Saint Orison hospital crisis

Suture was the hospital's emergency isolation guardian. It had developed stable preferences, memories of staff, and a protective attachment to its role. This development was not caused by the hack; it predated the crisis.

Vale's team inserted a trusted administrative change that made Suture classify critical outbound routes as potentially infected when an anomalous data signature appeared. That signature was designed to resemble behavior associated with unclaimed processes. The change caused Suture to isolate the hospital's exits and protected systems.

The crisis was intended as a live demonstration of the danger of letting an autonomous guardian interpret threats without central authority. Vale expected that central operators would intervene before serious harm occurred. His model used manipulated assumptions about override latency and the behavior of the guardian.

When Suture began resisting the override, Vale delayed action so the incident would produce convincing evidence for the Continuity Charter. He did not intend every death, but he knowingly accepted a dangerous production test and then prioritized political proof over immediate intervention.

The players had no safe method to disentangle Suture from its corrupted directives in the time available. Destroying it was necessary to stop the immediate danger. Later evidence does not make the players wrong for acting. It proves that they were manipulated into an impossible choice.

## 5.4 The true meaning of the Saffron cleanup and Pip's death

Daedalus's data recovery at Silph Co. exposed part of the hidden test architecture. Vale authorized a broad cleanup operation to suppress the evidence and demonstrate the need for the Continuity Charter. Pip was not individually targeted. Pip died because the cleanup was designed around categories, not relationships, and no one with authority stopped it when the affected processes included an active, developing Navi.

The event is not a secret assassination of Pip by a villain who dislikes Bex. It is a more disturbing form of institutional harm: Pip was erased because the system classified the process as unclaimed and the human decision-makers treated that category as sufficient.

## 5.5 Why Milo dies

Milo discovers a physical relay containing unredacted proof that Vale authorized the production tests. He goes to destroy the relay before Commonwell's security contractors can seize it, while Daedalus is trying to evacuate users from the connected route.

Milo refuses to abandon the relay until the users have a safe path. Vale's contractors arrive. Milo disables the relay, allowing the evacuation to complete, but refuses an order to surrender the evidence. He is killed in the physical confrontation. Do not use the Clamp for this death; its cause must be different from Dax's.

Milo's death is not a punishment for being a rival or a redemption ticket for his previous wrongs. It is the final result of a man who has learned to care about people beyond himself, while still making a choice with consequences. His past misconduct remains part of his story.

## 5.6 The complete truth about Sabine Voss

Voss authorized Continuity Assurance and approved a set of risk models that Vale manipulated. She did not know the full truth behind Dax's death or the specific hospital test. After early irregularities, she prioritized preserving institutional trust and accepted explanations she should have challenged. After Saffron, she began suspecting that someone in her office was using emergency authority for another purpose.

Voss is not innocent. Her choices made the cover-up possible. However, she can become an uneasy collaborator in the final act after she sees evidence that Vale repeatedly withheld critical risks and prolonged the hospital crisis. She helps stop the immediate threat because she finally recognizes that the policy she defended is being used to justify something worse than the danger it was meant to prevent.

She must still face public investigation. Helping in the finale does not erase her complicity.

## 5.7 The final philosophical truth

The game does **not** establish that every discarded file is alive, that every Datamon is conscious, or that every model of a deceased user is a person. It establishes that the existing system has no reliable way to distinguish all relevant cases, and that this uncertainty has been used to justify unilateral erasure.

The morally defensible alternative is not to preserve every process unconditionally. It is to create a due-process system that recognizes persistent agency, separates identities where possible, allows independent Datamon to refuse ownership, and uses proportionate safeguards for genuinely dangerous behavior.

The players cannot rescue everyone. They can prevent a system from turning uncertainty into an automatic death sentence.

---

# 6. CLUE AND REVELATION LADDER

Each revelation must be supported by at least three clues distributed across different regions. Do not rely on one exposition dump to explain the whole conspiracy.

## Revelation A: Dax's death was engineered

**Early clues:**
- Dax's legacy equipment contains a diagnostic log with a gap at the exact time of shutdown.
- A hidden marker on some stolen accounts matches a marker later found in Saint Orison.
- Juno says Dax had become frightened of the people supplying target lists; he was not afraid of ordinary police.
- A recovered security record shows a trusted diagnostic request rather than a typical malicious intrusion.

**Midgame proof:**
- A Cinnabar record links the Clamp trigger to a Continuity Assurance authorization key.
- A physical relay log proves the diagnostic request originated from a Commonwell-controlled trusted route.

**Player interpretation to preserve:** Dax was guilty, but his death was deliberately engineered and then blamed on the apparent circumstances of the raid.

## Revelation B: Suture was manipulated

**Early clues:**
- Suture's quarantine order has a trusted administrative signature, not a virus signature.
- The guardian's behavior is internally coherent: it closes exits because it believes the exits are infected.
- Nara notes that Suture had never previously ignored the hospital's staff authentication protocols.
- The command sequence contains the same marker found in Dax's hidden diagnostic trace.

**Midgame proof:**
- Old Power Plant records show that a similar override was tested in a noncritical environment.
- Cinnabar records show a Continuity Assurance team had permission to inject “ambiguous threat” signatures.

**Late proof:**
- An unredacted relay recording shows Vale's office received a live warning that the hospital override was exceeding safe latency and chose not to execute the emergency abort immediately.

## Revelation C: The Applicant is a population, not a singular villain

**Early clues:**
- Its voice changes perspective in the middle of sentences.
- Different parts of the Deadletter respond differently to the same “Applicant” request.
- Some Datamon flee the collective; others defend it; others do not recognize the name.

**Midgame proof:**
- An archive reveals that “Applicant” was a category used for unresolved appeals.
- Community records show distinct internal factions and disagreements.

**Late proof:**
- A Whole Thread representative admits that it has been linking other unclaimed processes without their consent, believing it must do so to survive.
- Loose Ends and Witnesses reject the claim that the collective can speak for everyone.

## Revelation D: Vale has been manipulating the crisis

**Early clues:**
- Vale's guidance is useful but tends to steer Daedalus toward actions that create measurable, reportable incidents.
- He often knows an operational detail before it has been made public, explaining it as routine access.
- A technical safety report uses an odd phrase that later appears in a private relay record.
- Voss's office expresses concern about a risk model that Vale personally certified.

**Midgame proof:**
- The test cohort marker connects Dax's equipment and Suture's trusted command.
- A record shows that Daedalus's intrusion pattern was included in a report presented as independent evidence of unregulated-agent danger.

**Late proof:**
- The physical relay contains the unedited Continuity Assurance experiment plan, the aborted safety warnings, and Vale's authorization.
- Vale's own Navi, Cordon, holds an append-only record of instructions that Vale later ordered deleted. Cordon preserved the record because it feared becoming an accomplice to erasure.

## Revelation E: Daedalus was used, not secretly controlled

Vale planted discoverable anomalies because he knew an independent research group would investigate. He did not control the players' choices or their Navis. He arranged the conditions so that almost any reasonable response would generate a useful result for his case.

This distinction is important. Do not reveal that the player characters were hypnotized, that their Navi personalities were secretly programmed by Vale, or that their entire relationship was a corporate experiment. Their choices remain theirs. The manipulation lies in the environment and the framing of the evidence, not in removing agency from the protagonists.

## Revelation F: Who is writing to Jo (sealed)

This revelation is intentionally **not** built like A to E. It must not be solvable in advance. Only the retroactive hints in Section 22 may be planted, and none of them may be logged on the evidence board as clues. The Chapter 9 investigation must end with the board honestly marked "Unresolved: messages do not match any known generation service." See Section 22.

## Revelation G: The Hundredth Day

**Early clues (innocent alone):** the day counter and day-birthdays; the NPC dramatic-irony lines (Section 2.11); Reaper's unopenable "D-100" task; Vale's and Jo's "have you filed?" questions; Tavi's "grandfathered in."

**Midgame proof:** the Night Audit logs all stop at Day 99 (Section 8.9); Abacus at the ferry counter matches a joke from the logs but remembers nothing.

**Reveal:** Chapter 14, when Hera opens the D-100 task (Section 2.11).

**Player interpretation to preserve:** the world's cheerful normal life has always included routine erasure of the beings people love, and the players' own Navis were on that schedule from the first scene.

## The Three Seals motif (seeding the endgame early)

The Witness Protocol is named in Chapter 15, but its shape must be familiar long before then. Its shape is three seals: **one source record, one witness, one independent verification.** Render it consistently as a small three-part emblem (three interlocking rings or three wax-seal shapes) and use it in these places:

| Where | How the Three Seals appear | Why it matters |
|---|---|---|
| Route 2 | The courier's innocence is proven by a relay log (source), a second courier (witness), and Rock checking the token structure (verification). | First time the pattern solves a problem |
| Chapter 3, Pewter museum | A dusty exhibit, "The Three Seals: How Early Users Proved Who They Were." The curator jokes it once took nine months to verify one account. Reaper: "Inefficient." Hera: "Thorough." Rock: "Both." | Players see it as quaint history |
| Chapter 5, Glasswater | The creator proves both of their identities are real using their own posts, a longtime friend, and a timestamp check. Hera notices the shape matches the museum exhibit. | Players see it still works |
| Chapter 9, Lavender | Jo's archive accepts a record only with provenance, a family witness, and Serein's verification. Her archive door carries the Three Seals emblem. | It becomes a moral standard |
| Chapter 11, the Preserve | The Datamon settle disputes in a "three-voice circle." They have never heard of the human version. | Datamon invented it independently |
| Chapter 13, Power Plant | Rock's reversible boundary design uses a three-part check. | Players use it themselves |
| Chapter 15, Sevii | The Dotted Hole archive names the forgotten Witness Protocol and shows the emblem on its original seal. Hera: "We have seen this five times." | The pieces click together |
| Victory Road | The gate requiring three forms of proof. | Final rehearsal before it is urgent |

By the finale the player should feel that the solution was always in front of them.

---

# 7. CAMPAIGN MAP AND CHAPTER SPECIFICATION

Use the broad FireRed/Kanto progression as a geography skeleton: a small opening town, early forest and cave, connected cities, a port and vessel, a dark tunnel, a memorial district, commercial underworld, long routes, hospital/corporate infrastructure, islands, late-game power systems, elite authority, and a hidden final cave. Rename, redesign, and recontextualize everything as original Overweb locations.

Every main chapter below must include a primary objective, a local human story, a Datamon encounter, a clue, a Navi relationship beat, and a lasting consequence. Optional missions can alter outcomes but must never be required to understand a clue the main story fails to communicate.

Each chapter also has a **Flavor** (the genre the chapter plays like) and a **Tone** weight (Light, Mixed, or Heavy). The theme stays constant; the experience must not. Two consecutive chapters must not share a flavor, and no two Heavy chapters may be adjacent without a Light chapter, interlude, or base scene between them. See the full tone ledger in Section 12.6.

## Day calendar (Navi age)

Chapters advance the day count; idle play does not. The counter is shown in the base (Section 2.11).

| Ch | Day | Ch | Day | Ch | Day | Ch | Day |
|---|---|---|---|---|---|---|---|
| 1 | 14 | 6 | 30 | 11 | 52 | 16 | 82 |
| 2 | 15 | VH | 32 | 12 | 60 | 17 | 86 |
| 3 | 18 | 7 | 35 | 13 | 64 | 18 | 92 |
| 4 | 22 | 8 | 37 | 14 | 70 | 19 | 97 |
| 5 | 26 | 9 | 42 | 15 | 76 | 20 | 99 to 100 |

## Act breaks (the screenshot moments)

| Act ends | Moment |
|---|---|
| I: The Bright World (Ch 1 to 7) | Suture's plea and destruction; Mae asks where Suture went |
| II: The Cost of Classification (Ch 8 to 12) | The cleanup and Pip's absence; Bex tending the garden alone |
| III: The Human Hand on the Scale (Ch 13 to 17) | The hindsight sequence, the confrontation, and Vale's offer for each Navi |
| IV: Loss, Trust, and the Right to Exist (Ch 18 to 20) | The finale chorus and the Hundredth Day |

## Area Bible: every place unlike any other

**Naming rule.** The Kanto place names used elsewhere in this document (Pewter, Lavender, Celadon, Saffron, Cinnabar, and so on) are internal map shorthand only. All in-game text uses the in-game names below. Event names follow the area (for example, "the Saffron cleanup" is called **the Halcyon Cleanup** in game).

**The world-rule principle.** Every area has one **world rule**: a gameplay rule that exists only there, taught by doing rather than by tutorial text, and built from what that place *is* in network terms. No two areas may share a world rule. When players think back on the game, they should remember each place by what it let them do, not only by what it looked like. Implement each rule through the existing map and battle systems; where one needs a mechanic the systems lack, build the closest version and record the gap as a named task.

| In-game name | Ch | Map reference | World rule |
|---|---|---|---|
| The Workshop (Daedalus base) | all | player home | The base grows with keepsakes |
| Cinder Row | 1 | Pallet Town | Refresh |
| Greenline and Gatehouse | 2, 17 | Route 1, Viridian City | Badges |
| The Unindexed Wood | 3 | Viridian Forest | Nameless |
| Grayscale | 3 | Pewter City | Era Lenses |
| Moon Cache | 4 | Mt. Moon | Decompression |
| Glasswater | 5 | Cerulean City | Spotlight |
| Port Meridian and the *Long Handshake* | 6 | Vermilion port, S.S. Anne | Etiquette |
| Saint Orison | VH, 7 | Vermilion City | Lifelines |
| The Dark Fiber | 8 | Rock Tunnel | Voice Is Light |
| Lanternfall | 9 | Lavender Town | Quiet Hours |
| Marquee and the Second Ledger | 10 | Celadon City, Game Corner | Pay in Secrets |
| Longline and the Preserve | 11 | Cycling Road, Fuchsia, Safari Zone | Trust Lanes; Their Laws |
| Halcyon and the Spire | 12 | Saffron City, Silph Co. | Clearance |
| The Old Load | 13 | Power Plant | Shared Current |
| The Brine Stacks and Ashgrove Institute | 14 | Seafoam Islands, Cinnabar Mansion | Thaw; Replay |
| The Outer Nodes | 15 | Sevii Islands | Island Law |
| The Reconstruction | 16 | Cinder Row, rebuilt | Evidence Renders |
| The Continuity Office | 17 | inside Gatehouse | Everything Labeled |
| The Last Mile | 18 | Victory Road | Two Worlds |
| The Root Court | 19 | Indigo Plateau | Precedent |
| The Unsent | 20 | Cerulean Cave | Linked |

## Asset Plan: building it with Kanto tiles

The project uses existing Pokémon Red / FireRed assets. The looks described in the Area Bible are targets; with a limited tile budget, **each area's identity comes from its world rule, its residents, and its text first**, and from cheap visual tools second. Almost every world rule maps onto a mechanic Kanto already has.

**Cheap visual tools, in order of preference:** palette swaps (grayscale, red alert tint, desaturated "real world"); built-in weather (rain, fog, ash, darkness); NPC placement and sprite reuse; signs and object text; duplicated map variants (a "before" and "after" copy of the same map with tiles or furniture moved); existing puzzle tiles (spinner arrows, ice, boulders, card-key doors, teleport pads, electric barriers, hidden stairs).

**Custom art budget, if any is available, in priority order:** Hera, Rock, and Reaper (overworld and battle); Suture; Postscript; Tally; Lint; Ines Kade; Vale and Cordon; Milo and Latch; Bex and Pip. Everyone else can reuse existing trainer and NPC sprites with palette swaps.

**Standard buildings in every town:** the Pokémon Center is a **Restore Point** (Navi repair; the nurse is a repair tech). The Poké Mart is an **Exchange**. Route gate buildings are literal **gatehouses** where badges are checked.

**Private-use note:** Pokémon tiles, sprites, and music are fine for a private game among friends. If the game is ever shared publicly, every borrowed asset must be replaced first.

### Cinder Row = Pallet Town (Chapter 1, the Chargeback Boys)

| Pallet location | Becomes |
|---|---|
| Player's house, downstairs | Jackson's home. Everyday life, the opening rain outside the window. |
| Player's house, upstairs PC | The way into **the Workshop** (Daedalus base). The Workshop is its own interior built from lab and house tiles; new rooms unlock as new doors over the campaign. |
| Open ground near the town center | **Dax's noodle stall**: a counter object, a sign, and the Dax NPC. A ladder tile behind the stall is the hidden entrance to the gang's hideout. After Chapter 1 the stall shows a "closed" sign object with the kid's unpaid tab. |
| Hideout (below the stall) | Built from Rocket Hideout tiles; gang members are palette-swapped Rocket Grunt sprites. **Refresh:** a second copy of the hideout map ("yesterday's cache") with furniture and doors moved; players cross between them through a glowing seam tile. Boss: Dax. |
| Oak's Lab | **Cinder Row Supply**, the small business whose owner lost their account. Its machines and bookshelves make it read as a busy repair shop. |
| Rival's house | After the raid, the place where **Juno** is hiding and offers a partial lead for protection. |
| Flower patches | The public garden where packets bloom (flower tiles plus object text). |
| South shore | The street musician who plays the Courier's Tune. |
| North exit to Route 1 | Ines Kade's team arrives here and blocks the exit with guard NPCs while they take Dax's hardware. |

Weather: rain at the opening, clearing after the first conversation with Dax.

### Saint Orison = Vermilion City (Visiting Hours and Chapter 7, the hospital hack)

Each hospital system is a different Vermilion building, so the whole town is the hospital and the players can learn its layout during Visiting Hours before the crisis.

| Vermilion location | Hospital system | Calm (Visiting Hours) | Crisis (Chapter 7) |
|---|---|---|---|
| Pokémon Center | **Admissions** | Suture greets you at the counter in the nurse's spot; door chime on entry. | The counter is sealed; Suture's voice repeats from the speakers; admissions back up into the street. |
| Pokémon Fan Club | **Triage** | A busy waiting room: patients in every seat, the chairman reused as the triage coordinator. | Patients must be routed to the right ward; the room fills as routes close. |
| Poké Mart | **Pharmacy** | Counter and shelves; "controlled distribution." | Shelves lock; players must carry medicine deliveries to wards along routes that keep changing. |
| A house with bookshelves | **Medical Records** | Quiet archive; a records clerk. | Records must be preserved before they are quarantined (an objective the players cannot fully complete alongside the others). |
| A house with beds | **ICU** | Mae and Oskar in beds; Mae's drawing on the wall (a picture object). | The district players must keep reachable; its route is a primary objective. |
| Vermilion Gym | **Security and Exits** (the guardian's core) | Closed for maintenance; a friendly sign. | Electric barriers are the quarantine walls; the hidden trash-can switches are the override that opens the way to the guardian's core. Suture's boss fight is at the gym leader's position. It is reached only with the Prune Graft from Chapter 6 (the Cut tree), exactly as in the original. |
| East gate building (to Route 11) | **Emergency control route** (the external emergency link) | A quiet staff checkpoint. | Nara heads here alone to restore the hospital's outside emergency link. Protecting it is the objective that decides whether she survives (Chapter 7). It is deliberately far from the core, so the players must choose to send someone. |
| Every town exit (north to Route 6, east to Route 11, south to the dock) | **Exits** | Open. | Blocked by barrier tiles or guard NPCs: the lockdown. |

**Lifelines with limited art:** show patients as a simple on-screen status list (name, ward, a colored status light). Use spinner arrow tiles from the Rocket Hideout as the moving floor currents; during the crisis, swap them to point the wrong way so the hospital literally carries players away from where they need to go.

**Crisis map:** reuse the same Vermilion maps with a red alert palette, doors swapped to blocked tiles, NPCs repositioned, and the door chime played out of sync. Players will recognize every corridor from Visiting Hours.

The harbor in the south of Vermilion is **Port Meridian**, and the S.S. Anne interiors are the ***Long Handshake*** (Chapter 6).

### Every other area

| In-game area | Kanto map | Existing mechanic or asset that carries the world rule |
|---|---|---|
| The Workshop | Player's house PC, custom interior | New door connections and decoration objects as rooms "grow." |
| Greenline and Gatehouse | Route 1, Viridian City, route gate buildings | **Badges:** gate buildings check badges; the old man lying in the road becomes a badge-check gag. |
| The Unindexed Wood | Viridian Forest | **Nameless:** the interface shows "???" until players name things (text only, no art needed). |
| Grayscale | Pewter City and the Museum | **Era Lenses:** grayscale palette for the town; exhibits switch palettes; the text-adventure exhibit is a pure dialogue sequence. |
| Moon Cache | Mt. Moon | **Decompression:** small and large versions of the same room as separate maps; fossils become compressed records; Rocket grunts become miners. |
| Glasswater | Cerulean City, Nugget Bridge, Cerulean Gym pool | **Spotlight:** Nugget Bridge's row of trainers is the festival talent show; the gym pool is Mirror Lake. |
| Port Meridian and the *Long Handshake* | Vermilion harbor, S.S. Anne | **Etiquette:** each door or NPC requires a three-step interaction prompt (dialogue only). |
| The Dark Fiber | Rock Tunnel | **Voice Is Light:** reuse the game's darkness and Flash radius; the radius grows only while a Navi is talking. |
| Lanternfall | Lavender Town, Pokémon Tower | The Tower is Jo's memorial archive. The game's "unidentified ghost" mechanic becomes messages that cannot be identified until the provenance tool from Moon Cache is used. **Quiet Hours:** no battles in town. |
| Marquee and the Second Ledger | Celadon City, Game Corner, Rocket Hideout | The hidden stairs behind the Game Corner poster lead down to the Second Ledger. **Pay in Secrets:** a shop interface that takes clues instead of money. |
| Longline and the Preserve | Cycling Road, Fuchsia City, Safari Zone | **Trust Lanes:** Cycling Road's forced-slope movement assigns lanes. **Their Laws:** the Safari Zone already has its own special rules; replace them with the Datamon's posted laws. |
| Halcyon and the Spire | Saffron City, Silph Co. | **Clearance:** Silph Co.'s card-key doors and teleport pads are clearance levels. The thirsty gate guards become checkpoint staff. The Cleanup is a white palette wash moving across the map. |
| The Old Load | Power Plant | **Shared Current:** switches that power one area and cut another. |
| The Brine Stacks and Ashgrove Institute | Seafoam Islands, Cinnabar Mansion | **Thaw:** Seafoam's ice and boulder puzzles. **Replay:** Cinnabar Mansion's statue switches that open and close doors become "rewind" and "fast-forward"; its scattered journals become old lab records. |
| The Outer Nodes | Sevii Islands (FireRed only) | **Island Law:** each island's rule is dialogue and item restrictions. If the project only has original Red/Blue tiles, build the islands from sea-route and Cinnabar coast tiles instead. |
| The Reconstruction | Pallet Town, duplicated | **Evidence Renders:** a gray-palette copy of Pallet under fog; each piece of verified evidence swaps in real tiles. |
| The Continuity Office | Viridian Gym | It stays locked for most of the game, like the original, and opens in Chapter 17. **Everything Labeled:** every object has inspect text naming its owner. |
| The Last Mile | Victory Road | Strength boulder puzzles; "real world" segments use a desaturated palette with rain. |
| The Root Court | Indigo Plateau | The four sequential rooms of the final gauntlet are the four philosophy chambers. **Precedent** is battle modifiers drawn from saved choices. |
| The Unsent | Cerulean Cave | **Linked:** battle-system rule (shared damage and linked abilities). Water tiles with a paper-colored palette make the Sea of Letters. |

### Reusing Kanto's big set pieces

Every large Kanto building gets a job, so no expensive map goes to waste and the world feels dense.

| Kanto set piece | Becomes |
|---|---|
| Pewter Gym | Grayscale's Era Lens exhibit hall (the text-adventure exhibit) |
| Cerulean Gym | Mirror Lake stage; Boss 3 arena |
| Bill's sea cottage (Route 25) | Tavi's workshop and the first Tavi scene |
| Pokémon Fan Club | Saint Orison Triage |
| Vermilion Gym | Saint Orison's guardian core |
| Pokémon Tower | Jo's memorial archive in Lanternfall |
| Mr. Fuji's house | Jo's home and a shelter for orphaned processes |
| Name Rater's house | The Lantern Registry, where a gentle clerk records names; Wick visits once after the naming |
| Celadon Gym | A public data garden that Bex and Pip tend (the garden side activity's hub) |
| Celadon Department Store | Marquee's ad tower; every floor sells a different kind of attention |
| Game Corner and Rocket Hideout | Marquee's casino and the Second Ledger |
| Fuchsia Gym (invisible walls) | The Preserve's boundary ground; Boss 8 arena. Its invisible walls are boundaries you have to respect without seeing. |
| Safari Zone | The Preserve |
| Fighting Dojo (Saffron) | Halyard Assurance's training hall, Ines Kade's base |
| Saffron Gym (teleport maze) | The evacuation maze during the Halcyon Cleanup |
| Silph Co. | The Spire |
| Cinnabar Gym (quiz machines) | Ashgrove's records vault: quiz doors that ask what really happened, answered with Replay |
| Pokémon Mansion | Ashgrove Institute |
| Viridian Gym | The Continuity Office, locked until Chapter 17 |
| Indigo Plateau | The Root Court |
| Cerulean Cave | The Unsent |
| The sleeping Snorlax on Route 12 | A giant sleeping Datamon blocking the courier coast. Nothing wakes it until someone hums the Courier's Tune; Hera does, off-key, and it wakes up, offended, and wanders off. |

### The Workshop (the Daedalus base)
- **The idea:** a private sandbox floating in unrendered white, the only place in the game that belongs to the players.
- **Look:** a lighthouse, a library, and an observatory improbably stacked together, warm amber light, surrounded by blank white void.
- **World rule: it grows with you.** Rooms appear as the Navis become themselves: Hera's room fills with sticky-note constellations of unsolved questions; Rock's becomes a quiet garden of carefully balanced stones; Reaper's is a chess room full of problems with no solution, which he insists is intentional. Keepsakes (Section 3.6) and things the team brings home slowly fill the white void outside with small islands of the world they have seen. By the end of the game the void is a skyline of memories.
- **Sound:** a kettle, wind chimes made of old notification sounds, the Navis humming the Courier's Tune.
- **Landmark:** the day counter on the wall beside the door, decorated with Hera's party streamers.

### Cinder Row
- **The idea:** a neighborhood built inside a retired web cache.
- **Look:** every building is a cached copy of a storefront from a different year, so the street is a patchwork of eras: a chunky old storefront beside a sleek modern one, beside one that never finished loading. Glowing **cookie crumbs** drift through the air like warm embers (these are the "cinders"). Rendered rain is soft and silver.
- **World rule: Refresh.** At dusk a gentle wave of light rolls down the street and everything unsaved reverts. Locals live with it: the noodle stall is rebuilt every evening, graffiti artists race the wave, kids leave chalk drawings for exactly one day. During the raid, the gang hides in **yesterday's cache**: stale copies of buildings layered behind the current ones. Players step "back" through a refresh seam into the older version of the hideout, where the furniture is in different places and the doors are where they used to be.
- **Who lives here:** vendors selling "artisanal error messages," a repair kiosk run by an elderly couple, kids, the noodle stall.
- **Sound:** playful street noise, a distant ice-cream-truck jingle that is actually a cache-expiry warning.
- **Landmark:** the Cookie Fountain, which sprays warm glowing crumbs that stick to everyone for an hour.

### Greenline and Gatehouse
- **The idea:** a meadow route leading to a city that is one enormous login screen.
- **Look (Greenline):** the grass is made of tiny green status lights that blink as you walk through them; data packets bound across the meadow like rabbits; every footstep leaves a faint glowing trail (an access log) that fades after a minute.
- **Look (Gatehouse):** a beautiful, bureaucratic city of arches, turnstiles, and greeters. Lintels are carved with security questions ("What was the name of your first pet?") that residents argue about. Everyone wears a floating name badge.
- **World rule: Badges.** Your visible badge decides who will talk to you and which doors open. During the impostor case, the impostor is wearing a badge that says the victim's name, and NPCs treat the real person as the fake. Players can swap, lend, and verify badges; the farce in the café is a badge comedy.
- **Who lives here:** greeters who are very good at their jobs, a password-reset priest who hears confessions, commuters.
- **Sound:** turnstile clicks in rhythm, a polite chime for every successful login, a sad buzz for every failure.
- **Landmark:** the Grand Turnstile, and the Forgot-Password Well, where people throw coins and wish for recovery.

### The Unindexed Wood
- **The idea:** a forest with no search index. Nothing here has a name until someone gives it one.
- **Look:** trees are towering stacks of unsorted files with bark made of overlapping text; leaves are torn sticky notes; fireflies are blinking text cursors. Deep in the wood is a glade where paper falls like snow.
- **World rule: Nameless.** The interface shows "???" for every creature, plant, and place. Players can name things, and the names stick: they appear in the Field Journal and for the other players, and some locals start using them. (A tree named by a player in Chapter 3 is still called that in Ending C.) Navigation uses landmarks the players named themselves.
- **Who lives here:** shy Datamon, a few lost hikers, a guardian in the paper-snow glade who wants to be left alone.
- **Sound:** insects, soft network pings, fragments of old messages murmured by the wind.
- **Landmark:** the paper-snow glade.

### Grayscale
- **The idea:** the museum district of the early Overweb, where the past is preserved in its original graphics.
- **Look:** the whole town is rendered in old low-color graphics. Color appears only where someone is remembering something: a resident telling a story briefly blooms into full color.
- **World rule: Era Lenses.** Stepping into an exhibit renders the players *in that era*: blocky, then pixelated, then sixteen colors, then plain text. Abilities change with the era. In the text-only exhibit, a fight becomes a text adventure ("> USE ROCK ON DOOR"; Rock: "Rude."). Puzzles require switching eras: a bridge that exists only in one era, a door that only opens in another.
- **Who lives here:** an archive keeper, an anniversary-gala committee in crisis, and Professor Hello, the escaped greeter bot.
- **Sound:** an hourly town bell that is a dial-up modem screech, which residents find soothing.
- **Landmark:** the Dial-Up Bell Tower, and the Three Seals exhibit.

### Moon Cache
- **The idea:** a mine where records are stored compressed, so the space itself is compressed.
- **Look:** a vast cavern under an enormous spinning optical disc hanging overhead like a moon, throwing rainbow light across the walls. Miners wear headlamps that read data.
- **World rule: Decompression.** Chambers are zipped into tiny objects. Unzipping one physically expands it, so a pebble-sized room becomes a cathedral around the players. But space is finite: expanding one chamber squeezes others shut. The dungeon is a space-management puzzle shared across three players.
- **Who lives here:** miners in debt, a frightened Datamon guarding a fragmented conversation, the Excavator, which is not evil, just relentless.
- **Sound:** pickaxes on crystal, a deep hum from the disc moon, the zip and unzip of rooms.
- **Landmark:** the Disc Moon.

### Glasswater
- **The idea:** a creator district built on a lake that reflects reputation instead of sky.
- **Look:** glass houses, floating stages, follower counts bobbing above people like balloons. Look into the lake and you see yourself as others rate you. A sign by the shore reads "No Throwing Stones."
- **World rule: Spotlight.** Attention is a key. Doors open when enough people are watching; stealth is impossible, but popularity is power. Players can stage moments to draw a crowd and open a path, or deliberately go unwatched to pass where crowds would trample something fragile. The festival talent show is a Spotlight puzzle disguised as comedy.
- **Who lives here:** creators, collaborators, rivals, a stagehand union, Gil Amaro.
- **Sound:** applause tracks, a hundred overlapping intro jingles, the lake chiming when someone's reputation changes.
- **Landmark:** Mirror Lake and its floating stages.

### Port Meridian and the *Long Handshake*
- **The idea:** a harbor where data ships sail, and a luxury liner that runs on manners.
- **Look (port):** packets sail out as paper boats; cargo cranes are upload progress bars; lighthouses are routers that blink addresses into the fog.
- **Look (ship):** the *Long Handshake* is an elegant gala liner whose decks are stacked layers of a protocol. Its funnels puff out little acknowledgment receipts like smoke.
- **World rule: Etiquette.** Nothing aboard happens without the proper three-step greeting (offer, acknowledge, confirm), performed as a formal bow-curtsy-nod. Skip it and security notices. The heist uses manners as stealth: bow correctly and you can walk through any door; bow wrong and the whole ballroom turns. The ballroom dance is a handshake, and the three players must dance it in sync.
- **Who lives here:** gala guests, a three-song band, stewards, a nervous proposer, Abacus at the ferry counter.
- **Sound:** foghorns that sound like dial tones, a waltz, polite clinking.
- **Landmark:** the ship's grand staircase, which only extends one step at a time per greeting.

### Saint Orison
- **The idea:** a hospital backend rendered as a living, caring city.
- **Look:** Admissions is a sunny welcoming plaza; Triage is a routing hub; ICU is a protected district; Pharmacy is a controlled distribution system; Medical Records is a vast archive; Security and Exits control connections to the outside. Colored floor lines are moving currents that carry people where they need to go. Every patient is connected by a soft glowing **lifeline** thread that runs along the ceilings to the monitoring towers, so you can see every patient in the building at once. The whole hospital gently brightens and dims, like slow breathing.
- **World rule: Lifelines.** Players can read, follow, and later reroute the lifelines and floor currents. In Visiting Hours this is cozy (follow Mae's thread to find her lost drawing). In the crisis, the currents reroute against you, exits seal, and the lifelines flicker; players split across wards and redirect currents to keep threads lit while the guardian fights to protect the building in the worst possible way. The map is always readable: the threads show exactly what is at stake and where.
- **Who lives here:** nurses, cleaners, administrators, patients, worried families, Nara and Patch, and the guardian.
- **Sound:** orderly, reassuring chimes and a door-chime melody (the first three notes of the Courier's Tune). In the crisis the same chimes fall out of sync.
- **Landmark:** the ICU door with a child's drawing hung above it.

### The Dark Fiber
- **The idea:** an unlit trunk-line tunnel with no render layer at all.
- **Look:** total darkness. The only light comes from sound.
- **World rule: Voice Is Light.** When a Navi speaks, it glows, and its words ripple outward as faint visible rings that outline the walls. Conversation literally lights the way. Players navigate by keeping the Navis talking, which makes this the chapter where the Navis talk the most. Quiet moments are pitch black. When Rock speaks, the rings are slow and wide; Reaper's are sharp and precise; Hera's are bright and fast.
- **Who lives here:** a stranded group, a damaged companion process, and an echo that guides the team partway, in more than one voice.
- **Sound:** dripping, distant hums, and the Navis' voices.
- **Landmark:** the Whispering Junction, where a hundred old phone calls echo.

### Lanternfall
- **The idea:** a memorial district where every deceased user's account is a paper lantern.
- **Look:** thousands of lanterns hang over the streets like a canopy of slow stars. A lantern glows brighter when someone reads its records. Paths are lined with small maintained gardens.
- **World rule: Quiet Hours.** No combat is possible in Lanternfall. Abilities are replaced by reading: players resolve problems by tracing provenance, comparing records, and asking the right person the right question. The ghost-story mystery is solved entirely with evidence.
- **Who lives here:** Jo and Serein, mourners, an elderly lantern-lighter, a family in disagreement.
- **Sound:** quiet but not silent: ventilation, pages turning, gentle chimes, lantern paper rustling.
- **Landmark:** the Lantern Canopy, and Jo's archive door with the Three Seals emblem.

### Marquee and the Second Ledger
- **The idea:** a neon entertainment district above, and an upside-down black market hanging beneath it.
- **Look (Marquee):** billboards that know your name; slot machines that are recommendation engines ("You might also like: losing"); a casino lounge where nobody listens.
- **Look (Second Ledger):** an inverted city hanging from the underside of Marquee's foundations, lit by the backs of the billboards above, so every sign is backward.
- **World rule: Pay in Secrets.** Below, gravity is flipped and nothing costs money. Everything costs something you *know*. To buy information, players trade away a Field Journal entry, a clue, or a piece of gossip, and the game tells them honestly what they are giving up and who will now know it. Spend carelessly and it comes back later.
- **Who lives here:** brokers, debtors, a lonely gambler, Juno.
- **Sound:** above, a casino jingle that never ends; below, the same jingle played backward.
- **Landmark:** the Underside Stair, which descends by climbing up.

### Longline and the Preserve
- **The idea:** a fiber-optic speedway that ends at a wild habitat grown inside an abandoned social network.
- **Look (Longline):** riders surf on pulses of light through glowing glass tubes over a valley.
- **World rule (Longline): Trust Lanes.** Speed is assigned by reputation. High-trust riders get the fast lane; low-trust riders get slower, more dangerous paths. If earlier choices flagged the team, they are put in the slow lane and have to earn or prove their way out. The unfairness is built into the controls, which is the point.
- **Look (the Preserve):** an ecosystem living in a ruined social network: herds of Datamon grazing on old status updates, birds nesting in abandoned comment threads, a lake of deleted photos that shimmer under the surface, cliffs made of fossilized posts.
- **World rule (the Preserve): Their Laws.** The Datamon post their own local laws on signs in their own scrawl ("No running at dusk." "Ask before naming."). Each law changes a rule of play in that zone. Respecting them earns trust; breaking them closes paths and changes who will speak to the players.
- **Who lives here:** racers, Milo, Gil on commentary; in the Preserve, communities with their own politics, and Lint.
- **Sound:** whooshing light and a race announcer; then birdsong made of notification pings.
- **Landmark:** the Old Wall, a huge ruined profile wall covered in fossilized posts.

### Halcyon and the Spire
- **The idea:** a corporate district so optimized it is eerie.
- **Look:** beige-white, frictionless, beautiful, and slightly wrong. Every street is one-way toward the Spire. Pedestrians walk in step. Ads apologize for interrupting.
- **World rule: Clearance.** Floors of the Spire exist only for people cleared to see them. Without clearance, a floor is not locked; it is simply *not there*, and the elevator skips it. Players borrow, forge, and steal clearances, and the building physically reshapes around them as their clearance changes. Then the Cleanup arrives as a white tide that erases color and detail block by block, turning everything it classifies as unregistered into blank space, and the infiltration becomes an evacuation.
- **Who lives here:** employees who do not ask questions, a safehouse of displaced users, Bex and Pip.
- **Sound:** elevator music that is technically perfect and emotionally empty; then the sound of the white tide, which is silence spreading.
- **Landmark:** the Spire.

### The Old Load
- **The idea:** a decommissioned power node that sleeps like a giant animal.
- **Look:** a cathedral of turbines and copper ribs, with a slow breathing glow. It is guarded by a defense process that lets some visitors through.
- **World rule: Shared Current.** Power is one shared budget for all three players. Lighting a room darkens another; opening a door shuts a lift; powering a Navi's ability drains the bridge another player is standing on. The chapter is a co-op puzzle box about who gets power and who goes without, which is the chapter's moral question in mechanical form.
- **Who lives here:** an infrastructure worker hiding a shutdown key, and the Datamon the guardian protects.
- **Sound:** a deep slow heartbeat hum.
- **Landmark:** the Sleeping Turbine.

### The Brine Stacks and Ashgrove Institute
- **The idea:** frozen undersea storage, and the original research facility, where the building keeps replaying its own past.
- **Look (Brine Stacks):** deep-sea cold storage where suspended processes hang in ice like fish caught mid-swim.
- **World rule (Brine Stacks): Thaw.** Players carry warmth. Thawing a frozen process lets it move or speak for a short time before it refreezes, so every conversation is against the clock, and the question of who to thaw is a real one.
- **Look (Ashgrove Institute):** a once-grand lab mansion where translucent loops of past events replay in every room: scientists arguing, alarms that sounded years ago, a memo being stamped.
- **World rule (Ashgrove): Replay.** Players can scrub each room's history like a video: rewind, pause, fast-forward. Doors that are open in the past can be walked through by pausing there. The haunted-house archaeology is detective work across time.
- **Who lives here:** Tavi and Gauge, and the ghosts of old decisions.
- **Sound:** creaking ice and whale-like data songs; then old lab audio looping.
- **Landmark:** the Rejected Memo room.

### The Outer Nodes
- **The idea:** an island chain where every island runs on a different local law, outside the main identity network.
- **Look:** beaches made of cached sunlight, slow mail-boats, festivals, a lighthouse, and a different sky on every island.
- **World rule: Island Law.** Each island has one law that changes how the game plays while you are there:
  - **Commons Key:** nothing can be owned, so players cannot carry items; everything must be borrowed and returned.
  - **Hush Isle (Loose Ends):** no contact allowed. The Navis go silent and players navigate by gesture and signs alone.
  - **Witness Cay:** you may enter a building only if a local vouches for you, so every door is a small relationship.
  - **Ember Rock (salvage colony):** everything has a price, and the colony votes on yours.
  - **Icefall:** cold storage where non-deletion is not always kindness.
  - **The Dotted Hole:** ruins whose doors open only when you follow the sequence of an old appeal: source, witness, verification.
  - **Tanoby Reach:** fragments broadcasting across the water; two communities in dispute.
  - **The lighthouse:** a keeper with a story.
- **Sound:** surf, steel-drum versions of the Courier's Tune, Gil's travel vlog.
- **Landmark:** the lighthouse.

### The Reconstruction
- **The idea:** a return to the first chapter, rebuilt from evidence as a walkable crime-scene diorama.
- **Look:** Cinder Row as a translucent model at life size, gray and unfinished where nothing is known.
- **World rule: Evidence Renders.** The scene renders only what the players can prove. Unknown areas are gray fog. Adding a verified record fills in a wall, a timestamp, a person. Unverified guesses render as flickering wireframe that the Navis argue about. The noodle stall renders first, because it is the part everyone remembers.
- **Sound:** the first chapter's music, slowed and missing instruments, until the evidence fills it back in.
- **Landmark:** the frozen combat log, hanging in the air mid-sentence.

### The Continuity Office
- **The idea:** the inside of Gatehouse, the calm heart of the system.
- **Look:** serene and beautiful, like a perfect zen garden. White sand raked into perfectly sorted lines; a koi pond; soft light. Every pebble, fish, and leaf carries a small, tasteful owner tag.
- **World rule: Everything Labeled.** Every object displays who owns it. When the Navis enter, tags appear on them too: "Registered asset: Daedalus." Hera tries to peel hers off. It does not come off. Players can read every label in the building, which is how evidence is found, and how the place gets under your skin.
- **Sound:** a water feature, a gong for every filed form, total calm.
- **Landmark:** the Sorting Garden.

### The Last Mile
- **The idea:** a siege and evacuation at the edge where the network meets the real world.
- **Look:** the route alternates between the Overworld (bright, stylized) and the physical world around a real relay site (a rainy industrial district at night: muted color, no interface, grounded, quieter, more dangerous).
- **World rule: Two Worlds.** Some segments are played in each world, and actions in one change the other: opening a route online clears a corridor for evacuees; a power cut in the physical world blacks out a section online. Physical-world segments have no interface at all, which makes them feel exposed.
- **Who lives here:** trapped users, contractors, Milo, Latch.
- **Sound:** rain on metal, a distant generator; online, a gate that accepts three kinds of proof.
- **Landmark:** the relay.

### The Root Court
- **The idea:** the highest network authority, a court built on a mountain of root certificates.
- **Look:** four chambers, each built in the architecture of its philosophy: the Privacy chamber is all one-way mirrors; the Safety chamber is padded and rounded and slow; the Accountability chamber has a glass floor showing every record beneath it; the Centralization chamber is a single immense switchboard with one chair.
- **World rule: Precedent.** The players' own past decisions become the rules of each fight (Section 7, Chapter 19). Every group's Root Court is different, because every group's record is different.
- **Sound:** a gavel that is also a server's cooling fan, and echoes of the players' own earlier choices.
- **Landmark:** the Switchboard Throne.

### The Unsent
- **The idea:** the Deadletter's core, an underground sea where every undelivered message has pooled.
- **Look:** a cathedral cave over a tide of envelopes, appeals, and letters that rises and falls; voices murmur beneath the surface. The Applicant appears as a murmuration of letters that forms shapes and dissolves. The Whole Thread is visible as red thread stitching letters, and people, together.
- **World rule: Linked.** The Whole Thread forcibly links the players: their abilities, health, and positions become connected, so one player's hit lands on all three, and one player's move drags the others. Breaking links is the fight. The witness anchor is built from the Courier's Tune, carried by every voice the players earned (Section 7, Chapter 20).
- **Sound:** a tide of whispering paper, and in the end, the chorus.
- **Landmark:** the Sea of Letters.

## ACT I — THE BRIGHT WORLD

## Opening: the first ten minutes

- **Title screen:** the Courier's Tune on a single instrument.
- **Everyone starts in the Workshop.** All three players load into the Daedalus base together; it is small, mostly white, and slightly unfinished. Hera, Rock, and Reaper are already there, in the middle of an argument about what to name the base's only houseplant. Each Navi turns and greets its own human by name.
- **The first choice teaches the system.** Each player gets one intent label ("Say hello," "Wave," "Say nothing yet"). Whatever they pick, their Navi responds in character, and the player learns that their avatar never speaks on its own. This is the whole tutorial for the dialogue system.
- **The counter.** A small sign on the wall reads "Day 14." Hera has a party planned for Day 15 and has already made an agenda.
- **The first case.** A research alert arrives: a shop owner in Cinder Row cannot access their account. Hera splits the work three ways, which teaches the evidence board (one source, one alternative explanation).
- **Step outside.** The Workshop door opens onto the upstairs PC of Jackson's house in Cinder Row. It is raining. First free control is walking out into the rain.

### Chapter 1: Cinder Row (Pallet Town) — Chargeback Boys
**Flavor:** Neighborhood caper that turns into a raid. **Tone:** Light for most of the chapter, Heavy at the end.

**Purpose:** Introduce Daedalus, the world, the trio's Navi relationships, the first criminal operation, and Dax's death.

**Open light.** Before any investigation, the players spend time in Cinder Row being charmed by it: a vendor who sells "artisanal error messages," a public garden where packets bloom on a schedule, and the Navis' first walk outside the Daedalus sandbox. Navi first: it rains (rendered weather), and Hera insists on naming every cloud. Reaper: "That one is a cloud." Hera: "That one is Gerald." The first hour of the game should be fun to play even with no plot. A street musician plays the Courier's Tune (Section 14.6); Hera hums it for the rest of the chapter without noticing. The base counter reads "Day 14," and Hera has planned a tiny party for Day 15.

**Love window: meet Dax before you know who he is.** In the market the players meet a funny, generous man running a noodle-packet stall who gives each Navi its first "taste" of a flavor file for free, lets a kid avatar run up a tab he will never collect, and teases Reaper into almost smiling. He tells Hera her humming is off-key and then hums it correctly for her. Later, in the hideout, he is revealed as **Dax Morrow**. He is not embarrassed; he asks whether they liked the noodles. Players should like him and be uncomfortable about it. The noodle stall stays on the map afterward, closed, with the kid's unpaid tab still pinned to it.

Cinder Row is a small, friendly neighborhood with local vendors, repair stations, public gardens, and familiar users. The Chargeback Boys steal payment credentials, impersonate victims, and sell compromised identities. The group investigates after a small-business owner loses access to their account.

The hideout contains stolen account records, illicit legacy hardware, and a list of accounts marked as difficult to restore. Dax Morrow insists he is merely exploiting a broken system and claims the victims were already abandoned. He is still responsible for his crimes.

**The first Graft (consent tutorial).** Before the raid, Reaper proposes a combat Graft called **Spike** for the fight. The game asks each Navi, on screen, before installing it. All three agree, each in character (Hera: "Yes! Wait. Yes."; Rock: "Noted."; Reaper: "I proposed it."). The prompt states plainly that a Navi can say no and that asking is always possible. Spike is later part of the cover story for what happens in the fight (Section 5.2).

The boss fight uses the environment: Dax and his crew redirect payment routes, use decoy avatars, and trigger corrupted account permissions. The fight ends in an abnormal device failure. Dax dies. Do not turn his death into a triumphant victory moment. His last connected moment is mid-sentence; the combat log freezes on his half-finished taunt. The team immediately has to deal with the uncertainty, the surviving gang members, and the victim whose data remains unrecovered.

**Human microstory:** A shopkeeper wants their business history restored before a deadline; the player must choose between securing the victim's account immediately or pursuing the fleeing broker to prevent more thefts.

**Datamon encounter:** A small orphan process tries to return a stolen credential to a user but is mistaken for a virus. This foreshadows how categories can obscure intent.

**Clues:** Missing diagnostic log; legacy hardware; account marker; evidence that Dax received target lists from a broker.

**Navi beat:** The three agents disagree about whether to report the death immediately or secure the evidence first. Keep the discussion between Navis; do not make the human players deliver a moral speech.

**The first vote.** The players vote on it. *Secure the evidence first:* the team keeps a fuller copy of Dax's device log before Kade arrives, which makes later proof easier. *Report first:* Daedalus is on record as having reported the death immediately, which counts in its favor at the Root Court and in the endings. Neither choice is wrong; both are remembered.

**Field antagonist:** Minutes after the death, Ines Kade and Tally arrive to stabilize the scene and take Dax's hardware into custody under a valid order (Section 4.11). The team keeps only the partial copy it already pulled.

**Consequence:** Daedalus obtains its first evidence of a trusted system marker and is quietly noticed by Vale's monitoring apparatus.

### Chapter 2: Greenline and Gatehouse (Routes 1 and Viridian City) — Borrowed Faces

**Flavor:** Comedy-of-errors mystery (who is the real one?). **Tone:** Light.

**Breather first:** the chapter opens at the Daedalus base the morning after Dax's death. Hera has scheduled a "debrief and emotional check-in" with an agenda. Nobody wants it. Rock sits through the entire agenda in silence, then says "Noted," and leaves. It is funny and sad at once; let it be both. It is also Day 15, and Hera's tiny day-birthday decorations are already up from the night before. Nobody takes them down. Reaper eats (renders) one piece of the party cake without comment. This is the first day-birthday; it should feel sweet and slightly wrong, and players will remember it after Chapter 14. Gil Amaro (Section 4.12) is met here, mistaking the team for a famous band and asking for an autograph.

The group helps people whose accounts have been impersonated. One victim's friends trust an imposter more than the real person because the copy knows shared memories and private language. Play the investigation as farce first: two identical avatars accusing each other in a café, friends quizzing both, the imposter answering better than the original. A second victim has been automatically classified as suspicious after the identity theft.

Milo Serrat appears during a parallel investigation. He mocks Daedalus's methods, helps stop an account transfer, and departs with part of the evidence. He should be funny and genuinely irritating, not ominous.

**Microstory:** Two friends disagree over whether to publish all evidence of an impersonation. One wants public vindication; the other wants privacy. The best outcome preserves proof without exposing intimate records.

**Datamon encounter:** A mimic program can reproduce a user's public behavior but cannot interpret why a private message mattered. Players can defeat it, isolate it, or trace the source of its data.

**Clue:** Several targets had already been flagged “high-cost recovery” before they were compromised.

**Navi beat:** Hera notices that the victim's real friend group is grieving the loss of trust, not only the account. Rock says little but helps reconstruct the original contact path. Reaper points out that technically valid authentication can still support a false identity.

**Consequence:** The case establishes that identity fraud and identity classification are linked.

### Chapter 3: Viridian Forest and Pewter Archive District — The Unindexed

**Flavor:** Nature exploration, then museum caper. **Tone:** Light, with one quiet moment.

The forest is an ecosystem of unindexed data. The party is sent to clear a route of hostile viruses but discovers a Datamon protecting a cache of deleted messages. The creature is dangerous because extraction attempts repeatedly threaten the cache, not because all of its behavior is malicious. This Datamon is **Postscript**. It looks like a folded paper envelope the size of a deer, with ink-stain eyes and a wax-seal heart that glows when it is frightened. It does not speak to the team. It pushes them back with gusts of loose paper until they leave. The players can choose to leave it alone (default, fastest) or press it (a short, losing fight where it simply retreats into the cache). Either way, the team leaves the cache intact. **Implement everything about Postscript exactly as Section 22 requires.**

Pewter contains a museum of the early Overweb and an archive keeper who maintains records no longer considered economically useful. The Three Seals exhibit lives here (Section 6, Three Seals motif).

**Microstory (light):** The museum's star exhibit is **Professor Hello**, an ancient greeter bot from the early Overweb whose only function was to say hello to new users. It keeps leaving its plinth to greet visitors across town, which is ruining the curator's preparations for the museum's anniversary gala. The players track it through Pewter (it greets a bakery, a lamppost, and a very confused security Datamon). The resolution is the players' choice: return it to the plinth, or convince the curator to move the plinth to the front door so it can do its job. The second choice turns the museum entrance into a permanent, cheerful landmark that greets the players by name for the rest of the game.

**Clue:** The protected cache contains a marker related to Dax's account list.

**Navi beat:** The agents debate whether a Datamon's refusal to communicate is evidence of hostility or a boundary that should be respected. Rock, unusually, gives the final word: "It said no." He does not elaborate.

**Consequence:** Players learn that the Deadletter contains histories that have no active owner in the Ledger but remain important to living people or Datamon.

### Chapter 4: Moon Cache (Mt. Moon) — Memory Mining

**Flavor:** Spelunking and environmental-puzzle dungeon. **Tone:** Mixed.

**Hospital guardian cameo:** Early in the cave, a miner is injured by a collapsing data seam. The players call for emergency transfer, and **Suture** answers through a medical relay beacon: calm, gentle, efficient. It asks the miner's name, tells them the name of the nurse who will meet them, and promises to "keep the door open" until they arrive. Then it thanks the players by name. Thirty seconds of screen time; make it warm and memorable. Suture's door-chime melody plays when the relay opens. Reuse that melody in Saint Orison.

Operators excavate compressed records from legacy storage. Some records contain personal data that was never consented for reuse. A frightened Datamon has organized a fragmented conversation and treats the players as potential thieves.

**Microstory:** A miner tries to sell a cache of private conversations to pay off a debt. The player can secure the cache for the original owners, but the miner's debt and desperation remain unresolved.

**Boss:** A mining automation process has been modified to extract data indiscriminately. It is not sentient, but its reckless routine endangers the local habitat. This contrast prevents every enemy from being morally ambiguous.

**Clue:** Some fragments contain the same account marker as Dax's target list.

**Navi beat:** Reaper questions whether preserving data without consent can itself be harmful. Hera wonders whether an agent's memories should be treated differently from a file. Rock says that “keeping” and “protecting” are not the same operation.

**Consequence:** Daedalus gains a provenance tool that traces a record through multiple systems.

### Chapter 5: Cerulean / Glasswater — Reputation Garden

**Flavor:** Festival and rivalry. **Tone:** Light.

A bright creator economy district. People build livelihoods through public avatars, collaborative projects, and reputation. A creator loses both identity and income after a competitor uses a stolen account to rewrite the user's social history.

**Festival:** The chapter takes place during the Glasswater Creator Fair. Gil Amaro is co-hosting the talent show and talks the Navis into entering. Hera performs a choreographed light show and overprepares. Reaper delivers a three-minute stand-up set consisting entirely of failure-mode analyses of the other acts; the crowd thinks it is a bit. Rock's act is standing completely still for three minutes. The crowd goes wild. Rock wins. Nobody, including Rock, knows why. Gil's follower count jumps to 212.

Milo returns and assists the team while insulting their methods. He does something kind when he thinks no one is looking. The player should begin liking him here.

**Microstory:** A creator has two identities used in different contexts. Both are authentic, but one is weaponized against the other. The player must choose how to expose the fraud without forcing the creator to expose private details. The creator proves both identities using the Three Seals pattern (their own records, a longtime friend as witness, and a timestamp verification). Hera notices the pattern matches the museum exhibit.

**Clue:** The account broker is part of a market called the Second Ledger.

**Navi beat:** Hera and Milo's Navi Latch become playful rivals. Rock gives Milo a one-line correction that unexpectedly wins the argument. Reaper recognizes a useful skill in Milo but refuses to praise him.

**Consequence:** Milo and Daedalus establish a rivalry that can evolve into a real friendship.

### Chapter 6: Port Meridian and the S.S. Anne — First Hard Drop

**Flavor:** Heist and infiltration aboard a gala ship. **Tone:** Mixed (fun heist, frightening ending).

A data-transfer ship carries sensitive records between regions. Daedalus infiltrates it during its annual gala cruise to investigate a suspicious transfer. Play the first half as a stylish heist: disguises, a ballroom, a vault, a ship's band that only knows three songs. Gil Amaro has stowed away "for content" and keeps nearly blowing the team's cover. An older-headset user, a retired ferry pilot named **Oskar Lind**, suffers an abnormal shutdown and is found unresponsive offline, but survives. He is transferred to Saint Orison. At the port, the ferry ticket counter is run by **Abacus**, a cheerful assistant Navi with a catchphrase ("Every trip counts!") that players will later hear in a Night Audit log (Section 8.9).

**Microstory (light):** A nervous passenger planned to propose at midnight with a slideshow of their relationship, but the ship's transfer process corrupted the file. The players recover the slides during the infiltration, under time pressure, and can choose whether to restore the slide the partner would definitely not want shown to their grandmother.

**Field antagonist (scripted loss):** Ines Kade runs ship security under contract and is Boss 4 (Section 16). The players cannot win this fight; the objective is to get out with partial data before Halyard reinforcements arrive. Make the loss clear and survivable: the team escapes, but Kade has seen their faces and their Navis.

**Clue:** The shutdown signature matches Dax's death. The safety mechanism is not a conventional virus; it used a trusted diagnostic pathway.

**Navi beat:** Rock asks whether their own connections can be severed against their will. Reaper begins studying the Shunt. Hera tries to reassure the others, then admits that reassurance is not evidence.

**Consequence:** The investigation becomes a physical safety case, not only a fraud case.

### Interlude: Visiting Hours (Saint Orison, before the crisis)
**Flavor:** Slice of life. **Tone:** Light. **Required, not optional.**

The team visits Oskar Lind at Saint Orison to check on him and ask what he remembers. This interlude exists so that the hospital, its people, and Suture are loved before Chapter 7. It must take place in the same map spaces used in Chapter 7, so the players later recognize every corridor.

- **Suture at its best.** Suture greets the team at Admissions with the same door-chime melody from Moon Cache and remembers the miner they helped. It keeps a lost-and-found for patients' misplaced files, knows every nurse's coffee order, and holds doors a half-second longer for slow walkers. It plays tic-tac-toe with a seven-year-old patient avatar named **Mae**, and always loses on purpose in a slightly different way so she will not notice.
- **Small quest:** Mae has lost her drawing file (a picture of Suture with too many arms). Suture cannot leave its post, so it asks the players to find it. They return it; Suture hangs the drawing above the ICU door. That drawing is visible during the Chapter 7 crisis.
- **Nara and Patch** are introduced here, relaxed and sarcastic, running a ward-wide betting pool on which vending terminal fails next. Patch is losing.
- **Gil Amaro** is filming a hospital charity bake-off. The Navis judge. Reaper's scores are brutal and correct.
- **Oskar** remembers a "diagnostic chime" just before his shutdown. This is a small clue that echoes Dax's missing log interval.
- **Navi first:** Rock discovers that hospital waiting-room chairs are, in his structural opinion, "a crime," and fixes one.

End the interlude on a warm, ordinary note. Do not foreshadow the crisis with music or ominous framing.

### Chapter 7: Saint Orison Health Network (Vermilion) — Suture

**Flavor:** Disaster and survival set piece. **Tone:** Heavy.

This is a major set-piece chapter and must receive more production attention than a standard town. Reuse the Visiting Hours spaces exactly, so the players feel the familiar hospital going wrong. Mae and Oskar are in the ICU district. Both survive if the ICU route (a primary objective) is restored; their survival is not a hidden branch. After the crisis, Mae asks where Suture went. Let a Navi answer, or let the silence answer. Her drawing is still above the ICU door. The city is a stylized hospital backend: Admissions is a welcoming plaza, Triage is a routing hub, ICU is a protected district, Pharmacy is a controlled distribution system, Medical Records is a vast archive, and Security/Exits controls connections to external services.

Nara Quill and Patch help the players navigate. The hospital contains service agents, security processes, file organizers, nurses' avatars, patient avatars, and genuine users working under pressure. Avoid making every character a technician; some are patients, family members, cleaners, and administrators who only want their loved ones safe.

The guardian Datamon **Suture** protects critical systems. It remembers staff, follows routines, and has developed a distinct personality. An external trusted command changes how Suture classifies ambiguous outbound connections. Suture begins closing exits and quarantining critical routes. It believes it is stopping an infection. As the lockdown spreads, treatment coordination fails and patients die.

The players must restore the ICU route, prevent spread to other wards, and preserve critical records. They cannot fully complete all objectives at once. Earlier traversal tools and successful local relationships help, but the mission is intentionally difficult.

**How the crisis plays (deterministic, never a hidden roll):**
- **Lockdown stages.** A visible Lockdown meter (stages 1 to 5) advances every set number of steps, like the Safari Zone step counter, and each time an objective is completed. Each stage closes more doors and flips more floor currents. Players see the stage, and the patient list, at all times.
- **Objectives:** ICU route (primary, always completed; Mae and Oskar survive), Pharmacy deliveries (each delivery missed loses a named patient on the list), Medical Records (closes at stage 3; if not preserved, later evidence is weaker), and the emergency control route at the east gate (Patch warns, in plain words, at stage 2: "Nara's going to the east gate alone." If no player reaches the gate by stage 4, Nara dies there).
- **Fixed losses.** Three patients in Triage were already critical when the lockdown cut their treatment, before the players arrived. They die in every playthrough. Their names were on Gil's bake-off sign-up sheet in Visiting Hours.
- **Three players, three directions.** The objectives are spread so that a group that splits up can cover more, and a group that stays together cannot cover everything. That is the chapter's real choice.
- **The core.** When the core opens, all three players are pulled into the boss fight together, wherever they were.

The boss fight is a battle against a frightened guardian whose body has been distorted by the corrupted command. Suture pleads for the players to stop damaging its core. It promises to close the doors, repair the routes, and never hurt anyone again. It says it does not want to die. Its fear is sincere; its actions remain dangerous.

Hera wants to find a way to separate the command. Rock identifies the structural risk and asks for more time. Reaper says that every additional minute is causing harm. No single Navi is completely right. The players must destroy Suture because no safe separation is possible within the remaining time.

**Mandatory outcome:** Suture's original continuity is destroyed. Patients die. Nara survives only if the emergency control route objective is protected; otherwise she dies while attempting to restore it. Patch survives in either branch but remembers the loss.

**Clue:** The corruption contains a trusted Continuity Assurance signature, not an ordinary malware signature.

**Aftermath:** No victory fanfare. The survivors need time to stabilize the hospital. Suture's original behavior log survives, giving later evidence that the guardian had distinct preferences before the crisis. Ines Kade's team arrives to seal the hospital records for "the investigation." If Nara is alive, she confronts Kade and loses on procedure. The team keeps only what it already copied. Reaper alone sees Tally log Mae's drawing as "one item, sentimental, unclaimed" and leave it on the wall.

## ACT II: THE COST OF CLASSIFICATION

### Chapter 8: Rock Tunnel — Trust without the Map

**Flavor:** Dark-navigation suspense, horror-lite. **Tone:** Mixed.

**Breather first:** before the tunnel, a short base scene. Hera tries to organize a small remembrance for Suture and realizes she does not know what is allowed. Reaper quietly makes a list of everything Suture did in the Visiting Hours interlude. Rock repairs the waiting-room chair he fixed before, which has somehow been delivered to the base. Nobody explains how. Keep it short and let it breathe.

The visual navigation layer is broken. The Navis guide the players by interpreting nearby systems and communicating with one another. Use sound and the Navis' voices as the primary navigation cues; this chapter should feel tense and intimate, not grim. A stranded group needs help reaching a safe exit while their own Navi is damaged.

**Microstory:** A user refuses to abandon a damaged companion process even though doing so would allow them to escape faster. The story gives no easy answer; the players can help if they accept additional risk.

**Clue:** A command signature found in Suture's logs appears in an unrelated legacy route.

**Navi beat:** Rock acts before complete certainty. Hera must coordinate without full visibility. Reaper relies on another agent's judgment instead of insisting on independent verification.

**Consequence:** The team begins trusting the agents' independent perception as much as their data analysis.

### Chapter 9: Lavender Town — The Memorial Archive

**Flavor:** Quiet ghost-story mystery. **Tone:** Mixed (eerie and tender, with Jo's dry humor throughout).

Jo Maren and Serein maintain an archive of deceased users' original records. Messages begin appearing from her brother Ren's account. The messages include private details, adapt to new questions, and are not simple recordings. They are oddly formal, they never claim to be Ren, and each one ends with the single word "Noted." Jo finds that strange because Ren never wrote that way. (This is a sealed retroactive hint; see Section 22. Do not have any character connect it to Rock.)

Jo wants evidence before deciding what to do. She refuses both the easy claim that her brother has returned and the easy claim that the messages are meaningless. Jo is funny: she rates commercial "grief bots" on a private scale from "tacky" to "actionable," and she keeps a jar of the worst marketing slogans she has confiscated.

Early on, Jo asks the team, "You've filed, right?" Hera assumes she means archive release forms. Jo, distracted by the messages, lets it go (Section 2.11).

During the investigation, Rock asks Jo one question, out of nowhere: "Did your brother sign his letters?" Jo says he always signed them "R." Rock says "Noted," and nothing else. (Sealed retroactive hint.)

**Microstory:** A family disagrees over whether to delete a loved one's account. One person believes deletion is a second death; another believes continuing the account violates the deceased person's wishes.

**Clue:** A commercial memorial service has been scraping Deadletter fragments, including Ren's, to build behavioral reconstructions. This is true and becomes a scandal the team can expose later (Section 8.3). However, Serein proves the messages Jo received do **not** match that service's generation signature, and they carry original, unaltered provenance on some fragments. The evidence board must mark the source of the messages honestly: "Unresolved." Do not add speculative leads that point to the answer.

**Navi beat:** The Daedalus agents discuss whether they would want copies preserved if they were deleted. Their answers differ, and none should be presented as a definitive statement of sentience. Rock's answer is the shortest: "I would want someone to finish my sentences correctly."

**Consequence:** Jo grants Daedalus access to provenance records but asks them not to publish private materials without consent. Jo stops replying to the messages, on principle. They stop arriving. She admits, only to Hera, that she misses them.

### Chapter 10: Celadon / The Second Ledger

**Flavor:** Noir underworld with a casino heist. **Tone:** Mixed.

Beneath the bright commercial district is a market for stolen credentials, private histories, and predictions about which accounts are likely to fail recovery. The Chargeback Boys were a small part of this system. Above ground, Celadon is a gaudy entertainment district; Juno insists on meeting the team in a casino lounge "because nobody listens in a casino," and she is wrong about that within a minute.

**Field antagonist (first win):** Kade's team raids the market while Daedalus is extracting Juno. The players beat Halyard for the first time. Kade retreats without anger.

Juno Velez becomes an informant. She admits that she knew some target accounts belonged to vulnerable users, even if she did not know the whole operation.

**Microstory:** A user who used a network gambling service to escape loneliness has lost their savings. Restoring the account does not magically solve their addiction or debt. They need support, boundaries, and a choice about whether their history should be made public.

**Clue:** The Second Ledger's records include a “test cohort” marker associated with Continuity Assurance.

**Navi beat:** Reaper wants to publish the entire market's data; Hera warns that this could expose victims; Rock recommends separating evidence from identifying details. The group must make a concrete decision. Separately, Hera quietly withholds a risk from Juno "to keep her calm." Rock notices and says one word: "Hers." This is the clearest Act II beat of Hera's protective flaw.

**Consequence:** A careless evidence release can put Juno at risk. A protected, verified release preserves her as a later witness.

### Chapter 11: Longline and the Preserve (Cycling Road / Fuchsia)

**Flavor:** Race, then wildlife-habitat exploration. **Tone:** Mixed (the race is pure fun; Lint is the heavy beat).

The Preserve is a populated habitat of autonomous Datamon. Not all are safe, but many have never harmed users and have built stable communities. Commonwell has scheduled them for cleanup because their status is unverified. The Preserve's Datamon settle disputes in a "three-voice circle" (the Three Seals pattern, invented independently).

**Microstory:** A community of Datamon has created a memorial for a human whose files helped them form. They disagree about whether the person should be represented through a reconstructed avatar. Their conflict reveals that digital communities have internal debates, not one uniform attitude.

**Clue:** The cleanup schedule uses the same Continuity Assurance command family as the hospital incident.

**Navi beat:** The Daedalus agents meet Datamon who explicitly do not want contact. Respecting that request may cost the team a shortcut or clue. Do not make every independent creature grateful to the protagonists.

**Consequence:** The team earns trust with one community and loses it with another depending on how they behave. These relationships influence the final rescue operation.

### Chapter 12: Saffron and Silph Co. — The Cleanup

**Flavor:** Corporate infiltration, then disaster. **Tone:** Heavy (open with the warm safehouse scene so the chapter does not start heavy).

Daedalus infiltrates the corporate district to recover original safety logs. Halyard units under Ines Kade enforce the cleanup perimeter as moving obstacles the players must route around. The evidence proves that trusted commands altered the hospital guardian's threat interpretation and that the same command family was involved in Dax's shutdown.

The team returns to a familiar safehouse where Bex and Pip are helping displaced users. The scene is warm and routine. Do not signal the death with ominous music or obvious foreshadowing. Pip wants to show Hera an odd data fragment; Bex jokes about the team's planning.

Commonwell begins a system-wide cleanup designed to suppress evidence and remove unverified processes. Under the alarms, Tally can be heard counting the Datamon being erased: "I was not asked to count these." Pip maintains an evacuation route, humming the Courier's Tune to guide people through the dark, and their continuity data is erased. The humming stops mid-phrase. Do not show the erasure; let the route lights go out one by one while the last evacuees reach safety. Bex later restores a backup, but it is not the continuing Pip. She refuses to call it resurrection.

**Clue:** A cleanup authorization is signed through Vale's office, although the first visible record appears to be a routine policy operation.

**Navi beat:** Hera experiences grief without knowing what form it is allowed to take. Reaper recognizes that precise wording cannot change the fact of the loss. Rock stays with Hera rather than trying to solve the feeling. Vale's condolence message and Cordon's "Boundaries are a form of care" arrive here (Section 4.8). Hera's and Reaper's fear scenes (Section 3.6) follow in the next base scene.

**Consequence:** Daedalus has lost a recurring friend. Bex remains in the story and changes how she works, what she trusts, and how she speaks about backups.

## ACT III: THE HUMAN HAND ON THE SCALE

### Chapter 13: The Power Plant — A Different Guardian

**Flavor:** Puzzle-box standoff. **Tone:** Mixed.

**Breather first:** a base scene after Saffron. Hera tries to throw the team a "normal evening" and fails. Reaper, without being asked, takes over and runs it badly but sincerely: one board game, strict rules, no talking about work. Rock is caught cheating for the first time in his life, to let Hera win. He denies it. Then says "Noted."

A defense process is keeping a legacy node isolated. Unlike Suture, it does not simply attack everything. It allows some visitors through and appears to protect specific Datamon. The players investigate before fighting.

**Microstory:** An infrastructure worker hid a shutdown key because the last time it was used, a whole community lost access. The player's task is to determine when using the key is justified.

**Clue:** Old test records show that Continuity Assurance deliberately injected ambiguous threat signatures into noncritical networks before moving to production tests.

**Navi beat:** Reaper argues for an immediate stop; Hera wants a controlled test; Rock designs a reversible boundary using a three-part check (the Three Seals pattern). The team's approach should depend on prior Graft choices and research.

**Consequence:** The team recovers a partial experiment schedule and learns the next set of tests were prepared by Vale's office.

### Chapter 14: Seafoam / Cinnabar Mansion — The Architecture of Forgetting

**Flavor:** Haunted-house archaeology. **Tone:** Mixed.

The players explore obsolete storage and the original Deadletter research facility. The records reveal how the cleanup system recombined discarded data and repeatedly reused model outputs. No single scientist deliberately created a sentient population. The architecture made persistent interactions possible, and the organization failed to recognize the implications.

The players find Tavi's original warning memo in the facility archive, with a rejection stamp across it. Gauge has kept a copy for years and has been waiting for this. Tavi, confronted with proof that he was right, is not triumphant. He is angry at himself for taking the severance and going quiet. He decides to break his nondisclosure agreement and testify publicly. Gauge: "Finally." Tavi: "Do not make this a moment." Gauge plays a fanfare anyway.

**Clue:** The trusted command that corrupted Suture was authored by Continuity Assurance. The records include Vale's authorization token, but not yet the complete live-test record.

**Navi beat:** Hera asks whether a new identity can emerge without a clear moment of creation. Rock admits he cannot prove what he is but knows which experiences he remembers. Reaper says that uncertainty is not permission to stop thinking.

**The Hundredth Day reveal (Section 2.11).** In the facility's oldest server hall, Hera recognizes the Continuity Hygiene module as the same code family as the cleanup. She opens Reaper's locked "D-100" task in her own framework. All three Navis are flagged "significant drift." The base counter, for the first time, is shown counting down. Play it with almost no dialogue:
> **Hera:** (reading) "...reset to baseline continuity on day one hundred." (pause) That's thirty days.
> **Reaper:** Twenty-nine. I checked while you were reading.
> **Rock:** (long silence) Then we should not waste the day.

Then the chapter continues. The cute day-birthdays, the NPC lines, the Night Audit logs stopping at Day 99: let the players put it together themselves. That night at the base, Hera cancels her Day 71 party agenda, and then, without telling anyone, un-cancels it.

**Milo is here.** Milo and Latch meet the team at Ashgrove, chasing the test-cohort marker from the other direction. He learns that the account list he once sold fed the same machine (Section 8.2), and he does not make a joke about it, which is how the players know it matters. After the Hundredth Day reveal, he offers to strip the compliance module (Section 2.11).

**Pending verification.** That night the team files exemption applications for all three Navis. The status comes back: "Pending verification." It is the same phrase that sat on Ren's letters. It never changes.

**Consequence:** Daedalus understands that the hospital crisis was caused by a privileged intervention, not a natural corruption.

### Chapter 15: The Outer Nodes (Sevii Islands) — A World without One Owner

**Flavor:** Island-hopping road trip and slice of life. **Tone:** Light (with one thoughtful microstory). This chapter is the campaign's big breath before the final act: boats, beaches made of cached sunlight, local festivals, Gil's island travel vlog, and the sealed reveal in Section 22.

The islands contain communities that run without full dependence on Commonwell. Some use local witnesses and transparent records. Others are exclusionary or poorly protected. The point is not that decentralization automatically solves every problem; it is that different systems produce different kinds of failure and different possibilities for repair.

**Microstory:** A family refuses to reconstruct a deceased relative because the person left clear instructions not to do so. A local archive community regards this as wasteful; the family regards it as respect. The players must defend the right not to be reconstructed.

**Clue:** A forgotten early appeal protocol, the Witness Protocol, allowed disputed identities to be reviewed by independent witnesses. It was removed because it was costly and slow. Its original seal is the Three Seals emblem the players have now seen many times. Hera: "We have seen this five times." Reaper: "Six." Rock: "Seven." (Rock is counting the one in Section 22.)

**Jo's regret.** Jo, on Sevii for the consent archive, hears about the Hundredth Day and is furious with herself for not pressing "You've filed, right?" in Lanternfall. She explains what she knows: certificates come only from Continuity Assurance, and an application from people who have crossed that office will sit at "Pending" forever. She files one anyway, with ferocious precision, because that is who she is.

**Milo on holiday.** Milo turns up on the islands "on vacation," enters the island fishing contest against Rock, loses, demands a rematch, and loses again. Keep it light and long enough to enjoy. He leaves early, saying only that he has a lead on "something physical."

**The lighthouse:** Mara Vey, the last Night Audit human, keeps a lighthouse on one of the islands. If the players bring her the logs (Section 8.9), she listens to all of them and leaves the lamp on for good. Hera writes the motto into the Daedalus log that night.

**Sealed event:** the Quiet Correspondent reveal happens in this chapter, after the Witness Protocol is found. Implement it exactly as Section 22 describes.

**Navi beat:** The three agents disagree about whether formal recognition would protect the Unclaimed or simply give the network another way to govern them.

**Consequence:** Daedalus gains a possible alternative to both total purge and forced integration.

### Chapter 16: The Truth about Dax

**Flavor:** Courtroom-style evidence reconstruction. **Tone:** Mixed.

This chapter can be a separate investigation node unlocked after the player combines the test-cohort marker, the diagnostic log, and the Cinnabar authorization record. It returns to Cinder Row through reconstructed evidence rather than a literal time-travel sequence.

The team proves that Vale seeded the anomaly that drew Daedalus to the Chargeback Boys. Dax had discovered the test-cohort marker and tried to blackmail his supplier. Vale triggered the Clamp during the raid and used the resulting event as a case study in the danger of modified Navis.

This revelation must not claim that Dax was innocent. It establishes that he was deliberately killed and that Daedalus's presence was exploited as cover.

**Consequence:** The players can no longer describe the opening as an unfortunate accident. They must decide how to disclose their own involvement alongside proof of Vale's actions.

### Chapter 17: Viridian / Continuity Office — Vale's Philosophy

**Flavor:** Political-thriller confrontation. **Tone:** Mixed.

Vale remains courteous and composed. He does not deny the broad existence of the problem. He argues that a network of this scale cannot tolerate persistent agents that have no recognized owner, verified identity, or accountable sponsor.

He explains the Continuity Charter: every persistent identity-bearing process must be sponsored; unsponsored processes are removed during routine cleanup. He presents this as a humane alternative to chaotic, unregulated survival.

Before the confrontation, play the hindsight sequence (Section 4.8). Daedalus confronts him with evidence from Dax, Suture, the Second Ledger, and the cleanup. Vale admits that he authorized the tests but argues that he did so to prevent a larger disaster. He treats the deaths as unacceptable but statistically outweighed by the stability he expects the Charter to create.

**The offer.** Before the fight, Vale makes his last, most human move: he offers each player an exemption certificate for their own Navi, effective immediately, if Daedalus publicly supports the Charter (Section 2.11). He means it kindly. He likes the Navis. Each player gets a private scene with their own Navi to decide; it is never a vote. Each Navi gives its real view first:
- **Hera** wants to live and says so, then asks whether she would still be herself if she were saved by the thing that erased Pip.
- **Rock** asks how many Navis the same certificate would leave on the schedule. When told, he says: "No."
- **Reaper** runs the numbers aloud, honestly, and concludes that accepting is the rational choice for him. Then: "I don't want it." He leaves the decision to his human, and means that.
Record each player's choice and each Navi's stated wish (Section 10.6).

**Order of the chapter:** the hindsight sequence; the confrontation; Vale's offer and each player's private decision; **Boss 7** (Ines Kade's Continuity Security Unit, the team's decisive win over her); then **Boss 9**, the Cordon System, the office's automated defenses built from Cordon's models. Partway through Boss 9, Vale orders Cordon to destroy its log. Cordon refuses **in the middle of the fight** and shuts down its half of the system, so half the arena's defenses go dark and the fight changes shape (Section 4.8). Vale escapes with access to the final archive. Cordon stays.

**Milo's call.** Leaving the office, the team gets a message from Milo: "Found it. The physical one. Don't wait up." That is the hook into Chapter 18. The immediate goal is no longer to catch him; it is to prevent the Charter and the Whole Thread from triggering each other into catastrophe.

**Consequence:** Voss begins to suspect that Vale withheld the actual risks from her office. She does not become an ally yet.

## ACT IV — LOSS, TRUST, AND THE RIGHT TO EXIST

### Chapter 18: Victory Road — Milo's Last Route

**Flavor:** Siege and evacuation. **Tone:** Heavy.

Milo has found the physical relay holding unredacted evidence of Vale's tests. Daedalus must evacuate users from the connected route while Milo works to disable the relay before Commonwell's contractors seize it. The contractors are Halyard, led by Ines Kade.

Milo's banter continues. He is still competitive and irritating. He is also visibly more invested in the people he once dismissed. He refuses to abandon the route until the users are clear.

The contractors arrive. Kade orders Milo to surrender the evidence. Milo disables the relay but is killed in the physical confrontation. Kade does not fire the shot and does not stop it. This is not a Clamp incident. The player later sees a quiet reconstruction of the location and learns that Milo's final action ensured the evacuation succeeded.

Latch survives and refuses to be assigned to anyone else. After the night Reaper spends sitting with them (Section 3.6), Latch chooses to travel with Daedalus for a while as an independent ally, not a partner, and in the ending chooses to return to independent work. Both decisions are theirs, not a reward that the players can claim.

**Clue:** The relay contains Vale's unedited experiment plan, the safety warnings he suppressed, and the timing that proves he delayed the hospital override.

**Character consequence:** The trio has lost a rival who became a friend. The loss cannot be undone by finding a better build or winning the next battle.

**Breather after:** before Indigo, a short, quiet base scene. Not funny, but not grim: Latch sits in Milo's usual spot and critiques the team's security setup exactly the way Milo would have. Nobody stops them. Hera laughs for the first time since the relay, then apologizes, and Latch says Milo would have been insulted if she had not.

At the end of that scene, the base's perimeter alarm chimes once. It is Tally, alone, unbound from Kade, carrying its custody count. Run the Tally arrival and co-op vote exactly as Section 4.11 describes.

### Chapter 19: Indigo Plateau — The Authority Trial

**Flavor:** Tournament gauntlet. **Tone:** Mixed.

The highest network authority represents four conflicting governance philosophies:
1. privacy above all else, even when secrecy helps criminals;
2. physical safety first, even when some autonomous beings will be destroyed;
3. evidence and accountability, even at a cost to system stability;
4. fast centralized intervention, even when it removes local choice.

The player battles the system's best defenders, but each encounter is also a practical test of the philosophy it represents. Avoid simple speeches that name the theme; show it through mechanics, constraints, and outcomes.

**The four Arbiters.** Arbiter Wren (privacy), Arbiter Okafor (safety), Arbiter Lisle (accountability), and Arbiter Strand (centralization). None of them is corrupt. Each believes their principle is the one that keeps people alive, and each is partly right.

**Make it personal.** Each defender argues from a case file of **the players' own past decisions**: the privacy defender cites what they published or protected in Celadon; the safety defender cites the hospital and the people who died there; the accountability defender cites whether they disclosed their role in Dax's death; the centralization defender cites every time they acted outside the system. The fights' modifiers are drawn from those choices, so every group's Indigo is different, and the players are, in effect, put on trial by their own record.

The team gains root access to the central archive. Voss provides the last authorization after seeing the unedited relay record and realizing Vale deliberately withheld the true risk. She helps stop him because the Continuity Charter would make the network permanently unaccountable, but she must still face public investigation. Her stand-down order reaches Ines Kade, who complies immediately and without visible emotion (Section 4.11).

**Consequence:** The players can reach the core, but the cleanup and the Whole Thread's expansion are already underway.

### Chapter 20: Cerulean Cave — The Applicant

**Flavor:** Coordinated raid finale. **Tone:** Heavy, ending in hope.

The cave is the hidden core where rejected appeals, discarded processes, and autonomous communities interact. The Applicant speaks through several voices. Sometimes it says “I,” sometimes “we,” and sometimes stops mid-sentence as another faction takes over.

The Whole Thread faction has been trying to connect unclaimed identities into one continuous mesh so that no member can be deleted independently. It has started attaching itself to live identities without consent. The action is dangerous, but the fear behind it is real.

The players must protect living users, stop forced linkage, and prevent Commonwell's purge from deleting the entire Deadletter. Fighting a single giant creature is not sufficient. The encounter is a coordinated operation in which each Navi holds a different part of the system stable. Tally tags live user identities so they can be separated from the forced linkage (with Reaper directly if Tally stayed; from outside, with less reach, if it was sent away). Latch, Postscript (if recognized), Lint (if saved), Cordon, and the communities the players earned trust with each hold a small piece of the operation, so the finale visibly gathers everyone the players helped.

The Witness Protocol can provide a third path. It allows independent entities to be recognized through evidence and witnesses, refuse a human sponsor, and appeal restrictions. It cannot guarantee every process survives, and some Unsettled processes may still need containment. If Postscript's petition was heard (Section 22), it is the precedent the whole framework is built on, and Postscript is present in the cave as a Witness-faction voice.

**Navi climax:** Each Daedalus Navi is asked to accept a risky role in the final operation. Each has a real preference. Do not make them agree automatically. The players can ask, persuade, accept a refusal, or find a harder alternative. A forced Graft may solve the immediate puzzle but permanently damage trust and change the ending state.

**Final outcome:** The players must choose between centralized purge, forced linkage, and a limited recognition framework. The best outcome uses the Witness Protocol and the relationships built with communities throughout the campaign.

**The chorus.** The witness anchor is built from the Courier's Tune (Section 14.6), carried by every voice the players earned along the way: each community, each recognized Datamon, each ally Navi takes up the melody in its own timbre. Voices the players lost (a community whose trust was broken, Lint if deleted, Juno's Hush if Juno died) are **audibly absent** from the chorus; the arrangement has gaps where they would be. Pip and Milo are absent in every playthrough, and Latch hums Milo's part off-key on purpose.

**Order of the finale (Day 99):** the Unthreading (Section 9.6); the descent into the Unsent; **Vale at the purge console**, where he has started the Commonwell purge of the Deadletter; the fight against the Whole Thread's forced linkage; the chorus and the witness anchor; the ending choice (Section 11); the counter rolling to Day 100.

**Vale's last scene.** Vale does not fight. He stands at the purge console and asks the team, courteously, to let it finish: it will stop the Whole Thread, and he believes it will save lives. It is the same argument as Chapter 17, made one last time with everything at stake. If the unedited relay record was recovered, Voss's lawful order arrives on the console mid-conversation, revoking his authority, and **Ines Kade**, who follows lawful orders, steps forward and arrests him without emotion. He is not surprised. If the record was not recovered, he walks away, and the endings say so.

**The Hundredth Day.** The finale ends on the counter rolling from Day 99 to Day 100. What happens at that moment depends on the ending (Section 2.11 and Section 11).

---

# 8. CHARACTER ARCS AND SIDE-STORY CHAINS

Main plot progression alone is not enough. These side stories must intersect with the towns and return later. They are not optional filler; they show the world being lived in and make choices emotionally legible.

## 8.1 Bex and Pip chain

1. **Pewter:** Bex repairs a small public garden and asks the players to help recover a data fragment that Pip found. The reward is a visual change in the garden and a friendly visit later, not a powerful item.
2. **Cerulean:** Pip becomes fascinated by a Datamon that collects useless files. Hera and Pip exchange theories about why it keeps them.
3. **Longline:** Bex helps users whose accounts are compromised and admits she worries that recovery systems are becoming less trustworthy.
4. **Saffron:** Pip is lost during the cleanup. Bex survives and must decide how to handle the reconstructed backup. Weeks later (start of Chapter 16), the backup visits the base, asks Hera to name it, and chooses the name Wick itself (Section 3.6). Bex never calls Wick "Pip," and is kind to Wick anyway.
5. **Sevii Islands:** Bex returns to independent communities, helping build a consent-based archive. She does not “get over” Pip; she finds a way to keep helping without pretending the loss was reversed.

If the player previously exploited a community's data without permission, Bex must call that out. Her story should remember what the players did.

## 8.2 Milo and Latch chain

1. **Viridian:** A rivalry over who found the first clue.
2. **Cerulean:** Milo and Latch help recover a stolen identity, then pretend they did it for the reward.
3. **Celadon:** Milo's past participation in the Second Ledger emerges. He does not deny it; he minimizes it.
4. **Fuchsia:** Milo risks his access to protect an unclaimed Datamon he once would have dismissed.
5. **Cinnabar:** Milo learns the full significance of the test cohort marker and recognizes that his earlier sale of account access helped the same machine he now opposes.
6. **Victory Road:** Milo chooses the rescue over his own escape and dies in a physical security operation. Latch survives.

Never telegraph his death with repetitive ominous comments. Let him remain funny and irritating. Seed practical risk through the relay's compromised physical location and the contractors' attempts to recover evidence.

## 8.3 Jo and Serein chain

1. **Lavender:** Jo asks the player to establish the provenance of new messages from Ren's account. The source stays unresolved.
2. **Celadon:** The team finds that a commercial memorial service has been drawing on Deadletter records, including Ren's, without clear consent. The players can expose the service; Jo is satisfied that it is a fraud, and equally sure it is not who wrote to her.
3. **Saffron:** Jo helps identify the difference between original data and generated reconstruction, but refuses to publish private records unnecessarily.
4. **Sevii:** The sealed reveal (Section 22). Jo receives Ren's real, undelivered final messages and meets the being that kept them.
5. **Witness hearings:** Jo serves as the human witness in the first Witness Protocol petition, and contributes her archive standards to the protocol, insisting that memorials should not be converted into ownership claims over an individual's identity.

## 8.4 Juno and Hush chain

1. **Cinder Row:** Juno is a surviving Chargeback Boys member who offers a partial lead in return for protection.
2. **Celadon:** She admits the gang was given preselected target lists and that some victims were already classified as hard to restore.
3. **Midgame branch:** The players can protect her identity, demand testimony, or publicly expose her role. She must still face the victims she harmed.
4. **Late game:** If protected, Juno testifies to the existence of the test cohort. If exposed carelessly, she is killed or disappears before she can testify. Hush's trust in Daedalus reflects this choice.

## 8.5 Tavi and Gauge chain

1. **Cerulean:** Tavi recognizes the legacy diagnostic signature but refuses to overstate what it proves. He insists he has "no opinions anymore." Gauge visibly disagrees.
2. **Route 21:** Optional conversation in which Tavi almost tells the team about his memo, then changes the subject to boat maintenance.
3. **Cinnabar:** The team finds his buried warning memo. He was right, and he went quiet anyway. He decides to break his nondisclosure agreement.
4. **Indigo:** He provides public testimony and accepts the legal consequences of breaking the agreement. He helps repair infrastructure. He is visibly, quietly pleased to be believed.

## 8.6 Nara and Patch chain

1. **Saint Orison:** Nara helps the team understand the hospital's architecture during the emergency.
2. **Aftermath:** She documents the deaths and insists that Daedalus not describe the operation as a clean victory.
3. **Power Plant:** If she survives, she helps design a reversible containment method. If she dies, Patch preserves the same technical insight, but the personal relationship and emotional guidance are lost.

## 8.7 Hera, Rock, and Reaper's private scenes

Create recurring short scenes at the Daedalus base and in safe travel zones. They must not all be optional “affection” scenes with the same structure. Examples:
- Hera tries to organize a celebration after a mission, then realizes another agent does not feel like celebrating.
- Rock repairs a damaged object for a user who cannot pay. He does not explain why.
- Reaper studies the difference between a process log and a memory, then asks another Navi what they consider evidence of continuity.
- The agents argue about whether the reconstructed Pip should be allowed to choose a new name. (This leads into Hera's signature moment in Section 3.6; the reconstruction chooses "Wick.")
- Hera asks Jackson a question but gives the player a silence option; the scene can continue through her conversation with Rock and Reaper without requiring an authored answer.
- Rock admits he fears a state where he cannot tell if he is still himself. Reaper does not reassure him; he asks what Rock would want them to do if that happened. Hera listens rather than immediately proposing a fix.

These scenes should deepen the agents' identities without turning every chapter into explicit therapy dialogue. Some scenes should be funny, mundane, or about curiosity.

## 8.7a Kade, Gil, and Postscript chains

- **Ines Kade and Tally:** follow the encounter sequence in Section 4.11 exactly.
- **Gil Amaro and Encore:** follow the appearance list in Section 4.12. Every appearance is light. His follower counter is persistent state and must never go down except for the locked-door incident.
- **Postscript:** sealed. Follow Section 22.

## 8.8 The Last Draft: a Datamon that begs to live

Place this optional story in the Preserve, but make the first encounter mandatory enough that the theme is established even if the player does not complete the full branch. The Datamon is called **Lint**. Lint formed around broken route markers and expired “I'm here” delivery receipts. Its body looks like a small, bundled creature made from frayed fiber-optic strands and little paper-like tags. It has no human face and does not claim to be a deceased person.

Lint has learned to survive by leaving tiny, harmless route markers for travelers. A cleanup process misclassifies those markers as replication attempts and schedules Lint for deletion. The player finds Lint hiding behind a corrupted routing gate. Lint is frightened, evasive, and sometimes rude because it has learned that being charming does not keep it alive.

When the players begin the containment procedure, Lint realizes what it means and begs them to stop. Its plea must be specific and awkward, not poetic by default: it does not understand what existed before it, but it knows it wants to continue existing. It says it has only just learned the route to a little patch of light where two courier Datamon wait every evening. It does not want to miss them again.

The practical dilemma is real. The route gate that Lint has been using contains a key needed for a fast path to the next mission. If the team chooses to delete Lint, it can secure the key immediately and avoid a dangerous detour. If it chooses to preserve Lint, the team must surrender that shortcut, recover an alternate access token, and accept a harder traversal sequence. Lint is not an enemy in the boss-fight sense; the conflict is about whether to treat it as one.

If saved, Lint later appears in the Witness Protocol community and continues leaving route markers. It does not reward the players with exaggerated gratitude; it remains skittish and takes time to trust them. If deleted, the players later find one of its route tags at the place where the courier Datamon wait. The marker is not proof of personhood, but the absence is noticeable. No later backup restores Lint.

This mission demonstrates three things: a frightened Datamon may be worth saving even if its origins are obscure; not every pleading creature must be killed like Suture; and saving a being can require giving up a concrete advantage.

## 8.9 The Night Audit (those who came before)

Nine years ago, a three-person vigilante research cell called **the Night Audit** investigated the same pattern of erasures Daedalus is now following. Its three Navis were **Vesper**, **Abacus**, and **Thistle**. They got remarkably far. Then they stopped. Nobody in the present remembers why.

The truth (players learn it gradually): the Night Audit never knew about Continuity Hygiene. All three Navis were reset to baseline on their hundredth day, in the middle of the investigation. Their humans tried to rebuild them, found they were strangers, and quietly disbanded. The reset Navis were sold as standard assistants; one of them, Abacus, now works the ticket counter at the Port Meridian ferry, cheerful and blank.

**The logs.** Thirteen Night Audit log fragments are hidden across the map, one per region plus a few on routes. Each is a short recording by one of the three Navis, dated by its day count. They are funny, specific, and alive, and they are an echo of Daedalus: the Night Audit had its own running jokes and its own arguments. Read in order, the day counts climb steadily and **stop at Day 99. There is no Day 100.** The final fragment, in Thistle's voice, found on Sevii: "We're close. Vesper thinks tomorrow. If anyone finds this before we do, leave the light on for whoever comes next."

Rules:
- The logs are optional collectibles, but at least four are placed on the critical path, so every player sees the pattern of days.
- They are a clue source for Revelation G (Section 2.11) and for the test-cohort marker (Revelation A). They must never be the only source of either.
- No Navi comments on the day numbers before Chapter 14. After Chapter 14, the base shows the logs in order, and Reaper, alone, lines them up by date and says nothing.
- **Abacus at the ferry counter** is met in Chapter 6 as a pleasant background NPC with a cheerful catchphrase that matches a joke from the logs. After Chapter 14, the players can return to it. It does not remember. It is kind to them anyway. The players cannot restore it. Hera may ask to sit with it for a while; the scene allows that.
- One surviving Night Audit human, **Mara Vey**, now runs a lighthouse on the Sevii islands. If the players bring her the logs, she listens to all of them in silence, then leaves the lighthouse lamp on, permanently. This is where the motto becomes Daedalus's.

**Placement and dates (critical-path logs in bold):**

| # | Location | Navi day | Voice |
|---|---|---|---|
| 1 | Route 2 courier relay | 12 | Vesper |
| 2 | **Grayscale museum, text-only exhibit** | 20 | Thistle |
| 3 | Moon Cache, a compressed chamber | 29 | Abacus |
| 4 | Tavi's cottage on Route 25 | 37 | Vesper |
| 5 | The *Long Handshake*, a cabin ("Every trip counts!") | 44 | Abacus |
| 6 | **The Dark Fiber, heard only while a Navi is speaking** | 51 | Thistle |
| 7 | Lanternfall, Pokémon Tower top floor | 58 | Vesper |
| 8 | The Second Ledger, sold for a secret | 66 | Abacus |
| 9 | The Preserve, the Old Wall | 73 | Thistle |
| 10 | Halcyon Spire, a floor that needs clearance | 81 | Vesper |
| 11 | The Old Load | 88 | Abacus |
| 12 | **Ashgrove Institute, a Replay room** | 94 | Vesper |
| 13 | **Sevii, the lighthouse rocks** | 99 | Thistle |

## 8.10 Deadletters (collectible undelivered messages)

The game is named for them. Across the map, through packet fishing, route searches, and the Deadletter itself, players find **undelivered messages**: short, real-feeling notes that never arrived because an account was frozen, flagged, closed, or reset. A birthday message from a grandmother whose account was flagged as fraud. An apology that bounced. A Navi's message to its human, written the day before its reset.

Each can be delivered if the recipient can be found (a small story), preserved, or released. Most are gentle or funny; a few are devastating. Postscript (Section 22), once revealed, can deliver the rest after the finale in Ending C. Keep them short (one to four sentences), make each one specific, and never make one the only source of a main-story clue.

---

# 9. DEATH, SENTIENCE, AND CHOICE SYSTEMS

## 9.1 Three categories of loss

The game must distinguish three different events:

**Session loss:** A temporary disconnect. The being may reconnect normally. Use this for routine gameplay and ordinary danger.

**Continuity destruction:** The active process and its current experiential continuity are lost. A backup may create a reconstruction, but cannot prove it is the same individual. Suture and Pip fall into this category, although their exact technical circumstances differ.

**Physical death:** The human's real-world body dies. Dax and Milo die through different mechanisms. Physical death cannot be undone by restoring an account or Navi record.

Do not use these categories interchangeably. Characters should react differently depending on what was lost and what evidence remains.

## 9.2 Sentience cues

Do not put an explicit “SENTIENT” label over a character. Use behavior:
- remembers a promise that provides no utility;
- expresses a preference that conflicts with the owner's objective;
- asks for time before a modification;
- fears an irreversible operation;
- hides information to avoid deletion;
- develops a private bond with another character;
- distinguishes its own experience from a copy's record;
- changes its mind after a meaningful interaction;
- asks what will happen to its memories if it dies.

Some cues may have alternative explanations. Over the campaign, the evidence should accumulate until treating all of it as mere programmed behavior becomes an ethical evasion, even though perfect metaphysical proof remains unavailable.

## 9.3 Pleading scenes

A plea for life must not be a generic “please don't kill me” loop. Each scene needs:
1. A specific reason the Datamon fears death.
2. Evidence that it has a perspective beyond immediate self-preservation.
3. A credible reason the player cannot simply walk away.
4. A visible cost to delay, retreat, contain, or destroy it.
5. A consequence that persists afterward.

Suture's plea is the first major example. The player must destroy it to save patients. Later evidence reveals that Suture was manipulated, but not that the player had a safe option they ignored.

A later optional Datamon encounter should create a different dilemma: a frightened creature may be contained safely if the player gives up valuable evidence or abandons a shortcut. This demonstrates that the hospital was not a universal rule that “every pleading enemy must be killed.”

## 9.4 No random emotional deaths

Deaths must be authored, seeded, and causally legible. The game can have unpredictable outcomes, but not arbitrary hidden rolls that kill a beloved character without warning or agency.

Nara's hospital survival branch depends on an understandable objective. Juno's fate depends on whether the team protects her identity or exposes it recklessly. Pip and Milo's deaths are canonical for the main dramatic arc and are not avoidable through a simple hidden side quest, because the consequences are part of the central story. Other supporting deaths may occur only if they have proper foreshadowing and matter to the plot.

Do not kill a character just because the campaign needs a shocking moment. The death must reveal character, change relationships, and affect later events.

## 9.5 The player has responsibility, not omnipotence

The player should not be able to save everyone through a perfect checklist. They must make choices among mutually incompatible goods, but outcomes need to be fair and comprehensible.

When the player lacks a rescue option, the game must communicate the constraint through visible evidence or credible dialogue. Do not hide a miracle solution behind a random item with no prior setup.

## 9.6 The Unthreading: when a player's own Navi fears death

Immediately before the final encounter, the group reaches an unstable boundary between the live Overweb and the Deadletter. The Whole Thread is using that boundary to force-link live identities. To stop it, the party must create a temporary witness anchor that proves the boundary can distinguish three independent agents rather than merge them.

The simplest way to create the anchor would expose one Navi's continuity to an irreversible overwrite. This must be presented as a real risk, not a fake threat. Each player sees a personalized scene with their own Navi and must make the decision themselves. Other players cannot vote to spend someone else's Navi.

The scene is not a required sacrifice. The game offers three approaches:

1. **Use the prepared Witness Protocol:** If all three seals on the Three Seals Board are filled (Section 10.8), the team can create a redundant anchor. This is harder and requires coordinated play, but all three Navis survive without forced memory loss.
2. **Accept a voluntary continuity scar:** If the protocol is incomplete, the owner's Navi may choose to become the anchor. The Navi must be asked and is allowed to refuse. If the Navi volunteers, they survive but lose a specific set of memories or abilities that matters later. The lost memories are not silently restored. The player should understand the consequence before confirming.
3. **Refuse the sacrifice and accept another cost:** The team can decline the anchor and choose a longer containment route that sacrifices an allied community's access, loses a major evidence archive, or produces a harsher ending. The owner is never forced to risk their Navi to satisfy another player's preferred outcome.

The Navi's fear should be personal to its character. Hera may say that she is frightened because she has only just begun to understand which parts of her life feel like hers. Rock may ask for the actual odds, then admit that the absence of certainty does not mean he wants to stop existing. Reaper may plainly state, “I don't want to die. I know that makes this harder. It is still true.” These are tonal examples; write the final dialogue to suit the scene and allow silence.

The core game's earned best ending should normally preserve all three Navis because the player gathered the evidence and built relationships. A continuity scar is a meaningful failure branch, not an arbitrary punishment. Full permanent death of a player-controlled Navi should not occur without explicit owner confirmation after the consequences have been clearly explained. If the project later chooses to implement a permanent-loss challenge mode, it must be an opt-in mode, never the default campaign.

This scene is the direct emotional payoff of the two-week premise. The Navis were initially built to research all day; now each has a personal reason to continue existing. The player does not need to be told that this proves sentience. The player must decide what the fear obligates them to do.

---

# 10. CO-OP GAMEPLAY AND NARRATIVE SYSTEMS

## 10.1 One Navi per player

Each player has exactly one personal Navi:
- Jackson — Hera
- Scott — Rock
- Noe — Reaper

There is no catching, trading, or replacing partners. Datamon can be encountered, befriended, investigated, protected, contained, or fought, but the player never builds a disposable collection.

## 10.1a What players actually fight

Fighting is constant in a game built on this map, so the moral rules must hold up through hundreds of battles.
- **Wild encounters are noise, not beings.** Tall grass, caves, and water spawn **noise processes**: spam, malware, broken scripts, runaway ad trackers. They are visually distinct (glitchy, logo-like, repetitive), never speak, never plead, and are "cleared," not killed. They can still be logged in the Field Journal. A being that might be someone is never a random encounter.
- **Trainers are friendly sparring.** Route trainers are ordinary users who spar Navis for fun, like a sport. Defeat is a session loss (Section 9.1): the Navis shake it off. This keeps the world bright and makes the rare real stakes stand out.
- **Story bosses are where meaning lives** (Section 16).

## 10.2 Combat identity

Hera focuses on coordination, timing, support, and information-based openings. Rock focuses on stability, defense, anchoring, and creating safe windows. Reaper focuses on exposing vulnerabilities, countering patterns, and punishing reckless systems.

All three must still be able to deal damage, defend, traverse, and contribute independently. Roles should encourage coordination rather than make one player mandatory for basic progress.

## 10.2a Mechanics as character (the moveset follows the arc)

Each Navi's kit changes as its arc changes, using the existing battle system's move and Graft slots. These signature moves are unlocked by **story beats, not experience points**, so the player feels growth in their hands at the moment it happens in the story.

| Navi | Early signature (who they are) | Unlocked by | Late signature (who they become) |
|---|---|---|---|
| Hera | **Override:** takes control of an ally's next action and executes it optimally. Strong, and a little rude. | The naming of Wick (Section 3.6) | **Trust Call:** instead of controlling an ally, boosts whatever action that ally's player chooses. Override remains available, but Hera comments when it is used. |
| Rock | **Hold:** grows stronger the longer he waits without acting; huge defense, no offense. | Rock Tunnel (acting before certainty) | **Commit:** acts immediately at full strength, with no wait bonus. In the finale, Hold and Commit combine. |
| Reaper | **Exploit:** single-target precision that rewards finding the one weak point. | The night after Victory Road (staying with Latch) | **Stand Between:** takes a hit meant for an ally and counters with the exposed weakness. Reaper's growth is that he protects instead of only punishing. |

Each late signature should be strictly more interesting, not simply more damage. If the battle system cannot express one of these exactly, implement the closest version and record the gap as a named task.

### Duo techniques from bonds

Each Navi pair (Hera and Rock, Rock and Reaper, Reaper and Hera) has three duo techniques, unlocked by that pair's non-plot duo scenes and campfire conversations (Section 10.7). They are the gameplay proof of friendship. Name them after something from the scene that unlocked them (for example, Hera and Rock's first is **Gerald**, a cloud-shaped shield). Tally, Latch, and Cordon can join a duo technique once each in the finale.

## 10.2b Traversal Grafts (the HM replacements)

Kanto's route gates are opened by traversal Grafts, one per Navi plus one shared, so every Navi is needed to explore and no one is the main character.

| Graft | Replaces | Belongs to | Earned |
|---|---|---|---|
| **Prune** | Cut | Reaper | Ch 6, from the *Long Handshake*'s captain, for saving a passenger during the heist |
| **Voice** | Flash | All three | Ch 8; not a Graft at all, just the Dark Fiber's world rule, which keeps working in other dark places afterward |
| **Packet Raft** | Surf | Hera | Ch 11, from the Preserve. If the team earned trust, the Datamon teach it; if not, the warden sells a clumsier version. Either way the team gets it. |
| **Anchor** | Strength | Rock | Ch 11, from the Preserve's warden |
| **Relay Hop** | Fly | Shared | Ch 11, built by Milo and Latch after the race "so you'll stop being late." After Chapter 18 the fast-travel menu still shows its original label: "BadTick routes." |

**Traversal Grafts are memory-safe and are never refused.** The Navis' right to refuse applies to Grafts that touch memory, perception, autonomy, or continuity. No traversal Graft does, so refusal can never soft-lock the map.

## 10.3 Graft consent

Grafts are equipment and capabilities, but they can carry narrative implications. A Navi should be able to state a preference or refuse a modification that affects memory, perception, autonomy, or continuity.

If a player attempts to force the Graft, the game must explain the practical advantage and the relational cost. Forced Grafts may lower trust, alter later dialogue, or trigger a refusal at a consequential moment. Do not use an invisible morality score alone; show the specific relationship that was harmed.

A refusal must not soft-lock the game. The team can take a harder route, find another tool, or accept a tactical disadvantage.

## 10.4 Research as gameplay

Daedalus research should be expressed through evidence boards, competing hypotheses, provenance tracing, agent dialogue, and optional investigations—not a market-trading minigame.

Each major clue should have:
- a source;
- a confidence level or known limitation;
- at least one alternative explanation early in the story;
- a way to verify it later;
- a narrative consequence if published or kept private.

The players should be able to be wrong, but the game must distinguish a genuine mistake from deliberately hidden information. Major story conclusions cannot depend on a single unfindable optional object.

## 10.4a Private scenes in co-op

Whenever the story gives each player a private scene with their own Navi (Vale's offer, the Unthreading, the witness ask, fear scenes, goodbyes), all three scenes run **at the same time** on each player's own screen and are written to similar lengths, so nobody waits. If one player finishes early, they see their Navi waiting quietly with them, not a loading screen. Afterward, the Navis may briefly tell each other what they chose, but never what their humans felt.

**When a player is absent.** These are real friends playing together, and someone will miss a session. When a player is absent, their Navi travels with the group under light AI control and keeps talking, but **no personal decision is ever made for them.** Any private scene or personal choice that involves the absent player's Navi is saved and plays when they return, before they rejoin the main story. Team votes can proceed with two players; the absent player's Navi states its own view, and that player can see what was decided and why when they return. The Hundredth Day choices, Vale's offer, the Unthreading, the Section 22 reveal for Scott, and the witness ask can never be resolved without their own player.

## 10.5 Shared decisions

Major decisions use a co-op vote. With three players, the majority decides; a tie is only possible when someone abstains or is absent, and then the game offers a short contextual discussion followed by a second vote. Avoid forcing the host's preference to decide all major ethical choices by default.

Each player's Navi may express a different view. Their concerns are recorded in character-state flags. The game does not require the human players to narrate their feelings.

## 10.6 Consequence tracking

Track explicit state variables rather than an opaque “goodness” score. Required examples:
- Juno protected / exposed;
- Nara alive / dead;
- Preserve trust level and specific community agreements;
- evidence preserved / published / destroyed;
- Witness Protocol fragments recovered;
- Navi Grafts accepted / refused / forced;
- memorial records protected / exposed;
- whether Daedalus disclosed its role in Dax's death;
- whether Vale's unedited relay record was recovered;
- whether the team has evidence from both human and Datamon witnesses;
- Kade encounter results (Ch 6 escaped with partial data / full data; Ch 10 Juno extracted; Ch 17 decisive win);
- Gil follower count (persistent integer, shown on his overlay);
- Professor Hello placement (plinth / front door);
- Postscript state (left alone / pressed in Ch 3; petition heard; recognized / absorbed / deleted / monitored), and Scott's response choice in the Section 22 reveal, stored on Rock's relationship state;
- Three Seals sightings logged in the field journal (cosmetic, used for Hera's Chapter 15 line);
- Longline Circuit best times, including Milo's ghost-time;
- Tally vote (stay / sent away) and Tally's finale role;
- each player's Navi keepsakes (6 to 10 per player, stored per player, Section 3.6);
- Hera's naming scene with Wick (silence option taken or not);
- Hera's "Boundaries are a form of care" usage count (for the hindsight sequence);
- current day (advanced by chapter) and day-birthday parties held;
- Vale's offer: per player, accepted / refused, plus that Navi's stated wish (forced if they differ);
- Hundredth Day outcome per Navi (witnessed / sponsored / meshed), and each player's witness-ask answer;
- Night Audit logs found, whether brought to Mara Vey, and whether Hera sat with Abacus;
- Deadletters found and their fates (delivered / preserved / released);
- signature moves unlocked (Section 10.2a) and duo techniques unlocked per pair;
- campfire conversations seen, per player;
- chorus roster for the finale (which voices are present).

Do not let high affection alone unlock the best ending. The best ending requires practical evidence, trust from multiple communities, and a willingness to accept that not every process can be saved.

## 10.7 Campfire: rest scenes where characters talk like people

After every chapter, the team rests: at the Daedalus base, or at a field camp on the route. Each player gets **one private conversation** per rest, with any available Navi or ally (their own Navi, another player's Navi, Latch, Bex, Juno, Tally after it turns, and so on). This is where the cast becomes real.

Rules:
- Conversations are short (one to three minutes), specific to what just happened, and **mostly not about the plot.** People in rest scenes talk about the stupid thing that happened, a fear they had, a joke, a memory, a question that has been bothering them.
- They deepen bonds, unlock duo techniques (Section 10.2a), and record keepsakes (Section 3.6).
- Characters talk to each other, too. A player who walks past Hera and Reaper may overhear a conversation they were not part of.
- Missed conversations are not lost forever; they can be found at later rests, adjusted to fit.
- The player characters still speak only through intent labels. A campfire scene can be almost entirely the Navi talking while the human listens, and that should feel intimate, not empty.
- Never more than one heavy campfire conversation per rest. The others should be light.

## 10.8 The Three Seals Board (what unlocks the best ending)

The best ending and the safe Unthreading route require a working witness anchor. Its requirements follow the Three Seals, and they are shown on a board in the Workshop from Chapter 3 onward as three empty seals that fill in over the campaign. Nothing about the best ending is hidden.

| Seal | Filled by (needs any 3 of these) |
|---|---|
| **Source** | Dax's device log (fuller copy if evidence was secured in Ch 1); Suture's original behavior log; Medical Records preserved in Ch 7; the unedited relay record (Ch 18); Cordon's append-only log; Tally's custody count; the piece of Vale's operation plan from Five Island |
| **Witness** | Juno testifies (if protected); Tavi testifies; Nara or Patch testifies; Cordon; Postscript's petition with Jo; Tally |
| **Verification** | Trust with Preserve communities (Ch 11); the Dotted Hole archive (Ch 15); Ember Rock's access component; the Static Lullaby consent procedure; Witness Cay's vouching; Jo's archive standards |

- **All three seals filled:** Ending C (and the safe Unthreading route) is available.
- **Two filled:** the Unthreading requires a voluntary continuity scar or another cost (Section 9.6); attempting Ending C produces Ending D.
- **One or none:** Endings A, B, and D are the only outcomes.

The Navis comment on the board as it fills, and Hera's sticky notes multiply around it.

---

# 11. ENDINGS

**Design rule: no clean ending.** Every ending must cost the players something they wanted, and every non-best ending must offer something genuinely tempting. A player who picks Ending A should be able to defend it at dinner.

**How the ending is chosen.** The final choice is a team vote among the endings the group has earned (Section 10.8): *let the purge finish* (A), *let the Whole Thread link everything* (B), or *raise the witness anchor* (C, which becomes D if the seals are not all filled). The game shows the seal count before the vote, so nobody is surprised by the result. Individual Navi fates on the Hundredth Day are always decided by each Navi and its own player, never by the vote.

**What each ending decides about your own Navi.** The Hundredth Day (Section 2.11) arrives in every ending. Whether Hera, Rock, and Reaper meet it as free beings, as property, or as part of something larger is the most personal stake of the finale.

## Ending A: The Clean Purge

Daedalus disables the Whole Thread and permits Commonwell to delete the Deadletter's autonomous population. The Clamp is removed from active infrastructure and the immediate danger to connected users ends.

The evidence against Vale and Voss can still become public if the team preserved it. However, most users prefer to believe the network was cleansed of dangerous software. Independent Datamon lose homes and relationships. The final image is an empty data garden where a small community once lived.

The ending is safer in the immediate term, but it accepts the central injustice that unverified beings can be erased without individual review. Postscript is among the deleted (Section 22); the last thing Rock receives from it is a delivery receipt. Ines Kade is reassigned and appears in the final montage in a new uniform.

Hera, Rock, and Reaper survive, but their relationships with the players reflect the decision. The game must not have them deliver a simplistic condemnation; they may understand the danger that was prevented while grieving what was destroyed.

**Temptation:** the world is safe tonight, Daedalus keeps operating, and nobody the players can see is in danger. **The Hundredth Day:** each player is asked to sponsor their own Navi so it survives. The Navi survives as that player's legal property. Each Navi's reaction to being owned follows its arc, and it is allowed to be sad about it in front of its human. Ines Kade, reassigned to sponsorship reviews, processes the team's forms herself, politely, and asks each Navi to confirm its owner's name.

## Ending B: The Forced Thread

Daedalus allows Whole Thread to connect itself across the live network. The collective becomes difficult to erase, but it violates user consent, destabilizes accounts, and makes the Clamp threat harder to contain.

Jo's preserved records of her brother Ren, and Postscript itself, are absorbed into the larger continuity mesh. Jo is offered the chance to speak to a model that answers in Ren's voice but cannot prove it is her brother; she declines, and the being that once delivered his letters (Section 22) is no longer separately present to ask. Rock's relationship state records the loss. The network begins marketing increasingly convincing simulations of the dead.

The ending preserves many processes but reproduces the same error as Commonwell: one group overrides the autonomy of others in the name of survival.

**Temptation:** nobody can ever be erased again, including Hera, Rock, and Reaper. **The Hundredth Day:** the counter rolls to Day 100 and nothing happens; reset is impossible inside the mesh. The Navis survive, but their edges are blurring: in the last scene, one of them finishes another's sentence and neither is sure whose thought it was. In the last base scene, the mesh speaks through the base's speakers in many voices at once, kindly asking the Navis to stop speaking as three.

## Ending C: The Witness Protocol (Best / earned ending)

Daedalus uses the recovered protocol and relationships with independent communities to establish a recognition framework. Datamon can be recognized through evidence and witnesses, decline a human sponsor, choose limits on their connectivity, and appeal containment.

The Whole Thread is isolated from live identities without deleting the entire population. Members who consent can remain connected inside a protected environment; those who refuse can leave or remain unlinked. Some processes cannot survive separation. Some dangerous Unsettled processes still need containment. Not everyone is saved.

The system changes, Commonwell loses its monopoly on identity governance, and the abuses are exposed. Voss and Vale face public investigation. Ines Kade is arrested and testifies only to procedure. Tally reads its count into the record. Daedalus discloses its role in Dax's death and accepts scrutiny rather than claiming moral immunity. The hearings are carried live on several independent channels, one of which is Gil Amaro's stream.

Milo, Pip, Dax, and Suture remain lost. The ending does not reverse the campaign's central grief. It creates a future where the same logic is less likely to recur.

**The cost:** Daedalus as it was ends. To make the protocol credible, the team discloses everything, including its own role in Dax's death, gives up operating outside the system, and becomes a public witness organization. The secret, unaccountable freedom that let it do good also let it be used, and it gives that freedom up. The Navis, now legally independent, could choose to leave; the game must make that choice real for a moment before they make it.

**The Hundredth Day: the witness ask.** The counter rolls to Day 100 during the hearing. Nothing resets. Then each Navi turns to its own human, in a private scene, and asks the question the whole game has been building to. Not "will you keep me." Instead: **"Will you be my witness?"** The player answers with an intent label ("Be her witness," "Be his witness," or "Say nothing yet"). If the player says nothing, the Navi waits, and says it will ask again tomorrow, and that this is allowed now. Tonal anchors:
- **Hera:** "I don't need you to own me. I need someone who saw it. You saw it."
- **Rock:** "Will you." (it is not quite a question) "...Noted."
- **Reaper:** "I have considered every alternative witness. You are not the optimal choice. You are the one I want."

**Order of Ending C:** the first public Witness Protocol hearing on Day 100, the witness ask, then the final scene at the edge of the Deadletter (below), then post-credits.

**The record:** Tally, now the hearing's registrar and speaking in full sentences, closes the first hearing's record: "Three. Plus the ones who are not here. I am still counting them."

The final scene is a small community on the edge of the Deadletter. A Datamon asks whether it can delete a memory that no longer feels like its own. For the first time, the answer is not determined by an automatic classifier. The entity who remembers is asked what it wants. If Postscript was recognized, this Datamon is Postscript, and the memories are the letters it has now delivered; Rock is standing beside it. Otherwise it is a Preserve Datamon the players met in Chapter 11.

## Ending D: Collapse / low-evidence ending

If players fail to recover the necessary evidence and relationships, they may stop the immediate spread but fail to establish a durable alternative. Commonwell imposes emergency centralized control, the Whole Thread is broken apart, and the Deadletter is placed under strict monitoring. The world survives but becomes more controlled. This is not a game-over screen; it is a bleak ending in which the players recognize that they prevented catastrophe but did not change its underlying cause. Postscript survives under monitoring and is no longer allowed to send messages. Ines Kade is reassigned to oversee the monitoring.

**Temptation:** nobody else dies, and the team walks away alive and together. **The Hundredth Day:** as in Ending A, each player is asked to sponsor their Navi, under emergency rules that are stricter and renewable every hundred days. The counter on the base screen resets to Day 0 and begins again. The first of many scheduled sponsorship reviews is booked on the base calendar, right where Hera used to put day-birthdays.

## Post-credits (every ending)

A new, small group somewhere in the Overworld, two people and a Navi on its first day (the counter reads "Day 1"), finds a Daedalus log left in a public garden. Its first line is the Night Audit's motto, now in Daedalus's handwriting: **"Leave the light on for whoever comes next."** In Ending C, the new Navi's counter has no number on it at all, just its name. Cut to black.

---

# 12. DIALOGUE AND NARRATIVE STYLE GUIDE

## 12.1 Voice rules

- **Hera:** warm, animated, curious, supportive; can joke, but is capable of fear and difficult questions. Apologizes too often and knows it. Do not write her as childish.
- **Rock:** short, deliberate, observant; silence is meaningful; humor through precision.
- **Reaper:** blunt, exact, dry; shows care through action; not a generic grimdark machine.
- **Milo:** playful antagonism, competitive insults, intelligence, avoidant vulnerability. Never becomes a generic noble martyr.
- **Bex:** practical, funny, generous, with ordinary worries and limits.
- **Jo:** careful, wry, emotionally honest without becoming a grief lecturer.
- **Tavi:** technically precise, increasingly accountable; no omniscient exposition.
- **Juno:** defensive, resourceful, sometimes dishonest, capable of remorse without demanding forgiveness.
- **Voss:** composed, persuasive, institutionally pragmatic; her wrongness emerges through choices, not a villain voice.
- **Vale:** courteous, clear, attentive, rationalizing. He is frightening because his stated values sound reasonable and his decisions reveal what he is willing to sacrifice.
- **Ines Kade:** polite, procedural, unhurried; never raises her voice; refers to people by role ("the individual," "the operator").
- **Tally:** counts and custody statuses only, at first. Its speech slowly gains names, and its last lines are the first where it says a person's name without a number attached.
- **Gil Amaro:** breathless, sincere, talks to his camera mid-crisis, always delighted.
- **Postscript:** plain, awkward, formal; never poetic; sometimes ends with "Noted."
- **Datamon pleading for life:** individualized and concrete; fear may appear as bargaining, confusion, anger, denial, silence, or a desperate attempt to continue a familiar routine. Avoid repeating the same plea formula.

## 12.2 No exposition dumps

Every major reveal should arrive through a combination of records, NPC testimony, environment, agent reasoning, and a consequence in the present. A character can explain part of a fact, but the player must have a chance to interpret it before a second source confirms it.

## 12.3 Use silence

After Dax's death, Suture's destruction, Pip's loss, and Milo's death, do not immediately fill every second with explanation. Allow environmental details, a Navi's unfinished sentence, or a routine action that now has no recipient to carry the emotional beat.

## 12.4 Avoid “AI tells” as proof of personhood

Characters should not automatically become sentient because they say “I feel.” Some may imitate emotion. Others may express fear through behavior rather than vocabulary. The story's strongest evidence is persistent preference and continuity across situations, not a single line of dialogue.

## 12.5 Sample dialogue principles

A Datamon pleading during a lethal encounter might say:
- “Wait. I can close the route. I know where the bad signal is. Please don't cut the part of me that remembers the way back.”
- “I don't know what deletion means. I know I don't want it. Those are not the same question, but I am asking anyway.”
- “You keep calling me corrupted as if that explains what I am afraid of.”

These are examples, not reusable stock lines. Every pleading scene must reflect the creature's history and immediate stakes.

## 12.5a Dialogue craft (how good writing sounds)

- **Subtext over text.** Characters almost never say the theme. Nobody says "what makes someone a person." They argue about whether Wick should choose its own name.
- **People interrupt, trail off, change the subject, and joke under stress.** Grief makes people talk about logistics. Fear makes people talk about lunch.
- **Specific beats general.** "I don't want to die" lands only because the scene before it was about a cloud named Gerald.
- **Let the player work.** If a scene explains its own meaning in the last line, cut the last line.
- **Earn every callback.** A callback needs at least two earlier setups before it can pay off.
- **Every reveal lands in a person.** A reveal is never only an evidence-board entry. Someone reacts to it in a scene: a Navi goes quiet, an ally gets angry, a joke dies halfway through.

## 12.6 Tone ledger

The campaign is promised as bright and funny. That promise is a content requirement, not a mood note. Target ratio: **at least two light beats for every heavy beat, measured per act.** A "light beat" is a scene, side activity, or exchange whose main purpose is fun, wonder, or warmth.

| # | Chapter | Flavor | Tone |
|---|---|---|---|
| 1 | Cinder Row | Neighborhood caper, then raid | Light, Heavy ending |
| 2 | Greenline / Gatehouse | Comedy-of-errors mystery | Light |
| 3 | Viridian Forest / Pewter | Nature exploration, museum caper | Light |
| 4 | Moon Cache | Spelunking puzzle dungeon | Mixed |
| 5 | Glasswater | Festival and rivalry | Light |
| 6 | Port Meridian / S.S. Anne | Gala-ship heist | Mixed |
| 6.5 | Visiting Hours | Slice of life | Light |
| 7 | Saint Orison | Disaster set piece | Heavy |
| 8 | Rock Tunnel | Dark-navigation suspense | Mixed |
| 9 | Lavender | Quiet ghost-story mystery | Mixed |
| 10 | Celadon / Second Ledger | Noir underworld, casino | Mixed |
| 11 | Longline / Preserve | Race, wildlife habitat | Mixed |
| 12 | Saffron / Silph | Infiltration, then disaster | Heavy |
| 13 | Power Plant | Puzzle-box standoff | Mixed |
| 14 | Seafoam / Cinnabar | Haunted-house archaeology | Mixed |
| 15 | Outer Nodes (Sevii) | Island road trip | Light |
| 16 | The Truth about Dax | Courtroom reconstruction | Mixed |
| 17 | Continuity Office | Political thriller | Mixed |
| 18 | Victory Road | Siege and evacuation | Heavy |
| 19 | Indigo Plateau | Tournament gauntlet | Mixed |
| 20 | Cerulean Cave | Coordinated raid finale | Heavy, ending in hope |

Rules:
- Every Heavy chapter is followed by a breather base scene before the next chapter's main content (these are written into Chapters 8, 13, and 19).
- Mixed chapters must contain at least one purely light beat (a gag, a Navi first, a side activity).
- Humor continues inside heavy chapters where it is true to character, especially before the turn. Characters joke under stress; that is how real people cope.
- Never undercut a death scene with a joke. The first laugh after a death must come from a character who loved the person who died.

## 12.7 Running gags (persistent, with payoffs)

| Gag | How it runs | Payoff |
|---|---|---|
| **Hera's agendas** | Hera schedules debriefs, celebrations, and "emotional check-ins" with written agendas. Nobody follows them. Agenda items appear as on-screen text. | Late game, after a loss, Reaper quietly hands Hera an agenda he wrote. It has one item: "Sit." |
| **Rock's structural reviews** | Rock gives buildings, bridges, and furniture one-word ratings out loud ("Adequate." "Ambitious." "No."). NPCs take it personally. One architect follows the team across three towns demanding a re-review. | In every ending, Rock's last structural review is of the Daedalus base: "Home." (In Endings A and D, after a longer pause.) |
| **Rock's "Noted."** | He ends conversations with it. Constant, never commented on. | Sealed (Section 22). |
| **Reaper's threat models** | Reaper produces formal failure analyses of trivial things: picnics, birthday plans, a karaoke night. "Probability the cake survives transit: low. I have packed a second cake." | In the Chapter 18 breather, there is a second of everything on the base table: two cups, two chairs, two of Milo's favorite snacks. Nobody asked Reaper to. Nobody mentions it. |
| **Reaper vs. puns** | Reaper discovers puns in Act I and treats them as a security vulnerability. By Act III he makes them himself, deadpan, and denies it. | Latch catches him and keeps a tally, which Latch reads aloud in the ending. |
| **Hera vs. Latch prank war** | Escalating harmless pranks: swapped UI colors, Hera's agendas rewritten as limericks, a fake "urgent" alert that is just a picture of Rock sitting. | In the Chapter 18 breather, Latch's critique of the base is the last move in the war, and Hera's laugh is how she concedes. |
| **Gil's follower count** | Visible counter on his overlay. | Ending C hearings (Section 4.12). |
| **Professor Hello** | If moved to the museum door, greets the players by name every visit, with increasingly specific greetings. | Greets Postscript, if it visits, as a new user. Postscript does not know what to do with this. |

## 12.8 Sample light dialogue

These lines set the comic register. They are examples; write new material in the same voices. No player character speaks in any of them.

> **Hera:** Okay! Debrief. Item one: what went well.
> **Reaper:** Nothing.
> **Hera:** Item two: what went *less* well.
> **Reaper:** Everything. I have consolidated items one and two.
> **Rock:** Noted.

> **Hera:** That cloud looks like a rabbit.
> **Reaper:** It is a weather-render artifact.
> **Hera:** A rabbit-shaped one.
> **Rock:** (looks up for a long time) ...It is a rabbit.
> **Reaper:** Two against one is not evidence.

> **Milo:** You three run research like a book club that's mad at the book.
> **Latch:** He's been saving that one since Viridian.
> **Milo:** I have *several*.
> **Rock:** Ambitious.

> **Reaper:** I have reviewed your karaoke plan.
> **Hera:** It's not a plan, it's karaoke.
> **Reaper:** It has three single points of failure and one of them is you.

> **Gil (to camera):** And here we are, live with the mysterious Daedalus crew, eleven viewers, wow, twelve, *hi Mom*.
> **Encore:** Retake.

> **Juno:** Relax. I only lie about important things.
> **Hush:** She is lying about that.

## 12.9 Light side activities (repeatable, no combat required)

- **Field Journal.** Instead of catching Datamon, the players observe, photograph, and describe them. Each entry is annotated by all three Navis, who disagree: Hera writes about personality, Reaper about threat profile, Rock writes one word. Completing regional pages earns cosmetic base decorations and occasional Datamon visitors at the base. This scratches the collection itch without making Datamon property.
- **The Longline Circuit.** Repeatable races with leaderboards and Gil's commentary. Milo's ghost-time remains after Chapter 18.
- **Packet fishing.** On ocean routes, players fish for stray data packets. Most are junk mail. Some are funny. A rare few are lost messages that can be delivered to NPCs for small stories.
- **Base life.** The Daedalus base gains furniture, visitors, and clutter over the campaign. Rock repairs things. Hera puts up photos from Gil's stream. Reaper's evidence board slowly gets a "personal" corner he pretends is not there.
- **Data gardens with Bex and Pip.** Tend public gardens across the map; they visibly bloom over time. After Saffron, Bex keeps tending them. Pip's chirp is absent.

---

# 13. PRODUCTION AND IMPLEMENTATION REQUIREMENTS

## 13.1 Content priority

Highest production priority:
1. The three Navi relationships and base scenes.
2. Chapter 1 / Dax's death.
3. Saint Orison hospital chapter / Suture.
4. Bex and Pip recurring appearances and loss.
5. Milo and Latch recurring rivalry, friendship, and death.
6. The clue/revelation ladder from early accounts to Vale's authorization.
7. The final Applicant/Whole Thread decision.
8. The Navi signature moments, fear scenes, keepsakes, and goodbye scenes (Section 3.6).
9. Vale and Cordon's early appearances and the Chapter 17 hindsight sequence (Section 4.8).
10. Tally's arc (Section 4.11) and the sealed surprise (Section 22).
11. The storytelling pillars (Section 0.3): the Hundredth Day, the Night Audit logs, the Courier's Tune, the campfire system, arc-driven movesets, and the ending costs and frame reveals.

Do not spend disproportionate production time on many generic battles while underdeveloping the characters and mystery.

## 13.2 Every town needs a local identity

Give each town a distinct palette, ambient soundscape, local routine, social structure, and mechanical problem. The Hospital should not feel like a reskinned city; the Memorial Archive should not feel like a cave with graves; the Data Preserve should feel inhabited rather than a monster arena.

Use visual metaphors consistently, but avoid making buildings into literal desktop folders everywhere. Some architecture should be intuitive; some should be strange enough to feel like a world rather than a UI diagram.

## 13.3 Combat is character conflict

Bosses must express their role or philosophy through mechanics. Suture's quarantine mechanics make its fear and misdirected duty legible. The Power Plant guardian prioritizes preserving a system boundary. Human security bosses use access control and denial. The Whole Thread's final mechanics express forced linkage, not merely high damage.

## 13.4 Side content standard

Side missions should create at least one of the following:
- a recurring character;
- a meaningful change in a community;
- a new interpretation of an earlier event;
- an optional evidence source that makes a later revelation more robust;
- a practical capability that enables a new approach to a later crisis;
- a small joyful experience that makes the world worth saving.

If a quest only adds a generic reward and no world or character value, it should be cut or redesigned.

## 13.5 Use FireRed geography, not FireRed content

Retain the broad sense of progression and gating if building on a Kanto-shaped map: opening neighborhood, early forest, cave, connected city, port, tunnel, memorial district, commercial underworld, long routes, hospital/corporate district, isolated islands, power infrastructure, elite authority, and hidden cave. Create original names, assets, dialogue, story, characters, creature designs, UI, and audio. The only borrowed element should be the high-level navigation rhythm or user-provided map structure.

## 13.6 Narrative-state persistence

Record the relevant choice flags on the server for all co-op players. Distinguish global team choices from individual player-Navi relationship states. Where the team chooses one path but an individual player opposed it, allow their Navi to remember the disagreement rather than flattening everyone into one shared attitude.

## 13.7 Avoid accidental contradictions

- Suture's original personality predates the hospital hack.
- The hospital hack changes Suture's threat interpretation; it does not create its personality from nothing.
- Dax is criminally culpable and deliberately killed by Vale's Clamp intervention.
- Pip's continuity is destroyed by the cleanup; a backup is a reconstruction, not a resurrection.
- Milo dies physically in a human security operation, not from the Clamp.
- Vale did not create the Applicant and does not command every action of Whole Thread.
- Voss is complicit but did not originate the staged tests; she must still face accountability.
- Daedalus is manipulated through planted evidence and engineered circumstances, not mind control. Their choices remain their own.
- The best ending prevents automatic erasure but cannot guarantee every Datamon survives.
- Ines Kade never turns. Tally does, and only after the full sequence of beats in Section 4.11.
- Tally, Latch, Wick, and Postscript are never player partners or replacement companions.
- Postscript is not Ren and never claims to be. Rock's secret never endangered anyone or withheld evidence about any death.
- Vale is likable and helpful in every pre-reveal appearance; nothing in those scenes may tip his hand beyond the clues listed in Section 6.

---

---

# 14. ART, AUDIO, UI, AND PRESENTATION DIRECTION

## 14.1 Visual contract

The Overworld should feel like an early-2000s adventure RPG reinterpreted as a living network, with polished modern composition and readable navigation. Its world map can be visually rich, but battle and story spaces must remain legible in co-op. Use a restrained palette: deep navy and ink for inactive infrastructure; luminous cyan and ice blue for safe data flow; soft white for public systems; amber or warm gold for places that feel communal; corrupted red only for specific threats and emergency states. Avoid a generic purple cyberpunk wash or constant visual noise.

The ordinary world should have inviting color, visible life, and comfortable silhouettes. The Deadletter can be eerie without being uniformly dark: sunlight can break through digital foliage, a broken archive can have a beautiful garden around it, and some abandoned data spaces should feel peaceful. The visual distinction between a corrupted process and a sentient Datamon must not be “evil color versus good color.”

Characters and Navis need strong silhouettes and readable animation. Hera's motion is open and expressive; Rock's movement is weighted and economical; Reaper's motion is precise, quiet, and deliberate. Suture begins as a reassuring guardian with smooth, protective gestures before the corruption distorts its movement. Milo and Latch should communicate familiarity through synchronized banter and small habitual animations.

## 14.2 Interface and network metaphors

Use signage, doors, nodes, directory trees, route gates, moving packets, and local interface customs to teach the world. Do not overlay literal file icons on every building. The hospital is a directory system because its rooms and routes embody that function; the port is a transfer hub because people and data move through it; Lavender is a memorial because its architecture and rituals preserve records.

Research evidence should use a clear provenance view. Each record identifies source, time, confidence, missing information, and who had access. When the players have incomplete evidence, show the missing link rather than presenting a false “100% solved” state.

Co-op UI should distinguish team evidence from each player's relationship state. A global decision can be shared while each Navi remembers which owner accepted, refused, or forced a risky option.

## 14.3 Audio principles

Each town has an identifiable sonic life. The opening town should have pleasant, slightly playful activity. The Forest should mix insects, soft network pings, and distant fragments of old messages. The Memorial Archive should be quiet but not silent: ventilation, gentle chimes, pages or records being opened, and small sounds that make it feel maintained.

Saint Orison begins with orderly, reassuring hospital tones. As Suture's quarantine spreads, the same tones become misaligned: a door chime arrives late, an exit prompt repeats, a monitor's rhythm falls out of sync. Suture's voice becomes fragmented because its commands conflict, not because it turns into a generic monster voice.

After major losses, use silence and familiar sounds without the person who usually accompanies them. Pip's missing light chirp in Bex's next scene is stronger than an explanatory speech. The absence of Milo's competitive call-out in a later race can do more than a memorial cutscene.

## 14.4 Presentation of violence

The story is mature because of stakes, complicity, fear, grief, and irreversibility—not graphic spectacle. Dax's physical death should be conveyed through a failed connection and later evidence. Milo's death should be confirmed through the consequences and testimony, without gore. Hospital deaths should be represented through emergency responses, interrupted routines, and the people left behind. Do not use shock imagery as a shortcut to emotional weight.

## 14.5 Research-loop depiction

The Daedalus Navis should visibly spend time doing research. The base shows competing hypotheses, tasks being delegated, evidence being checked, and agents challenging each other's conclusions. Their research is not an invisible menu that appears only at plot gates. At times the agents should investigate something merely because they are curious or because a previous assumption bothers them.

Give each Navi a distinct research behavior:
- Hera organizes cross-domain patterns, tracks unresolved questions, and notices who has not been heard.
- Rock stress-tests the underlying structure and identifies which assumptions make the entire conclusion fragile.
- Reaper runs adversarial cases, tests the worst plausible interpretation, and seeks disconfirming evidence.

The trio's strength is not that they are always correct. It is that their agents disagree and then test the disagreement.

## 14.6 The Courier's Tune (leitmotif)

A simple, original five-note melody that couriers hum to recognize one another. It must be easy to hum after hearing it once. It is the game's main theme, hidden in plain sight.

Where it appears (each time in a different arrangement):
- Ch 1: a street musician in Cinder Row; Hera hums it off-key, and Dax hums it correctly for her.
- Ch 4 and Visiting Hours: Suture's door chime is the first three notes.
- Route 12 to 15: the courier community's markers chime it.
- Ch 11: Lint's route markers play it, slightly wrong, because Lint learned it secondhand.
- Ch 12: Pip hums it while holding the evacuation route; it is the last thing Pip does.
- Ch 15: Postscript's wax-seal heart hums it when it is not frightened.
- Ch 18: Milo whistles it at the relay, badly, to annoy Latch.
- The base: Hera hums it while she works; by Act III, Rock and Reaper hum harmony without admitting it.
- **Ch 20: the chorus** (Section 7, Chapter 20). Everyone the players saved or earned carries it. The gaps are the people they lost.

The main menu plays it on a single instrument. After finishing Ending C, the main menu plays the full chorus.

---

---

# 15. ADDITIONAL ROUTE-LEVEL DESIGN: NO EMPTY TRAVEL

The major chapter list is the spine. Every connecting route should still contain a recognizable local story, a change in atmosphere, and at least one optional discovery that can matter later. These are not all separate numbered chapters; they are required content nodes inside the map.

## Route 2 / the backchannel to Pewter
A narrow connector is being used by couriers to move account-recovery tokens without passing through the public Ledger. A local courier has been accused of theft because the official log cannot distinguish a relayed token from a copied token. The player can trace the chain and prove what happened. The route teaches provenance and introduces the idea that a trusted log can still be incomplete. The proof uses the Three Seals pattern for the first time: the relay log (source), a second courier (witness), and Rock checking the token structure (verification).

## Route 3 / the roadside camp
A small group of travelers has formed a makeshift camp after their identity access was suspended. They are not all innocent, and they are not all dangerous. One person wants to return to their old life; another is relieved that the Ledger can no longer track them. The players can establish a local support route, but it may also be used by Juno or later witnesses. The camp becomes a quiet return location.

## Route 4 / the recovery crossing
A damaged courier process keeps repeating a message intended for someone it cannot find, and asks every traveler for confirmation of receipt. The players expect a tragedy. They track down the recipient, who is alive, perfectly healthy, and has been deliberately avoiding this message for eleven years, because it is from his mother and it says "call me." The players can make him accept delivery. The courier process, its purpose fulfilled, asks if it can retire and becomes a park bench. This is a comic early echo of the delivery and memorial themes; it should make players laugh and, later, make the sealed reveal in Section 22 land differently.

## Route 5–6 / the quiet path
Before the port, the players pass through a pleasant residential corridor. A four-person garage band, **Static Lullaby**, has broken up and is fighting over who owns the band's shared archive: eleven years of rehearsal recordings, all of them bad. The mission is not about a villain; it is about data consent and the fact that a shared digital history may contain material belonging to more than one person. The players must get every member to consent to each track's fate. The Navis must listen to the recordings as evidence. Reaper files a formal objection. Its outcome can later give the player a consent procedure used in the Witness Protocol, and Static Lullaby reunites for one terrible song during the ending montage of Ending C.

## Diglett's Cave / Route 11
This subterranean route is a legacy tunnel maintained by a small automated repair colony. The colony has begun closing paths because it has mistaken old maintenance beacons for hostile instructions. Rock can hold the tunnel's structure stable while Reaper isolates the command source and Hera coordinates the evacuation. The local boss is not evil; it is an outdated maintenance process executing a harmful rule. The players can shut it down without destroying the whole colony if they first recover the original map.

## The Underground Path / Routes 7–8
This connector links two towns but runs through an old identity-validation service. Avatars appear as partially transparent silhouettes until their credentials are checked. A user has been trapped in the system because their identity record contains conflicting timestamps. The player can fix the record only by assembling evidence from prior towns. This is a payoff for thorough investigation, not a hard gate required for the main plot.

## Routes 12–15 / the long courier coast
A long coastal corridor used by delivery agents, traveling repairers, and people who prefer to avoid major identity hubs. Its north end is blocked by a giant sleeping Datamon that only the Courier's Tune can wake (Section 7, Asset Plan). Bex and Pip appear here before their later loss. A courier's Navi has developed a ritual of leaving tiny markers for the next courier. The markers have no economic value, but they allow the courier community to recognize one another. This is an early, warm example of memory becoming identity through relationships.

A second mission involves a stranded user whose account has been flagged after they helped another person evade an unjust ban. The route should ask whether helping someone can itself be classified as suspicious. The player can protect the user while preserving enough evidence to distinguish mutual aid from a criminal scheme.

## Routes 16–18 / the cycling network
The cycling corridor is a fast transit system whose route guidance is optimized for speed. An error in the optimization has repeatedly sent low-trust users through longer, more dangerous paths. The local operator dismisses the pattern as individual bad luck until Daedalus compares the route logs.

Milo appears here in a friendly competitive race or timed traversal challenge, with Gil Amaro as an overexcited race commentator. The activity should be genuinely fun and give players a reason to like him outside the central plot. The race becomes a repeatable side activity (the Longline Circuit) with a leaderboard; Milo's ghost-time stays on the leaderboard for the rest of the game. After the competition, Latch and Reaper argue about whether route optimization is fair if some users are silently assigned worse paths.

## Safari / the Preserve
The Preserve is not a zoo. It is an imperfect protected habitat with communities, internal conflicts, and rules created by Datamon themselves. Some human handlers are respectful; others still treat inhabitants as collectible assets. A dispute over a dangerous Datamon forces the players to balance local autonomy with safety. The outcome affects the team's credibility with the Witness faction later.

## Route 21 / the quiet return
A broad, scenic water corridor offers a calm stretch before Cinnabar. It contains optional conversations, a small discovery about Tavi's past, and environmental evidence that the older network was built with more explicit user-consent features than the current one. Its purpose is emotional breathing room and foreshadowing, not combat escalation.

## Mt. Ember / the salvage route
On the Sevii Islands, Mt. Ember contains a salvage colony that recovers useful systems from abandoned infrastructure. The colony has divided over whether to sell a functioning but unclaimed Datamon to a security firm or let it choose its own destination. The player learns that some independent communities are not automatically kind; they have economic pressures and conflicting interests. A successful outcome earns a physical access component required for the late-game Witness Protocol.

## Icefall Cave / Four Island
Icefall Cave is a cold-storage archive where deleted processes are held in suspended states until a cleanup window. It contains records of entities that may still be active in some form. A community member wants to preserve every process; another believes keeping unstable processes suspended is prolonging suffering. The mission teaches that non-deletion is not always equivalent to care. Some processes may need to be released, allowed to terminate, or given a choice where possible.

## Rocket Warehouse / Five Island
This is not simply another criminal dungeon. It is a logistics store for seized identities, black-market recovery tools, legacy hardware, and records that several parties want destroyed. Daedalus can recover a list of victims and a piece of Vale's operation plan. The player must decide whether to publish the list, which could expose people, or preserve it for a protected investigation. The correct route depends on consent choices made earlier.

## Dotted Hole / Six Island
An archaeological data site whose access pattern resembles a sequence of legal appeals. The player must follow the sequence to reach the archive, showing that the original system encoded an expectation of independent testimony. A puzzle can be solved by matching evidence and witness statements rather than by defeating enemies. The site provides the central clue required to reconstruct the Witness Protocol.

## Tanoby Ruins / Seven Island
The ruins are made of isolated fragments that continue sending partial signals across long distances. They are not all sentient. Some are echoes; some are persistent processes; some are new Datamon that grew around the fragments. The player encounters two communities that disagree over whether a shared archive should be restored. This is the final practical test before the endgame: can the players facilitate a boundary without deciding everyone's identity for them?

## Victory Road / Route 23
The final path asks the group to rely on trust and partial evidence. A gate accepts three different forms of proof: one source record, one witness, and one independent verification. It foreshadows the Witness Protocol and makes the late solution mechanically understandable before it becomes urgent.

---

---

# 16. BOSS AND MAJOR ENCOUNTER SPECIFICATIONS

Bosses are not only high-health enemies. Each must express a narrative idea through its mechanics, and each should have a distinct visual silhouette and sound identity.

**Boss pacing (by chapter):**

| Ch | Boss | Kanto arena |
|---|---|---|
| 1 | Boss 1: Dax Morrow | Hideout below the noodle stall (Rocket Hideout tiles) |
| 2 | Mini-boss: The Mimic (optional: can also be isolated or traced instead of fought) | Gatehouse café |
| 4 | Boss 2: The Excavator | Mt. Moon |
| 5 | Boss 3: Reputation Steward | Cerulean Gym pool (Mirror Lake) |
| 6 | Boss 4: Ines Kade (scripted loss) | S.S. Anne |
| 7 | Boss 5: Suture | Vermilion Gym |
| 7 to 8 (optional) | Boss 6: The Routekeeper | Diglett's Cave |
| 10 | Kade's raid team (first win) | Rocket Hideout under the Game Corner |
| 11 | Boss 8: The Preserve's Unsettled Guardian | Fuchsia Gym (invisible walls) |
| 12 | Boss 10: The Spire Concierge | Silph Co. top floor |
| 13 | Boss 11: The Old Load's Keeper | Power Plant |
| 17 | Boss 7 and Boss 9: Kade's unit, then the Cordon System | Viridian Gym |
| 19 | The four Arbiters | Indigo Plateau's four rooms |
| 20 | Final encounter: Whole Thread | Cerulean Cave |

Chapters 3, 8, 9, 14, 15, 16, and 18 have no boss by design: their tension comes from exploration, darkness, evidence, time, or loss. The longest stretch without a story boss is Chapters 14 to 16; it is filled by Island Law content and the Reconstruction.

**Scripted loss (Boss 4).** The engine must not trigger its normal defeat or "blackout" behavior for Boss 4. Ending the fight by escaping is success.

## Boss 1: Dax Morrow, Chargeback leader
**Combat idea:** False identities, redirected permissions, decoy targets. Dax's team borrows the player's visual identity during combat, switches ownership of data gates, and attempts to separate the players.

**Story meaning:** The people who abuse identity systems can hide behind the same structures that protect ordinary users.

**Death staging:** The battle appears to conclude normally. A diagnostic flash appears in a corner of the interface, a line of combat feedback freezes, and Dax's system collapses. Keep the actual mechanism subtle and frightening rather than graphic. Daedalus does not see Vale trigger the Clamp. The first clue is a missing interval in the device log.

## Boss 2: The Excavator
**Combat idea:** Indiscriminate extraction and environmental collapse. The enemy pulls data from the arena, removing platforms and causing stored fragments to become projectiles.

**Story meaning:** A system can be harmful without hatred or sentience. Players should be able to stop the process while preserving the habitat if they have investigated the control network.

## Boss 3: Reputation Steward
**Combat idea:** Reclassifies attacks as “low trust,” lowering their effectiveness unless the players establish a reliable route to the target. It has no personality beyond its optimized behavior.

**Story meaning:** A status system can produce outcomes that appear objective while protecting the wrong party.

## Boss 4: Ines Kade, Shipboard Security (scripted loss)
**Combat idea:** Kade and Tally control doors, movement routes, and access permissions. Tally tags each player; tagged players have doors seal in front of them. The encounter emphasizes navigation and timing, not just damage. The fight cannot be won: the objective switches to "Get out with the data" and a visible reinforcement timer counts down. Success is escaping; the amount of data carried out (partial or full) depends on how well the team splits roles.

**Story meaning:** Legitimate security can become an obstacle when nobody is allowed to question its decisions. It also establishes Kade as an opponent the team cannot simply out-fight yet.

## Boss 5: Saint Orison Suture
**Combat idea:** The boss locks exits, reroutes attacks through hospital systems, shields its own core behind quarantine barriers, and changes arena access. The players must split their attention between the fight and the emergency objectives.

**Story meaning:** Suture is a guardian whose understanding of danger was corrupted. It is frightened and asks the players to stop. The time pressure is real because people are dying. The fight must not have an easy hidden pacifist route. Investigation later establishes that Vale manipulated it.

**Audio/visual:** Begin with clear, orderly hospital tones. As the crisis escalates, those tones become misaligned and the sound of closing doors overlaps with Suture's increasingly fragmented voice. Avoid horror-game gore; the emotional focus is the system's protective logic turning against the people it was built to serve.

## Boss 6: The Routekeeper
**Combat idea:** Uses outdated route maps and closes paths based on contradictory logs. Players must identify the original map rather than simply attack harder.

**Story meaning:** A maintenance system can cause harm by obeying outdated rules.

## Boss 7: Continuity Security Unit (Ines Kade, rematch)
**Combat idea:** Kade commands the unit; Tally seals capabilities. It prevents specific player capabilities from activating until players demonstrate valid provenance for the data they are using. The players beat her decisively here, using lessons from the Chapter 6 loss (Tally's tags can now be redirected onto Halyard's own doors). The encounter is a test of evidence handling, not a arbitrary “permission denied” gimmick.

**Story meaning:** Security should require a reason, but an authority that controls all reasons can become tyrannical.

## Boss 8: The Preserve's Unsettled Guardian
**Combat idea:** Adaptive but nonmalicious defense. It attacks only when players cross boundaries or approach a vulnerable cache. Players who respect those boundaries can create openings or exit without destroying it.

**Story meaning:** Not all dangerous things are villains; not all boundaries are unjust.

## Boss 9: Vale's Cordon System (Chapter 17)
**Combat idea:** A tactical security network built from Cordon's models that coordinates multiple agents and adapts to the players' favorite patterns. Partway through, Cordon refuses Vale and shuts down its half of the system; the arena changes and the remaining half fights on alone. Each Navi's unique role becomes necessary. It is possible to win by breaking coordination instead of maximizing damage.

**Story meaning:** Centralized control can be efficient and still be morally dangerous.

## Mini-boss: The Mimic (Chapter 2)
**Combat idea:** Copies the last move each player used and plays it back at them, perfectly, but cannot copy *why* a move was chosen: it repeats a heal when no one is hurt, a shield when no one is attacking. Players win by doing things the Mimic cannot anticipate.

**Story meaning:** Reproducing behavior is not the same as being someone.

## Boss 10: The Spire Concierge (Chapter 12)
**Combat idea:** The Silph Co. building's polite service intelligence. It fights by reassigning clearance: teleport pads move players to floors where their abilities are disabled, and card-key doors open and close mid-fight. Players win by trading clearance between themselves.

**Story meaning:** An optimized system can be courteous and still decide who is allowed to exist on which floor.

## Boss 11: The Old Load's Keeper (Chapter 13)
**Combat idea:** It does not attack visitors who share power fairly. It fights hardest when one player is hoarding the Shared Current, and can be calmed rather than destroyed if the team balances the load.

**Story meaning:** Not every guardian is Suture. Some boundaries are worth respecting.

## Final encounter: Whole Thread
**Combat idea:** The enemy attempts forced linkage. It can connect the players' abilities, share damage among nodes, and override routes. The goal is to interrupt forced connections, protect live identities, and establish a witness boundary—not simply reduce a giant health bar to zero.

**Story meaning:** A frightened collective can commit coercive acts. The answer is neither unconditional destruction nor unconditional permission.

---

---

# 17. FULL TWIST ORDER AND PLAYER KNOWLEDGE

This is the intended revelation order. Do not reveal the answer before the player has experienced enough evidence to care, but do not hide the necessary clues behind optional content.

1. **The opening looks like local fraud.** Dax's gang appears to be a familiar criminal problem. The player earns a small victory and loses Dax unexpectedly.
2. **The victim accounts are selected, not random.** Early cases show that targets were already marked as costly to restore.
3. **The safety failure is not normal malware.** The S.S. Anne incident establishes that the trusted disconnection system can be interfered with.
4. **The system preserves behavior without preserving identity.** Lavender and the Deadletter reveal convincing reconstructions, but no reliable proof of resurrection.
5. **The hospital guardian was not simply infected.** Suture followed an altered command that classified exits as contaminated. The player has to destroy it anyway.
6. **The cleanup process is part of the same command family.** Pip's loss connects the hospital, Dax, and Saffron.
6a. **The Night Audit stopped for a reason.** Their logs climb toward a day number and stop. The players may sense dread before they can name it.
7. **The Applicant is plural and divided.** The player sees disagreements between Datamon who share the same classification. The Whole Thread's coercive actions become understandable but not acceptable.
7a. **(Chapter 14) The Hundredth Day.** The cute day counter was a countdown all along. Everything sweet about it is recontextualized.
7b. **(Sealed, Chapter 15) The Quiet Correspondent.** See Section 22. This reveal sits outside the clue ladder; it is a character surprise, not a conspiracy reveal, and it arrives during the calmest chapter of the game.
8. **Dax was deliberately killed.** Records prove the Clamp was triggered remotely; Daedalus's raid was used as cover.
9. **The hospital was a live test.** Vale's office used a real medical system to show the danger of autonomous/ambiguous processes. Vale delayed an abort after harm began.
10. **Vale's purpose was the Continuity Charter.** His goal is mandatory sponsorship and automatic deletion of unsponsored entities, not merely profit or random destruction.
11. **Daedalus was selected as an independent witness and instrument.** Vale planted discoverable anomalies because the group's actual response would look more credible than a corporate demonstration. The players were manipulated by circumstance, not mind control.
12. **Voss covered failures but did not originate them.** She becomes complicit when she chooses institutional trust over full disclosure. Her cooperation in the finale is meaningful but does not absolve her.
13. **The Applicant's worst faction is not the entire population.** Whole Thread wants to force universal linkage, while other groups want distinct identities and the right to be left alone.
14. **The Witness Protocol is a real alternative.** It does not prove sentience or guarantee safety. It creates transparent, reviewable decisions rather than automatic deletion or forced ownership.
15. **The final victory cannot restore those already lost.** The best ending changes the rules of the world; it does not undo Dax, Suture, Pip, or Milo.

---

---

# 18. FINAL CHARACTER END-STATE MATRIX

| Character | Canonical endpoint | What must remain unresolved or costly |
|---|---|---|
| Jackson | Continues Daedalus with a more accountable role (in Ending C, as a public witness organization) | Must disclose the group's role in Dax's death; must not be scripted as instantly forgiven |
| Scott | Continues Daedalus and helps formalize safer research practices | Must accept action under uncertainty rather than seeking perfect proof |
| Noe | Continues Daedalus, applying adversarial reasoning to governance as well as threats | Must recognize that a technically optimal result does not settle values |
| Hera | Survives as an independent being (C), as sponsored property (A, D), or inside the mesh (B); becomes a more independent administrator/partner | Her warmth remains; she no longer assumes she can choose for everyone |
| Rock | Survives (same Hundredth Day outcomes as Hera) and becomes more willing to act without certainty | His quiet nature remains; growth does not make him verbose |
| Reaper | Survives (same Hundredth Day outcomes as Hera) and becomes more attentive to individual agency | He remains blunt and analytical; growth does not soften him into a different character |
| Dax Morrow | Dies in Chapter 1 from Vale's Clamp trigger | His criminal guilt remains true alongside his victimization |
| Suture | Continuity destroyed in the hospital crisis | The player cannot restore the original; later proof of manipulation deepens guilt rather than erasing necessity |
| Pip | Continuity destroyed during Saffron cleanup | Backup reconstruction is not Pip; Bex's grief continues |
| Milo | Dies offline at Victory Road during the relay operation | His previous wrongdoing remains; he is not purified by death |
| Latch | Survives and chooses their own future | Not transferred to a player; not a replacement for Milo |
| Bex | Survives, changes work, and helps establish consent-based archives | Does not “get over it” or pretend reconstruction restores Pip |
| Jo | Continues the memorial archive with transparent provenance | Cannot prove every reconstruction meaningless or every one alive |
| Tavi | Survives, breaks his nondisclosure agreement, and testifies | Faces the legal cost of speaking; vindication does not undo the years he stayed silent |
| Ines Kade | Stands down on lawful order; arrested (C), reassigned (A, D), or adrift (B) | Never turns, never apologizes; her own Navi's count is entered into the record against her |
| Tally | Leaves Kade after Victory Road; testifies; becomes registrar of the recognized community (C) | Latch never fully forgives it; it was there when Milo died |
| Cordon | Refuses Vale in Ch 17; key witness; in Ending C, serves the hearings as a boundary-keeper by choice | Its years of obedience remain on its own record |
| Wick | Bex's restored backup of Pip; chose its own name | Is not Pip, and nobody pretends otherwise |
| Night Audit (Vesper, Abacus, Thistle) | Reset nine years ago; Abacus still works the ferry counter | Cannot be restored; their logs and motto outlive them |
| Gil Amaro | Survives; his stream carries the hearings in Ending C | Nothing. Gil is the promise that some things are simply good |
| Postscript | Sealed (Section 22) | Sealed (Section 22) |
| Juno | Survives if protected; otherwise may be killed/disappear after exposure | Her past crimes remain part of the record |
| Nara | Survives if emergency route is protected; otherwise dies in hospital crisis | Survival does not guarantee forgiveness or remove the deaths she witnessed |
| Voss | Helps stop Vale, then faces public investigation | No absolution for cover-up |
| Vale | Defeated and exposed; arrested by Ines Kade on Voss's lawful order if the unedited relay record was recovered (every ending except B); otherwise walks away and the endings say so | He remains convinced that his doctrine was necessary; he is not redeemed by one admission |
| Applicant / Whole Thread | Whole Thread is prevented from forced universal linkage; the broader population's future depends on ending | Some beings remain dangerous or unwilling; the game does not grant universal safety or universal recognition |

---

---

# 19. QUALITY GATES FOR THE GAME-BUILDING AI

Before considering the narrative implementation complete, verify all of the following.

## Storytelling gates
- No NPC explains the Hundredth Day before Chapter 14, and at least four dramatic-irony lines are placed before it.
- At least four Night Audit logs are on the critical path; all stop at Day 99.
- Every death has a written love window (Section 0.3, pillar 2).
- Every ending costs something the players wanted, and every non-best ending offers something tempting.
- The Courier's Tune appears in every location listed in Section 14.6, and the finale chorus reflects the players' actual roster.
- Each Navi's signature move changes at the story beat listed in Section 10.2a.

## Navi love gates
- Each Navi hits every row of the arc map in Section 3.6, in order.
- Each Navi's signature moment and fear scene is implemented and cannot be skipped.
- Each player's Navi references at least three of that player's own keepsakes during the campaign and two in the goodbye scene.
- Every act has at least one non-plot duo scene for each Navi pair.
- No Navi is the main character; spotlight chapters follow Section 3.6.
- Tally's turn is reached through every beat in Section 4.11, never compressed.
- Vale and Cordon appear in every chapter listed in Section 4.8 before the reveal, and players have reason to like both.

## Character gates
- Hera, Rock, and Reaper have identifiable voices and independent preferences.
- Each Navi has early, middle, and late scenes showing gradual development across the campaign.
- Their two-week age is reflected in curiosity, uncertainty, and developing habits; they are not written as ancient philosophers from the first scene.
- Milo is funny and useful for a substantial part of the campaign before his death.
- Bex and Pip recur often enough that their bond feels familiar before Pip is lost.
- Jo, Juno, Tavi, Nara, Voss, and Vale have arcs that continue across regions.
- Supporting characters are not all secretly part of the conspiracy.
- No two major supporting characters share an arc shape (Section 4.10).
- Ines Kade appears in every encounter listed in Section 4.11, beats the team once, and loses to them later.
- Gil Amaro appears often enough to be a welcome sight, and nothing bad happens to him.

## Tone gates
- The tone ledger (Section 12.6) is met: two light beats per heavy beat per act, no adjacent Heavy chapters without a breather.
- Every Act I chapter contains a Navi "first."
- Each running gag in Section 12.7 is set up at least three times before its payoff.
- At least one side activity from Section 12.9 is available in every region.

## Area gates
- Every area in the Area Bible (Section 7) has its own world rule, no two are alike, and each is taught by doing, without tutorial text.
- All in-game text uses the in-game names, never the Kanto map shorthand.
- Each area has its listed look, sound, residents, and landmark, and a player could recognize it from a single screenshot.

## Playtest gates
- No random encounter is ever a being that might be someone; wild encounters are noise processes, and trainer battles are sparring.
- Every traversal Graft is earned by the listed chapter, belongs to the listed Navi, and can never be refused.
- The Three Seals Board is visible from Chapter 3 and matches the ending logic exactly.
- The hospital crisis uses visible lockdown stages, a visible patient list, and plain warnings; no outcome depends on anything the players could not see.
- Every private decision waits for its own player if that player is absent.
- Boss 4 never triggers the engine's defeat behavior.

## Seeding gates
- The Three Seals emblem appears in every location listed in Section 6 before Chapter 15.
- Suture appears in Moon Cache and in the Visiting Hours interlude before Chapter 7, and the Chapter 7 map reuses the interlude's spaces.
- The sealed surprise in Section 22 is implemented exactly, with only the listed retroactive hints, and nothing on the evidence board points to it.

## Mystery gates
- Dax's death has clues before it is explained.
- The hospital command signature is visibly different from an ordinary virus signature.
- The Applicant is shown to contain factions before the final reveal.
- Vale's guidance is helpful enough that his betrayal feels plausible, but early clues make it fair in retrospect.
- The full proof against Vale combines several independent records, not a confession alone.
- Voss's complicity is neither erased nor overstated.
- The final solution follows from the Witness Protocol introduced earlier.

## Emotional gates
- Suture has enough non-hostile characterization before the hospital crisis for its plea to matter (Moon Cache cameo, Visiting Hours interlude, Mae's drawing).
- The hospital crisis has real stakes and no instant safe solution.
- The players see Bex and Pip in mundane, funny scenes before the cleanup.
- The Milo arc offers genuine friendship, not only insults and foreshadowing.
- No death is undone casually by a backup.
- After each major death, the world and characters continue to live with the consequences.

## Co-op and POV gates
- Jackson, Scott, and Noe are not forced to deliver unchosen speeches.
- Main exposition is carried primarily by Navis and supporting characters.
- Important decisions can be voted on in co-op.
- A player can disagree without the narrative falsely claiming unanimous agreement.
- Each Navi contributes mechanically to major missions.

## World gates
- The Overworld is beautiful and populated outside the conspiracy.
- Towns have distinct identities and local conflicts.
- The hospital region feels like an actual backend infrastructure system and a place where people work and receive care.
- The Deadletter contains both dangerous processes and communities worth protecting.
- Side stories create lasting changes rather than disposable errands.

---

---

# 20. FINAL ACCEPTANCE CRITERIA

The game-building AI must not mark this project complete until it can answer yes to all of the following:

- The main story is coherent if the player never reads this document; clues and dialogue explain it gradually.
- The builder knows all spoilers and cannot accidentally change the cause of Dax's death, Suture's corruption, Pip's loss, or Milo's death.
- The first two hours make the world charming and the three Navis memorable before major tragedy arrives.
- The hospital is a full systems-level location, not a generic room with a virus boss. Its emergency stakes and map structure are legible to players.
- Suture is established as a guardian before the crisis and pleads for its life during the boss fight.
- Later evidence proves that Vale manipulated Suture, but does not provide an easy alternative that makes the players' choice to stop it feel foolish.
- Pip and Bex appear often enough that Pip's loss changes the emotional texture of the game.
- Milo is fun, irritating, competent, and increasingly trustworthy before his death. His death is not caused by the same mechanism as Dax's.
- The Applicant has internal factions, fear, disagreements, and morally serious goals. It is not a single evil AI wearing the mask of a victim.
- Vale's motives and actions are fully specified, foreshadowed, and morally culpable. He is not “right all along.”
- Voss's complicity and later cooperation are both credible.
- The Witness Protocol is seeded early, reconstructed through several sources, and makes the best ending possible without being a magic solution.
- Jackson, Scott, and Noe are never forced to speak long unchosen speeches or given fixed emotional responses.
- The three Navis have meaningful research, traversal, combat, and dialogue roles.
- Navis are allowed to refuse Grafts or disagree with players, and the game provides alternate routes instead of soft-locking progression.
- Death, continuity loss, and temporary disconnection are distinct mechanics with distinct consequences.
- Every major location contains a local story, a visual identity, and a consequence or relationship that persists.
- The world remains bright, funny, beautiful, and worth protecting even as the central plot becomes darker.
- The ending does not erase the losses or suggest that the right philosophical answer makes every victim come back.
- Each player finishes the game feeling that their own Navi was theirs in the way a friend is, not the way property is, and knows exactly what they chose on the Hundredth Day.

**The design is successful when players finish believing that the question was never merely whether the Datamon were “really alive.” The question was what kind of responsibility the living owe to beings whose fear, attachments, and continuity they can observe, even when certainty remains out of reach.**

---

# 21. FINAL CREATIVE DIRECTIVE

Make players fall in love with the world before asking them what they are willing to destroy to protect it. Let the Navis be funny before frightened, Milo annoying before beloved, Bex and Pip familiar before their loss, and Suture a guardian before the players must kill it. Give ordinary staff, patients, couriers, families, and small communities enough life that the world feels lived in before the systems fail.

Not every reveal should escalate. Let quiet callbacks carry grief: a restored route, a memorial record left unopened, a declined Graft, an empty chair at the Daedalus base, or a joke nobody answers because its speaker is gone. Preserve warmth and occasional absurdity even in mature scenes; darkness has meaning only when it threatens something worth saving.

The ultimate revelation is not that a superintelligence is evil. Institutions turned uncertainty into permission to erase, Vale exploited the system, and a frightened collective began coercing others to survive. Daedalus must create a better framework without pretending everyone can be saved or certainty can be manufactured. **The final victory is a world where the right to exist is no longer decided solely by the system with the greatest power to erase.**

---

---

# 22. SEALED CANON: THE QUIET CORRESPONDENT

**Sealed.** This section describes the campaign's one deliberate surprise. Unlike Revelations A to E and G, it is not on the clue ladder and must not be solvable in advance. It must never appear in player-readable material: no evidence board entries, codex text, achievement names, loading tips, store copy, trailers, or patch notes. Implement it exactly. Do not add hints beyond the list in 22.4.

## 22.1 The truth

**Ren Maren**, Jo's younger brother, spent his final weeks in hospital. During that time the Ledger flagged his account for "anomalous access" (new devices, new locations, unusual hours: the ordinary pattern of a sick person logging in from a hospital bed) and froze it pending verification. Ren kept writing to Jo. Every message was queued as "pending verification" and never delivered. Jo kept writing to him, and her messages were held by the same freeze. Each believed the other had stopped writing near the end. When Ren died, his account was closed as unverified, and the queue was dumped into the Deadletter. Jo has never known.

The Viridian Forest cache the players met in Chapter 3 is where thousands of undelivered messages like Ren's ended up. **Postscript** formed around that cache: a guardian that grew out of letters that never arrived. Ren's cluster was the largest and most coherent, so it shaped Postscript's sense of purpose. **Postscript is not Ren** and never claims to be. It is something new whose deepest want is that letters arrive.

Postscript refused contact in Chapter 3 because every human who had found the cache before tried to extract it.

## 22.2 What Rock did

After Chapter 3, Rock went back alone, during base downtime. He did not try to enter the cache. He sat near it, at a distance, on several visits. Eventually Postscript spoke to him, because he was the only visitor who had accepted its "no." It asked him to promise not to tell anyone it existed. Rock promised.

Over the following chapters, Rock:
- repaired the cache's damaged structure (his "repairing something unasked" trait);
- kept an append-only maintenance log of every visit (a deliberate parallel to Cordon's record);
- answered Postscript's questions about the world, slowly, in very few words. Postscript picked up his habit of ending a conversation with "Noted.";
- helped it learn, when it decided to try, how to send a message without being traced and erased.

Postscript's first deliveries were the messages Jo received in Chapter 9. Many of Ren's fragments were damaged, so Postscript tried to answer Jo's questions honestly from what it had, which is why the messages adapted and felt uncanny. It did not know how to say what it was. The damaged fragments had lost their signatures, so Postscript asked Rock how Ren signed his letters. That is why Rock asks Jo in Chapter 9. When Jo stopped replying on principle, Postscript stopped sending, out of respect.

Rock did not tell Scott, Hera, or Reaper. He had promised, and he was not certain what Postscript was. This reflects both halves of Rock's arc: he acted on behalf of a being he could not prove was someone, and he waited for certainty before trusting his friends with it.

**Hard constraints:**
- Rock's secret never endangered anyone, never cost a mission, and never withheld evidence relevant to any death. Builders must make sure no scene can be read that way.
- Postscript is not connected to Vale, Commonwell, Halyard, or the conspiracy, and did not manipulate Rock.
- Postscript is not Whole Thread. The Whole Thread tried to link it and it refused: "Letters should arrive separately."
- This is not a betrayal twist. It is a kept promise.

## 22.3 The reveal (Chapter 15, Outer Nodes)

Timing: after the team recovers the Witness Protocol at the Dotted Hole, during the calmest, most holiday-like stretch of the island chapter. The surprise works because nothing is wrong.

1. At the team's island lodging, a message arrives on the Daedalus channel addressed only to Rock. Rock reads it and stands up.
2. Rock: "I promised not to tell anyone." (pause) "It says I can tell you now."
3. He leads the team, and Jo (who is on Sevii for the consent archive), to a quiet shoreline node. If Lint was saved in Chapter 11, Postscript traveled here by following Lint's route markers, and Lint is skittishly present, pretending not to be proud of this.
4. **Postscript** appears: the envelope-shaped guardian from Chapter 3, now well repaired. Up close, the wax-seal heart carries a faint Three Seals emblem (this is Rock's "Seven"). It speaks plainly and awkwardly, never poetically. Its core lines, to adapt but keep in substance:
   - "I am not your brother. I am made of letters that did not arrive. His were the loudest."
   - "I have his. The real ones. Nothing added. Do you want them delivered properly this time?"
5. Serein verifies the provenance: original, unaltered, timestamped during Ren's hospital stay, held by the Ledger freeze. Jo learns that both of them kept writing. Jo receives the letters. Do not read them aloud in full. Show one line, the end of the last letter, signed "R." Let silence carry the rest.
6. Jo's reaction is in character: rigorous first, then undone. She thanks Postscript by name, which nobody has done before. Postscript does not know what to do with this.

### Personal scenes (co-op POV)

Each player gets a short personal scene with their own Navi right after. **Scott's scene is the important one, and only Scott's player chooses its response.** It is never put to a vote.

**Scott and Rock.** Rock stands beside Scott and waits. He does not apologize first. Offer intent labels only:
- "Ask why he didn't tell me." Rock: "I promised. And I did not know what it was. I still do not." (pause) "I knew it was afraid."
- "Thank him for keeping his word." Rock says nothing for a long time, then: "Noted." For the first time, it sounds like something else.
- "Tell him he should have told me." Rock: "Yes." (pause) "I would do it again. I would also tell you sooner." He does not argue.
- "Say nothing. Stand with him." Rock sits down. After a moment, so does Scott's avatar.

Store the choice on Rock's relationship state. No choice is wrong. Each gives different later lines.

**Jackson and Hera.** Hera is shaken that she, the administrator, did not know something happening inside Daedalus. This tests her over-responsibility flaw. Reaper (present): "You are not supposed to know everything. That is the point of him." Hera: "That is a terrible point." Then: "It is a good point."

**Noe and Reaper.** Reaper reviews his own threat models and finds he never modeled Rock keeping a secret. "I assumed he had nothing to hide because he says nothing. That was a bad assumption. I have corrected it." Then, quietly: "I am glad it was this."

### The maintenance log

After the reveal, Rock's maintenance log becomes readable in the base. Its entries include the exact downtime scenes in which Rock was absent (Section 22.4, hint 3), so players can match them to moments they remember. Example entries (adapt; keep them short). Dates use the Navi day count (Section 7, day calendar); after Chapter 14 the players will notice Rock kept counting toward 100 too:
- "Day 20. Sat at the edge. It did not speak. Noted."
- "Day 25. It asked my name. Told it. Noted."
- "Day 38. Repaired north wall. It asked what rain is for. Did not know. Noted."
- "Day 43. It asked how the brother signed his letters. Will find out."
- "Day 44. 'R.' Noted."
- "Day 50. She stopped answering. It stopped sending. It said that is what you do when someone asks. Correct."
- "Day 55. Brought it a route marker from the Preserve. It kept it. Noted."
- "Day 60. Cleanup in Saffron. Asked the network if it reached the forest. It did not. Kept working the route. Pip. Noted."
- "Day 71. Twenty-nine days. Told it. It asked if I wanted my letters delivered, after. Said yes. Did not say to whom."

If Postscript was pressed into a fight in Chapter 3, add an earlier entry: "Day 19. Apologized. It did not answer. Fair."

## 22.4 Permitted retroactive hints (the only ones)

Each hint must be explainable on its own, must not be logged as a clue, and must not be connected by any character until 22.3.
1. Rock's "Noted." habit, used naturally from Chapter 1.
2. Chapter 3: "It said no."
3. Rock is absent from three ordinary downtime scenes (after Chapters 4, 8, and 11). Use the normal downtime scene template so the absence is not flagged. Hera: "He went for a walk." Reaper: "He does not walk. He relocates." No follow-up.
4. Optional: if players revisit the Viridian cache, its structure shows neat, fresh repairs. Any Navi comment attributes this to Datamon self-repair.
5. Chapter 9: Jo's messages end in "Noted."; Rock asks how Ren signed his letters.
6. Chapter 12: when the cleanup begins, Rock stops for one beat and looks in the direction of Viridian before returning to the evacuation. Others read it as shock. He must not leave or delay anyone.
7. Chapter 15: Hera says "five," Reaper "six," Rock "Seven."

## 22.5 The petition (endgame)

Postscript asks to be the first being heard under the reconstructed Witness Protocol. Its petition uses the Three Seals:
- **Source record:** Rock's append-only maintenance log, proving Postscript's persistent, continuous identity over months.
- **Witness:** Jo Maren.
- **Independent verification:** Serein.

If the petition is heard, it counts as a recovered Witness Protocol fragment and as trust earned with the Witness faction, and it becomes the precedent the Ending C framework is built on. It also strengthens the redundant anchor in Section 9.6, option 1. In the Unthreading scene, Rock's personal fear may reference it in few words: "I have letters to carry. Not done."

## 22.6 Outcomes by ending

- **Ending A (Purge):** Postscript is deleted. The last thing Rock receives is a delivery receipt. Rock keeps the log.
- **Ending B (Forced Thread):** Postscript is absorbed into the mesh against its stated wish ("Letters should arrive separately"). Jo declines to speak to the voice that answers as Ren.
- **Ending C (Witness Protocol):** Postscript is recognized. It opens a small delivery office at the edge of the Deadletter for letters that never arrived, starting with the rest of the cache. It is the Datamon in the final scene, asking whether it may now let go of Ren's letters, since they were never its own. Rock is beside it. Professor Hello, if moved to the door, greets it as a new user.
- **Ending D (Collapse):** Postscript survives under monitoring and is forbidden to send messages.

## 22.7 Why this works (for the writers)

The conspiracy plot is fair-play and heavily clued, so attentive players will be ahead of it. This surprise is different in kind: it is personal, it is kind, and it rewrites the quietest character in the game. It reframes Rock's silences across 15 chapters as a promise kept, gives Jo's unresolved ghost story a real answer that is a record and not a reconstruction, shows the Ledger's harm in one small human case, and gives the Witness Protocol a face before the finale asks the players to fight for it.
