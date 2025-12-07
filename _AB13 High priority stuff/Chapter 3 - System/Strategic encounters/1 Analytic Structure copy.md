> [!NOTES]
> 
For those in the know on military affairs, the operational and strategic scales are not directly mentioned because those lie on a frequency so low that they are covered by the rest of the rules.
>
>Secondly, Deep encounters have the unfortunate problem of using real life terms at a scale it was not originally meant to be used for. In my defense, I'm a gigantic nerd about military jargon, and I felt that the macroscale utility of the terms was effective enough to apply to the microscale of a party of murder hobos. A sort of "As above, so below" situation.

Similar to the traditions of books, stage, or cinema, the  roleplaying game presents the dramatic beat of scenes and sequels as an encounter. The encounter typically consists of a single, contiguous point in time, such as a conversation, an affair, or a battle of sword and muscle.

For fantasy, this understanding is enough because any counterexamples are treated as deviations from the norm. But the modern story spans nonlinearly across vast regions of time and space. In fiction, examples include car chases, travelling, battles, being hunted down, a heist, or contact.

In real life, an example would be the Vietnamese People's Army (PAVN) doctrine of "one slow, four quick:" Slow plan, quick advance, quick attack, quick clearance and quick withdrawal. In this case the planning phase is the slowest, the attack is the quickest, and the advance and withdrawal phases are in-between.

[4 slow, 1 fast](https://en.wikipedia.org/wiki/NLF_and_PAVN_battle_tactics#Attack_doctrine:_%22one_slow,_four_quick%22)

examples
- https://youtu.be/qfzW3EUeuQk?si=zw95u18cJ2vqOE_8
- https://youtu.be/kaWah6FSLZI?si=DDz2TFLYdZ6OO7_Q

- [ ] #TODO revise for discontinuity

In these examples, the 

# mismatches in Distance and time

Lets make some basic observations. The definition of speed is distance over time. This anodyne observation has major ramifications for drama, since the speed of a game has an impact on the story and the players. For story, speed determines how hard the crash of drama will be, and for the players, the number of time increments has an impact on player engagement.

But we just can't make the distance units as big as possible and the time increments as small as possible. Game Settings exist in a context, and players have can make only so many decisions before the game exhausts them. Worse, static time increments aren't universally appropriate - a 400 mile road trip doesn't need 6 second turns, but a barfight might. These mismatches have a cost to the value of the game.

For dungeons and dragons, this issue of opposing increments isn't as bad because the probability of a mismatch between the players and the environment is low; even dragons are a low probability event, while typical deviations exist in the form of mounts, sailing ships, and magic. So mismatches were rare, and when they did occur they usually weren't a big problem that needed intervention.

This is not so in a setting with the car, gun and radio. In modern-esque settings, these mismatches are incredibly varied and numerous: it's rare to be attacked by a dragon, but it's a statistic to be hit by a car.

In most modern games, the solution has been to kludge a solution out of the design language of fantasy games or raw storytelling. This solution is probably also why Hollywood movies are known as a trope for their poor imitation of firearms. 

While this has the great advantage of keeping games brisk and interesting,  the flaw is that it leaves out the ability to explore the interactions in and between these different scales. Dnd cannot run a car chase very well out of the box.

# Methods

So, To handle this underserved area, we need better methods. 

We can find this through developing the design language and with new tools. Here's what I've come up with so far

# scaling

Since a landmass has features at all scales (fractal behavior) , from hundreds of kilometers in size to tiny fractions of a millimeter and below, there is no obvious size of the smallest feature that should be taken into consideration when measuring ... .

We must then make assumptions about the minimum feature size and when they are relevant.

The issue at heart for modern mapa is the need to change our assumptions when we derive a map from another of different scale. 

- scale
- spatial bit - the basic unit of distance in a map. Usually based in the system of measurement or a scalar of it
    -  One challenge with the information theory approach to generalization is its basis on measuring the amount of information on the map, before and after generalization procedures.[[9]](https://en.m.wikipedia.org/wiki/Cartographic_generalization#cite_note-Styk2011-9) One could conceive of a map being quantified by its _map information density_, the average number of "bits" of information per unit area on the map (or its corollary, _information resolution_, the average distance between bits), and by its _ground information density_ or _resolution_, the same measures per unit area on the Earth. Scale would thus be proportional to the ratio between them, and a change in scale would require the adjustment of one or both of them by means of generalization
- syllable (byte) - https://en.m.wikipedia.org/wiki/Coastline_paradox - the five foot square is a syllable in core dnd
- word (or byte) size - a word is any processor design's customary unit of data.
- scene
- sequence
- Chronos
- Kairos
- dramatic beat
- exchange
- adventure
- https://en.m.wikipedia.org/wiki/Fractal_dimension
- A fractal dimension is an index for characterizing fractal patterns or sets by quantifying their complexity as a ratio of the change in detail to the change in scale.[5]: 1  Several types of fractal dimension can be measured theoretically and empirically (see Fig. 2).[3][9]
- https://en.m.wikipedia.org/wiki/Cartographic_generalization
# Hierarchy

To resolve these differences, we need to be able to resolve mismatches. A scene (encounter) is defined by its point in time and place, but our new character - the act - is a volume of one or more scenes defined by its dramatic progression like the rising action, climax, and resolution.

An act that is one scene long is an independent scene - It can stand alone as a complete narrative fragment in a story. 

The deep encounter, or sequence is an act consisting of multiple dependent encounters (scenes) that can only work together. Because the Story is mostly developed as part of the sequence, not per encounter, dependent encounters demand less attention, but more connection between each other. This chapter will explain the structure of deep encounters and provide the mechanics/resources for running one in the AB13 setting.


## Beats

```
Kusok - bits or units of action, defined by a specific period of thought and action, an event and dynamic taking place between characters. These bits may be small, scene-length, or larger episodes.
```

We can divide Geography into blocks like story can be divided into beats. These bits are defined by distance as action is by time, while populated with attributes such as elevation or terrain.

From these geographic blocks we can convert from distance to action by dividing the distance by the move speed and multiplying that by the number of ticks it takes to act.

The one exception is that most weapons are unaffected by range. any weapons that take multiple seconds to hit their target do not count.


# Scale
(Major Revision required)

Skirmish scale, local scope - small units of 1 to 32 in size, map in 1m to 1km intervals

Skirmish scale, regional scope - small units of 1 to 32 in size, map in 1km to 100km intervals



Resolution - the ratio of the standard unit to the scale (or is it the scale between the Minima and maxima?) - https://en.m.wikipedia.org/wiki/Magnitude_(mathematics)
Scope?  - the ratio between the common scale and the spatial maxima
https://en.m.wikipedia.org/wiki/Spatial_scale - 

Examples of scales in geography and metereology[4]
Scale	Length	Area	Description
Micro	1 m – 1 km	1 m2 – 1 km2	local
Meso	1 km - 100 km	1 km2 - 10,000 km2	regional
Macro	100 km - 10,000 km	10,000 km2 - 100,000,000 km2	continental
Mega	10,000 km - 1,000,000 km	100,000,000 - 10,000,000,000 km2	global
Giga	>1,000,000 km	>10,000,000,000 km2	superglobal

Common Scale - the interval of common interest

Minima - the smallest depicted interval for an object. Fuzzy, but correlates to the smallest visible fraction of the standard unit.

Maxima - the largest depicted interval for an object. Correlates to map size

Interval - a division of distance or time

Standard unit - the major organizing division of distance

Large
Intermediate
Small

# Maps in AB13
# Combat  maps

Direct combat operates on a set of loosely related scales:

- small unit/individual
- tactical

The small unit scale is well known to D&D players as the skirmish scale of combat. This is the majority of brawls or gunfights and other high frequency encounters.

The Small unit scale in AB13 corresponds to the exchange of fire in TW13.

However, in fights with special conditions, such as long lines of sight, the use of vehicles, or when large amounts of terrain must be crossed, the larger distance, lower frequency tactical scale is used.
## Tactical Scale

>“Gone were the times when on the battlefield one might view an individual action during which victory was attained with a single blow.”
>- Clausewitz

The tactical scale in AB13 exbuilds the tactical pause from TW13.

Because it manages actions on a lower frequency, the tactical scale is designed to handle large scale actions quickly.

The tactical scale is organized into a sequence of tactical exchanges of an elastic length, but each exchange can be ~~packaged into a larger set, or~~ broken down into an individual scale exchange

---

# old

# Chosen: Candidate 1 

We're going to write in terms of tactical, operational and strategic encounters
## gameplay value of deep encounters
- You get to play a sniper type more effectively
- You can play characters with long distance endurance
- You can play with wider pieces of terrain to support your movements
- Flanking is more valuable
- Tactical depth
- Movement is more deliberate because range outpaces movement
- Assault phase

For the conflicts that the characters of modern shooter RPGs face, we can contextualize them with 3 overlapping scales of war: tactical, operational, and strategic. [^1]
## The Tactical Aspect
- the close quarters battle map where the toughest fighting is expected to happen
- hard combat
- individual responses, microterrain
## The operational aspect
- operational map - zoom in: general area map - make a rectangle of the area that'll matter. Roll for nodes.
	- Operational points - parts of town, sections of street
- the squad (party's) scale of command and decision, when everyone sits down and says "in this wide variety of objects, we're focusing on x"
	- the macro of combat, more generalized in keeping track of the firefight
	- During the command phase, there's a tactical pause 
	- there's a threat, but it's currently a pause
## The strategic aspect
- strategic points - the scale of the wider story.


## Operational maps
- node and connector system
- connectors are to scale
