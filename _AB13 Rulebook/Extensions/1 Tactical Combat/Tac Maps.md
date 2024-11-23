design long range combat maps ~~with QGIS~~ with draw.io using [pointcrawl](https://thealexandrian.net/wordpress/48666/roleplaying-games/pointcrawls) methods
- can either be literal topography
- or can be conceptual topology

- Also in cartography, a [topological map](https://en.wikipedia.org/wiki/Topological_map "Topological map") is a greatly simplified map that preserves the mathematical topology while sacrificing scale and shape


 **[Topology](https://en.wikipedia.org/wiki/Topology "Topology")** is a branch of mathematics concerned with geometric properties preserved under continuous deformation (stretching without tearing or gluing).

A [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") is a [set](https://en.wikipedia.org/wiki/Set_(mathematics) "Set (mathematics)") endowed with a structure, called a _[topology](https://en.wikipedia.org/wiki/Topology_(structure) "Topology (structure)")_, which allows defining continuous deformation of subspaces,

https://en.m.wikipedia.org/wiki/Shapefile

## questions

Future question to answer
- should players be able to place their own operational nodes

# Theory


4 slow, 1 fast

https://en.wikipedia.org/wiki/NLF_and_PAVN_battle_tactics#Attack_doctrine:_%22one_slow,_four_quick%22


https://youtu.be/qfzW3EUeuQk?si=zw95u18cJ2vqOE_8
https://youtu.be/kaWah6FSLZI?si=DDz2TFLYdZ6OO7_Q

## guidelines
### Terrain Patterns

Most common LOS

Eastern Europe - 5000 meters

North Korea - 2000m

Urban - 300-500m



Hex Table

	See the alexandrian

pattern 1: light forest

sector - depth - heightmap


<table>
  <tr>
   <td>plain
<p>
plain
<p>
copse of trees
<p>
plain
<p>
high grass
<p>
heavy forest
<p>
light forest
<p>
light forest
<p>
light forest
<p>
plain
   </td>
   <td>3000m
<p>
2000m
<p>
100m
<p>
300m
<p>
200m
<p>
200m
<p>
400m
<p>
1400m
<p>
1400m
<p>
300m
<p>
800m
   </td>
   <td>-1
<p>
0
<p>
0
<p>
+1
<p>
-2
<p>
-1
<p>
0
<p>
+2
<p>
+2
<p>
0
<p>
0
   </td>
  </tr>
</table>


Pattern 2: urban 

sector - depth - building height


<table>
  <tr>
   <td>residential
<p>
infrastructure
<p>
light business
<p>
light commercial
<p>
industrial
<p>
reverse OR rural
<p>
business park
<p>
storefront
<p>
highway
   </td>
   <td>15 blocks
<p>
2 blocks
<p>
6 blocks
<p>
4 blocks
<p>
3 blocks
<p>
10 blocks
<p>
2 blocks
<p>
3 blocks
<p>
1 block (wide)
   </td>
   <td>1
<p>
2
<p>
2
<p>
3
<p>
2
<p>
0
<p>
5
<p>
1
<p>
2
   </td>
  </tr>
</table>

Chose a granular scale(minomim size of blocks) 
Set by the expected weapon range you want



https://en.m.wikipedia.org/wiki/Oregon_Outback

Terrain templates

Bunch grass
Chaparral



---

For open world maps...

Negative space - the background or volume that surrounds the points of interest in a map
Positive space
Boundaries
Voids

Negative space is the background or the area that surrounds the subject of the work. ​Positive and negative space can form an important part of your overall

actually, for this - 

> This article [proposes that  levels of war] should be thought of as levels of analysis. 
> 
> There is overlap between strategic, operational and tactical levels, so there is no clear demarcation that can be uniformly applied

This assertion states that these two scales are not the same thing, but have levels of overlap which mud the waters.

But the more important part of this statement is that my thought is the GM use a parallel, but miniature set of levels of military analysis to run a story in a game. In my case, the patrol simulator would focus on modelling the activities of one party of people between a fireteam and squad in size as they patrol a battlefield to complete objectives. 

The best part is that the tabletop theoryhammer and gamedev types already have a grip on the party scale tactics and party scale strategy, which are used when the need arises. The only thing missing is a real condensation of the "party operational scale", and how to turn this theory into gameplay.


The void can be considered the Offscreen portion of a play space 

find vid on BSP

# Map design
Associate distances with environment types

Scales and combat types

Stealth - closer

Action - normal

Tactical - farther

---

8 little loops

2‐3 big loops

---

The most common segment type within a high-level linear layout is a linear branching one. (wot?)

---

The Myth games usually had you playing missions as special small scale operations with the mission briefings detailing other large-scale battles going in as narrative filler. This made it feel like you were always playing as a small-scale specialised operation command yo support the overall war effort against the dark rather than the chief army leading the charge, which really helped ground the experience.
# Microterrain
## Roll for microterrain
Two types 

Prepositioned - done at start of match, can only be placed in Los, Maximum distance is halfway between the enemy

Ad hoc - done once per operational action. Max distance microterrain may be placed from character is movement distance. Mt can be used piecemeal 


Modifier based on how congruent, harmonious, appropriate the object is to its environment

+5 Ubiquitous
+3 Widespread
+1 Frequent 
+0 Common
-1 Occasional
-3 Scattered
-5 Rare

Use side dice to determine the size of the microterrain

Failure costs microterrain points. When an operational area runs out of mtp, no more terrain can be added

Operational areas (aos) don't have a uniform size,  because there is no clear demarcation between the Tactical, operational and strategic scales. The gm therefore has wide latitude in the consistency or number of pieces of microterrain from node to node.

For instance, some microterrain may consist of windows in a building for one node, while another node may have entire houses or street intersections as microterrain.

---

# Old

Question: what if the combat comes to a very short distance? 
You have 2 standard procedures
If the action is limited to a single round, abstracting the subgranular 

Set a maximum scale(long range maximum)

Add terrain blocks of different scales in a contiguous fashion

Define the terrain blocks (type, height, objects 

Add terrain contours

Find (create) terrain .. roll a tactics check, compare to the terrains clutter value. 

Procedure 1
Compare the roll to a numeric clutter value. If the player beats the value, he has found terrain

Procedure 2
Clutter dice value: roll the clutter dice versus the 

Assumptions: if spotted, the characters by default are in the open and out of cover unless they indicate an sop. Gms are encouraged not to let players set and forget their sops

Device 1: degree of success is relative based on the gms preference. Default should be 1( 1 2 3)

# Mapping and patterns

# Gridpoint scattering

indexed points equally spread out on a grid with a distance D between each point, and we create a node from each index by shifting it a random amount from the index point.

can be for roads or squares or trees

how to incorporate regional terrain

how to make smooth curves

how to control the line deviation for stable/mountainous roads


# Patterns versus randomness

The sprawling forest, the bustling metropolitan blocks of a major city, the intemperate weather patterns that force the unwary to duck for cover; these are all situations where what seems random is actually patterned in some fashion. A collection of objects can fit a particular shape, or a sequence of objects can regularly indicate what comes next.

Because of the range of modern firearms and the complexity of modern environments, the playing fields of contemporary settings are much larger than their fantastical bretheren, as well as much more complicated. The fantasy standard of structuring encounters - the random number table, can’t cover for the level of predictibility that some collections need, such as what lies ahead onthe highway. To succeed, we need to dig deeper into how to construct patterns to mimic contemporary life.

We also need to find some formats to store these patterns quickly for recall.

# Uncompressed maps
Great if you have the time to prepare, but putting them down takes time. You need to abstract and simplify to shorten the length of time it takes to get into the fight.

This is where abstract modelling comes into play; we use abstraction to compress the time needed to make the terrain function without an appreciable loss in detail.

We can use many formats to compress our data, trading quality and details for GM performance and storage.

# abstracting the map: 2D terrain versus 3D terrain

2D terrain is great as long as you have 2 just two factions that settle down and make a fight. By simplifying the third dimension out as an abstraction, you do less work for yourself.

If the players (or the Enemy!) want to break out of two dimensional planning, it's fairly easy to abstract, refresh or draw a new surface to account for this: at the end of the day you still have a line connecting the two forces!

2D maps do well with chaining and songwritten mapping techniques. It's also easy to describe, as all you have to do is describe what's between you and them.

However, in terrain with more than 2 parties or factions, 2D terrain falls into the three body problem, in which you need 3D terrain.

Full maps are the theoretical ideal, but often it's useful to have premade, heatmaps, or positive/negative abstractions, or even use the living map concept to simplify the work. 

# Templates

```
Repetition is a part and parcel of [symmetry](https://en.wikipedia.org/wiki/Symmetry#In_music "Symmetry")—and of establishing [motifs](https://en.wikipedia.org/wiki/Motif_(music) "Motif (music)") and [hooks](https://en.wikipedia.org/wiki/Hook_(music) "Hook (music)"). You find a melodic or rhythmic figure that you like, and you repeat it throughout the course of the [melody](https://en.wikipedia.org/wiki/Melody "Melody") or [song](https://en.wikipedia.org/wiki/Song "Song"). This sort of repetition...helps to unify your melody; it's the melodic equivalent of a steady drumbeat, and serves as an identifying factor for listeners. However, too much of a good thing can get annoying. If you repeat your figure too often, it will start to bore the listener.
```

We can compose tactical terrain as a phrase made up of a pattern of terrain elements, which are then augmented by modifications in the pattern, or by breaking up the pattern with random inclusions.

Following music theory, this phrase should be about 1 to 4 notes in length. Standardizing the length of each element is recommended, but not necessary.

## Terrain blocks
#proposal 

tl;dr - use musical theory to act like a songwriter with terrain

we can even use a simpler version of positive and negative space

++-+- -

Or positive-negative chains

-4, -2, -2, +0, +4, +4

=

-2, -1, -1, 0, +2, +2

_ arid
VVV virgin jungle
VV dense jungle
V woods
LV light vegetation
R rough
H Hills
M Mountain
''> Pass (continue) - Problem, passes are usually orthogonal to the direction of travel
< Peak (delay)
M Marsh

-1 Valley
0 Flat
1..2 rolling
0..5 Hilly
10 peak

LR track (light road)
R  road
RRR Highway
RR Railroad
W Water Obstacle

X(Y)(+-Z)
X - terrain value,  
Y -terrain type
Z - height value

for example
```
measure: ~100m by 5 m
ratio = 1/6th 
beat - 16m

X X X X X X
R2 R2 R2 R2 R2 R2
R2 R2 R2 R2 R2 R2
R2 R2 R2 R2 R2 R2
R2 R2 R2 R2 R2 R2
R2 R2 R2 R2 R2 R2

X  X  R1 X  X  R2
R2 R2 R2 R2 R2 __
R2 R2 R2 R2 R2 __
R2 R2 R2 R2 R2 __
R2 R2 R2 R2 R2 __
R2 R2 R2 R2 R2 __

R2  R2  R2  X  X  X
__  __  __  R2
__  __  __
__  __  __
__  __  __        R2


```
X - obstacle

This is a street corner with an alleyway, intersection and sidewalk

# Pattern blocks

Noisy patterns

obfuscation

we can obfuscate this pattern to make it more difficult or less predictable for players to recognize.

The idea of introducing a chaos table comes from id Software’s DOOM, which had a pseudo random RNG table of ~100 elements baked into the code. While this compromised the randomness of the game to a degree undetectable by humans, it offered the advantage of producing the same output for every player input. For example, the screen melt transition pattern would always have the same pattern, but only with a different offset. While this theoretically could be gamed, Doom’s deterministic mechanics was essential for making replays possible in 1993.

To create a chaotic pattern, we create a sequential table which can be called a palette (a la Doom).  For a given period of time, we devise a pattern table that’s smaller than the period of time and can be made up of GM decided elements or an  RNG solution: but the important part is that the pattern needs to be at least somewhat determined.

Sequential palette

	Iterate through each element of the palette until you reach the end, then repeat back at the beginning.

Swapping palettes

	After the PCs get used to 

Sequential palette with wildcard scramble

	Same as sequential patterning, but a wildcard event is added: roll a dice  for the wildcard, and jump that many spaces forward in the pattern as a scrambling mechanism.

Sequential Palette with offset N

	After each iterative loop, the GM moves the starting node over N.

Sequential Palette with chance N offset or swap

	After each iterative loop, the GM rolls a dice to check for the probability that the pattern changes

	additional wildcards can be added that flow forward or in reverse in an attempt to create loops

Wildcard bounce

	every time a palette element is needed, the GM tags his current place, rolls a dice, and finds the element N places ahead. Which will become the new event.

	The benefit is that it provides a layer of obfuscation to hide the pattern


--

Random MicroTerrain generation
To find a bonus in microterrain automatically , use dgauge balance
DX-dY

Both can be changed avg is abt d6-d6 for a -5..5 bonus.

For unforgiving terrain mak Y bigger than x

For forgiving terrain make x bigger

Distance from feature

Terrain thats

Entry label
Name (type): roll @distance()

Car concealment 1d6-1d2@2.5x1d4 m

---


Individual scale - one location, the scene
Tactical level - a [sequence](https://en.m.wikipedia.org/wiki/Sequence_(filmmaking)), consisting of the softer decisions that go into a fight
Operational level - the chapter
Strategic level - the act

Rulebook
Theory book

Abstractions
¹

Future question to answer
- should players be able to place their own big nodes

We're trying to design topological node maps with GIS or attached media



https://en.m.wikipedia.org/wiki/Shapefile


- Also in cartography, a [topological map](https://en.wikipedia.org/wiki/Topological_map "Topological map") is a greatly simplified map that preserves the mathematical topology while sacrificing scale and shape

 **[Topology](https://en.wikipedia.org/wiki/Topology "Topology")** is a branch of mathematics concerned with geometric properties preserved under continuous deformation (stretching without tearing or gluing).

A [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") is a [set](https://en.wikipedia.org/wiki/Set_(mathematics) "Set (mathematics)") endowed with a structure, called a _[topology](https://en.wikipedia.org/wiki/Topology_(structure) "Topology (structure)")_, which allows defining continuous deformation of subspaces,



---


Group rolls
- trying to simplify a group's worth of rolls into 1 is difficult.

the number of dice represents the competence or consistency, while the difficulty represents the characters capability.


choose the 
- best capability - opportunity: when only one person needs to succeed
- worst capability - trial: when everyone must succeed
- average capability - task

competence depends on the highest 

---

Roll for microterrain

Two types 

Prepositioned - done at start of match, can only be placed in Los, Maximum distance is halfway between the enemy

Ad hoc - done once per operational action. Max distance microterrain may be placed from character is movement distance. Mt can be used piecemeal 


Modifier based on how congruent, harmonious, appropriate the object is to its environment

+5 Ubiquitous
+3 Widespread
+1 Frequent 
+0 Common
-1 broken
-3 Scattered
-5 Rare

Use side dice to determine the size of the intervening terrain

Failure costs microterrain points. When an operational area runs out of mtp, no more terrain can be added

Operational areas (aos) don't have a uniform size,  because there is no clear demarcation between the Tactical, operational and strategic scales. The gm therefore has wide latitude in the consistency or number of pieces of microterrain from node to node.

For instance, some microterrain may consist of windows in a building for one node, while another node may have entire houses or street intersections as microterrain.

---

Associate distances with environment types

Scales and combat types

Stealth - closer

Action - normal

Tactical - farther

---

8 little loops

2‐3 big loops

---

The most common segment type within a high-level linear layout is a linear branching one. (wot?)


# Composing Sessions

arrangement
- indoors
	- stadium
	- US residential
	- Continental residential
	- US Urban
	- Continental Urban
	- Secure
	- aesthetic
	- industrial
	- infrastructural
- outdoors
	- forest, light
	- forest
	- deep forest
- path
	- road
	- highway

patterns
3s
4s
5s
6s

1. introduce the idea
2. vary it
3. contrast
4. return to idea

https://www.artofcomposing.com/how-to-compose-music-101

https://www.reddit.com/r/musictheory/comments/12552li/what_is_your_structure_for_creating_a_musical/

