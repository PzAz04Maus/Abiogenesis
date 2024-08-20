# Design

While all rpgs can reasonably handle the gunfight, the room crawl and the dungeon brawl, most do not handle scales of 100 meters or more between combatants very well.

To handle these infantry battles in an efficient and fun manner, Ab13 needs to create a new structure for the longer infantry battle.

```
A **map** is a [symbolic](https://en.wikipedia.org/wiki/Symbol "Symbol") depiction emphasizing relationships between elements of some space, such as [objects](https://en.wikipedia.org/wiki/Physical_body "Physical body"), [regions](https://en.wikipedia.org/wiki/Region "Region"), or themes.
```
# Operational Combat

An **operational scene** is the collection of all exchanges of fire, pauses, operational actions, or operational movements. These are referred to as **operational decisions**. Operational scenes begin upon approach of the enemy.

Unlike tactical exchanges, operational scenes do not have initiative rolls. Each group makes an operational decision, then each turn is resolved simultaneously. Any group member interrupted by an exchange of fire during a non-combat operational action must give up their initiative check, even if they don't continue their operational action. This does not apply to movement.

To simplify matters, a group should sequence multiple operational decisions together and wait for 

Operational decisions last about 1 minute long in length, but can vary in time from 20 seconds to 80. With an **operational move** action, a group may move up to 10 times their best possible tactical speed. This move speed may be increased with an athletics or drive check as applicable.

Attacking doesn't occur on the operational scale. All small arms fire must be made during a tactical exchange of fire.

Information about the enemy group is limited during the operational scene; characters only know where the enemy's center is, and are to be given no instructions on enemy intentions other than what they can intuit themselves, unless they make a reconnaissance  check (previously known as the keep watch check). 

The Withdraw operational action is reclassified as a Stage I Rule. For Stage II rules, a group that wishes to disengage has to lose the opponent with obstructions or intervisible concealment.

## Stage III: Actions higher than operational

If Operational scenes aren't fast enough (A feat at this current stage), the GM can opt for a **strategic scene** instead.

Strategic scenes are simply operational scenes scaled up by a multiplier of 100, 300, 600, or 2400, which represent about 10 minutes, 30 minutes, 60 minutes, or 4 hour increments. At this timescale, the main things to be concerned about are movement and information.

# The approach
The first question is when do two forces meet? This is defined by the range which at least one force directly views another.
Stock Tactical engagement distance
---

- roll the engagement contest in advance, keep written on the scratchpad. Positive is in the party's favor, negative in the OPFOR's favor
- When the bang is about to happen, modify the contest result

problems with the engagement contest:
- it has 2 characteristics: when and how far the two forces are detected
	- but that is already the case because distance represents time...
- for instance 

- Far end of the grid

- XMS - as sux
- sux: exponential scale, +25% 
- 0 - as stock
- fail: linear scale, -25%
- XMF - Completely unaware

Looking into another grid has additional penalties

## Candidate 2 (winner): 
Range ranking system. tactical map only

All forces roll their stealth/observation checks and are then listed on a ranking system against each other.

Those with a +4 in the stealth game will see weaker opponents first at up to 200 meters

Those with +9 will see opponents first at up to 400 meters

those with +1 will only see opponents first at 25 meters.

Those who fail are considered last and will only see other opponents first at 25 meters

all tells increase other forces effective rating against that group

\+ simplifies multilateral force problems
\- all bilateral node relations are poorly modelled, such as distance between nodes (Only the players relation to all elements should be modeled tbh)
\- no mixed behavior for stealth/observation (probably too complicated to make a good model for)

# Operational terrain

The infantry battle has a major problem where relevant-critical details can exist on layer 0 or layer -1, but we can't draw both fully and efficiently - we must constantly simplify out things such as microterrain or dead space, while taking them into account.

Playing at the operational level requires terrain to be simplified with abstractions, called the level of detail.

Infantry battle maps have 3 layers. Each successive layer receives more player input

The most important level of detail is the base layer (0), followed by the landscape layer. Layer 0 handles most microfeatures as undepicted abstractions, unless necessary to a character.

**layer 1**: the landscape where the fight is located. The choice of layer 1 determines what layer 0 features can be picked and what mapwide behaviors exist in the map. layer 1 is always decided by the story. 

**layer 0**: the immediate features of the environment, the positive or negative space available that define the boundaries or spaces on the map. 

Layer zero starts with an initial subregion of (combat length) in distance with zero or more subregions attached to it. The combat value of a subregion depends on either random chance or the ability of a leader to locate good terrain.

Leaders can move across these different subregions, or find access to new subregions to move to work a tactics check, though at some point they will run out of options. Once a subregion is established it cannot be changed.

**layer -1**: the microfeatures that the players immediately use but are seldom drawn.

Characters may identify microfeatures to support their actions with a tactics check while supplies last and the enemy permits (ie: as they get progressively more pinned).

# Placing terrain

# Running operational maps

# Gameplay loop

1. Initial situation
	a. enemy is known
	b. enemy unknown
	c. mobile
	d. stationary
## [scaling](https://en.wikipedia.org/wiki/Level_of_measurement)
Is entirely determined by the gm, but by default consists of regions with a maximum length of 100 meters

Regions consist of either positive, negative, or some fraction of the two spaces

Regions can be any kind of polygon.
## Initial phase, GM 

1. GM determines the Level one region
2. Gm determines scale of a terrain piece

All terrain pieces must be touching at least at 1 point? Any gaps are to be determined as positive or negative space based on the GM's ruling until a group decides to uncover another terrain piece.

## Initial player phase, shaping field
This is known as the shaping phase because if the teams intend to fight, they will attempt to shape the battlefield to suit them, such as through an ambush or by acquiring higher ground prior to the opponent.

1. Groups determine their objective
2. both groups nominate a commander to make a competing tactics roll
- [ ] this could be called the reconnaissance check
3. on success, the commander nominates placement of 1 level zero piece of terrain and the initial spawn.
	2. The margin determines the quality of the terrain (is this based on GM's judgement or with soft rulings?) in regards to how well it supports their objective
	- [ ] what if the margin also determined the number of terrain pieces a side puts down?
	- [ ] what if the number of group elements determined the number of terrain pieces a side puts down
	1. the margin should be lose with normal successes or failures containing 'yes, but' results. Only exceptional margins should provide definitive results
	2. after consulting with the GM, the group arranges the piece of terrain according to their understanding of the situation.
4. on failure, who decides to put the terrain down? The commander choses the initial spawn

### Questions
- [x] What about minimum initial range or getting initial shots on? 
- [ ] What about holding terrain the enemy can't take
- [x] What is the size of a terrain piece
- [x] How does one handle split forces
- [x] How do we determine the shape of a terrain space
- [x] How does an actor move through a terrain space
- [ ] how are multiple pieces of terrain laid down?
- [ ] Can a recon roll be split so heterogenous terrain can be laid? (Ie barn house and field)

## Initial phase, no player shaping
If the two groups do not shape the battle prior to engaging (aka: complete surprise), the GM rolls for luck for each side (2d20L!6), then generates the terrain and  based on the fortune of each group. The groups have no decision in how this terrain nor their assembly is set up beyond what they were immediately doing prior to the interruption.
## Subsequent phases

1. GM determines whether players may add to the map depending on the local Level one terrain surrounding the immediate area in a particular direction
2. The group then rolls a terrain check with a modifier based on the local region the terrain is a part of in one cardinal direction.
	1. on success, the group adds a level zero terrain piece onto the map in an arrangement of their choosing in consultation with the GM. The margin of success determines how well the arrangement should suit them.
	2. On failure, the group adds a level zero piece of terrain onto the map, but the GM determines how the arrangement disadvantages them.

questions:
- [ ] What is the size (scale?) of this region?

## terms
- Negative space
- Positive space


# microterrain
## cover
A character who decides that they will look for dead space cover rolls a tactics check. 

On success, they may place one piece of terrain with a combat value equal to their margin of success adjacent to where they started or ended within reason.

This piece of cover stays for the duration of the fight

## paths

## level 1 features - broad landscape

Set n polygons on the board with m corners. Different polygons can lay on top of each other, but cannot intersect themselves

Is it a forest, town, plain

Is the predominant feature negative or positive space

Is the outlie/frontier positive or negative space.

Improvise these decisions


Typically n is set to 1, maybe 2

M is dependent on broad features.

Gms are encouraged to interpret, embellish and improvise these features according 

Level 1 polygons are the shape of the lands area

### using Simple polygons to shape level 1 map designs
https://en.m.wikipedia.org/wiki/Simple_polygon
a polygon that does not intersect itself and has no holes

https://en.m.wikipedia.org/w/index.php?title=Internal_and_external_angles&diffonly=true

https://stackoverflow.com/questions/8997099/algorithm-to-generate-random-2d-polygon

Drop a number of dice on the table and use each point as a polygon


A walk...
Take a line, then roll 1d36/2 = evens positive,  odds negative. This is how much of a turn is made in 10 degree increments.

We do this for n nodes, then connect the first and last node to finish a po
## level 0 polygons - features

Level 0 polygons are the shape of the features of the land. Players add


--- 

## Layer 0 placement.

A layer 0 test determines who places the terrain, what its general shape looks like and where that terrain goes. 

Successful tests favor the roller, unsuccessful tests favor the opponent


# Sources
https://en.wikipedia.org/wiki/Spatial_scale
https://en.wikipedia.org/wiki/Scale_(map)
https://en.wikipedia.org/wiki/Level_of_measurement

Level of detail

[Symbols](https://en.wikipedia.org/wiki/Map_symbol) versus scale


## gameplay value of long range combat
You get to play a sniper type

You can play characters who have long distance speed

You can play with wider pieces of terrain to support your movements

Flanking is more valuable

Tactical depth

Movement is more deliberate because range outpaces movement

Assault phase

# Running layer 0

Layer zero is decided by who can exploit their tactical initiative. If neither have tactical initiative then the roll is random. If a group has tactical initiative but fails the tactics roll they cannot exploit it well or at all, and if they succeed they get to roughly shape the layer 0 region.

Layer 0 elements
- Spawns
- Regions structure on board
- Number of initial regions
- Number of additional regions?


# Layer -1

Tactics check with a tn based on layer 0.
# Sources

https://www.reddit.com/r/40krpg/comments/vdx00o/space_hulk_map_generator_for_wrath_glory/
# old



---

using gravitational attraction to model chasedowns?

**Gravitational Force = (Gravitational Constant × Mass of first object × Mass of the second object) / (Distance between the centre of two bodies)2**.

Actor_observe \* target_stealth / distance (in 100 meters)

+2 \* -4 / 4

-8/4 = -2

+2 \* +2 / 2

4/2 = +2

Stealth - observe / distance

positive = stealth wins
negative = observe wins

-4 - -4 = 0

4\*2= 8
4\*1 = 4

4/1 = 4
4/2 = 2
4/3 = 1.33
4/4 = 1
4/5 = .8

---


# Of story beats and geographic kusoks

```
Kusok - bits or units of action, defined by a specific period of thought and action, an event and dynamic taking place between characters. These bits may be small, scene-length, or larger episodes.
```

We can divide Geography into blocks like story can be divided into beats. These bits are defined by distance as action is by time, while populated with dynamics such as elevation or terrain.

From these geographic blocks we can convert from distance to action by dividing the distance by the move speed and multiplying that by the number of ticks it takes to act.

The one exception is that most weapons are unaffected by range. any weapons that take multiple seconds to hit their target do not count.

# questions
Are regions always contiguous with each other or are they nodal in design?
# Geography blocks
## stage 1 tools
dimensionless distance - a geographic region can consist of a single median distance of all possible ways a character could cross from border to border. This number is then referenced whenever a Character attempts to cross or leave. Use rulings as to taste.

This simplification saves us from needing to accurately measure and scale each block of geography. Measuring from one block to another becomes a matter of adding the blocks between. 

## stage 2




---

Encounter methods

Timing
Spawn and behave
Track down

Maybe there's no way to realize observation as anything more than abstract numbers. Real detail may be too complicated to make

Explains why a lot of systems do empirical or probablistic models 

https://news.ucmerced.edu/news/2024/researchers-accurately-model-animals%E2%80%99-hunting-scavenging-behavior

---



Tactics roll as a detection footprint?
---

y=-2^(x-1)


## candidate 3:
Ranking system, distances by story. 

uses theatre of the mind

## candidate 4: max detection range, pattern recognition vs stealth only

nodes have a max detection field of view and notice everything in them, but roll for pattern recognition. poor competitive rolls reduce the range which actual detection is made at by a factor of 5% per point lost.


## candidate 5: time to detection

while in visual range, the comparison of 2 numbers determines how many turns it will take before the target unit is detected, such as detection vs camouflage. A fail is instant detection.


old
---
---

candidate formula 1: imagine a node with a detection radius around it: all nodes inside that detection radius automatically become aware of the node's existence.

\+ Simplified system
\+economical on resolving rolls
\-

according to the range band card, an MOS of zero would be a detection footprint of 7 meters.

All failures would exponentially rise in terms of the visual range penalty - aka: a fail of 1 is getting detected at 25 meters, a fail of 2 is 100 meters, a fail of 4 is 200 meters and 8 400 meters.

this wouldn't be very interesting for individuals. Many would be able to squeeze through enemy lines fairly quickly by default rules, unless a terrain range modifier for range bands was made for open fields.

this is probably because the visual penalty model in tw13 simplifies all factors of observation to 1 penalty, when reality has a poorly understood difference between noticing and identifying something.

Perhaps this could be remedied by having the notice range band be 1 range band further

alternatively, this could be in competition with the opponents' detection roll, but that breaks the candidate formula 1. Resolving rolls would be slower since it's a bilateral relationship between each.

---

rng system



Scaling time periods for range bands?

1 - 1x
7 - 1x
25 - 1x. 7/13
100 - 4x 28/52m
200 - 8x 104m
400 - 16x 208m
800 - 32x 416m
1600 - 64x 832m

100 - 1x - 13m tick 1.5 sec
200 - 2x - 26m tick 3 sec
400 - 4x - 52m tick 6 sec
800 - 8x - 104m tick 12 sec
1600 - 16x - 208m tick 24 sec

EFFECT STENO

https://en.wikipedia.org/wiki/Palimpsest

---
