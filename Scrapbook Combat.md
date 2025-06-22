https://phys.org/news/2024-10-reveals-mammal-evolution-sprawling-upright.amp
Sprawling
Semi upright
Upright

# Dice

2pt6
2pb6

Pick top pick bottom

---

- [ ] #resource Song of Blade and Heroes
And so I tried Song of Blade and Heroes

Sometime you don't want to play epic-scaled battles on big tables with a 100 models. Sometime you want to relax with simple rules, a bunch of miniatures on a small kitchen table for about 30 minutes.
Sometime you would like to play SoBaH.

Song of Blade and Heroes is a minimalistic skirmish game with unrestricted model range plus community driven supplements.

How does it play ? 
Unit profiles have 3 characteristics : a point value, a quality value (morale/discipline/initiative, etc), and a combat value. They also have special rules like move distance, range attacks, magic, size, etc.
During your turn you try to activate each model. You chose to roll 1, 2 or 3 dices. Each dice scoring equal or above the quality value of the model is a success. For each success, your model can make an action (you are allowed to take the same action multiple times). If you roll a failure, one enemy model can take an action (after you do). If you roll 2 failures or more, your turn ends and the adversary can play. This makes for very fast paced games and a lot of interaction between players. It represents one's ability to seize the initiative in the chaos of battle. Some units will activate more often but with less impact than big bruisers.

Combat is simple and deadly. Both fighters roll 1d6 and add their combat value. If one scores twice as much as the other, the loser instantly dies. If the winner rolls thrice as much as the loser, they make a gruesome kill causing morale testing for all enemy witnesses. You don't need to burden yourself with HP tracking and positioning is vital as allied support and terrain advantage can make a big difference.

Movement can be intriguing but makes terrain and positioning very important. There are 3 distances : short, medium and long. Unless stated otherwise you move at medium in straight line. No turning and obstacles stop your movement. If you want to change direction or cross an obstacle, you need an additional move action, provided you scored enough activation successes.

This is most of the rules and I won't go deeper. There are advanced rules with equipment details and even profile creation to fully customize your troops. There also exists rules for campaign and even a dungeon crawling rpg mode.
I really like it and plan to use it as a Mordheim replacement.



interstitial spaces

---

# terrain discovery system
Players can introduce their own terrain 

#candidate storytelling type
- storytelling kudos are granted for good roleplay, which can be cashed in for terrain points.
- roll, or use terrain points for successes.
- Each success means a higher subjective terrain value

#candidate competitive type
- roll only
- success or failure determines the terrain's subjective value

#candidate scarce resource type
- each team has one terrain point to add. Any additional terrain requires a roll. If the roll fails, the team is barred from discovering any more terrain

--- 

# Canalization factor
some places have terrain bottlenecks harder to roll for features or impossible to add. 
Examples of hard canals: a bridge, a valley
Examples of soft canals: tight forest
- if the GM says no, the Terrain point is refunded
- maximum discoverable terrain piece?


#candidate Using reconnaissance, players can get a trickle of terrain points to use, plus one potential roll for every zone

reconnaissance grants a roll of terrain points per hour (can be rushed at penalty). The margin of success determines how many are gained.

terrain points are shared with the team.

terrain points may never remove a piece of terrain

#candidate terrain features may never be placed between an enemy force if it would block line of sight.

Terrain points may be expended at any time, but are placed a minimum of 1 move action away. 

If a player wishes to, they can place terrain more than 1 move action away for a discount of 1 terrain point per move action.

The value of terrain is subjective, but a rule of thumb is that the most valuable terrain feature is cover: if a terrain feature offers complete cover for a distance of 1 move action, that terrain should cost 5 points. The least valuable would be a feature that offers concealment for one or two people, which should cost 1 point.

Because some features are rarer in certain terrains, the cost of a terrain feature may be modified by its rarity.
## time it takes to traverse the interior of an area

area 
pattern width
speed

time = a/w/s




![[Pasted image 20241126071020.png]]

![[Pasted image 20241126071037.png]]
![[Pasted image 20241126071116.png]]
![[Pasted image 20241126071152.png]]

what if teams had unmarked counters to represent every unit in LOS, but the GM had an invisible nametag that specified their actual name?

![[Pasted image 20241126071711.png]]
![[Pasted image 20241126072108.png]]
![[Pasted image 20241126072201.png]] 
Scan area should be called scan WIDTH.

![[Pasted image 20241126073056.png]]
![[Pasted image 20241126073140.png]]
![[Pasted image 20241126073249.png]]
![[Pasted image 20241126073325.png]]
![[Pasted image 20241126073454.png]]
![[Pasted image 20241126073535.png]]


# ideas for the commission
- Legendary relics
- legend of a famous character
- 


# random stuff


use speed as initiative for operational scale things?

Responders

flick flak spider
# Collecting modern RPG theory

https://forum.rpg.net/index.php?threads/are-there-any-proper-collections-of-modern-rpg-theory.876445/

https://www.enworld.org/threads/why-jargon-is-bad-and-some-modern-resources-for-rpg-theory.689000/

# Operational terrain generation

encounter generation methodologies
- object-oriented: the game's narrative is laid around an already defined terrain. Also known as terrain-pulled story generation
	- +better boundary management
	- +increases player challenge, improves tension and variety
	- -harder to scale
	- -loss of story control
- narrative driven: terrain is defined by the outcome of the narrative. Also known as story-pushed terrain generation.
	- +supports and rewards improvisation
	- +maximizes communal story telling
	- -harder to manage boundaries ; can lead to too much player agency
	- -requires logging, jit planning for consistency
	- -reduces terrain to an outcome instead of an independent obstacle
	- -terrain has a multidimensional value unlike a die result



Requirements for good operational scenes
- progression - if it ends, it should end with impact
- Tension - the outcome must be in flux
- Variety - the nodes must develop on the plot beats, allowing exploration, variation, or change. too much [repetition](https://en.wikipedia.org/wiki/Repetition_(music)#.) is bad, so might too little
- Agency - player decisions should change outcomes


# ProcGen



https://medium.com/@gadhvirushiraj/the-fascinating-world-of-perlin-noise-terrain-generation-cec7f5a28fa0

https://github.com/dandrino/terrain-erosion-3-ways

https://fate-srd.com/fate-codex/rethinking-stealth



```
Yes it is possible by using erosion algoritms.

Perlin noise is good as base, but you will not get realistic mountains with it alone.

[https://hal.inria.fr/hal-01262376/document](https://hal.inria.fr/hal-01262376/document)

May be this will hint to more information.

[https://filipalexjoel.wordpress.com/](https://filipalexjoel.wordpress.com/)

Some more.

Basically in nature multiple conditions would form shapes of mountains or cliffs.

You can try to simulate wind or hydraulic erosion, tectonics.
```

```
You're definitely on the right track with the concept of stacking (layering, blending) noise channels to achieve your desired outcome. It's not the most intuitive way to think about building complex terrain, but it's by far the easiest to turn into predictable, tweakable, expandable code.
```

```
  
Actual real-world terrain, however, is shaped to a great extent by erosion. Simulating erosion in a computer tends to be horrifyingly expensive compared to most PCG techniques. Generating eroded terrain across an infinite map is even harder (you'd probably have to chop up the map into finite-sized continents).

Depending on what you're doing, you _probably_ don't need to actually simulate erosion. There are some tricks for producing patterns that look like eroded terrain at much lower computational costs. If you need the terrain to look eroded, I'd start by thinking about those. If you _don't_ need the terrain to look eroded, then just don't worry about it and find some other algorithms that give nice results. (You mentioned elsewhere in the thread that you have roughly a 5km square, that's good, most of the interesting features of eroded terrain don't really show up on such a small scale so it's easier to get away with fudging it.)
```

```
You can get cliffs by sending a continuous noisefield through a 'stepping' formula (basically turns gradients into rounded staircases). You can layer up noisefields and have high ones poke up through lower ones to create discontinuities between terrain features. Various cliffs, ridges, valleys, etc can be produced this way. You can also leverage Voronoi techniques to get discontinuities in the terrain and generate features with particular shapes (such as adding circular volcanoes to underlying terrain, and so on). Most of these algorithms can be parameterized, so you can change up the aesthetic style in different maps, or even use noisefields to create continuously blending changes in aesthetic styles on the same map.
```



# Operational Stealth Gameplay

https://www.rpg.net/reviews/archive/classic/rev_2675.phtml

https://forum.rpg.net/index.php?threads/recommend-a-stealth-rpg-like-thief-tdp-metal-gear-tenchu.872801/

https://fate-srd.com/fate-codex/rethinking-stealth


# Strategic

https://www.campaignmastery.com/blog/structuring-campaign-flow/


# Operational gameplay requirements

important books:

- Night’s Black Agents
- Blades in the Dark
- Black Seven
- 

https://www.reddit.com/r/rpg/comments/19dixhq/what_makes_chase_sequences_good/

---

I find any chase scene needs to not be just about rolling for initiative then athletics then see if you take damage.

That's just attrition chipping away HP or whatever.

Chase scenes need phases and each phase changes the narrative a bit and you might want to plan out a handful of "events" that could happen. Like say it's a fantasy game and the heroes are in a wagon speeding down the road and behind them are furious centaurs with bows.

One element of that is "what do they need to roll to stay ahead of the centaurs. The dice exist to add tension. A failed roll shouldn't mean the chase is over. It should mean the centaurs are gaining and the danger is increased.

---

  

I believe Blades in the Dark has it about exactly how I prefer Chases. My two most interesting aspects are player creativity and hard choices (how much are you willing to pay for success).

Using just a Progress Clock means how the player decide to fill it is up to them. They aren't just looking at a static list of options and picking the one they are best at rolling or some other closed off mini-game. This is where they can take Actions/Skills and choose the ones that can be rewarded with increased Effect (filling the Clock faster) or a safer Position (costing less) for smart/creative and novel play. And because every Action Roll you take has that risk, its up to them to decide on how much they are willing to pay for success.

I really haven't seen Chase Mechanics I like better than a simple Progress Clock with flexible ways for a PC to interact to filling them. Its where there is a lot of collaborative storytelling so creativity matters the most.

  

Chase scenes are a horror staple for a reason. If you are running away from something, it is because you genuinely do not want the thing to catch you. Good chases start with the players saying they want to run, because the alternative is death or worse. 

Next, you need mechanics that allow everyone in the group to do something, even if someone leads the chase, you need to allow for side activities like dropping food or treasures to distract or creating obstacles.



---

Tabletop optimization and design

aptitudinal approach, or intuitive
Didactic approach, or constructive 

Melodramatic architecture

Movies have limited budgets and audiences have limited time to enjoy a movie. Directors planning to depict complex institutions or situations often turn to the use of simplification or exaggeration to fit the entire object into the shot.

For example, a military convoy tends to be highly condensed in a movie shot because attempting to depict the scene naturalisticly would make for a difficult scene. This is in spite of the fact had in real life these vehicles may be dangerously close.

Likewise, placing a federal government in a scene would be hard without condensing the scene, such as all of it inside of all of it it existinv in a single large room.

# animal behavior guidance


animal interactions cam be characterized into six types: competition, predation, commensalism, mutualism, parasitism, and curiosity.

# travel

### design discussion

Design discussion:
- irl, meeting engagements are a matter of how long you have to prep for a dynamic situation like a fight. We call this prep distance or time standoff
- it is a problem with multiple parameters like
- - ooda(init) - standoff
- - perception - how much data is received
- - communication
- - Concealment
- - group dynamics

Standoff can either be distance or time in a scaled increment. 

As an analog game we can manage a limited set of dimensions.

the multiparameter model of ab13 is multitask only - split dice pools are not synergistic.

For the purposes of this well need to ignore synergism (unless we do perception x ooda) and modelling communication. We ignore group dynamics by picking who's closest to the incident (point man rule).

We could also ignore modeling vision quality, such as distance

One candidate is ooda only. Success at the ooda roll determines how the amount of standoff. Failing the ooda roll means 0 standoff (hard fail)

Another candidate is ooda with standoff determined by perception

Another option is a multidimensional roll of ooda and perception, added together. The value determines standoff.

### data
Data in ooda is usually based around prediction and vision.

Data has 2 considerations 
- detection - the presence and location of an object
- recognition - determining the meaning of that object through patterns

Data also has several related terms
- entropy: the lack of data
- prediction: the ability to recognize meaning faster
- information: data that is fully interpreted

One candidate is to understand perception as a 1D likert scale that is interpreted by the gm

1 could be detection
5 could be recognition


Problem with this is that detection becomes unnecessarily strong: there is no room for subconscious awareness as needed by a Stealth game. 

Candidate 2: Number of facts
- reduction of ambiguity
- direct or indirect info
- Saliency
- can the players know if this is a good or bad thing?

- 


candidate 2: poor facts, good facts

However, the quantity of a fact is subjective

# Node based

Incidents are both time based and location based in a node graph layout.

Node graph

All sides make a turn simultaneously

Stage 1 travel: all forces move one node per turn

Stage 2 travel: distances are in hours (100 km to the hour). Nodes are scaled to a default length of time. Waypoints that are unmarked are assumed to be the scale away in distance.  If a group can travel faster, then they may move more turns. 

Numbered Nodes have unique times.

Every turn is the default time scale. 
## waypoints
## waypoint elements

Nodes have default values

Their terrain is specified by the topo map underneath

They are keyed to identifiable features (areas, landmarks, etc)

## types of values
- (Traffickability)
- Concealment
- cover
- area
- height

## quality types
- terrain
- 

## generating waypoints

A choice of one waypoint is a path. Ignore it or treat it as an encounter

A choice of more than one waypoint is a fork. The recommended absolute maximum number of branches is 6, the recommended number is 2.

Each waypoint path should have as high a contrast as the gm can develop. This is not always possible, but try.

Subpaths are distinctive variants of a path which are not visible on the graph. These variations are usually modified versions of the original path, usually changing in magnitude.

![[Drawing 2025-04-23 12.07.17.excalidraw]]



# periodicity of movement

the fraction of a combat distance that can be moved

a tick lasts between .1 and .5 seconds, averaging .3

| Speed/move | Value (m/m) | Average | Top |
| ---------- | ----------- | ------- | --- |
| Sprint     | 10+(mus/2)  | 13      | 16  |
| Run        | 8+(mus/3)   | 10      | 12  |
| Trot       | 6+(mus/4)   | 7.5     | 9   |
| Walk       | 4           | 4       | 4   |
| Stagger    | 2           | 2       | 2   |
| Crawl      | 1           | 1       | 1   |
|            |             |         |     |
Move is 5 ticks, 1.5 seconds

| **Speed/second** | **Average (m/s)** | Avg **m/exchange** | Avg **m/pause** | Top m/pause |
| ---------------- | ----------------- | ------------------ | --------------- | ----------- |
| Sprint           | 8.67              | 86.7               | 520             | 640         |
| Run              | 6.67              | 66.7               | 400             | 480         |
| Trot             | 5                 | 50                 | 300             | 360         |
| Walk             | 2.67              | 26.7               | 160.2           | 160.2       |
| Stagger          | 1.333             | 13.33              | 79.98           | 79.98       |
| Crawl            | 2/3               | 6.67               | 40.02           | 40.02       |
|                  |                   |                    |                 |             |

exchanges of fire rarely last more than 10 seconds
pauses last about a minute, so they are 6 exchanges in length

| distance | awalk period(300m/p) | a.run period(500 m/p) | T.run (640/p) |
| -------- | -------------------- | --------------------- | ------------- |
| 100      | <1                   | <1                    | <1            |
| 200      | <1                   | <1                    | <1            |
| 400      | 1.333                | <1                    | <1            |
| 800      | 2.667                | 1.6                   | 1.25          |
| 1600     | 5.333                | 3.2                   | 2.5           |
| 3200     | 10.667               | 6.4                   | 5             |

recommendations: 
- keep distances close to 3 times the character's expected speed per tactical pause for optimal math; 
- round results for ease - if a character lands on a decimal fraction, there is enough room to start a tactical exchange, but operational actions only get resolved at the end of the tactical exchange
- If you want the characters to sprint, double the periods.

---

The Cooper test (developed by an American PhD) consists of running as long a distance as possible in 12 minutes. As already indicated, the maximum aerobic speed can only be maintained for 4 to 6 minutes, so the half Cooper, which lasts 6 minutes, is more accurate.

distance
`INPUT[number:distance]` meters
pace per minute
a `INPUT[number:a]` : `VIEW[round({distance}/{a},2)][math]` turns
b `INPUT[number:b]` : `VIEW[round({distance}/{b},2)][math]` turns
c `INPUT[number:c]` : `VIEW[round({distance}/{c},2)][math]` turns
d `INPUT[number:d]` : `VIEW[round({distance}/{d},2)][math]` turns
3 `INPUT[number:e]` : `VIEW[round({distance}/{e},2)][math]` turns

kph
`INPUT[number:kilo]`
`VIEW[round({kilo}* 0.2777777778*1.5,2)]` meters per tick;`VIEW[round({kilo}* 0.2777777778*1.5*5,2)]` meter move
`VIEW[round({kilo}*16.66666667,2)]`meters per minute
`VIEW[round({kilo}* 0.2777777778,2)]`meters per second

 

### 1. How long can the average person run before getting tired?

The average person can run for approximately **10-15 minutes** before experiencing fatigue and needing to slow down or stop. This varies based on fitness level, training, and overall health.

A character can sprint for one pause before needing to test for exertion or slow down

characters can run (trot?) for 10 pauses before needing to test for exertion.

An exertion test is an attribute test. On success, the character may continue exerting; On failure, the character takes temporary attribute damage equal to the margin of failure that requires one hour rest. If the temporary attribute damage overflows the character's health, they take permanent damage instead.

For more information on Attribute damage, see [section x]

Each successive exertion test adds a -1 penalty.



# Section x

if a character has an attribute temporarily knocked down to 0, they pass out.

# ideas
what about attribute damage with timers associated with them?

Tag the damage with the requirements to disperse it, such as rest or healing

that way, all damage has a similar type, but is addressed differently


---
This duel is reminiscent of an old west duel, the drama isn't from flashy swordplay or gunfight, it comes the buildup, the anticipation, and then finally, the payoff as the duel ends as soon as it begins, short and simple, no flashy gimmicks, just three simple movements, and its all over.

fast ttk would be more about the above
# TW13 initiative software
- https://en.wikipedia.org/wiki/Flight_progress_strip

# Examples
- https://www.google.com/search?q=+flight+strip+github
- https://github.com/sslazio1900/AuroraFlightStripPrinter
- https://github.com/AntiFaffStrips/Strips
- https://github.com/KingfuChan/Flight-Strip-Manager-cpp
- https://github.com/KingfuChan/Flight-Strip-Manager
- https://github.com/AlexVialaBellander/efss



---
# Stability

rating from 1 to 10

Actions have a stability factor:
- If you are above that actions stability score, no change occurs
- if you are below, your stability worsens
- some actions always reduce stability. This stacks with the under stability penalty


# resources to build in a fight
- control
- stability

# resources to manage in a fight
- energy
- 


---

# Wilderness Crawl


Jojiro — Today at 8:13 AM
Random opinion: procedural travel with a set, finite set of actions, is way more engaging than open-ended travel with an infinite range of actions. Especially for city-crawling/dungeon-crawling, but I also feel this for wilderness crawls.
@Izzy | Hippogriff Enthusiast I know you've been thinking about this quite a bit, but yeah, this is a recent opinion of mine that's solidified in response to the current 5e game I'm in.
Toyo | Prompt 📌 in homebrew! — Today at 8:17 AM
sometimes tactical infinity is exhausting
Jojiro — Today at 8:19 AM
This isn't so much about that, right
With travel procedures, there are just a lot of potential distractions
Tamms — Today at 8:21 AM
I'll do you one better: procedural travel with an acknowledged finite range of rewarding actions is better than open-ended travel with an infinite unrewarding range of actions.
Jojiro — Today at 8:22 AM
GM: What would you like to do?
Player: I would like to dig a hole
GM: Why
Player: Just cuz, I guess. Sometimes when you travel you just...I dunno. Get bored and dig a hole
Tamms — Today at 8:23 AM
Mostly the same thing, but more about a range of reward than a list of reward.
Jojiro — Today at 8:23 AM
I think the idea of classifying individual actions/mechanics as "rewarding/unrewarding" is a bit of a red herring that sounds reasonable, but can lead you down a very gacha-game sort of design mentality.
I'm more interested in whether game loops generate engagement than if every single thing comprising a game loop is rewarding.
So I think that increased specificity isn't actually better, personally.
Tamms — Today at 8:24 AM
To be clear, I'm actually referring to this from a player perspective.
Jojiro — Today at 8:24 AM
Me too, in this instance.
But yeah my main thing here is noting a play habit I dislike, not so much trying to nail down best practices.
And the play habit I dislike is doing random behaviors in an attempt to add depth to an infinite range of actions, when that infinite range sort of...doesn't help constrain you to any particular play pattern or even provide guidance on how the game is meant to work.
So you can "grief" without intending to, because of that infinity.
Tamms — Today at 8:25 AM
Yeah, I fully agree with that. I think the "rewarding/unrewarding" is less about a tangible in-game reward and more about engagement, as you said.
SVKのLiQuiDaToR — Today at 8:26 AM
For two months and counting, the most rewarding thing for like half my party was finding a broken Immovable Rod I had in my handy "random trash for loot goblins" list
None of them even know what an Immovable Rod is, but they still enjoy whipping out "the horse stick" each session whenever a confounding problem arises, and giving the button a press just in case 
Tamms — Today at 8:28 AM
How I would describe my specific statement in a game context is that I know I will not be rewarded with engagement by digging a hole. I also know I will be rewarded with engagement by actions that fit within a range (defined by the campaign) of something that makes progress in some way.
I actually came up with a great parallel. You know those old text-based games where you could tell it to do something and it would say something like "You [what you just said]"?
PC: "I dig a hole."
DM: "You dig a hole."
PC: "I stand in the hole."
DM: "You stand in the hole."

Just shoot me, regardless of where I am in that situation. Most of all if I'm the one standing in the hole.
Jojiro — Today at 8:34 AM
In those old games I think most of the time it tells you that you can't do the thing, if it isn't relevant XD
Maus — Today at 8:36 AM
Just shoot me, regardless of where I am in that situation. Most of all if I'm the one standing in the hole.
man this just got Kafkaesque fast
SVKのLiQuiDaToR — Today at 8:37 AM
Did they at least get blasted by True Polymorph into a Giant Beetle tho
Maus — Today at 8:38 AM
"For the crimes of unrewarding behavior against the state and against the dungeon master, you have been sentenced to summary liquidation. You get in the hole."
Tamms — Today at 8:39 AM
Having the benefits of illusion of choice, with the context that choice guarantees nothing about results, is the sweet spot for me. 
Maus — Today at 8:48 AM
On a side note, this conversation is quite interesting because I've been working on a project that tries to deal with this situation as well as pass my formal grammars class, which I think would be a pretty good methodology for this context.

Formal grammars is a branch of logic that studies theoretical state machines like computers.
in this case what's going on is that you are trying to reject input that has no practical value from the gameplay in order to avoid wasting time on ambiguous or unhandled behavior.
Tamms — Today at 8:52 AM
That's what I was about to ask.
"In the context of the game, your request is nonsense and does nothing."
Maus — Today at 8:59 AM
tl;dr on it is that English is a language that is highly ambiguous compared to formal syntax because there are multiple ways to generate the same exact output. Furthermore, what this would do is effectively digitize your I/O stream into a set of allowed vocabulary for the object you're inputting/outputting - storytelling - that many consider has analog properties.

After all, story is made of an infinite variety of possibilities, many of them ambiguous or nonlinear. 
Tamms — Today at 9:11 AM
English being ambiguous, whaaaat?

wording a specific sentence of homebrew for 25 minutes
AnthonycHero — Today at 9:32 AM
But what else do you expect?

If your action has purpose and it's not immediately clear, you should specify it. When it's a whole system, I agree with Jojiro that there should be a procedure to set some boundaries so you don't need to specify your purpose every time. Everyone understands the purpose of making an attack against a monster or trying to open a locked door, but not all actions share this privilege in a vacuum.
Tamms — Today at 9:36 AM
To be clear, I'm on the side against that interaction even occurring in the first place. My view slightly deviates, though, in the sense that I believe the players should be able to meaningfully deceive themselves to believing they have free will that is confined to a specific range of actions. I'm not entirely sure if that's what Joji indirectly meant or not, though, as compared to set actions.
Jojiro — Today at 9:36 AM
I mean, I think for Wilderness Crawls for instance, this isn't quite a "solved science" - there are lots of procedures and people don't universally gravitate towards one.

But for Dungeon Crawls, having specific party and individual actions (taken from Basic/Expert D&D, the version before D&D 1st Edition), has made my dungeoneering experiences so much better that it's like night-and-day. It turns them into their own small ecosystem of gaming actions, and when I play with GMs that just do "freeform" dungeon exploration 5e as a player, it's excruciating how much time we waste on just faffing about, because there isn't that structure or guidance with default 5e gameplay assumptions.
(As well as how much time we end up dedicating to random, improvised asides that have very little to do with characterization OR dungeon crawling, just sort of mini improv scenes that happen when the GM is put on the spot because a player does something really out of left field)
Hit — Today at 9:37 AM
Honestly that's just DnD to me now
All the asides and improv is a part of it in my brain
Tamms — Today at 9:38 AM
I also may need to clarify what I mean by "range", because I just realized the way I mean it is not apparent, and is more akin to a "range of vision". 
AnthonycHero — Today at 9:38 AM
The reality, though, is that no travel is ever completely open-ended with an infinite range of actions.

You're trying to reach a certain point on a map. There may be some roads, or an obstacle, or you choose to follow the straighest route possible. You may want to check another location on the way if you know it's there, but on a blank map what else can you do other than just moving in the most direct route possible? Even not taking the most direct route is the same as doing it except perhaps for the time you want to invest into the travel itself, and that's the only difference: one single variable. Every time you add any point to the map you add one variable.

Now sure enough after the route is set the procedure starts and some random tables may be involved, but even then the outcomes are finite and set in advance. You may get lost and lose a few hours; you may encounter something that gives you a new hint, a piece of loot, a nice view or just again makes you lose a few hours. Everything is already there though.
AnthonycHero — Today at 9:39 AM
I mean digging a hole could have all sort of reasons. Even if it's just to crack a joke. The problem comes with not engaging with the game here not with the unpredicted choice of digging a hole 
Jojiro — Today at 9:39 AM
I don't mean infinite here as in, "might take infinitely long" or "encompassing the vastness of human experience".
I merely mean, a conceptual blank canvas upon which you can exert any action, rather than a delineated set of actions to solve an equally delineated set of challenges.
Put simply, I prefer having expectations be clear on both sides - and that clarity doesn't have to happen within the rules. It can happen organically, or as a result of everyone playing in similar types of tables and thus sharing play cultures, as well.
Jojiro — Today at 9:41 AM
Yeah to me improv that is challenge-independent and characterization-independent is not D&D, but rather "a distraction".
So one or both of those (ideally) need to be present for me to feel like I'm getting The Experience™️
AnthonycHero — Today at 9:42 AM
Ah well yes that helps with consistency. Exploring a room takes X time, moving from a room to another causes X, etc.

BTW this reminds me that I've delayed reading B/X far too long
Tamms — Today at 9:43 AM
Correct, which is what I'm trying to get at. Digging a hole is something that sits outside of the "range of rewards", so I as the player should be aware that no meaningful results will come about from me doing it. Therefore, there is acknowledgement that me digging the hole does not warrant any focus. If I follow-up digging the hole with an action relating to the hole that does sit in the "range of rewards", focus may be warranted on that specific action.
AnthonycHero — Today at 9:46 AM
I don't agree. Digging a hole is a tool just as much as tying a rope is. It just doesn't hold value on its own. Your example to me sounds like someone having thieves' tools and using them on a locked chest they themselves locked in the middle of a dungeon. Why would you do that? But that doesn't invalidate unlocking locks in itself as an action
Jojiro — Today at 9:46 AM
I think with Wilderness, part of the reason why over 30 drafts of procedures still hasn't "solved" for a Wilderness procedure that is popular is because it's harder to decide what is and isn't valid engagement with the game. With a dungeon, it's easier to say "okay, don't just try and dig a hole randomly". With the wilderness, it is more difficult to say "never dig, that's not part of the wilderness experience", because we can so easily imagine situations where it could be part of that experience.

And even if one were strict enough to get rid of that, there are a whole array of activities that become less and less obviously part of the "excise" or "keep" group.

Foraging, for example, isn't found in every wilderness procedure, but it's unclear without considering and analyzing a whole system whether its inclusion or exclusion is wise. And analyzing whole systems, from the perspective of the average D&D player, takes so much play time that most aren't able to do it, except for discrete units that repeat a lot.

Combat repeats a lot, so it's easier to understand for a layperson. Dungeons repeat a fair bit if you make regular use of them, and also have clear win conditions (get treasure, kill bosses). 

Wilderness not only tends to not repeat itself, it varies by biome, has a condition that feels somewhat inevitable (get from A to B), and feels like you have less control.
BUT
I still say that my preferences are the same across all of these: I prefer that finite and delineated set of actions for everything.

It's just, I acknowledge it's way harder to make a "comfortable" set for some aspects of D&D than others.
Tamms — Today at 9:47 AM
I don't think you are understanding what I'm trying to get at with the hole example. It's not about the hole itself, but the point Jojiro made about players taking actions and expecting there to be some sort of meaningful response from the DM.
AnthonycHero — Today at 9:48 AM
And I did answer to that. My answer is that players should put intent into their actions, not the DM.
Tamms — Today at 9:49 AM
My problem is that even with intent, it shouldn't always warrant a meanginful response.
The digging a hole and standing in it was with the context of a meaningless purpose like standing in the hole; they fulfilled their intent. 
AnthonycHero — Today at 9:50 AM
Even just "I enter the room" has set me back sometimes as a DM, and it's such a simple action.

Are you just walking there casually? Are you peeking around corners and moving carefully? Are you swatting the room trying to catch someone off-guard?
AnthonycHero — Today at 9:51 AM
Well, yes, but if the response is not meaningful then it's not needed.

Player 1: "I dig a hole and sit in there."
DM: "Ok. Player 2?"
Tamms — Today at 9:53 AM
Which is very fair and I wish was something people found more acceptable, though that type of response can have Player 1 interrupting to say that they want to do something else in the hole, which is debatably better or worse depending on length.
Maus — Today at 9:53 AM
Digging a hole is something that sits outside of the "range of rewards"
What issue I see is

your problem is that the list of valid actions possible isn't the same thing as the list of meaningful actions. Taking from the example of formal grammars above, you're mixing syntax and semantics. For example, "the colorless green harpy gracefully prognosticates on the lazy dog" may be a valid sentence syntactically, but it's quite clearly gibberish. In contrast, you can perhaps see an example where a PC digs a foxhole in order to create a punji trap. Limiting the syntax can be massive overkill for what your issue is.
 
Therefore, your issue isn't necessarily the syntax, but it's whether it actually means something.
AnthonycHero — Today at 9:55 AM
If Player 1 is just trying to waste everybody's time then it's a whole different point that can't really be addressed by the rules (or procedures) of the game. They will always find a way to waste everybody's time. If Player 1 just wants to add color to a scene or take a moment to characterize their character, I see no issue with it.

The fact they're sitting in a hole may or may not come up again when something else happens, but it can be set aside for now.
Maus — Today at 9:56 AM
Furthermore, there are situations in tabletop games where PCs are challenged on their decisionmaking. This can clearly include situations where players make wrong decisions which waste some of their IC time.
Doesn't mean that limiting syntax shouldn't ever be done, but it does play a significant role in changing how your game performs: You lose something in the process 
Tamms — Today at 9:59 AM
Correct. It has nothing to do with the hole, nor with the player intention, but with what meaningful response can be given that actually moves the gamestate forwards. Even setting up a punji trap can be meaningless if you are setting it up on the side of the road "just because" and then leaving.

The original "hole" example made by Joji includes a lack of meaningful actions on the part of the player.
⁠general_dnd⁠

It's also worth mentioning that I've never been discussing this in the context of the system solving it, but Joji might have been. 
AnthonycHero — Today at 9:59 AM
I'm not sure it's that hard. Travel mostly boils down to:
Where do you want to go?
Which way you choose?
Do you manage to stay on your path?
And eventually, food runs out or the day is almost over, so you need to forage/camp.
Jojiro — Today at 10:00 AM
It's not difficult to run, but nobody has yet made a procedure that has anything approaching universal adoption
While for combat and dungeon engines, there are popular ones people love.
That's all I'm saying.
Maus — Today at 10:00 AM
 if you are setting it up on the side of the road "just because" and then leaving.
The peasants need to be afraid of their superiors
lawfulevil.digahole
AnthonycHero — Today at 10:00 AM
There's no such thing for dungeons either as far as I'm aware, because the amount of complications people want are different
AnthonycHero — Today at 10:02 AM
I think nobody has made the system as entertaining as it could yet, yes. I also think this doesn't come from a lack of clarity in regards to what constitutes a set of valid actions for traveling. Those are not mutually exclusive.
Maus — Today at 10:03 AM
well there's two definitions of universal that we can use here
universal as in popular
universal as in handles every single possible important input
AnthonycHero — Today at 10:04 AM
I think most people treat travel by not treating it in this day and age, because they're more interested in what happens at the different locations you're traveling from/to. This is my perception. I've read 5e traveling procedure carefully and I've thought about implementing it at some point to make my ranger player happy. I didn't because there's always something else I'd rather have my players do so we just skipped travel most of the time.

I think I've rolled on weather once to know how much time it would take to reach some point with a boat because they were on a time limit and that's it.
Maus — Today at 10:05 AM
1 is ephemeral, because it's all down to what people are interested in

2 is impossible as far as I understand formal grammar.
Tamms — Today at 10:07 AM
The specific reason I'm focusing on the players having the illusion of freedom within that range of rewards is that I believe it causes people to engage in the world in a more authentic way. In reality, certain actions are mind-numbingly boring, and certain actions are so nonsensical that there's no meaningful reason or response from doing them. With that said, there may be times in which a characterization quirk makes sense to be showcased, so should be done in a way that isn't massively drawing focus in the context of time investment.
AnthonycHero — Today at 10:09 AM
I can't really answer about that. As a player I mostly care about rolling dice and getting to know what happens next really. I'm more interested in the topic as a DM
Maus — Today at 10:10 AM
the problem is that you're asking for what is essentially an algorithm that decides what is not meaningful for the GM when that isn't really decidable based on syntax alone without limiting the full range of meaningful actions. 
if a person figures this out they may feel shoehorned into a limited set of actions
Tamms — Today at 10:11 AM
Oh, I'm not asking for an algorithm at all, which is why I view it as a "range of vision."
It's less of a codified thing and more of a framework for thought.
It's meant to be philosophical/psychological, compared to mechanical.
The original context was "player behaviors", after all.
Maus — Today at 10:13 AM
well, in technical terms an algorithm is just a set of instructions that decides what action to take next.

To devise a list of whitelisted actions is to set instructions on the only valid inputs in the game.
Perhaps it would be better to create a list of preferred actions, ones that are valued far more than the others. 
Tamms — Today at 10:14 AM
This is exactly why I view it as a range, not a list, yeah.
Any hypothetical action that fits within an arbitrary range of "constructiveness" as defined by the context of the campaign is something that warrants focus, as it has a meaningful response within the context of the game/narrative. This doesn't actually restrict any actions, nor does it require any true boundaries to be set. It's a framework of thought that can be applied on the side of the players for them to have the impression that they can take unimportant actions without consequences, while simultaneously having a rough set of knowledge (informed by the context of the campaign) on what actions they can take that will provoke a meaningful response and/or request for elaboration. 
Just to be entirely clear, I am not referring to actually drawing any hard lines - within the context of the rules or outside of them -, nor has my intent been to do so from the beginning.
AnthonycHero — Today at 10:23 AM
I think what would really solve travel for me is treating it like an encounter.

When I read through The Hobbit there's two types of travel that happen. One is just skimmed, you may get a lot of detailed description of things, but nothing really happen and the characters don't really interact with the environment in a meaningful way outside of the occasional random encounters. The other part is the one we're really trying to reach here though I think, and it's the kind of travel that happens within the Mirkwood.

In Mirkwood, the characters are constantly making choices because the environment is hostile. And here's the key though, the environment itself is hostile. Sure, there's spiders, and elves, but the real issue here is not spiders. The issue is that the characters are fighting the wood that basically wants them dead. For the most part, we don't even know where they are exactly or how much does it take to get out of Mirkwood again.

I think trying to model Mirkwood as a place (or a road) is where the problem arises. The Mirkwood is really a monster just as much as the spiders are. The way D&D should model such a thing in my opinion is like an encounter where you want to achieve passing through and the environment wants to achieve you losing the way and dying some brutal death. You don't get out when you've walked enough, you get out when you've won the encounter. So summoning the spiders may be something the Mirkwood can do to stop you, or making you sleep, and you may have a meter you have to fill or whatever that gets you closer to coming out whenever you pass a challenge (whether it's a fight with random monsters or an ability check).


---

# ASL contour heights

December 22, 2024
NEW

stevelampon — Today at 6:33 AM
Can anyone tell me if there is a standard for the elevation levels and what each level represents in metres? Thanks.

Xenovin628 — Today at 6:57 AM
As far as I’m aware, this has never been defined.

BiLLSoz — Today at 7:06 AM
I was looking over Scenario P The Road To Wiltz and noticed the Americans have 21 A-P Mines, since minefields can only consist of 6, 8, & 12, I can only assume the # of A-P mines was suppose to be 20 and not 21.  Is or was there any errata for this scenario at any time?

Justiciar. — Today at 8:09 AM
21 AP divided by 3 (to convert to AT) gets you 7 factors of AT Mines.

1

@BiLLSoz
I was looking over Scenario P The Road To Wiltz and noticed the Americans have 21 A-P Mines, since minefields can only consist of 6, 8, & 12, I can only assume the # of A-P mines was suppose to be 20 and not 21.  Is or was there any errata for this scenario at any time?

Justiciar. — Today at 8:09 AM
See above.

@stevelampon
Can anyone tell me if there is a standard for the elevation levels and what each level represents in metres? Thanks.

jrv — Today at 9:16 AM
AFAIK this is never defined, and the mapping of levels to physical height is situational. I once compared one of the KGP maps to a contour map and got a value of around 20m per level. In most cases the value players have deduced is around 10m per level. The mapping seems to be situational, so a level two hill in a scenario in Norway might represent a vastly higher hill than one around Kursk. Similarly a level two building in the country (e.g. the chateau on board 6) might represent a building that would be dwarfed in a more urban environment like downtown Berlin. My guess is that a level represents from five meters to twenty meters or more.
