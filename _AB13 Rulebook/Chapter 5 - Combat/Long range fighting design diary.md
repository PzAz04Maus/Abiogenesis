# Theory

## Problem statement: how do I design interesting combat maps quickly

- map setting
- number, shape, placement of regions
- function amount
- structure
- choice

## Statement 2: is giving the players a role in designing the combat map going to help with statement 1
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

## how much value does a descriptor get you?
- how valuable is it
- how broad that value is

could use a side dice with the choice of how valuable or how broad taking up two slots

### what terrain functions are there?
- Cover
	- Use tactics roll to determine if cover is nearby
	- ~~Unaware enemies roll 2d20h for abstract cover~~
- Concealment
- observation
- obstacles
- frontage
- forage
	- We can game forage levels with the following mechanics
	- Patch yield
	- Clues for patch location: 
		- Patterning
- quantity/microterrain
### what are other terrain characteristics other than their direct utility
- positive/negative space
- % obstructions/clearings
- shape

## what general map conventions exist?
- average region size
- pattern
- number of regions found per discovery

## How do we record these characteristics in a short manner?

- Musical notation
- network graph
- Algorithm
# terrain utility results
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



# Types of level designs

## Procedurally generated
\+ 
\- 
## Cartographic levels
+high accuracy

+high fidelity

+easy to share

-lots of work needed (need abstraction layers to improve workflow, so money, effort or time investments)

-hard to edit

## Descriptive maps ( theatre of the mind )
-difficult to share

+easy to make ( few/easy abstraction layers)

+easy to edit

+high flexibilty

+ambiguous

## Thumbnail map

# Terms


## Success Curves
The descriptive result of a skill check. The success curve is usually described in a 0 part summary - an exceptionally positive result, a positive result, a 0 result (glance), a negative result, and an exceptionally negative result.
## [scaling](https://en.wikipedia.org/wiki/Level_of_measurement)
Is entirely determined by the gm, but by default consists of regions with a maximum length of 100 meters

Regions consist of either positive, negative, or some fraction of the two spaces

Regions can be any kind of polygon.

## Layers of abstraction

In computing and programming, a layer of abstraction is a layer that provides a simple way to access what is underneath it. For example, in a computer, the operating system is a layer of abstraction between a program and the physical disk.


---

# How to manage terrain 

What about a list of potential terrain cards for choosing? 

Terrain cards can be redesigned by the players, such as where the buildings are located in the square or the position of the treeline.

Ex: sector cards


3 buildings
3 buildings and road
5 buildings
5 buildings and road
Field
Forest
Forest edge, 70%
Forest edge, 30%
Copse
Road
Road and crossing
Mud
Swamp


Have a negative space card and 5 positive spaces that can be organized in any way.

A +5 sux can be a wildcard of whatever the players choose

---

# Read more


https://boardgamegeek.com/thread/2554256/terrain-effects

https://companyleader.themilitaryleader.com/2023/01/30/urban-terrain-analysis/

https://www.reddit.com/r/40krpg/comments/vdx00o/space_hulk_map_generator_for_wrath_glory/

---


[^1]: In [mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization "Mathematical optimization") and [decision theory](https://en.wikipedia.org/wiki/Decision_theory "Decision theory"), a **loss function** or **cost function** (sometimes also called an error function)[[1]](https://en.wikipedia.org/wiki/Loss_function#cite_note-ttf2001-1) is a function that maps an [event](https://en.wikipedia.org/wiki/Event_(probability_theory) "Event (probability theory)") or values of one or more variables onto a [real number](https://en.wikipedia.org/wiki/Real_number "Real number") intuitively representing some "cost" associated with the event. An [optimization problem](https://en.wikipedia.org/wiki/Optimization_problem "Optimization problem") seeks to minimize a loss function. An **objective function** is either a loss function or its opposite (in specific domains, variously called a [reward function](https://en.wikipedia.org/wiki/Reward_function "Reward function"), a [profit function](https://en.wikipedia.org/wiki/Profit_function "Profit function"), a [utility function](https://en.wikipedia.org/wiki/Utility_function "Utility function"), a [fitness function](https://en.wikipedia.org/wiki/Fitness_function "Fitness function"), etc.), in which case it is to be maximized. The loss function could include terms from several levels of the hierarchy.

[^2]: a [fitness function](https://en.wikipedia.org/wiki/Fitness_function "Fitness function") to evaluate the solution domain.


[^3]: evolutionary algorithm: The evolution usually starts from a population of randomly generated individuals, and is an [iterative process](https://en.wikipedia.org/wiki/Iteration "Iteration"), with the population in each iteration called a _generation_. In each generation, the [fitness](https://en.wikipedia.org/wiki/Fitness_(biology) "Fitness (biology)") of every individual in the population is evaluated; the fitness is usually the value of the [objective function](https://en.wikipedia.org/wiki/Objective_function "Objective function") in the optimization problem being solved