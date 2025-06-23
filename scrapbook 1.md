---

#candidate grapple is a penalty to movement based on where the target is held onto - characters cannot move faster than normal speed, while the grapple penalty requires them to spend x meters more to move any distance

#candidate attacks count as moves

#candidate the strength difference sets the default movement penalty for both characters. If a character wants to move more, they need to test against it.

#candidate #winner grapple acts as a slow on the target/brings the opponent with them. Stopping a target from moving requires an immobilization test


---

Abiogenic Dawn??
Abiogenesis Dawn

---

---
#Abiogenesis #reference
The franklin expedition

The center of the zone hasn't been reached

charles francis hall attempt to reach the center of arctic
- https://youtu.be/Qk7F3qj4iDg?si=-W3_TEjG-ntJ_FpF

the vanishing triangle - a Penrose tribar

#place Bridge of the gods, Oregon

Organelles are used to Bootstrap a meme into existence


#### Pacific northwest regional authority(pnwra)
- based on the [Pacific Northwest Regional Commission](https://www.nixonlibrary.gov/finding-aids/fg-357-pacific-northwest-regional-commission-white-house-central-files-subject-files)
- https://onlinebooks.library.upenn.edu/webbin/book/lookupname?key=Pacific%20Northwest%20regional%20planning%20commission

#### Norcal triage

A society in triage

Riverton’s hospital sits twenty-eight miles from Lander’s, but few Rivertonians would agree that Lander counts as local, at least in the case of a medical emergency. The brutal combination of snow and wind leads to travel bans multiple times each winter; whiteout conditions make it remarkably dangerous. “People say, ‘Oh, just drive to Lander,’” said Corte McGuffey, a Riverton native who moved home to raise his family after two decades away. “Well, there’s times we can’t.”



# Ticks before spot
- [ ] #mechanics Ticks before spot
The spot delta could represent how much movement a person can do in a targets Los before the target spots them
# Stat delta
- [ ] #mechanics Stat delta
Statistics rise and fall during play because bad things happen. On the stat sheet, performance stats have 2 values - their starting value denoted by \_, and their current value denoted by $\Delta$ 



---

For a given view V, a line of sight L is obstructed if L intersects the slope of the terrain set T from the point of sight L_p to V. Mathematically, the 3 conditions are

1. if L_p < T > V
2. if if Slope(L_p, T) > Slope (V,L_p)


---
- [ ] #campaign Bug hunt

---

AP - Action Points. 1) Often given to players for use during the game and may be spent to allow their characters to perform actions above and beyond what they may normally do

Attribute

An attribute is a statistic or trait that describes to what extent a character or other entity in a role-playing game possesses a specific natural, in-born characteristic common to all characters in the game. Attributes tend to be stable over time, but may increase slowly as part of character advancement.

Check

Static 

A diceless test for Concealment

Observe/conceal VS conceal/observe

Add the extrinsic values such as contrast,terrain, movement

Simplification: avg spot/conceal together


https://boardgamedesignlab.com/mechanism-master-list/

---

# action penalty due to speed

Divide the current speed by a penalty Modifier such as 3.

# map standards

1/10 scale

1 m in Blender = 10 irl

Height should be 1/10th of distance

In actuality it should be 1/100th, but that is too difficult to discern.

2 meters is the safe height to hide a standing person. 3 is the safe height to hide a tank

- Triangulate all meshes/models to avoid holes.
- Make sure the normals on your mesh are facing the right direction.
- Set the origin point of the model to the center of mass for best physics. Objects in TTS rotate around their origin point.
- Don’t go crazy with poly counts, use a normal map to add fine detail.
- Keep the vertices below 25k for best results, as any higher your objects may not import and/or crash your game.
- If you want to access additional elements for importing a Model, you might be interested in [Custom AssetBundles](https://kb.tabletopsimulator.com/custom-content/custom-assetbundle/) instead.

needs a mesh collider
	- blender addon


# Mesh instructions
1. find simple collider on github, unless you can donate to the creator on blendermarket
	1. If you don't donate, you need to download the release zip from the website and then set up the source files yourself
	2. blendermarket just makes it convenient to install
2. in blender, edit -> preferences -> get extensions
3. top right, there is a downward chevron. open it and select install from disk
4. navigate to the downloaded zip file and select it
5.  it will automatically enable on install
6. the tab will appear on the right side of the viewport next to the camera controls
7. select all objects to collide -> add mesh

current issue: vtt tokens ride high on the mesh - "float midair". Not good.

# 2D Node designer
## draw.io


### Process

1) add nodes
2) link nodes with edges
3) number nodes
4) import png into 2D VTT of choice
5) Add landcover in VTT


# 3D heightmap editor software
## Sketchup
	
- I don't like that they paywall exporting the model to a file. Otherwise, it's easy to use.
https://app.sketchup.com/share/tc/northAmerica/H_BAZK5114s?stoken=NZlM-imjRBigIkKjEDIo2dXW1klQ1tExmTsCA3-Cgpb92F_tfdvOXOR_V6tdmW4i&source=web

## Blender
https://github.com/domlysz/BlenderGIS

### Process

1) (object mode)
2) add -> Mesh -> plane
3) (edit mode)
4) scale to intended size of terrain
5) right click -> subdivide -> repeat step 2 until satisfied
6) move action to edit


### Additional actions
-  [Rip-fill](https://docs.blender.org/manual/en/2.81/modeling/meshes/editing/vertices.html)) :splits vertices, but fills the topology hole with more geometry. Allows you to make cliffs!
	- Alt-V when selecting nodes or edges
- 

	
Notes:
- there are 3 modes to edit by in the edit mode; vertex, edge, and face. All 3 are viable choices
- you can use the XYZ arrows to have tight control over object placement
- (edit mode) press g, then shift-z to move objects on the X and Y plane with the mouse cursor
- (edit mode) press g, then z to move objects on the Z plane with the mouse cursor




## Wings3D
## FreeCAD

# Voxel Editor
## MagicaVoxel
 - https://ephtracy.github.io/


[Magicavoxel Tutorials - Creating Real World Heightmaps](https://youtu.be/-3aFuODXB6k?si=G1NM_huNrxTC6eki)

https://docs.mapbox.com/help/getting-started/access-tokens/

https://www.reddit.com/r/gamedev/comments/ri2msg/where_do_you_guys_get_real_world_terrain_height/

https://manticorp.github.io/unrealheightmap/instructions.html

## Worldpainter


## 

---


As the los travels along the length, find the highest point between the origin and the destination. If the destination is below the highest point, it is obscured.

Ez version - The destination takes the height of the closest datapoint.


Magnitude

We have one for combat ranges

Not one for terrain

But we can simplify 1d6

We can also map outcomes to inputs with a distribution chart

1 1 2 2 2 3
1 1 1 2 3 6

https://medium.com/@srowen/common-probability-distributions-347e6b945ce4




or a formula (exponential)

N-1 = flatter
N+1 = hillier

2^n-1 m

1 2 4 8 16 32 64

1−((20−12)÷20)^(4)

https://www.fastcompany.com/91275004/xdown-killer-drone-designed-like-football


---

backstreet economy

dice Is a measure of consistency


# 
Strange animations. Rather than the monsters doing their idle, walk, attack animations, it would be interesting to have some plain strange things going on to freak the player out and keep things unpredictable. Perhaps an enemy is found laying on the floor, and has a seizure when the player approaches. Another one could be busy groping a wall before noticing the player. It could also be simple stuff, like "ticks" or enemies running off on some urgent errand.

# Stress

Cuf buffer
Once stress breaks through Cuf, stress is added to the stress Meter

Sleep adds the Cuf buffer back but has to clean residual stress first

Candidate

Fast fatigue consumption per exchange

Do 6 high energy actions and the character increases fatigue by 1 point

Stage iii - the number of high energy actions a character can do per turn before gaining fatigue is equal to their fitness

A Tactical pause reduces immediate fatigue by 1 point

Candidate?

Endurance is modeled by hp

If fatigue rises highee than fitness the characters endurance 

Candidate

Each exchange of fire a character takes a fatiguing action is added to a final count. At the end of the fight, the character makes a will test versus the number of fatiguing actions. On failure, the character gains x points of fatigue. 

Candidate 

https://www.science.org/doi/10.1126/sciadv.aaw0341?adobe_mc=MCMID%3D40315718329166467631190808447923398785%7CMCORGID%3D242B6472541199F70A4C98A6%2540AdobeOrg%7CTS%3D1740250861

https://pmc.ncbi.nlm.nih.gov/articles/PMC53679/

4000 calories or 2.5x bmr is the sustained max energy output for long endurance runs. Any higher and the character eventually slows down to that limit

People can go past this only for short sprints before returning to the limit. 

Excess fat

Minimum 80000 caloeies

A good round number may be 120000 calories

2000 calories is used per day with no or little exercise activity - rmr

120000
÷ 2000

=60 days

40% mass is muscle

Each kg of muscle is 1800 calories

32 kg muscle, 58000 calories

Each kg of excess fat is 9000


# Travel and time in story

Distance of things isn't necessarily important, it's distance OVER TIME 

So what you need to do is describe how fast it takes to get somewhere in an hour

A location 100 km away takes 1 hour to get to because you need to drive 100 km in that hour

If you drive at a speed limit of 50 kmh then you divide d/l

Distance
Limit

To get the effective time in hours

We can also do v this to find if an increase of speed changes the time taken

Distance / speed per hour = number of v hours to v drive

We then can also measure by gallons per kilometer to see fuel expenditure

## Time pressures
Roll a travel check to see if the distance increases. Increases should be rare unless players make detours, increases should be common

Fail should be increments of 10%


# attention in combat

When undistracted but not actively searching, attention is divided by 2

Movement penalties still matter

When distracted the attention is divided by 4

When searching, attention is at 100%, but is considered fatiguing effort

This can suggest that fatiguing effort requires will power tests at a certain point to continue

~~The length of time a person can maintain full vigilance during one period of overwatch is by default 1 hour. Additional side dice can increase this by 1 hour per most. ~~


# Equipment

https://youtube.com/shorts/fEAazTp87VI?si=Ve5RBiaj7-vNu30U

Fail gracefully

On an equipment failure, the margin of failure is reduced by n. This cannot turn a failure into a success

Exceptional failures

When this equipment fails a test, it fails more spectacularly than not. Increase the margin of failure by n. 

Jams on

The weapon experiences a failure on margin of failure n or worse. 

Weather can either magnify catastrophic results or increase the probability of them. 


# Lore


# Kirlians creature

## Gameplay

Electric eel
Emp
Flashbang
Static charged objects

Can craft electro anomalies

Can shape or weld steel

## Description

Chitinous steel creature with sleek rings, coils, apertures and crowns 

https://www.museumselection.co.uk/the-art-deco-movement/

Hollow on the inside, but the outline of organs can be seen when the corona discharges, if exposed

Creature produces a large coronal discharge across most of their body on readying or activating a power

https://en.m.wikipedia.org/wiki/Corona_discharge#/media/File%3A%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D1%80%D0%B0%D0%B7%D1%80%D1%8F%D0%B4.jpg

the smell of ozone, blue fog follows its discharge 

Can create intricate art by eroding metal 
https://www.reddit.com/r/pics/s/Wlbtu2W0yG that looks like itself






Kelp Dryad — Today at 5:17 AM
you've literally formatted it as a listttt
Maus — Today at 5:17 AM
No, I framed each as a description, then added a list of examples below
the list is pedantic, sure
Kelp Dryad — Today at 5:17 AM
hjlisadhgfjkhdkhgj"
THEN IT'S A LIST OF EXAMPLES
Maus — Today at 5:17 AM
but I wanted to make my point clear
Kelp Dryad — Today at 5:17 AM
okay yes
I have read and see the ting
Maus — Today at 5:18 AM
I'm  thinking about writing up groups with these types of characteristics for Abiogenesis, which is why there's a list
Kelp Dryad — Today at 5:18 AM
could still probably have a list of "fictional" legends.
cuz' solid snake and big boss have had a massive cultural impact on our generation alongside a shitton of other characters.
superheroes, game characters, etc. are as much legendary in our minds today as much as actors were to the past and still are today.
and even moreso, who the actors portrayed. the fictional characters on the big screen
caricatures of heroic and villainous figures - caricatures that are often used in storytelling and campaigns
Maus — Today at 5:20 AM
I can see it, but part of the issue with that is that they're more rolemodels than they are ideologues
Kelp Dryad — Today at 5:20 AM
not to use directly, maybe, but to definitely take inspiration from when designing more.
I wouldn't consider big boss a role model but his character is used to express an ideology
well, in MGS3 and peace walker I would but
definitely not after
Maus — Today at 5:22 AM
Is it an ideology as a force itself or as an example
Kelp Dryad — Today at 5:22 AM
how do you mean "as a force itself"
Maus — Today at 5:22 AM
well, lets go to the list :D
classic examples
Kelp Dryad — Today at 5:22 AM
Image
Maus — Today at 5:22 AM
The bomber mafia
The fighter mafia
the reformers
Kelp Dryad — Today at 5:23 AM
you motherfucker you circled me back in
the bomber mafia
the fighter mafia
the reformers


fighter + reformers, the attempt of the purpose behind Mother Base?
Maus — Today at 5:23 AM
The bomber mafia are a colleagueship of soldiers who believed in the utmost power of the bombing campaign back during WWII
Kelp Dryad — Today at 5:24 AM
ohhh they're specifics not generalizing descriptors.
...damn people suck at naming things.
Maus — Today at 5:24 AM
This is colloquial since I've literally redefined the term to cover this
I have seen no literature that looks at these sets like I am currently doing
they were the ones who advocated for primacy of strategic air bombing  during WWII by the United States, as a weapon which in and of itself could win the war
ie - put all your resources in bombers, we'll smoke em out.
This had a massive cultural impact because they were the predecessors of massive retaliation, the idea that the US would reduce its armed forces and primarily rely on the atomic bomb in case war broke out.
also because they were the guys who pushed for bombers capable enough for the task
Kelp Dryad — Today at 5:28 AM
I remember that discussion, during the time when the military branches were vying for supremacy in the eyes of the government, which one could successfully end the war
and the airforce being like "hold my beer"
Maus — Today at 5:28 AM
aye.
Kelp Dryad — Today at 5:28 AM
Image
I remember that part, yes.
I read a lil' history, okay? I'm not completely clueless.
Maus — Today at 5:29 AM
the  hope of the bomber mafia was that they were the most efficient means of waging war, so would cost the US taxpayer the least.
didn't turn out that way
Later on, the Fighter mafia came around, who named themselves such as a direct parallel to the bomber mafia. In short, they were convinced that the US was full of waste and bloat for aircraft that didn't perform, so what they wanted to do was redefine how we think of aerial combat and use that concept to make better fighters.
these guys later got lumped in with the reformists, which was a collection of soldiers convinced that graft and waste at the DOD had gotten to such levels that the US military was not fit for combat.
so they went around trying to reform the shit out of it.
If you recall them, these guys were absolute zealots who basically wanted to redesign how the entire military looked into something ridiculous.
the paypal mafia
It's Peter Thiel, Musk, and a bunch of other guys who created Paypal
a pack of techbros with a very distinctive opinion on how to shape American society
big juju
institute for advanced study
 It has served as the academic home of internationally preeminent scholars, including Albert Einstein, J. Robert Oppenheimer, Hermann Weyl, John von Neumann, Michael Walzer, Clifford Geertz and Kurt Gödel, many of whom had emigrated from Europe to the United States.
you've heard me jerk off Godel
Einstein redefined the universe
Oppenheimer redefined humanity's relationship with technology
Maus — Today at 5:36 AM
all of them were instrumental in our understanding of nuclear and quantum physics
they were all friends, colleagues
Kelp Dryad — Today at 5:38 AM
and got a lil' freaky with it
I see now, you're talking about legends that redefine on such a level that lives fundamentally change on a national or international scale?
Maus — Today at 5:39 AM
or at least that's their goal, yeah
culture heroes can do that but in truth I'm looking for the giants of history
so I can turn them into Mr. Johnsons for Abiogenesis.
The Senator Armstrongs
Kojima's villains are chock full of these types
Kelp Dryad — Today at 5:41 AM
I suppose in the context of its' own story, Big Boss was basically that as an example cuz' I'm a sucker for MGS
the catalyst for the most major changes in the world.
that and the russian who created the original concept for the Metal Walker
Maus — Today at 5:42 AM
though tbh I find Kojima's giants to be just straight up bizarre and dreamlike
but that's MGS for ya
Kelp Dryad — Today at 5:42 AM
I think the russian engineer was probably the best example of a more down-to-earth giant.
Maus — Today at 5:42 AM
mhm
though honestly
Abiogenesis has a helluva iceberg
Kelp Dryad — Today at 5:43 AM
whose accomplishments far outlived him, he was forgotten and was just a random drunk dude whose work was overshadowed in his time.
Maus — Today at 5:43 AM
Did you ever read about Erlkoenig
in the setting
Kelp Dryad — Today at 5:44 AM
in the setting...unsure, but isn't that a german poem?
Maus — Today at 5:44 AM
yes
Maus — Today at 5:45 AM
it's in this section
https://github.com/PzAz04Maus/Abiogenesis/blob/publicmain2/_AB13%20High%20priority%20stuff/1%20Settings%20Theory%20%26%20Fluff/Core%20Lore/0%20de%20Kuiper%20Event%20-%20SPOILER%20WARNING.md
GitHub
Abiogenesis/_AB13 High priority stuff/1 Settings Theory & Fluff/Cor...
Core repository for the AB13 system and Abiogenesis setting - PzAz04Maus/Abiogenesis
Abiogenesis/_AB13 High priority stuff/1 Settings Theory & Fluff/Cor...
Kelp Dryad — Today at 5:45 AM
Image
Maus — Today at 5:46 AM
:{V
how could it possiblyt be bait
Kelp Dryad — Today at 5:46 AM
drag me in with interesting conversation, dangle the bait and I didn't even notice the hook
congrats you got me to click on the github
Maus — Today at 5:46 AM
gehehe
Kelp Dryad — Today at 5:46 AM
now use this technique on other people
it worked
Maus — Today at 5:47 AM
We've got all these assholes these days
trying to achieve the singularity with AI and all this shit
and all they've created so far aren't reasoning machines, but syntax machines that spit out responses
pale imitations to the real thing
Kelp Dryad — Today at 5:48 AM
we were so worried about the physical machine, the robot, the android replacing our lives and our jobs
but forgot the humble line of code stored in the cloud.

If you don't want a blank page, don't write from white
	- psychologically start with a canvas that isn't bright on the eyes with a text color
	- blue or grey


soft orange tint
dark grey back
dust in the air
mist
atmosphere of roadside picnic

retromachines for de kuiper
Djinn

the idea of the movie playing just spilled out

---

thing of 

https://cdn.discordapp.com/attachments/151499379436421120/1337800469304573983/image.png?ex=67a8c347&is=67a771c7&hm=39a79b9d70f77251946b63d32836354a59d6fab83461f6b954a68787a73a749a&


fragmented reality, broken mirrors, vague, wispy

just brushed against her, the skin had a haemoraggenic reaction to an allergen that doesn't belong here because these realities don't like each other

this causes skin to look like severe burns, anaphlylactic shock over something that shouldn't exist

the creature is minding its own business and doesn't even acknowledge  her

freaked itself out like a squid

aerial squid or fish

- doesnt belong in this reality, far less visually comprehensible than this

-doesnt belong in this reality, far less visually comprehensible than this
-moves like a fish in water, may dart away suddenly
-hard to look at, like thousands of broken mirrors in rainbow refractory patterns
-may cause severe "allergic reaction" on skin contact, to the point of "anaphylatic shock" symptoms - as if bodies in this reality is allergic to things that don't belong, this is how reality interprets it, being touched by a "foreign body" that the physical body "rejects" like an allergen.
-isn't really hostile? like a confused fish out of water that can still swim. you took a trout and threw it in the sky and somehow it can still swim but really doesn't understand what this wind pressure is or what clouds are. (edited)

fabric or material may not be able to protect against it because even the fabric fuses with the material as they intersect

fabric may be fused into the character

---

skywires, telephone wires slewn across the sky, exist in clouds

long, geometric 8 sided diamond that at the start of it like a creature with a long tail

very UFO vibe, but a zipline of telephone wire

---

cloud of disintegration?
	people touched convulse, die, explode


---
![[seryeon-jung-asdgdsdss2_ArtStation - Merfolks, Seryeon Jung.jpg|500]]
![[abiogenesis_cavitation_maxresdefault.jpg]]
The stranded whale

very high intelligence
	sapience
	pretending to be a baby crying like a cat
	its camouflage is communication

a master of adoption
- initially a filter feeder, Geophageous
- a temporally beached whale that adopted land-based characteristics
- Not in the native oceans
- ability to mutate its own characteristics, forced evolution
	requires a lot of food to mutate itself
	requires a lot of fat content
	attempting to imitate humanity, develop communication with humanity

- its original form was aquatic, but it was forced to change
- different world
- psionic
	if I just eat enough dense energy sources I can exploit my psychic powers
	- but it projects images to express meaning and conversation, but this is so rapid that it hurts human minds. It evolved without the concept of written or spoken language, usually communicates through imagery
		- arrivals will use alien knowledge
		- a bioluminescent flashshow to show panic
	- normal methodology is the slideshow
	- but it uses mimicry to talk with humans because it doesn't know how to communicate otherwise
	- memes would be a hoot (check phone)
	- cigarettes

- This creature is from another galaxy, another supercluster is so different that it's an alternate reality
	- separate sections of the universe that are too twisted and different to not be similar to ours
	- creatures from a nearby galaxy clusters

bottom one has no natural predators, defense against smaller things
	its typical defense is trampling
	or create weapons
	develop tougher skin



filtration system to deal with the air, cooling for the brain

like the spider lady that's so mutated she can't move from her spot

We can work with all of deerchip's designs to


---
![[tumblr_pd005nMNAV1qgazkvo1_1280 3.png]]

dropbear Lunger

Arborial hunter, predatory intelligence

- feet talons, lots of lunging
- grappling
- disembowel the prey
- rip and tear
- transported
- grip onto trees, hang offwards horizontally
- sloth-like attitude
- sexual dimorphism for 
- red-assed baboons
- red is a display symbol
	- red gets more intense
	- fleshy?
	- tusks grow in

usually it's the male doing the displays

females less defined in coloration

some form of intelligence
	tribal/hunter intelligence

	near homo sapiens intelligence

---


# Complications

The more complicated an action is, the more potential for complications arise

Complications can come from anywhere with multiple magnitudes 

Sources of complications

Extreme failures
Equipment complexity
Large scale
Long distance
Long time frame
Large numbers of help

Example complication

Weapon jamming

3d printed scales


---

Gun weight lessons

Much of character weight at low to medium loads is not a weight phenomenon, but partially a psychological and inertial phenomenon

The pivot point of a load bearing person isn't at the shoulder but at the center of mass

For the purposes of model simplicity the center of motion is the center of mass

https://en.m.wikipedia.org/wiki/Ordinal_data

https://www.rockpapershotgun.com/lysergic-fps-mohrta-is-a-medieval-western-gothic-blend-of-morrowind-and-doom

---


I'm struggling to define it, but what I want to energize the audience with an atmosphere of red hot growth, friction as the region captures an interwar boom town atmosphere where opportunities have to be made with resourcefulness. People want to create out their own little patch of an American Eden in a place that is growing scarce. There's a level of FOMO to motivate people.

The PNW has traditionally had a dichotomy between boosterism and its hope to remain a far corner of the United States. People are torn between showing what they're made of and conserving what already exists. This can be expressed as a sort of ambivalent idealism trying to survive the extreme pressures of war, disaster, and economic shifts.

Edge of the world


Biggest influencer actors and orgs in Seattle

https://www.builtinseattle.com/articles/largest-companies-seattle-tech

https://www.glassdoor.com/Explore/top-companies-seattle_IL.14,21_IM781.htm

https://www.bizjournals.com/seattle/news/2017/10/19/seattle-power-brokers-sound-off-on-amazon-hq2.html

https://propertyclub.nyc/article/celebrities-who-live-in-seattle

https://seattlemag.com/features/25-most-influential-people-seattle-2020/

https://www.seattlemet.com/news-and-city-life/2021/12/the-most-influential-seattleites


We need an LA for the pnw 
We could pick a historical one

Or amalgamate one from all the cities and place it in vancouver



https://www.pdxmonthly.com/news-and-city-life/2023/11/portland-personality-introverts

Cascades, Washington. 

part of the Olympia-Vancouver-Portland metro area
Ic Set on Vancouver-Portland region

 Ooc Characteristics is a mix of every big pnw city
 Acts as a metaphor for the region
 

- vancouver/tacoma
- portland
- seattle
- salem

Sad for a lost past

What the takeaway from that post is, is that we're commitment-averse. I think it has something to do with not wanting to intrude in other peoples' daily lives - that's why talking to strangers in public isn't something that happens very commonly here. You can make friends, but not out of the blue - friendships tend to crop up within interest groups and cliques, and they're about quality over quantity.



---

As the battle of Taiwan continued to rage between two nuclear powers unabated, the west coast prepared for the worst. Because of its proximity and its many strategic assets, Washington state became not only a potential nuclear target, but was under a concerted hybrid war campaign. The electrical grid was contested ground, hospitals were shut down by ransom ware, wireless communication were bricked via backdoor, a campaign of civilian drone strikes had resulted in one airliner crashing on takeoff - no survivors - thousands of federal public servants including rank and file service men and women were defrauded of their lives and identities on a breathtaking scale. 

These efforts all presented extremely disturbing futures. What would happen first? Would the war effort to defend Taiwanese sovereignty be crippled first, the social fabric, or was the next step the bomb, or something worse?

To address all of these issues, a joint effort was struck. The us has a wealth of materiel, but the wartime strains on the official channels meant that domestic disaster preparedness was too much of a choke on throughput. In recognition of the unthinkable, vast quantities of military and civil emergency stock was placed in prepositioned sites across the state. The largest such stockpile was centered around Vancouver, Washington. 

Then, the De kuiper event struck, launching the domestic disaster that so many feared to pass. Emergency plan Unthinkable was put into action. 

For Vancouver, the young, out of the way city known as vantucky by neighbors became a victim of its own success. Supply depots, headquarters, and encampments grew like mushrooms in every lot and park. Contractors drove hundreds of trucks a day in military convoys in bumper to bumper traffic the Columbia River became a deluge of barges,trying to rescue an ailing state. 

then California began to collapse.

it was the largest internal migration in the history of the American people. Every single city and county north of weed California became a home for 60 million dispossed citizens. The Portland Vancouver Metropolitan area flash grew from 2.5 million people to over 6 million, quickly tying the western seaboard of Washington state into the Seattle combined statistical area, population 18.3 million.

 at the urging of federal authorities, Vancouver and Portland were merged into a single government called the Cascades metropolitan district. 

# Economy


# Culture

"Come visit us again and again... But for heaven's sake, don't come here to live.[13]" - Oregon Tom McCall in a televised interview with Terry Drinkwater. January, 1971

The uncertain truce presaged the zeitgeist of postwar america. a war of intense, near peer bloodshed that held a loaded gun to the head of life on planet earth, the Taiwanese conflict brought a sense of clarity, a drive to achieve in the harsh peace where nothing could be taken for granted anymore. The De kuiper event, the "natural" disasters, and the resulting recession soon drove this further home: not only was the moment under threat, but so was mankind's place on earth and their understanding of the universe. 

As the nickname of McCalls Failure suggests, Cascades, Washington has become an unwanted microcosm of the pacific northwest,where the rural, working class and high tech communities have been squeezed uncomfortably together, causing intangible differences to precipitate into very real anger. An example of this is the concept of Californication, where foreigners have come to a region with its own ways to compete, to bring their problems, to wreck all the values that pacific northwesterners spent a century to conserve.

Life in the Cascades has become about seizing that moment before someone else gets it first. Whether the reasons are for rebuilding a cherished past or to escape to some future, everyone is toughing out the moment to make it.





---

The outside economy

Smoking section of the economy

Influence VS being in charge

Good Intentions, Bad Outcomes


# Terrain topics


#candidate 
# Poker cards system for microterrain

suit of the best card determines type

- protection
- mobility
- firepower
- concealment

max number of cards determined by skill

You give up a set of cards to place down cover

replenishing your deck with 1 card requires a turn of movement

# Old (1/8/25)

Terrain chunking

Regionalize tracts of land. 

Set a primary terrain

Set a %chance per unit area of alternate terrain places

Ie - the tract has 3% buildings

Roll d100 to see proximity to the region

Rolling under %chance means the region is within one turn of movement or y distance

Every multiple of %chance is another turn of movement or y x N distance





# Genetic engineering

https://genomebiology.biomedcentral.com/articles/10.1186/s13059-015-0607-3#:~:text=A%20fundamental%20concept%20in%20biology,genetic%20material%20between%20different%20species

A fundamental concept in biology is that heritable material, DNA, is passed from parent to offspring, a process called vertical gene transfer. An alternative mechanism of gene acquisition is through horizontal gene transfer (HGT), which involves movement of genetic material between different species. HGT is well-known in single-celled organisms such as bacteria, but its existence in higher organisms, including animals, is less well established, and is controversial in humans

https://pmc.ncbi.nlm.nih.gov/articles/PMC2933358/

https://en.m.wikipedia.org/wiki/New_Delhi_metallo-beta-lactamase_1

Humans can acquire new enzymes through gene duplication and divergence, a process that has contributed to the evolution of new metabolic and regulatory enzymes. According to studies, gene duplication followed by mutations can lead to the emergence of new enzyme activities. However, the likelihood of a duplicated gene acquiring a new function is much lower compared to the loss of that gene. The Innovation-Amplification-Divergence (IAD) model suggests that new functions often originate from promiscuous secondary activities that become important for fitness due to environmental changes or mutations. These new activities can then be improved through mutations, leading to the divergence of a new enzyme.

---

An evolutionary catalyst is a factor that accelerates or facilitates evolutionary changes in organisms. This concept is evident in various contexts, such as the origin of life, the spread of antibiotic resistance, and the development of social behaviors.

In the context of the origin of life, catalysts like hydrogenases and carbon monoxide dehydrogenase/acetyl-CoA synthase (CODH/ACS) played crucial roles in early chemical evolution. These enzymes, present in the last universal common ancestor (LUCA), helped in the conversion of CO2 to methane under reducing conditions, which is a thermodynamically favorable but kinetically challenging reaction. The presence of suitable catalysts was essential for overcoming these kinetic barriers and facilitating the synthesis of organic compounds necessary for life.

Regarding antibiotic resistance, plasmids and specific genes like ampR act as evolutionary catalysts. Plasmids are small DNA molecules that can transfer between bacteria, carrying resistance genes and enabling rapid evolution of new resistance forms. The ampR gene, for instance, regulates the expression of hundreds of other genes, including those involved in antibiotic resistance, thereby accelerating the evolution of resistance in bacterial species.

In the realm of social behaviors, evolutionary catalysts can be seen in the convergent evolution of similar social behaviors in distantly related species. For example, socially monogamous mating systems and biparental care have evolved independently in various species, suggesting that common selective pressures can lead to the same social behaviors through different biological mechanisms.

Dr. Gerhard Hochreiter, an expert in organizational design and strategy, uses the concept of an evolutionary catalyst in his work on driving innovation and transformation in organizations. His approach includes creating cultures of innovation, implementing agile management practices, and fostering systemic changes to adapt and evolve in the 21st-century business landscape.

Overall, evolutionary catalysts play a significant role in accelerating and shaping evolutionary processes across different biological and organizational contexts

https://phys.org/news/2023-04-catalyst-human-brain-evolution.html

---

Rapid evolution refers to the phenomenon where species adapt and change at a faster rate than traditionally thought possible. This can occur within observable time frames, such as decades or even shorter periods. Here are some examples and insights into rapid evolution:

- **Trinidad Guppies**: Evolutionary biologist David Reznick observed that Trinidadian guppies adapted to their environment much faster than expected. Changes in predator presence led to significant evolutionary shifts in just a few generations.
    
- **Green Anole Lizards**: In Florida’s Indian River Lagoon, green anole lizards developed larger toepads with more scales in just 15 years to better cling to branches after brown anoles invaded their habitat.
    
- **Tawny Owls**: Finnish ornithologist Patrik Karell found that tawny owls in Finland changed their coloration in response to warming winters, adapting to new environmental conditions over a relatively short time.
    
- **Purple Loosestrife**: This invasive plant species spread rapidly across North America, adapting to new environments and climates over a span of 150 years. Researchers have used common garden experiments to study the genetic basis of its rapid evolution.
    
- **Bacteria and Viruses**: These microorganisms are known for their rapid evolution, particularly in response to environmental pressures like antibiotics or disinfectants. For example, E. coli can develop resistance to Lysol in just a couple of years.
    
- **Brassica Rapa**: A study on this plant species showed rapid evolutionary changes in gene expression in response to climate fluctuations, demonstrating how plants can adapt quickly to changing environmental conditions.


https://en.m.wikipedia.org/wiki/Mutagen

https://en.m.wikipedia.org/wiki/Genotoxicity

Mutagens are also featured in video games such as Cyberia, System Shock, The Witcher, Metroid Prime: Trilogy, Resistance: Fall of Man, Resident Evil, Infamous, Freedom Force, Command & Conquer, Gears of War 3, StarCraft, BioShock, Fallout, Underrail, and Maneater. 

https://en.m.wikipedia.org/wiki/Gene_transfer_agent

De kuipers aurora
Kleene stars
Pollination
Energy field (magnetic side phenomena)
- Toss metal shavings at it and you get a cubist mandala in the air
- Energy fields glow and create emissions at some times

Microbe factory
- produces viroids which replicate and modify a host through horizontal gene transfer to the entire body

A set of xenoforming events that invoke high speed evolution through several phenomena, including memetic adaptation, horizontal evolutionary transfer, viruses and enzymes

Viral gene transfer is a technique that uses viruses to deliver a healthy copy of a gene to a specific cell. The process involves packaging the gene into a replication-deficient viral particle, called a viral vector, which then delivers the gene to the cell. 


> ==No, with current gene therapy practices, genetic modifications made through gene therapy cannot be passed on to future generations== because most research focuses on altering somatic (body) cells, not germline (reproductive) cells, meaning any changes are limited to the treated individual only. 

Key points to remember:

- **Somatic gene therapy:**
    
    This is the most common type of gene therapy, where modifications are made to body cells and cannot be passed on to offspring.




- [ ] #TODO #resource strategic CoMbat - shattered worlds

# Morale stuff
# TXT mod
1. I only vaguely remember it but it essentially acted as a second HP pool that ticked down from stressful events and would inflict debuffs at certain thresholds

# Moral resistance model

Resistance 5,meaning a + 5 to tests

This can be countered by harder tests

# morale penalties (selected)

All actions done in harms way can have a morale penalty based on the person's fear of the threat (pressure, suppression) 

After a certain point the threat could be so severe that it requires a test (what about side dice?) to even attempt. 

Severity is narratively determined

A person may be able to commit themselves with a cuf check to reduce all penalties for the duration. This bears a risk (not repeatable on failure) and a cost (those who commit have a penalty to retreat) 

A tactics check can amplify the pressure or shape the battle

Penalty rating samples

1 weak harassing fire
2 near miss harassing fire
4 near miss automatic fire
8 near miss explosives
16 direct artillery bombardment

Hits quadruple the penalty (2 step)

# moral cohesion model (selected)

> Moral factors can sustain troops far beyond the normal physical and mental limits of human beings, provided they perceive their cause as a righteous moral imperative worthy of their lives

All units have survival points retermed as morale

Morale is lost with failure, gained with  success on a ladder rating. Exceptionally good performance is rated as a 5, exceptionally poor performance at 0

Good logistics improves morale

Morale can be lost to surprise, threat (mass or Firepower), or worry. These are collectively referred to as shock

Morale is spent on improving individual actions

Problems like can create shock with results such as a penalty, a margin penalty, or a failure mode

In such a case, morale has to be spent or generated with a cuf check in order to cancel *1* shock penalty. 

Morale can also be used to improve a roll by adding 1 additional dice. 

If a cuf check fails, the character cannot generate more during that phase of fire

Because morale is intangible, the gm must be reminded that it cannot be codified into substantiated mechanics, but only narratively characterized

When in doubt, make a random roll

---

