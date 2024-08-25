#Shorthand #solution-pending
# Questions & Theory

## How do I run long range combat maps?
all map types
- open
- closed
-  battle
- adventure
##  How do we record these characteristics in a short manner?

- "Musical" notation
- network graph
- ~~Algorithm~~

- node polygons
- [zones of influence](https://www.youtube.com/watch?v=2-qoa6GFdss)
	- zones are spaces that tell players a POI exists
		- zones of influence are where players should be able to see the POI
		- a POI has secondary elements
		- subelements are connected to each other by visible paths or sensible circuits that funnel players
		- characters should never be too far from a particular play hint
	- you want your roads to end at content, not be complete circuits
	- random city related content can also be placed by the paths
	- between each zone of influence is a default medium
	- problem is the source is adventure, not battle
- lane lines
- wall lines
- blockouts and clusters
- positive/negative space

### Procedurally generated
\+ 

\- requires software
\- requires export
### Cartographic levels
+high accuracy

+high fidelity

+easy to share

-lots of work needed (need abstraction layers to improve workflow, so money, effort or time investments)

-hard to edit

### Descriptive maps ( theatre of the mind )
-difficult to share

+easy to make ( few/easy abstraction layers)

+easy to edit

+high flexibilty

+ambiguous

---

use vectors

multiple layers for heightmaps

different colors for types

**living rooms** - spaces where characters live or handiwork

using open battle maps
- borders should dissuade interest by having fewer subelements and less paths the further away from the center they are.

## Problem statement: how do I design interesting combat maps quickly

- map setting
- number, shape, placement of regions
- function amount
- structure
- choice

## Statement 2: is giving the players a role in designing the combat map going to help with problem 1
- having this discovery check pushes players to deeply interact with their environment
- the design of the system already depends on players discovering valuable microterrain (lv-1) like cover concealment supplies or paths
- it makes little sense to deny them the ability to discover (lv0)
- the subjective nature of terrain value

## Statement 3: What is the utility[^1] of certain terrain?

When a unit rolls their discovery check, they are determining what that terrain's utility will be in regards to them.

This utility is dependent on a relationship between
- the general characteristics of the terrain
- the units resources and preferences
- the opposing units resources and preferences
- the game's meta

Utility is subjective because of these dependencies, so it can't directly become an objective value that authentic gameplay requires, but only converted. For example, the discovery check currently cannot distinguish between flat ground and rolling valleys without a lot of lookup tables, nor can it support a unit's preferences.

The most efficient way we can convert a terrain's utility into mechanical benefits while taking preferences and characteristics into account is through player choice constrained by open ended descriptors: the players determine what kind of terrain they receive, the dice decide the value.

## Statement 3: how much value does a descriptor get you?
- how valuable is it
- the volume of that valuable terrain in the region

the choice of terrain can add bonus value or volume

could use a side dice with the choice of how valuable or how broad taking up two slots

slot 2 success curve is at least a glancing success/foil

### what utility does terrain have?
- passage ![[ButtonDelLastPressed.png]]
- obstacles ![[ButtonHeightPressed.png]]
- Cover ![[ButtonArmoredPressed.png]]
	- Use tactics roll to determine if cover is nearby
	- ~~Unaware enemies roll 2d20h for abstract cover~~
- Concealment ![[ButtonLosPressed.png]]
- observation ![[ButtonReconPressed.png]]
- pace ![[ButtonFastPressed.png]]
- frontage ![](https://hoi4.paradoxwikis.com/images/8/86/Tactics_combat_width.png)
- forage ![[ButtonMapPressed.png]]
	- We can game forage levels with the following mechanics
	- Patch yield
	- Clues for patch location: 
		- Patterning
- quantity/microterrain
![[ButtonWedgePressed.png]]
### what are other terrain characteristics other than their direct utility
- positive/negative space
- % obstructions/clearings
- shape

## what general map conventions exist?
- average region size
- pattern
- number of regions found per discovery
### Tips

\# of paths/options
- 1 = not enough
- 2 = okayish
- 3 = admired number
- 4 = almost too much
- 5 = about the limit
- 6 = too many

- frequency of options
- players need more options in the places they'll most likely fight
- a room needs to be big enough to feature cover, or else its irrelevant and too cramped
- having cover against walls of living rooms can be unnecessary 
- treat cover as player magnets
- object placement in open spaces is heavily contextual to the environment
	- avoid an even distribution; should have a pattern; think in terms of a cover network
- cover is one of your primary ways to guide through the map
- dont strictly follow all guidelines at all times or else the worlds will feel artificial

# terrain utility results
## [Gen 2](https://www.youtube.com/watch?v=U4dutbP0DwU)

### Path
a distinct course or direction a character can move

### high level lanes
- foundation 
- most expensive to change

### mid-level options
- mid-level are the additional options which complement your high-level layout
- adds options between and within main lanes
- The more your layout design has a subconscious impact and feel to it, the better.
- medium expense to change

That means you are finally ready to start adding extra mid-level paths and shape them to the environment. For example, you could consider adding thin alleyways between houses, shortcuts through buildings, conveniently placed doors or windows, grid-like streets for the US or smaller curvy routes in European cities, or organic outdoor setups. However, of course, you should stay true to your abstract high-level fundamental composition.

If you always know the main paths of your enemies or they know yours, you cannot surprise each other anymore, and the level/game quickly becomes boring.

base path length on .5-1 intended weapon range

### low level options
- microterrain
- the benefits that complement what a character is trying to do

the riches of a piece of terrain should relate to its type and the number of options it affords a player

- midlevel paths are valuable for fighting because they allow concealment, cover, tactics, protection
- traversal areas are valuable for moving from POI to POI quickly

the frequency of paths should be limited, but... "You need more choices the longer the lanes and the more players/AI you build your map for. Especially around combat encounters, you need a good amount of get-out paths for players and potential ways for AI reinforcement."

### default costs for purchasing new paths

- +2: midlevel choice
- +4: high level choice
- each option increases penalty in region by 1
- base bonus dependent on terrain type
	- forests are cheaper, +5 to check
	- open fields - are option poor, -2 to check
	- flat football fields - are barren, -5 to check

## Gen 1
the terrain discovery check uses the standard TW13 skill check to determine a result between +x .. 0 .. -y that defines the terrain's utility in a direct relationship - higher positive values are better for the user.

The catch is that this utility needs to be converted into a results that helps, foils, or hinders the user with a real value

## Terrain utility success curve

the terrain utility curve is a gradient between helping, foiling, or hindering results.

- 1..-1 = foil result. "sidegrade" that is neither helpful nor hindering
- 2..-2 = slight help or hinderance
- 3..-3 = moderate help or hinderance
- 4..-4 = serious help or hinderance
- 5..-5 = critical help or hinderance

Other examples of success curves include
## 1. standard success curve

yes,yes but, no but, no and

## 2. hard success curve

Yes,yes but, no, no and

Storytold/Abstract infantry combat

V

Tabletop infantry combat

Encounters and dramatic encounters


---


[^1]: In [mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization "Mathematical optimization") and [decision theory](https://en.wikipedia.org/wiki/Decision_theory "Decision theory"), a **loss function** or **cost function** (sometimes also called an error function)[[1]](https://en.wikipedia.org/wiki/Loss_function#cite_note-ttf2001-1) is a function that maps an [event](https://en.wikipedia.org/wiki/Event_(probability_theory) "Event (probability theory)") or values of one or more variables onto a [real number](https://en.wikipedia.org/wiki/Real_number "Real number") intuitively representing some "cost" associated with the event. An [optimization problem](https://en.wikipedia.org/wiki/Optimization_problem "Optimization problem") seeks to minimize a loss function. An **objective function** is either a loss function or its opposite (in specific domains, variously called a [reward function](https://en.wikipedia.org/wiki/Reward_function "Reward function"), a [profit function](https://en.wikipedia.org/wiki/Profit_function "Profit function"), a [utility function](https://en.wikipedia.org/wiki/Utility_function "Utility function"), a [fitness function](https://en.wikipedia.org/wiki/Fitness_function "Fitness function"), etc.), in which case it is to be maximized. The loss function could include terms from several levels of the hierarchy.

[^2]: a [fitness function](https://en.wikipedia.org/wiki/Fitness_function "Fitness function") to evaluate the solution domain.


[^3]: evolutionary algorithm: The evolution usually starts from a population of randomly generated individuals, and is an [iterative process](https://en.wikipedia.org/wiki/Iteration "Iteration"), with the population in each iteration called a _generation_. In each generation, the [fitness](https://en.wikipedia.org/wiki/Fitness_(biology) "Fitness (biology)") of every individual in the population is evaluated; the fitness is usually the value of the [objective function](https://en.wikipedia.org/wiki/Objective_function "Objective function") in the optimization problem being solved