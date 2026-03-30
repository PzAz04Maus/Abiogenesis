# The Game
## Draft note

==This document is an attempt to weave multiple related, but discrete concepts into one common solution. It is therefore a work in progress.==
# Touchstones

==Add literary stuff here==
# The core system

Abiogenesis is a different breed of roleplaying experience from typical RPGs. Unlike the dungeoncrawls of D&D or the cinematic drama of pulp characters in World of Darkness, Abiogenesis has a more expeditionary, outdoors character, taking after its father STALKER: Shadow of Chernobyl. 

That's not to say that there is no place for a secret lair of enemies or suspense and intrigue, but Abiogenesis is most distinct when treated like a Neo-western. The players explore a vast, harsh frontier to support themselves or their country, using modern weapons to come home with the spoils of a cosmic disaster. Supporting this requires a different framework to what either GMs or players are used to.

for instance, Abiogenesis needs a different type of prep or improvisation than games are typically used to. Instead of starting from a predetermined map of a given location or frontloading all of our decisions, we instead treat our locations abstractly, and form the resulting scene from the ways that players discover and traverse them.

# The importance of Terrain - ==Thesis

> Terrain is not neutral—it either helps or hinders each of the opposed forces. 
> 	- U.S. ARMY FIELD MANUAL 700-5(1993)


# The problem of terrain - ==antithesis
### Location-oriented Design

In an **environment-oriented pattern**, the player enters a space specifically defined by the storyteller — a chamber, a dungeon, a battlefield, a palace, a ruin — and their decisions are reactions to the circumstances held inside. Place becomes the defining structure of the scene.

By default, this benefits the GM because keeping to a bounded space promotes control and the player's sense of perception. However, since the environment precedes the player, **strategic agency** is limited: player actions are only supported by the boundaries of what has already been built.

When players deviate from expectations, the GM must create more space, which can push the GM into a reactive stance. If this happens frequently, the GM is left chasing the players’ actions instead of guiding them.

**Advantages**
- Structure creates high environmental fidelity (maps, puzzles).
- most common pattern in roleplaying games
- best supports games set in small, pre-industrial, sedentary, parochial societies
- Strong sense of place and immersion.

**Challenges**
- Highly structured
- player agency is constrained by prep.
	- more strategic decisions = higher GM workload, prep
- poor at supporting mobile campaigns
- distances become exponentially expensive
	- very long distances are wasteful
- static scale of time/dimension

##### Popular examples
- Theatre and plays
- Dungeon Crawl
##### Important Location-centric terms

- scene
- location


# Our solution - ==synthesis==
## Game structure: path-oriented design

To understand path-oriented design, we start by defining its opposite. ==This section should be rewritten later==
### Path oriented Design

example: Dirty Harry
> it has quite a bit of path centric scenes in it for a movie of the time. Harry's always between places, in alleyways, on streets, on rooftops. oftentimes there's so much more backdrop than there are full locations

With a **path-oriented** grammar, The GM focuses not on designing an explicit location, but on an ambiguous environment with the available player opportunities, the consequences, and drama. Our scene becomes unfixed from the specifics of a single location and instead is a [[curation|curated]], emergent territory.

Because of this emergent behavior, GMs have more room to compress or adapt their notes, secrets are easier to hide, and players can gain strategic agency by filling in the map with the stuff they find important

However, this pattern comes with its own challenges. It is easy to disorient players in a unstable or discontinuous space. Playets additionally will expect a location-centric framework — fixed boundaries or concrete maps.

**Advantages**
- Best supports games set in modern or Itinerant cultures: driving games, nomads, travel
- High strategic agency: players choose their challenges.
- Lower GM prep load: responses can be systemic or narrative rather than pre-mapped.
- Naturally supports emergent storytelling
- better at covering large traversable areas

    
**Challenges**
- new pattern: no familiarity
- Lower environmental fidelity: locations are defined only as they become relevant.
- Requires robust, coherent world states to respond meaningfully to player behavior.
- Ambiguous; harder to maintain orientation or continuity when players unwittingly define their own trajectories.

##### Popular examples:
- Star Trek
- Traveller
- Pokemon

### Terms

It may be useful to describe path-oriented design with its own distinct language. For this I propose that the location-centric design takes from standard fiction, and then we devise terms for our path-centric design.

##### Path-oriented replacements
- scene -> situation
- location -> territory

## Semantic rules

Another difference in Abiogenesis is the explicit use of loose rules.

Earmarked by the ~ operator or `code bloc`, Semantic rules are a type of loose mechanic that have no formal definition to look up. Instead, they are meant to be interpreted by the GM each time.

For example, there is no explicit "cover" stat or mechanic in Tw13. Instead, "~+2 cover" would be a semantic modifier which is interpretable in a variety of ways, such as +2 Armor, -2 to getting spotted, 2 pieces of cover, or +2 to OODA.

The advantages of semantic modifiers come from its interpretive nature. It promotes flexibility, streamlined play, shorthand, abstraction, and most importantly, [avoids crunch](https://rpgalchemy.com/farewell-to-modifiers/). Most of all, semantic modifiers are optional - they cannot force anything.

### **What the GM Actually Does**

When you see **“~+2 cover”**, you must decide whether it applies to...

- attack rolls
- detection difficulty
- accuracy
- movement exposure
- line-of-sight

The rule expresses a condition (“cover reduces effectiveness”) but doesn’t specify an implementation because it's meant to be descriptive and improvised, not accurate.

The system doesn’t specify — **your judgment fills the gap.**

## The trailcrawl

What a path-centric decision looks like is one of three things

1. list
2. node map
3. freeform

### list

For a path list, the GM curates a list of critical paths, each one defined with qualities called keywords that specifiy the value of traversing that particular decision.

For instance, if players need to travel somewhere, the GM can suggest 4 types of paths:

- the standard path
- the risky path
- the safe path
- the secret path

If players wish for another path, then the GM may allow them to have it as long as the they can define the keyword and it fits the possibility space of the region. If successful, they unlock the new path.

The benefits are:
- the place space is not rigidly defined, allowing for ambiguous or hidden places
	- No map is necessary unless the players sit down and draw it.
- All that needs to be written down is the backdrop and the keywords
- keywords can be reused

### Nodemap

A nodemap is a more graphic form of the list method. There are a number of nodes linked by paths. Which each path may have qualitative behavior, one of the benefits of the nodemap is that it allows for an amount of loose quantitative or spatial behavior, such as the distance of another node, or whether one node has line of sight to another, but without the mess of needing to rigidly define everything.

### Freeform

The GM does not list any specific paths, but improvises keywords through play.



# Feedstock

# Keyword Palette

Use a 2D array of keywords with light details as a selection board for
## Trailcrawl (old)
 trailcrawl. A waypoint system with connecting links.

- players can sometimes add, modify, append, or edit nodes
- GM picks states from a keyword palette related to a given regional template
	- a palette is a stack of cards with main attributes
		- this palette then can be copied into modified variations that populate the palette for ease of access
- gms can add, modify, or elaborate on current terrain

-  depends on quantizing branches with the most significant impact on the gameplay
	-  because weak differences between paths is an inefficient use of resources.
	- branch variants
		- major - GM defined
		- modified: players can discover new attributes to current branches 
		- entirely player defined

```yaml
Node:
  Type: Forest Path
  Category: Natural / Woodland / Travel
  Features: width=medium, canopy=light, hazard=low
  Base Tags: travel-route, forest, outdoors
  Links: [North Ridge, Riverbank Bend]
```

```yaml
Behavior Overlay:
  Name: Dense Underbrush
  Keywords: stealth-friendly, slow-movement, concealment
  Effects:
    MovementCost: +1
    StealthBonus: +2
    DetectionDifficulty: +1
    CoverValue: +1
  Visual Cue: tangled brush, narrow trail
```

```yaml
Local Modifier:
  Name: Recent Rain
  Keywords: mud, tracks-visible, difficult-footing
  Effects:
    MovementCost: +1
    TrackingBonus: +2
    NoiseOnMovement: +1
```
## Procedure

```
- GMs tag each node with a small set of primary keywords, then add complementary secondary keywords by by matching or complementing those tags.
- Players discover new paths or slight variants by discovering **new combinations of keywords** applied on-the-fly.
```

1. Players choose a primary branch (quantized node).
    
2. GM picks or rolls a _tagged variation_ from the palette.
    
3. GM optionally adds one or two _local modifiers_ representing weather, recent traffic, patrol presence.

```
Base Node: Highway Onramp (Category: Urban/Transit)
Overlays:
  - Overgrown Verge (stealth-friendly)
  - Abandoned Construction Access (cover-rich, confusing)
  - Patrol Drone Route (detection↑)
Local Modifier:
  - Recent Accident (hazard↑, opportunities↑)
  - Heavy Fog (vision↓, stealth↑)
```


```yaml
topography:
  terrain_shape:
    - name: flat
      difficulty: low
      visibility: high
      weight: 1.0
    - name: rolling
      difficulty: low
      visibility: medium
      weight: 1.0
    - name: hilly
      difficulty: medium
      visibility: variable
      weight: 0.9
    - name: mountainous
      difficulty: high
      visibility: variable
      weight: 0.7
    - name: ridge
      tactical_value: high
      weight: 1.2
    - name: plateau
      tactical_value: medium
      weight: 1.1
    - name: gully
      concealment: high
      weight: 1.3
    - name: ravine
      concealment: very_high
      speed_penalty: high
      weight: 1.1
    - name: canyon
      movement_penalty: high
      exposure: medium
      weight: 0.8
    - name: escarpment
      traversal_difficulty: extreme
      weight: 0.5
    - name: bluff
      exposure: high
      weight: 0.7
    - name: mesa
      elevation: high
      tactical_value: high
      weight: 1.0
    - name: sinkhole
      hazard: collapse
      weight: 0.4
    - name: depression
      visibility: reduced
      weight: 1.0
```

---

```
# Node Title
Type: (forest path / ridge / highway onramp / river bend)
Category: (biome or structural category)
Base Description: 
  A concise description of the stable, quantized node.

Base Keywords:
  - (3–6 tags)

Links: 
  - Node A (difficulty/modifiers)
  - Node B (distance/time)

## Overlays (choose 1–3)
- Name:
- Keywords:
- Effects:
- Visuals:

## Local Modifiers (0–3)
- Name:
- Keywords:
- Effects:

## Possible Discoveries
- Shortcut?
- Variant path?
- Clue or sign?
- Environmental resource?
```

```yaml
# Highway Onramp (Primary Node)
Category: Urban Transit
Base Keywords:
  - exposed
  - concrete
  - multi-level
  - bottleneck

Overlays:
  - Service Access Road (cover-rich, stealth-friendly)
  - Construction Debris (hazardous, cover, slow-movement)
  - Emergency Turnout (fast-movement, visibility↑)
  - Sound Tunnel (echoing, detection-range↑)
  - Surveillance Camera Grid (detection↑↑)

Local Modifiers:
  - Traffic Jam Remnant (obstacles, hideouts)
  - Rain-Slick Surface (jukes↑, braking↓)
  - Flash Flood Drainage (surprise hazards)
```

## Terrain on location
GMs need to be able to convert between location-oriented and path-oriented obstacles. For example, microterrain - the tiny undulations or debris that provide cover in a modern gunfight.

To do this, we have to convert potential terrain into actual terrain.

### Potential and actual Terrain 
### Actual terrain
- **Confirmed** to exist
- Visible or perceptible on the map
- **Stable** and does not change unless explicitly altered
### Potential Terrain
Terrain that:

- **plausibly exists** given the environment, but not guaranteed
- Only appears if a character **searches**, **scouts**, **advances**, or **spends a resource**
- Represents **grain-level** detail below the resolution of the abstract map
- Become **actualized** only when mechanically invoked (rolls, spendable points, skill checks, OODA margin, etc.)

### 1. Discovering terrain
Tactics or scouting check

These take time to do.

Time spent pushes the clock forward to another encounter or complication.

May be awarded with terrain points

#candidate 1
 “Potential → Discovery Roll”

A single roll determines whether the player can convert a piece of potential microterrain into actual microterrain

1. Each region/cell gets a **Microterrain Difficulty** (0..+5):
	- **-3 Minimal** — Flat open field, asphalt, rooftops
	- **+1 Light** — Sparse brush, patchy slopes
	- **+3 Moderate** — Forest edge, broken ground, natural clutter
	- **+5 Heavy** — Dense forest, rubble field, complex hillside
2.  The Player Makes a “Discovery Action”
	- Scouting
	- Move & Find action (higher tick cost)
	- Spending OODA margin(?)
	- Spending “awareness points” if you’re using those
3. The player rolls for discovery for a particular microterrain tag ==what skill?==. The tag's difficulty modifier is added to the test
4. Outcome
	- On success
		- Player selects 1 available microterrain of the chosen tag to reveal as a piece of actual terrain.
		- Player places it on the map within ==what distance?==
		- ==can Players hold onto microterrain?==
	- Exceptional Success (MOS >=5
		- player discovers 2 microterrain features, or can upgrade a feature
	- Failure
		- No microterrain revealed, but no penalty.
	- Critical Failure
		- layer exposes themselves (negating cover/disadvantage)
		- Enemy discovers a piece of microterrain instead
    
### 2. Discovery points
1. Players get **X Discovery Points** per scene (usually 1–3).
2. Spend 1 point → reveal 1 microterrain if it is environmentally plausible.

Best for:
- Narrative-heavy games
- Speed
- High-player-agency systems
    
### 3. Microterrain Clock (PbtA/Blades influence)
1. Every attempt fills a “microterrain discovery clock.”
	- difficulty 0 → 2-segment clock
	- difficulty 1 → 3-segment
	- difficulty 2 → 4-segment
	- difficulty 3 → 6-segment
2. Each scan/check fills 1–2 segments.  
3. When the clock completes, microterrain is discovered

### 4. Opposed Scan (Wargame sim)
1. Player and Enemy roll OODA
2. If player wins → discover 1 microterrain, or more per MOS
3. If enemy wins → they discover 1 microterrain, or more per MOS.
4. On a successful OODA roll, characters may spend initiative to discover more microterrain

Extra ideas:
	- **MoS 1–2** → discover 1 feature
	- **MoS 3–4** → discover a strong feature
	- **MoS 5+** → discover microterrain _and_ gain positional advantage   

This directly connects discovery to small-unit tempo.

microterrain allows players to create opportunities

### 5 Environment-Driven Tables (wargame flavor 2)
1. When the player takes a Discovery test
2. Roll d10 on a terrain table tied to the region keyword.
3. Forest table → 20% micro-cover, 20% concealment patch, 10% dead ground, 10% micro-height, 40% no find.

### Microterrain Value

==Should these consist of semantic values with a magnitude (+5 cover, -3 concealment), or should I lay out mechanical rules for what a magnitude represents?==

# story beats: Chronos and Kairos
==chronos and kairos is not a required basic concept. I recommend this for a designers briefing unless kairos becomes important later==

Another problem with large spaces or long distances is that often there are spaces of extensive time where nothing is happening, or something is happening slowly as to be imperceptible until the great change occurs. To handle these well, it's important to understand different ways to reckon with time.

With typical stories, GMs have free license to gloss over the specifics of time, but in a patrol simulator, they need to be more careful.

## story beats

For abiogenesis in particular, chronological timekeeping is often not the right choice. 

## logistics beats

This applies doubly so to logistics, since the historical wargaming solution is that most of chronological systems, the beancounting.

For the purposes of the game, a progress clock representing the slings and arrows of the supply situation is used. When the timer hits 0, a random event will occur, usually some form of supply attrition.

==blocking draft==

If the supply hits 0, then the team starts accruing penalties.

# resource management: bulk

Ab13 runs on a bulk system where volume and weight are factors with the larger of the two defining it. 

1 kg is 1 bulk, 3.5 L is 1 bulk

Volume equation

Volume is done in 1000 cm^3 = 1 liter

Liters/3.5

14 L/f = 4
F = 3.5

Bounding box of l w h / f





## Progress clocks

```
A progress clock is a circle divided into segments (see examples at right). Draw a progress clock when you need to track ongoing effort against an obstacle or the approach of impending trouble

When you create a clock, make it about the obstacle, not the method. The clocks for an infiltration should be “Interior Patrols” and “The Tower,” not “Sneak Past the Guards” or “Climb the Tower.” The patrols and the tower are the obstacles— the PCs can attempt to overcome them in a variety of ways.

Long term clocks

Each faction has a long-term goal (see the faction write-ups, starting on page 283). When the PCs have downtime (page 145), the GM ticks forward the faction clocks that they’re interested in. In this way, the world around the PCs is dynamic and things happen that they’re not directly connected to, changing the overall situation in the city and creating new opportunities and challenges

- Blades in the Dark
```


See [[Tools for Location centrism]]

See [[Chronos and Kairos]]
## Wear, supply and fatigue

A crucial component for stories in the frontier is the threat of Supply. But approaching supply in a chronological manner is rarely fun - just ask anybody who uses the phrase 'beancounting' disparagingly. To alleviate this, we introduce our own system...

==to be continued==
# Path centrism and strategy

==this is not a required basic concept. I recommend this for a designers briefing unless strategy becomes important later==

Another inspiration for Abiogenesis is the concept of the Patrol simulator, where the way people approach a ==locale== is highly important to the 

See [[Strategic encounters]], strategic story?

