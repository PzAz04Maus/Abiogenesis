

# Tag typing

Simple question: what keywords should be generic tags, and what keywords are important enough to have their own entry?

Is there a way to categorize tags? Yes, use a reference lookup table

sample
```yaml
combat:
  - ambush
  - sniper-lane
  - close-quarters

social:
  - trader
  - scared-civilians
  - lost-traveler

exploration:
  - lost-ruins
  - hidden-cache
  - strange-object
```


# Palette

Region

|   |   |   |   |
|---|---|---|---|
|Arid<br><br>- stat|Dense Jungle<br><br>- stat|Forest/Jungle<br><br>- stat|Woods<br><br>- stat|
|Vegetation<br><br>- stat|Rough<br><br>- stat|Hills<br><br>- stat|Mountains<br><br>- stat|
|Pass<br><br>- stat|Peak<br><br>- stat|||

LandUse

|   |   |   |   |
|---|---|---|---|
|Rural<br><br>- stat|Suburban<br><br>- stat|Exurb<br><br>- stat|Urban<br><br>- stat|
|None|Residential<br><br>- stat|Commercial<br><br>- stat|Industrial<br><br>- stat|
|Infrastructure<br><br>- stat|Extraction<br><br>- stat|Government<br><br>- stat|Science<br><br>- stat|

Travel

|   |   |   |   |
|---|---|---|---|
|Track<br><br>- stat|Road<br><br>- stat|Highway<br><br>- stat|Railway<br><br>- stat|
|Water Obstacle<br><br>- stat|Canalized<br><br>- stat|Intersectional<br><br>- stat|Roaming<br><br>- stat|
|N<br><br>- stat|S<br><br>- stat|E<br><br>- stat|W<br><br>- stat|

Terrain Primitives

|       |       |       |       |
| ----- | ----- | ----- | ----- |
| VA 0  | RA 5  | RH 9  | RD 14 |
| VD 18 | LD 23 | LH 27 | LA 32 |
|       |       |       |       |

### Description Card Sample 2
```yaml
region:
  id: "ridge-line-03"
  name: "Ridge Line"
  summary: "Narrow trail overlooking a valley."
  Cover: 5
  Concealment: 8
  Traffic: 6
  # Paths(Edges) do not have POI; Locations (Nodes).
  POI: False
  # tags should have minimum 2 keywords - type region, type travel. POI also goes here.
  # keys marked with ? are optional
  tags:
    - id: forest
      cat: region
      note?: -2 vis
      wt?: 3
      
    - id: clearing
      cat: region
      note?: +2 vis
      wt?: 1
            
    - id: trail
      cat: travel
      note?: no vehicles, low foot traffic only
      
    - id: steep
      cat: geography
      note?: -2 mv
      wt?: 5
      
    - id: rainy
      cat: weather
      note?: -1 vis 
      
    - id: wildlife preserve
      cat: landUse
	...
```
# Yaml Key suggestions

### Minimalist
```yaml
region:
  id: "ridge-line-03"
  name: "Ridge Line"
  type: "wilderness"
  tags:
    - forest
    - steep
  notes: "Narrow trail overlooking a valley."

```

### RNG
```yaml
region:
  id: "swamp-hollow"
  name: "Swamp Hollow"
  tags:
    static:
      - wet
      - low-visibility
    rng:
      palette: "biomes"
      roll-from:
        - hazards
        - wildlife
      mode: normal     # normal | invert
      count: 2         # number of RNG tags to pick
  notes: "Deep water, thick reeds, hard navigation."
```

### Regional Collection

```yaml
region:
  id: "upper-basin"
  layer: "layer-1"
  nodes:
    - "n1023"
    - "n1029"
    - "n1034"
  edges:
    - "e993"
    - "e994"
  properties:
    difficulty: "normal"
    movementCost: 1
  tags:
    - wet
    - cold
    - slippery
```

### Weight override
```yaml
region:
  id: "canyon-pass"
  name: "Canyon Pass"
  rng:
    defaultWeight: 1
    weights:
      ambush: 2.0
      sniper-lane: 1.8
      close-quarters: 0.5
  apply-to: "layer-nodes"   # selected | layer-nodes | layer-edges
  mode: normal              # or invert
  notes: "Narrow rock corridor ideal for ambushes."
```

### Mixed use Worldbuilding + Game
```yaml
region:
  id: "ashen-coast"
  name: "Ashen Coast"
  environment:
    biome: "volcanic"
    weather: "ashfall"
    visibility: "poor"
  mechanics:
    movementCost: 3
    hazardLevel: 2
    recommendedGear:
      - respirator
      - insulated-boots
  tags:
    - hazardous
    - low-visibility
    - unstable-ground
  rng:
    roll-from:
      - hazards
      - fauna
    mode: invert
    count: 1

```

# My sample Wishlist
```yaml
Node:
# Callsign
  - ID: 001
# RNG Weight
    Weight: 2
# characteristics
    Attributes:
	    - Terrain: [Forest, dry]
		- LandUse: [Rural]
		- Industry: [construction]
	    - Traffic: [highway, canalized]
		- Climate: [Humid, Windy]
		- Behavior: [Cold]
		- Population:
			- Human: 3
			- Wild: 8
			- Xeno: 5
		- Communications: 9
		- Infrastructure: 5
		- Government: 5
	Note:
		- 
# Misc stats
	Attr: 
		- +1 Mv
		- +1 Danger
	Paths: 
		- 001
		- 002

... 
  - ID: 002
    etc 
```


# Node Card (Full specification sample)
```yaml
Node:
# Callsign
  - ID: 001
# RNG Weight
    Weight: 2
# characteristics
    Attributes:
	    - Terrain: [Forest, dry]
		- LandUse: [Rural]
		- Industry: [construction]
	    - Traffic: [highway, canalized]
		- Climate: [Humid, Windy]
		- Behavior: [Cold]
		- Population:
			- Human: 3
			- Wild: 8
			- Xeno: 5
		- Communications: 9
		- Infrastructure: 5
		- Government: 5
	Note:
		- 
# Misc stats
	Attr: 
		- +1 Mv
		- +1 Danger
	Paths: 
		- 001
		- 002

... 
  - ID: 002
    etc 
```
##### road to Armageddon style
```yaml
- Region:
  
	  Territory:
	  Terrain:
	  GovType:
	  Ratings:
		- Defense:
		- Government:
		  Administration:
		  Control:
		  Corruption:
		  Security:
		  
		- Infrastructure:
		  Civil:
		  Communication:
		  Industry:
		  Military:
		  
		- Population:
		  
```
### data type

```

```
# Reference data

```yaml
Reference:
  - ID: Forest
    Weight:
    
    
  - ID: Desert
    
```
