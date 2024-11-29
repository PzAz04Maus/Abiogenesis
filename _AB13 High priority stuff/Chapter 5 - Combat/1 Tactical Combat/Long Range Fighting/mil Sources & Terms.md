# Terms
# Mil Terms
My definitions
## Microterrain
See  [intervisibility lines](https://leaderbusiness.blogspot.com/2008/05/intervisibility-lines.html) and [dead space](https://en.wikipedia.org/wiki/Enfilade_and_defilade).
## Engagement
The point at which two forces are close enough to fight or to make an effective attack during an encounter.
### Skirmish
An engagement with only limited commitment between the forces and without decisive results. [^2] See raids, patrols, and meeting engagements.
### Battle
A tactical engagement with committed forces intended for a decisive effect.

> The conduct of war in the era of Napoleon schematically consisted of two basic stages that were far from equal in scope and duration. These stages included a long march along an extended operational line and a short battle in one locale upon completion of the march. Clausewitz described the situation as follows: “In the eyes of strategy, the field of battle is no more than a single point, just as the duration of battle is no more than a single moment.”[^3]

Modern battle has acquired depth in the dimensions of time and space, therefore it is sometimes defined as a *set* of engagements.
## Tactics
The efforts used to succeed on the battlefield[^1]
## Operation
tl;dr - the arrangement of related tactical efforts over a period of time or space.

There is debate over whether operations actually exist, or should be considered a type of modern battle. For our purposes, a battle of large duration and an operation overlap.

> During the second half of the nineteenth century, the brief battle of shock action was transformed into a continuous firepower battle that acquired a protracted dimension in time. Battles during Moltke’s age extended 10-12 hours. At the same time, they failed to yield the decisive outcome so typical of Napoleon’s time. Firepower appeared unable to resolve the issue during one act in a single sector. At the conclusion of a battle, the enemy was not completely destroyed; he gradually retired, reorganized his formations in a new sector, and once again prepared to give battle. Thus, the chain of combat efforts became distributed in depth.[^3]

> Operational art ... is the planning, preparation, synchronization, and sustainment of tactics over a sustained period of time, a large geographic expanse, or both.[^1]
## Strategy
The creation, achievement of war goals through tactical and operational efforts.[^1]
## POI
Point of Interest
# Concepts
## Success Curves
The descriptive result of a skill check. The success curve is usually described in a 0 part summary - an exceptionally positive result, a positive result, a 0 result (glance), a negative result, and an exceptionally negative result.
## [scaling](https://en.wikipedia.org/wiki/Level_of_measurement)
Is entirely determined by the gm, but by default consists of regions with a maximum length of 100 meters

Regions consist of either positive, negative, or some fraction of the two spaces

Regions can be any kind of polygon.

## Layers of abstraction

In computing and programming, a layer of abstraction is a layer that provides a simple way to access what is underneath it. For example, in a computer, the operating system is a layer of abstraction between a program and the physical disk.

# Read more
- https://boardgamegeek.com/thread/2554256/terrain-effects
- https://companyleader.themilitaryleader.com/2023/01/30/urban-terrain-analysis/
- https://www.reddit.com/r/40krpg/comments/vdx00o/space_hulk_map_generator_for_wrath_glory/
- Bauer, Benjamin. A Practical Guide to Level Design: From Theory to Practice, Diplomacy and Production. CRC Press. Kindle Edition. 
![](https://youtu.be/WnR40rBjGzc?si=q7JrE1122uqqthUg)
![](https://youtu.be/y5zZ2hj5tJ4?si=pNxNKstlxa8xHxQg)
![](https://youtu.be/RwlnCn2EB9o?si=i2-hxK3JEAOc5B9H)
![](https://youtu.be/o4YbGGv1n00?si=yCiTB91GSVXdetd6)
![](https://youtu.be/uTOyP9hOhgA?si=Yr2VBBdGs2KCGbXV)
![](https://youtu.be/S3cPJL4ISlU?si=kyv4D_YYIOdZwX-u0)


---

## samples
Also known as the overworld

https://en.m.wikipedia.org/wiki/Overworld#:~:text=An%20overworld%20or%20a%20hub,all%20its%20levels%20or%20locations.

Highfleet

Quasimorph system map

Jagged alliance

Xcom

A jagged alliance manager game? 


---
# Extra reading
- https://kotaku.com/hub-worlds-can-be-games-greatest-pleasure-1822520149
- https://www.gamedeveloper.com/business/how-the-i-jagged-alliance-2-i-developers-dealt-with-90s-gun-culture#close-modal

# Procedural Level Design for Platform Games
https://web.archive.org/web/20210824162807/https://users.soe.ucsc.edu/~michaelm/publications/compton-aiide2006.pdf

This paper proposes a new four-layer hierarchy to represent platform game levels, with a focus on representing repetition, rhythm, and connectivity. It also proposes a way to use this model to procedurally generate new levels

Platformer level generation is a more difficult problem than level generation in either RPG or strategy games, since very small changes, such as slightly changing the width of a chasm, can change a whole level from challenging to physically impossible. Rogue-like level generation can make heavy use of relatively unconstrained, random decisions. The playability of the level is ensured by the constraints implicit in the human-designed atomic units employed by the generator (e.g. rooms, hallway connectors, terrain tiles). In contrast, the playability of a platformer level is strongly determined by the relationships

between units, requiring that these relationships be explicitly modeled and manipulated during level generation. The loosely constrained, random placement of elements that works in dungeon level and terrain generation, can easily lead to accidentally unwinnable platformer levels

Basic Patterns. A basic pattern consists of a component, either by itself, or repeated several times with no variation. 

Complex Patterns. A complex pattern is a repetition of the same component, but with the tweaks changed according to some set sequence, such as a series of horizontal jumps of increasing width. 

Compound Patterns. A compound pattern alternates between basic patterns made of two different types of components. An example of this would be a series of three horizontal jumps, followed by three spiky hurdles, followed by three horizontal jumps again. Note that compound patterns introduce a rhythmic pattern at a higher level of abstraction, in the form of changing the rhythm in a rhythmic manner. 

Composite Patterns. A composite pattern consists of two components placed so close to each other that they require a different kind of action, or a coordinated action, that would not be required for each one individually. This requires the player to take the knowledge of the two problems and synthesize it into a solution. A timed spike requires the player to judge the right time to pass, and a gap requires a judgment of distance, but placed together, they require the player to coordinate the timing with the run-up to the jump



##

The structure of this hierarchy is inspired by “A Novel Representation for Rhythmic Structure,” a paper describing a model for representing complex rhythmic patterns in African and African-American music (Iyer 1997). Iyer describes a hierarchical representation that captures rhythmic repetition and the combination of short rhythmic sequences into longer, more complex passages. Though relating musical composition to the design of platformer levels may seem like a stretch, level design in platform games relies heavily on rhythm. Rhythmic actions help the player reach a “flow” state in games, a state of heightened concentration

Components

Components, such as vines, platforms, little hills, and spikes, are the basic units out of which platform games are constructed. Often a component will have both an obstacle and a resting spot, which may be as simple as a stretch of empty air that must be jumped over, along with a platform to land on.

Cells and Cell Structures

Cells, the building blocks of non-linear level design, are constructed from linear patterns. A cell is an encapsulation of some pattern. At this level, the characteristics of the specific pattern are ignored; it is only important that it is possible for the player to get from one end of the pattern to the other.

Level Design Algorithm 
This model can be partially represented as a context-free grammar, with a level as a start symbol, patterns and cells as non-terminal symbols, cells structures and pattern combinations as productions, and components as terminal symbols. Since generating strings from a grammar is very simple, the process of constructing a new valid level is equally straightforward.

Those cells are each given a pattern, which, like the cells, can be recursively expanded into more patterns. Finally, each bottom level pattern is translated into a series of components.

Pattern-Building 

To build a pattern, the system starts with a short list of possible component types and two bracketing components already present in the level that mark the beginning and the end of the desired pattern. For each possible set of component types and number of components, the optimal pattern is built, and then the best of these is selected as the final pattern.

To start the hill-climbing search, the system creates an initial pattern by first selecting random values for the component parameters (e.g. random angles and platform lengths), and then evenly sub-dividing the space between the start and end locations of the pattern with these components. To then find a pattern close to the desired difficulty, the system adjusts the component parameters in the direction of steepest assent.

Cell Structure Decisions Patterns are generated for an initial cell. As the player reaches the outer limits of that cell, a new cell, or set of cells, is connected to it with one of the cell structures mentioned above. This new cell is populated with patterns through the previously described algorithm. Which cell structure to use is based on pre-determined values for the level, such as the level of desired branching. The direction and dimensions of the cell are based on physical constraints of the already developed space, as well as some degree of randomness.


# How to design a good overworld
[Zeldix](https://www.zeldix.net/) :: [Zelda III Hacking](https://www.zeldix.net/c1-zelda-iii-hacking) :: [General Discussion](https://www.zeldix.net/f44-general-discussion
https://www.zeldix.net/t2578-how-to-design-a-good-overworld

Conjecture

though think about it like designing a city or a neighborhood.  you need a major thoroughfare that you use to get around, some side streets that are a bit slower and more twisty, and various little "parks" for secrets to be hidden in.. etc  
  
think back to games that had an overworld you liked, play them again and identify what you liked and why.  use that to design your own.

# Overworld Design - r/gamedesign, 3yr ago
https://reddit.com/r/gamedesign/comments/oidux3/overworld_design/

Conjecture

An Overworld is partitioning stuff into regions.

Just start with the starting area and expend outward as needed, possibly in a spiral.

You can eventually refine it to be more cohesive once you have all the levels implemented and already have something to work with.

# How hub worlds shape game design - Wired, 2021
https://web.archive.org/web/20210824214408/https://www.wired.com/story/how-hub-worlds-shape-video-game-design/

theory

Considered to be one of the first stealth games (by _Guinness World Records_ of all things), the 1981 arcade game [_005_](https://web.archive.org/web/20210824214408/https://en.wikipedia.org/wiki/005) would also lay the foundation for what a hub is. Unlike overworlds that a character traverses between dungeons or missions, or a world that flows from start to finish like a single level or experience, hub worlds are generally one level that players often return to, and that then leads to other levels.

_Super Mario 64_, one of Mario’s first 3D platforming games, is also many gamer’s go-to for explaining what a hub world is. More than just a level selector, Princess Peach’s castle gives the player details and clues as to what happened before your arrival. But more than that, it gives the player a sense of mood for the levels outside of the hub. That midi-synthesized violin as you run along the bright, saturated reds and blues of the castle decor? It’s more than just a way to make loading easier and for levels to process faster. It’s also used to get the players into the right mindset and suspension of disbelief for the game. Martin Hollis, one of the developers at Rare who worked on the Nintendo 64 classic _GoldenEye,_ says the hub world in _Mario 64_ influenced their thinking on _GoldenEye_. Writing on a blog that can only be obtained through the [Wayback Machine](https://web.archive.org/web/20210824214408/https://web.archive.org/web/20110718160021/http://www.zoonami.com/briefing/2004-09-02.php), Hollis says “the idea for the huge variety of missions within a level came from _Super Mario 64.”_

In their paper “[Procedural Level Design for Platform Games](https://web.archive.org/web/20210824214408/https://users.soe.ucsc.edu/~michaelm/publications/compton-aiide2006.pdf),” programmers and researchers Kate Compton and Michael Mateas of the Georgia Institute of Technology used cell structures to describe how to implement nonlinear level design. One such design, as described in figure 2, refers to a “hub” design, where a central space then leads off to multiple other spaces that players can enter.

When referring to this cell design, they write, “The player chooses not only between the two paths, but the two possible destinations, which might lead a player to choose a harder-looking path with the expectation of a greater reward at the end.”

Aside from adventure games, platformers, and multiplayer games, hubs have been crucial to another genre: the dungeon crawler. Released last year, _Hades_ is a great example. [The game earned high praise](https://web.archive.org/web/20210824214408/https://www.wired.com/story/hades-review/) for the way it handles player death and its replayability, but also for its characters. [Based on Greek mythology](https://web.archive.org/web/20210824214408/https://www.wired.com/story/hades-ancient-greek-masculinity-classics-representation/), Hades uses its hub world to tell and develop the characters’ stories. But to do so, the characters’ story and dialog are mostly removed from the main game mechanics. Their story arcs and personalities are front and center for the player to experience, rather than shown through gameplay.

# Is there still a place for Overworlds in today's games? - r/gamedesign, 3 yr ago
https://www.reddit.com/r/gamedesign/comments/ptv4pk/is_there_still_a_place_for_overworlds_in_todays/

conjecture

  
I personally love overworlds and I really like ones that don't have random encounters like Lunar Eternal Blue Complete or Breath of Dragon III.

Imo the illusion of a bigger world by having an overworld just works for me.

Like, when there's a bunch of zones I don't quite get the geography of the entire world in my head right. Overworlds help me understand which cities border where and what continents are on what part of the world. It's visual reinforcement of the world I'm in.

I love overworlds. Too many games rely on massive open worlds that are ultimately empty. Having an overworlds allows a developer to make a more compact, but denser, open world. You get all the exploration of a true open world without all the boring travel.

Can't see why not. In a way, a lot of indies have these differences in scale (Battle Brothers), and even some bigger games, like XCOM 2. Sure, it's not the exact same implementation, but it's the same gist - the "largest map" in which your pawn represents your entire party traveling across vast distances.

Overworlds doesn't feel to me like a huge feature that sets a genre, really. If you are trying to target an older JRPG vibe, it might be an expected part of the aesthetic, but that's it. If you think your game is less linear than the final fantasies you mentioned, it might be a good feature to "let the players roam".

Now, if random battles aren't a important aspect of your systems, I wonder what do you gain by allowing overworld travel that you wouldn't gain via a node-like system, seen in most cRPGs, like Pillars of Eternity or Baldur's gate.

Does an overworld fit the vision of your game? This is the only question you should be asking. It doesn’t matter if you haven’t seen an overworld in twenty years. It doesn’t matter what all the _new_ games are doing. What matters is that you understand what you are trying to do with YOUR game. Does it fit your vision? You have to think about that. Like really think about it. But that is all. If you don’t have a vision you don’t have a game. You have a collection of ideas. Think about the benefits of an overworld. Making the world feel bigger without having to build the whole thing out. Giving reasons to have varied terrain without building in the transitions. Now apply that to your vision. Does it fit your goals? Yes? Then add an overworld.

An overworld is usually just a transit hub and a random encounter generator. It both makes the world feel larger and gives you the opportunity to inject a random, unbounded amount of encounters so you can technically always grind for XP/loot/materials/etc:.

Even without overworld encounters like in Chrono Trigger (unless I'm mis-remembering), overworlds make the world feel bigger and more lived-in. "Gameplay" screens are often things like a single floor in a single building, which often fails to give you a sense of scope to the whole world in which your game is set.

There is nothing about overworlds that is "obsolete", it's just a question of whether your game can make good use of them. Chrono Trigger would be **much** harder to navigate around if the whole thing were just a series of continuous main gameplay screens going from town to castle to mad scientist's lab or whatever rather than having overworld breaks. If anything, overworlds logically separate specific areas from one another without the player really noticing. It's an intuitive kind of separation.

A recent indie that made great use of its overworld IMO is **Phoenotopia: Awakening**. Its "levels" are side-scrolling, but its overworld is the usual overhead view. You can find somewhat hidden side areas by observing tiny little trails in the overworld. When you move from place to place, it feels like you actually went somewhere rather than screen transitioning abruptly from a farm to a giant city or whathaveyou.

An overworld's role in setting your game's context and displaying your world's scope can be pretty important for games that would benefit from it, including a lot of RPGs.

Take a look at Pathfinder: Kingmaker, which has a system similar to the old Realms of Arkadia. You have a big overworld where you see your party and get a choice in which direction you want to follow the road. Once you hit the next crossroads you can choose again, unlocking the map that way. You can even find hidden tracks, depending on your skills and have events which might affect your party (like crossing a river). It adds exploration and a sense of scale without having to animate and model all the stuff and boring players with endless walks through empty terrain.

# Jagged Alliance 3 Dev Diaries

https://community.jaggedalliance.com/index/dev-diaries/devdiary-2-legacy-and-writing-r4/
https://community.jaggedalliance.com/index/dev-diaries/devdiary-5-world-building-r9/
https://community.jaggedalliance.com/index/dev-diaries/devdiary-9-satellite-view-r13/

Gamedev


While it was followed by a small mission-based sequel that introduced multi-player gameplay (titled ‘Deadly Games’), the original game was preferred for its more open-world feel. This, along with many other aspects, was expanded upon in what became a more appropriate sequel to Jagged Alliance.

 Many of the characters that players grew to love from the previous games returned along with many new characters. One of the goals of the Jagged Alliance series was to create tension between the attachment to characters and the need to acquire more skilled team members.

## The World of Jagged Alliance 3

For those of you who haven't played the previous games back at the time, Jagged Alliance isn’t just another turn-based tactical game. It also features certain RPG elements that are its heart and soul. The player takes command of a weird company of mercs with all their differences, peculiarities, likes and dislikes, and not just a squad of replaceable carbon-copied soldiers.

That defined our approach to world building. We wanted to create a game that responds to your actions, characters that have their own agenda, and events that follow their own logic. You can try things, fool around and see what comes out of it.

It would be pity if they existed only as tactical background to battles, so we made sure to provide lots of little things to discover. Having a diverse mercenary team will open up possibilities - from just salvaging parts of wrecked equipment that can be used to improve the mercs’ weapons, to the whole complexity of a crime investigation.

We wanted to give players as much explicit and implicit choice as possible. But what is choice without a consequence? Ideally, the game would react to every decision you do and reward you with narrative or mechanical consequences - though this is not quite possible to guarantee. Freedom of choice comes with a price: the more branches a conversation or a mission provides, the less content we would be able to create in general. We solved this conundrum by weighing up the content case by case: there are minor encounters that just tell you a story - if you care to look closer; and there are huge quests that span across the map and involve multiple characters and sectors.

While building the world of Jagged Alliance 3, we aimed to deliver a realistic experience - and generally avoid fiction. However, time and again we had to go back to the confines of Mark Twain’s famous quote: “Truth is stranger than fiction, but it is because Fiction is obliged to stick to possibilities; Truth isn't.”

With regards to good old Mr. Twain, at times we allowed ourselves a bit of fun.

Soon enough it will be your turn as well to explore Grand Chien and see for yourself!

## Satellite View

  
The 90s were a golden age for PC strategy games. It is no wonder that both big tactical games from that era - XCOM and Jagged Alliance – featured not only excellent tactical combat but also a deep strategic element. For me this blend is one of the key ingredients for their success and my own fond memories of spending countless hours with them.

[![01_JA2.thumb.png.d5508504beabc7348a48ee151883a251.png](https://content.invisioncic.com/o315288/monthly_2023_06/01_JA2.thumb.png.d5508504beabc7348a48ee151883a251.png)  
Map of JA2](https://content.invisioncic.com/o315288/monthly_2023_06/01_JA2.png.0d2b6727c9309fac24af5d3181b04c9c.png)[![02_JA1.thumb.jpg.ab4a6ca9de6366a96c650139efc7fe8b.jpg](https://content.invisioncic.com/o315288/monthly_2023_06/02_JA1.thumb.jpg.ab4a6ca9de6366a96c650139efc7fe8b.jpg)  
Map of JA1](https://content.invisioncic.com/o315288/monthly_2023_06/02_JA1.jpg.a6faf7df1bb5ac6d76b259e45df2989b.jpg)

But what exactly is needed to make a fun and engaging strategic layer? And also, what makes a good strategic layer within the context of the Jagged Alliance series?

Strategic gameplay requires planning and tough decisions, managing different resources, be it money, time, or people. It also needs a big playground where these plans can unfold.

  
Welcome to the Adjani Valley – the world of Jagged Alliance 3. This is what we call the Satellite View – the strategic layer of the game where you will command your squads of mercenaries.

As is tradition set by the game’s predecessors, the world map is divided into a sector grid. More than 160 of these sectors (including underground locations) have their own playable, handcrafted maps to explore.

Certain sectors are more strategically important than others. They can be parts of a city, diamond mines, ports that allow sea and river travel, hospitals or just a safe place to rest and relax. Other sectors can be enemy strongholds that are heavily fortified and send out enemy squads to attack you (but more on that later). Liberating these sectors and taking control of vital resources is key for success. Planning which sectors to prioritize and where to attack next forms the core of your long-term strategy.

While it is completely possible to go through the entire game with a single squad I feel that the strategic aspect of Jagged Alliance 3 shines the most when you split the party.

You can send out Alpha squad to capture a diamond mine and secure funds. Bravo squad can go after a particular side mission on the other side of the Adjani River. While mercs in Charlie squad will train militia and repairs items in the town you recently liberated. Squads are limited to 6 mercs, but there are no limits to how many squads you can have or where you choose to send them.

  
**Operations & The Timeline**

It’s not all fighting, marching and resting for your mercs. In sectors under your control you can assign mercs to different operations. These are tasks that can help you recover after a difficult battle or prepare you for upcoming conflicts. Let me give you a quick overview of each key operation:

- **Treat Wounds** – assign a merc as a doctor to heal the wounds of his teammates by spending Meds
- **Hospital Treatment** – available only in certain sectors, hospitals allow you to heal wounds very quickly but at a high monetary cost
- **R&R** – In city sectors your mercs can spend some downtime to recover faster and even gain the “well rested” status
- **Repair Items** – weapons and armor deteriorate with use, mercs with good Mechanical skill can repair items at the cost of some Parts
- **Craft Ammo** & **Craft Explosives** – tied to the Explosives skill, allows crafting of different ammo and explosive ordinance
- **Scout Area** – Mercs can spend some time gathering intelligence of nearby area gaining hints about enemy positions as well as nearby side missions
- **Train Militia** – train militia to defend certain key positions. Militia are allied soldiers which are not directly under player control but can defend a sector even when mercs are not present
- **Train Mercs** – allows mercs with high stats to train other mercs with the speed

As we initially developed the Satellite View we stumbled on a problem that play testers were struggling with. It’s difficult to keep a mental picture of all these events and how they fit with each other. Which operation will finish first? When will a merc contract expire? Do I have time to get to a particular location?

The timeline was the answer to this problem – it helps keep track of different ops, merc contracts and provides a clear sense of how time flows in the game. Each operation, squad travel times and important occurrences are marked on the timeline. You can easily see the sequence of events that will take place in the near feature and hover over an event to gain more information.

Keeping mercs active in the field has ongoing costs – you have to renew contracts periodically. You can choose the time frame of the contract but there might be complications. A merc will occasionally want to renegotiate if they’ve gained experience and gone up a level. Some may require more money the first time you hire them if they see you as an inexperienced commander. Some may outright refuse to join your team if you have someone they don’t like on the payroll or if you’ve caused the death of too many mercs under your command.

  
With the contracts ticking away as time passes in the Satellite View you will want to optimize the time of your mercs. Chose which sectors to attack first as travel time is a factor, pick operations that will help you prepare but don’t waste too much time on them as there’s an implicit cost. Do you need to keep such a large force of mercs on payroll or could you even hire some additional help?


# Jagged Alliance 1 - [Jagged Alliance Wiki](https://jaggedalliance.fandom.com/) - started 2011

- A sprawling map divided into 60 sectors. Every sector on the map is filled with enemies and the map must be conquered sector by sector. in order to secure victory.
- Interactive environments and environmental conditions, such as bodies of water with [Metavira Eels](https://jaggedalliance.fandom.com/wiki/Metavira_Eels "Metavira Eels"), sweltering heat, and densely forested jungles provide an immersive tactical experience.
- A continually ticking day, that begins at sunrise (7 AM) and ends at sunset (7 PM). If your squad is caught in enemy territory when the sun goes down, they can be wounded or killed whilst retreating.
- Underhanded enemy tactics such as detonating buildings you are trying to capture or attempting to kidnap important NPCs means that tactics remain key both on macro and micro levels.

# Game Review - 2013
https://tactdb.blogspot.com/2013/12/jagged-alliance-2-privatized-low.html

Study

Players are limited by several factors including finances which are used in buying equipment, intelligence, and mercenary contracts, as well whatever local purchases that may crop up.  Not all mercenaries would be available for hire as a chunk would be on assignment for other employers.

- Vehicle Transportation; **JA2** featured a few logistical vehicle transportation such as Hummers and Helicopters.  These vehicles allowed squads to move across vast distances at much faster speeds.  The helicopter was the fastest vehicle but it was susceptible to enemy Surface to Air missile fire, which meant players had to undergo an operation to knock out enemy SAM Sites in the region before being able to fully use the helicopter in that particular area.  As a bonus the helicopter pilot would give you a recon report if he spotted enemies nearby the drop zone.  Ground vehicles required fuel which can be found throughout the country and the driver was the only person in the squad that had to be awake allowing the rest of your squad to rest up.  **Back in Action** had no vehicle transportation what so ever.

---
[^1]:Friedman, Brett. On Operations: Operational Art and Military Disciplines. Naval Institute Press. Kindle Edition. 
[^2]: https://en.wikipedia.org/wiki/Battle
[^3]:Isserson, Brigade Commander Georgii Samoilovich . The Evolution of Operational Art. Kindle Edition. 