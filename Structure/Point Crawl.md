# Design

Pointcrawls are a pretty straightforward scenario structure: You create a map with locations which are connected with paths, forming a node map.

  

During play, PCs in a location can choose one of the paths connected to that location and travel along it to another location. They can thus crawl (there’s the other half of the name) through the pointmap.

  

The structure is quite flexible, with points of different “scale” easily coexisting. (For example, “that strange red rock outside of town” and “the city of Warnock” could easily both appear on the same pointmap.) It can also be trivially fractal, with the point on one pointmap being an entirely self-contained pointcrawl in its own right.

## LITERAL vs. ABSTRACT PATHS

A pointcrawl exists within a strata, and to truly understand, design, and run the pointcrawl, you need to have an understanding of that underlying reality. For example, the city of Warnock and our strange red rock aren’t just floating nebulously in a hypothetical node map: The red rock lies east of Warnock in the Forest of Arden. Or maybe it instead lies to the west on the far side of the Daggerpoint Mountains.

  
Understanding this will allow you to answer questions like:


Which connections exist (and don’t exist) in the first place?

How long does it take to travel from point to another?

How should you describe the journey along the path?

And so forth.

  

The most literal application of a pointcrawl system is to model wilderness travel along a trail system (i.e., the connections between points are literally wilderness trails or roads running between those locations). These are examples of literal paths, and are almost always a player-known structure: The pointmap has a one-to-one correspondence with the game world, and the characters can see the trails or roads that they’re following.

  

But pointcrawls can also work with abstract paths, which seek to capture the conceptual navigation of an environment in a way that allows you to focus prep and structure play. An example of this is an urban pointcrawl, where a pointcrawl would not for example, include every single street and building in the city. Instead, the connections of an urban pointcrawl represent the way we think about traveling through a city.

  

This can be a bit harder to get your hands around than literal paths, so how does it actually work?

  

When the players indicate a navigational intention, the GM basically acts as an “interpreter” who translates that intention into the pointcrawl system, uses the pointcrawl system to resolve it, and then describes the outcome to the players in terms of the fiction.

Although the examples vary, in each case the basic structure of connection-point-connection-point becomes a comfortable framework for the GM to describe the journey, and for the players to understand it and make choices during it.

  

BASIC POINTCRAWL PROCEDURES

  

The basic procedures for a pointcrawl are very simple.

  

STEP 1 – FOLLOW A PATH. The PCs choose one of the paths connected to their current point and follow it.

  

Time: The length of time it takes to follow a path may be standardized for an entire pointcrawl. (For example, you may assume it always takes 10-15 minutes to move from point to another in an urban setting.) Alternatively, different connections may take different amounts of time. If so, this can be indicated directly on the map using either small numbers or dots (with each dot representing one standard interval of time). In setting these times, you’ll most likely be taking the strata of the pointcrawl into account (e.g., traveling one mile down an open road will take less time than traveling ten miles through the tangled bracken of a wild forest).

STEP 2 – RANDOM ENCOUNTER. Check for a random encounter.

Procedure: Any number of random encounter procedures could be employed here. I discuss these options in more detail in Part 5 of the 5E Hexcrawls series. If you are using standard time intervals for your connections, you might consider making one check per interval.

STEP 3 – ARRIVAL. The PCs arrive at the next point.

  

If the PCs are in a point on the pointmap, you can simply follow this procedure. If for some reason they’ve slipped “off” the pointmap, simply funnel them logically into the pointmap and continue from there. (You might be able to assume they’re “at” the nearest point on the map; e.g., they may not be at the cathedral, but they’re close enough that they’re basically “coming from the cathedral” as far as other points are concerned. Alternatively, if you want to get all formal with it, you can think of their current location as a “temporary point” and think about how it would attach to the pointmap.)

# Software

PyVis is an interactive network visualization python package which takes the NetworkX graph as input. It also provides multiple styling options to customize the nodes, edges and even the complete layout. And the best part, it can be done on-the-go using a setting pane where you can play with the various options and export the final settings in form of a python dictionary. This dictionary can later be passed as config while calling the function, resulting in as-it-was drawing of the network. Apart from this, in terms of visualization, you have the basic option of zooming, selecting, hover, among others. Cool isn’t it! 😉

## Node map Design (old)

### Strata

Layer list

Node list

### Config

Literal vs abstract

Strata

### Settings

Actor list

	Actor speed

Layers visible

Permissions

	Player visible?

Speed/time toggle
``
	Pick whose speed

### Node

x,y

Title

Edge list

key list

detail list (dictionary?)

	Description

### edge

  

Node1,N2

directionality (0,0->1,1)

Detail list
	Description

	trafficability (AB)  
	Encounter table

	…

Detail list, JSON
	tba

  

### Detail

	int “part” - defaults to 0

	string “type”
	string “value”