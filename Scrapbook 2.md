

---

Tech stack for mapping

GIS

Vector drawing
- https://www.reddit.com/r/vectorart/comments/b9ori0/which_vector_graphics_software_would_you_recommend/

# Performance dice

# Dimensional dice

multiple functional characterizations for one test

A test always has at least one dimension. Additional dimensions must be bought with performance dice before they exist.

If a dimension isn't tested for but its performance must be determined, the GM either assigns a minimal success value, or the test automatically fails because the character failed to recognize what criteria was important in the task

![[Pasted image 20250328104318.png]]

![[Pasted image 20250328105302.png]]

ADA219373

# Warthunder

One of the big failures is the game seems to handle residual behavior poorly. For instance, an eroding projectile that barely perforates the composite armor array should have a significant decrease in projectile mass and velocity, both parameters which should reduce the behind armor debris


# 
> All modern armor should do this - Gaijin hasn’t considered this because the materials and composition of most modern armor are classified. They also haven’t given any tank crews spall vests either.

> Fact of the matter is - what they are modeling on the T-90, Bradley, etc… it is an internal spall liner on the interior of the tank armor within the crew area. The Abrams has NEVER had anything of the sort. IRL it is because it simply doesn’t need it, but it will suffer in-game because of this. You’re better off wasting your time suggesting they add spall vests to modern tank crews instead.

# Meeting engagement range

BV + winners $\Delta$ * 10%
# Terrain vision

A topographic surface, or terrain, can be viewed from a mathematical perspective as 
the image of a bivariate function f defined over a domain D in the Euclidean plane. A 
digital elevation model (DEM) is a model of terrain built on the basis of a finite set of 
digital data.

Terrain data consist of elevation measures at a set of points S in the two-
dimensional domain D. Points in S can either be scattered or distributed on a regular 
grid. A DEM built on S represents a surface that interpolates, or approximates, the 
measured elevations at the points of S.

In the mathematical field of numerical analysis, interpolation is a type of estimation, a method of constructing new data points based on the range of a discrete set of known data points. [Wikipedia](https://en.wikipedia.org/wiki/Interpolation)

> planar graphs are to be drawn in such a way that no edges cross each other.[[1]](https://en.wikipedia.org/wiki/Planar_graph#cite_note-1)[[2]](https://en.wikipedia.org/wiki/Planar_graph#cite_note-2) Such a drawing is called a **plane graph**, or a **planar embedding** of the graph.


# Mapping

Only use irregular triangle, regular square, or irregular square polygons

Do not overlap polygons

a polygon face needs to be a flat surface. Any changes in elevation must be between polygons

A point on a TIN is visible if a segment vp doesn't intersect the terrain on its way from v to p


# QGIS

https://www.qgistutorials.com/en/docs/3/working_with_terrain.html

We will be working with GMTED2010 dataset from USGS. [GMTED (Global Multi-resolution Terrain Elevation Data)](https://eros.usgs.gov/#/Find_Data/Products_and_Data_Available/GMTED2010) is a global terrain dataset that is the newer version of GTOPO30 dataset.


wheres the land cover data?

# procedural generation

You're definitely on the right track with the concept of stacking (layering, blending) noise channels to achieve your desired outcome. It's not the most intuitive way to think about building complex terrain, but it's by far the easiest to turn into predictable, tweakable, expandable code.

## Processing

https://www.youtube.com/watch?v=fFrTZllf33Q&t=90s&ab_channel=RemptonGames




determine how epic or personal the campaign will be

Most of the time, a single skill roll should be enough to decide how a par-ticular situation in play resolves. You’re not obligated to describe actions in a particular timeframe or level of detail when you use a skill. Therefore, you could use a single Athletics roll to find out whether you can safely navigate a rock face that will take days to climb, or use that same single skill roll to find out whether you can safely avoid a swiftly falling tree that’s about to crush you.

Sometimes, however, you’ll be in a situation where you’re doing some-thing really dramatic and interesting, like pivotal set pieces in a movie or a book. When that happens, it’s a good idea to zoom in on the action and deal with it using multiple skill rolls, because the wide range of dice results will make things really dynamic and surprising. Most fight scenes fall into this category, but you can zoom in on anything that you consider sufficiently important—car chases, court trials, high-stakes poker games, and so on. We have three ways for you to zoom in on the action in Fate:

# Maps 

- sidescroller
- abstract zones
- TINs
- node graphs

# Friction in fiction
```
proactivity
Characters in a game of Fate should be proactive. They have a variety of 
abilities that lend themselves to active problem solving, and they aren’t 
timid about using them. They don’t sit around waiting for the solution to a 
crisis to come to them—they go out and apply their energies, taking risks 
and overcoming obstacles to achieve their goals.
```

```
You roll the dice when there’s some kind of interesting opposition keep-
ing you from achieving your goals. If there’s no interesting opposition, 
you just accomplish whatever you say you’re trying to do.
```

A caveat with modern storytelling is murphy's law: sometimes, the inconsequential things people overlook comes to become a major obstacle for friction later. For instance, forgetting to top off a vehicle's gas tank may come to haunt people later. In the moment, it's mundane, but forgetting to do so may have an interesting impact on the drama later.

Resolving these should be simple: Murphy's law should not take a roll to complete - you simply do it and get on with your life unless you voluntarily wish to add a little extra.

# Murphy's law

Food, Fuel, supplies, and all the ancillary problems of working with limited supply are a function of Murphy's law. By the game's rules, you do not need to count it or fix it until you run out or forget.

Therefore, Murphy's law is an operational test by the gm which covers an entire period of activity. Murphy's law can is triggered either by failure or by when the GM decides.

The murphy test is a 1d20 roll for the entire squad against a murphy factor - the squad's murphy value plus all the gear, ammo, fuel, food, battery needs of the squad. If Murphy fails this test, no bad things happen; but if Murphy succeeds, then the GM is granted a number of Murphy points to spend on messing with the player.

Additional preparedness can increase the number of dice in a murphy test (if implemented, need to reverse murphy's law sux/fail states)

A player can declare they paid murphy off for a specific situation, such as bringing extra supplies or paying extra attention to a delicate piece of kit. Paying murphy off cancels one application of Murphy's law to that situation.

If 
# Time

Actions in T13 can be split into several categories.

https://fate-srd.com/fate-codex/rethinking-stealth

## rapid time (old tactical, Quick action (Fate))

Rapid time covers things such as shooting, clearing a room, bandaging a wound, or scaling a fence. They happen more or less in real, chronological time.

Typically, The most important effect for a rapid task is whether the test succeeds.

Often, players will focus on the quick. They’ll say they want to do something, roll the dice, and then it’s done.

## Tactical time (old operational)

Tactical time is things that exist over the span of minutes or hours, such as casing a bar, combing a room, or bugging a car.

 The typical primary criteria for a tactical task is whether it succeeds or how long the action takes.

## Operational time (new)

Operational actions are things like sneaking through a facility, finding a buyer for a highly illegal magical artifact, or combing a crime scene for clues. They can take minutes, hours, or even days to complete.

The typical primary criteria for an operational task is how long the action takes, unless the task is extremely difficult.

 Longer things are thought to be more boring, the kind of “downtime” events that go on between adventures, like crafting magical items or learning new languages.

# Stealth

by convention, the length a stealth success lasts is semi-indefinite, lasting until the next stealth check is tested.



## Stealth and time

https://www.therpgsite.com/pen-paper-roleplaying-games-rpgs-discussion/good-stealth-mechanics/

I have found the Wrath & Glory rules for Stealth interesting and useful for gaming. You roll your stealth score (after including modifiers for environment, gear, special abilities, etc.) and your successes (it's a dice pool system) give you a stealth score. This is the score opponents need to beat with their passive awareness to detect you. The trik is that various actions taken can increase or (more commonly) decrease your stealth score. If the GM wants to keep you on your toes, they can switch the flat increases/reductions to a randomized value and keep track of your score out of players' sight so they don't necessarily know the exact moment they are detected.

---

I think the best stealth mechanics I've encountered recently are in a Stars Without Number supplement "Darkness Visible" which is about espionage campaigns.  
  
Basically, you get everyone to roll their Stealth skill normally. The person with the highest Stealth skill has their skill level (Traveller-rated, so 4 is the highest) in free passes that they can dole out to the less ghostly party members. It keeps it light and fast, while also preventing one bad stealth roll from screwing the whole infiltration.  
  
I do like the idea of a Stealth pool, where time and actions degrade the pool. I wouldn't use a HP mechanic, but I might use poker chips or something like that.

---

I guess I'd start by asking "What do you mean by Stealth?"  
  
  
When I think of stealth, it either boils down to encounter stealth, or whole-scenario stealth. The D&D rulesets have an acceptable level of abstraction for encounter stealth, but really fall flat if you try to apply them to whole-scenario stealth.  
  
Key principles I would suggest for designing a system for whole-scenario stealth:  
  
* More players rolling dice should not necessarily lead to higher chance of failure  
* Every character can contribute something unique to the encounter (not just "I roll Stealth")  
  
In my mind, whole-scenario stealth is more along the lines of Ocean's Eleven or Mission Impossible. You need to define key roles for characters like face-man, technical (hacker, mage), muscle, diversion, etc. The roles need not be specific to the character but could be fluid to the scenario -- e.g. Russian character is a more effective face-man in a Moscow-based scenario, even if he's normally the strong-man who knocks out guards.  
  
What you probably end up with is some kind of progress-clock minigame where you give players a certain number of moves to accomplish their objectives. I also like the idea of a stealth pool that automatically ticks down, which implicitly creates some tension and you can either force players to do certain things (hide, knock out a guard, make a diversion, etc) to maintain stealth, or complete objectives.


---

With stealth as with other skills, what I like to do in skill-based systems (as opposed to class-based) is that if you have the skill, you're not rolling to see _whether_ you succeed, but _how well_ and _how quickly_ you perform the skill.  
  
So for example with stealth,  
  

- fail - you move slowly and noisily, you can be mistaken for an animal moving around in the area, or a person friendly to the watcher
- success - you move quickly _or_ quietly. If quickly, you're still noisy, but they can't get a precise bead on you. If quietly, you're quiet but it'll take you a long time to get from A to B
- great success - you move both quickly and quietly

  
with this in mind, only a great failure is a traditional "fail." Two of the other possible three results give the player a choice - and it may be a difficult choice. Let's say you're doing a prison break and trying to sneak by a guard - you can make noise but move quickly, or be quiet but be slow - but both you and the guard are outside the building, he's on the opposite side, if you choose to be slow he might come across you soon, but if you're noisy while he might ignore you, his mate up on the tower might notice you, and...  
  
Indeed, if the player is willing to have their character do something slowly enough, they can _always_ do it well - without even rolling. Got mechanics? Want to fix an overheated engine? Got a week? No worries, hold your dice, pass the cheetos. Want to do it in ten minutes? Want to do it so it won't burn out again after another hour of driving? Better roll.  
  
Combat skills, by the way, _always_ need to be done well and quickly. That's why you always roll for combat, and why the results are either/or with success/failure. That's combat.

## Levels of Stealth



---

