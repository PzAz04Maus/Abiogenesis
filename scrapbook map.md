
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


---

- 
- [Microscale meteorology](https://en.wikipedia.org/wiki/Microscale_meteorology "Microscale meteorology")
- [Misoscale meteorology](https://en.wikipedia.org/wiki/Misoscale_meteorology "Misoscale meteorology")
- - [Synoptic scale meteorology](https://en.wikipedia.org/wiki/Synoptic_scale_meteorology "Synoptic scale meteorology")
- The **POLYGON experiment** was a pioneer experiment in [oceanography](https://en.wikipedia.org/wiki/Oceanography "Oceanography") conducted in the middle of the [Atlantic Ocean](https://en.wikipedia.org/wiki/Atlantic_Ocean "Atlantic Ocean") during the 1970s.[[1]](https://en.wikipedia.org/wiki/Polygon_experiment#cite_note-MunkDay-1)[[2]](https://en.wikipedia.org/wiki/Polygon_experiment#cite_note-coord-2) The experiment, led by [Leonid Brekhovskikh](https://en.wikipedia.org/wiki/Leonid_Brekhovskikh "Leonid Brekhovskikh"), was the first to establish the existence of so-called [mesoscale eddies](https://en.wikipedia.org/wiki/Mesoscale_eddies "Mesoscale eddies"), eddies at the 100 km (60 mi) and 100-day scale, which triggered the "mesoscale revolution".[[1]](https://en.wikipedia.org/wiki/Polygon_experiment#cite_note-MunkDay-1) The existence of mesoscale eddies was predicted by [Henry Stommel](https://en.wikipedia.org/wiki/Henry_Stommel "Henry Stommel") in the 1960s,[[3]](https://en.wikipedia.org/wiki/Polygon_experiment#cite_note-Mikhalevsky-3) but there was no way to observe them with traditional sampling methods.[[1]](https://en.wikipedia.org/wiki/Polygon_experiment#cite_note-MunkDay-1)


**Mesoscale meteorology** is the study of [weather](https://en.wikipedia.org/wiki/Weather "Weather") systems and processes at horizontal scales of approximately 5 kilometres (3 mi) to several hundred kilometres. It is smaller than [synoptic-scale](https://en.wikipedia.org/wiki/Synoptic_scale_meteorology "Synoptic scale meteorology") systems (1,000 km or larger) but larger than [microscale](https://en.wikipedia.org/wiki/Microscale_meteorology "Microscale meteorology") (less than 1 km). At the small end, it includes **storm-scale** phenomena (the size of an individual thunderstorm[[1]](https://en.wikipedia.org/wiki/Mesoscale_meteorology#cite_note-1)). Examples of mesoscale weather systems are [sea breezes](https://en.wikipedia.org/wiki/Sea_breeze "Sea breeze"), [squall lines](https://en.wikipedia.org/wiki/Squall_line "Squall line"), and [mesoscale convective complexes](https://en.wikipedia.org/wiki/Mesoscale_convective_complex "Mesoscale convective complex").


**Microscale meteorology** or **micrometeorology** is the study of short-lived [atmospheric](https://en.wikipedia.org/wiki/Earth%27s_atmosphere "Earth's atmosphere") phenomena smaller than [mesoscale](https://en.wikipedia.org/wiki/Mesoscale_meteorology "Mesoscale meteorology"), about 1 kilometre (0.6 mi) or less.[[1]](https://en.wikipedia.org/wiki/Microscale_meteorology#cite_note-1)[[2]](https://en.wikipedia.org/wiki/Microscale_meteorology#cite_note-FOOTNOTEFoken20172-2) These two branches of [meteorology](https://en.wikipedia.org/wiki/Meteorology "Meteorology") are sometimes grouped together as "mesoscale and microscale meteorology" (MMM) and together study all phenomena smaller than [synoptic scale](https://en.wikipedia.org/wiki/Synoptic_scale_meteorology "Synoptic scale meteorology"); that is they study features generally too small to be depicted on a standard [weather map](https://en.wikipedia.org/wiki/Weather_map "Weather map").


**Misoscale** is an unofficial scale of [meteorological](https://en.wikipedia.org/wiki/Meteorology "Meteorology") phenomena that ranges in size from 40 metres (100 ft) to about 4 kilometres (2 mi).[[1]](https://en.wikipedia.org/wiki/Misoscale_meteorology#cite_note-1) This scale was proposed by [Ted Fujita](https://en.wikipedia.org/wiki/Ted_Fujita "Ted Fujita"), the founder of the [Fujita scale](https://en.wikipedia.org/wiki/Fujita_scale "Fujita scale"), to classify phenomenon of the order of the rotation within a [thunderstorm](https://en.wikipedia.org/wiki/Thunderstorm "Thunderstorm"), the scale of the [funnel cloud](https://en.wikipedia.org/wiki/Funnel_cloud "Funnel cloud") or a [tornado](https://en.wikipedia.org/wiki/Tornado "Tornado"), and the size of the swath of destruction of a [microburst](https://en.wikipedia.org/wiki/Microburst "Microburst").[[2]](https://en.wikipedia.org/wiki/Misoscale_meteorology#cite_note-Fujita-2) It is a subdivision of the [microscale](https://en.wikipedia.org/wiki/Microscale_meteorology "Microscale meteorology").

# scale

The [ratio](https://en.wiktionary.org/wiki/ratio#English "ratio") of depicted [distance](https://en.wiktionary.org/wiki/distance#English "distance") to actual distance.

_This map uses a **scale** of 1:10._


# choosing the appropriate scale

https://colorado.pressbooks.pub/makingmaps/chapter/chapter-8-generalization/
https://mapscaping.com/map-scales-and-measuring-distances/
https://www.sciencing.com/create-map-scale-5161226/
https://www.ncesc.com/geographic-faq/how-do-i-scale-my-map/



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
