# [[Abiogenesis/_AB13 Low priority stuff/Chapter 5 - Combat/_Master#[[tactical movement|Vanilla]]
- (m/a) = meters per action, 5 ticks)
- (m/s) = meters per second
- (m/t) = meters per tick (about 1.5 seconds iirc?)

##### Human Speed Ranges
- Sprint   - 10 .. 16 m/a = 4 .. 6.4m/s
- Run      - 8 .. 12 m/a = 3.2 .. 4.8 m/s
- Trot      - 6..9 m/a = 2.4 .. 3.6m/s 
- Walk     - 4m/a = 1.6 m/s
- Stagger - 2m/a = .8 m/s
- Crawl     - 1m/a = .4 m/s

- Fastest character -  10+6 = 16/12/9/4/2/1
- average character - 10+3 = 13/10/7.5/4/2/1
- worst character - 10+.5 = 10.5/8.3/6.25/4/2/1


sprinting distance per tick - 2..3.2 m/t (10..16 a turn)

sprinting distance per second  - 4 .. 6.4m/s

See: [[#Research]] for additional stuff

## #candidate Monster designer system (2024?)

- Deliberate - maximum [[attention]]
- Walk - maximum sustained speed
- Rush - ? VO2 max?
- Sprint - maximal anerobic sprint. Has a time limit (1 minute for humans)

##### 1. How long can the average person run before getting tired?
The average person can run for approximately **10-15 minutes** before experiencing fatigue and needing to slow down or stop. This varies based on fitness level, training, and overall health.
##### Outcome
A character can sprint for one pause before needing to test for exertion or slow down

characters can run (trot?) for 10 pauses before needing to test for exertion.

An exertion test is an attribute test. On success, the character may continue exerting; On failure, the character takes temporary attribute damage equal to the margin of failure that requires one hour rest. If the temporary attribute damage overflows the character's health, they take permanent damage instead.

For more information on Attribute damage, see [section x]

Each successive exertion test adds a -1 penalty.

## #candidate Speeds (See AB13) (2025)
When designing creature speeds, we write a multiplier for the designer sample, but record the product in the game sample.

- Normal
- Double time
- Running
- Sprinting
- Crawling

 
## Tactical Movement #candidate (2024)
Movement during an exchange of fire is a special type of action known as an open action, costing 5 ticks.

~~Characters cannot change stance during movement.~~

Tactical movement is divided into two broad paces - normal speed and top speed - with their own properties and restrictions. Additionally, there are multiple special paces which further modify either speed.

Normal, top value

| Pace         | Value             | Modifiers |     |
| ------------ | ----------------- | --------- | --- |
| Top Speed    | 10 meters + mus/2 | -3 to hit |     |
| Normal speed | Top speed/2       | -1 to hit |     |
# combat paces
## Crawl

## Sniper stalk
https://snipercentral.com/sniper-movement-techniques/
https://www.ausa.org/articles/no-need-speed-slow-and-steady-are-hallmarks-army-snipers

## Methodical
+Maximizes awareness
## Combat glide
https://policeandsecuritynews.com/2017/01/18/doing-the-combat-glide/
https://www.vickerstactical.com/shooting-on-the-move.html
+Best for shooting
+Relatively fast
-tiring(unnatural movement)
-needs training
## Low or crouched movement
https://www.armyprt.com/endurance_and_mobility_activities/crouch-run.shtml
+Low silhouette
-tiring
# #candidate Move penalties

| Speed       | Encumbrance  |
| ----------- | ------------ |
| sprint      | unencumbered |
| sprint  - 4 | light        |
| trot        | moderate     |
| trot - 2    | heavy        |
| trot - 4    | overloaded   |
| 1 mv        | crawl only   |


## Sprinting
~~#candidate Characters can sprint once per exchange of fire for free. Each additional sprint requires a fitness check. On failure, the character cannot sprint until the next operational pause.

#candidate at the end of an exchange of fire, roll for fitness. On failure, the character gains fatigue.

If a character loses half of their trauma to fatigue or damage, they cannot sprint.

add: every turn spent sprinting increases fatigue by 1?

# Research
https://mammals-locomotion.com/walking.html
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7655479/
https://www.naturalhistorymag.com/biomechanics/112078/born-to-run
https://www.pnas.org/doi/10.1073/pnas.2108471119
https://sportsmedicine-open.springeropen.com/articles/10.1186/s40798-015-0007-y
https://www.nature.com/articles/s41598-019-53329-5

# Research

# Figures of thumb

5 ft/sec = 4 mph
1m/s = 3.6 kph
empirical minimum flying speed (not statistically determined)


For an approximation of kmh to ms, divide kmh by 4

For movement, ticks appear to be denominated in .5 second increments

to convert m/s to m/action, multiply m/s by the denomination, then multiply by 5

to convert m/a to m/s, divide by 5 and by the denomination
## SRD notes
tick denominations
- .1 = 20..32 m/s
- .3 = 6.67..10.67 m/s
- .5 = 4 .. 6.5 m/s
### Original rules & notes

- sprint -3 penalty to hit
- run -2 penalty to hit
- trot -1 penalty to hit
- walk no penalty

- 0/-1/-3
- 4/8/16 = 12
- 4/7/14 = 6
- 4/6/12 = 1
- 4/5/10

- 12-4=8 for str 1, diff 7

- 14-4=10 for str 6, diff 4

- 16-4=12 for str 12, diff 0


## Biology

For a human, the TW13 move speed is a brisk pace  of 3.5 mph, equivalent to a trot or march

https://en.wikipedia.org/wiki/Lion

Skeletal muscles of the lion make up 58.8% of its body weight and represents the highest percentage of muscles among mammals.[[50]](https://en.wikipedia.org/wiki/Lion#cite_note-51)[[51]](https://en.wikipedia.org/wiki/Lion#cite_note-52)

https://www.speedofanimals.com/animals/coyote

# Generic Individual speeds

## Human

performance by a practiced athlete

Deliberate - 2 - .8 m/s - easy pace

Move - 4 - 1.6m/s  - 4 mph march
Put Move at 1/4 

run pace
Run - 8 - 4.8 m/s

The maximal aerobic sprint, running is the speed that can be held for long periods of time. By default it is around 1/2 maximum anerobic velocity

Sprint - 16 - 6.4m/s

The maximum

## M&K (metrics & kinematics)

Human body length - 1.7 m
Height - 1.7 m
Move to BL Ratio - 1.6 /1.7 - .94118
S:L Ratio (Real, NCAA M) - 4.5882 m/s per meter

- Leisurely walk - 2.5mph /1.1176 m/s
- quick time - 3.4 mph, 1.5m/s
- Double march - 6.14 mph, 2.74 m/s

basketball NCAA = 7.8m/s (=sprint speed 19.5 or 18 mus w/ .5 tick)

17.448 mph

Usain bolt .. 23.35 mph, 10.44 m/s (=his sprint speed would be 26.1 per turn or 32 mus w/ .5 tick)

Usain has run 6.1 average body lengths a second at top speed, while NCAA Athletes run 4.59

#question Do we measure against the average human body length, or the person's individual body length?

book value:

female hockey -
36.6 m/7.19s = 5.09 m/s (=sprint speed 12.725 or ~4 mus w/ .5 tick)

11.386 mph


# biology of fatigue


The amount of lactic acid buildup from running depends heavily on the intensity and duration of the run, with ==a typical resting blood lactate level around 1-2 mmol/L, which can significantly increase to over 20 mmol/L during intense exercise like sprinting==, where lactic acid production is high due to anaerobic metabolism; however, most of this lactic acid is cleared from the body within an hour after exercise is finished. 

Key points about lactic acid buildup during running:

- **Intensity matters:**
    
    Higher intensity runs, like sprints or hill repeats, will lead to greater lactic acid buildup compared to moderate-paced runs. 
    
- **Fitness level:**
    
    More fit individuals have a higher "lactate threshold," meaning they can exercise at a higher intensity before experiencing significant lactic acid buildup. 
    
-

$f(Ad20v  Bp1 = \frac{x}{2^x}$



### stopping distance 

stopping distance is a function of speed squared



# Old

# Open actions

When a player declares his character is taking an open action, he can also simultaneously execute another tactical action with a tick cost less than or equal to than the open action's cost, with limitations specified by the open action.

Both actions are resolved simultaneously.
# posture
## Prone
## Crouched

## Injured



# Notes

Terrain effects load carriage: one compilation of studies has shown that for the same load weight, walking through swamp or on sand essentially doubles the energy cost of walking on a paved road, and walking in snow without snowshoes can increase this cost by 4 to 6 times.

The addition of an external load increases energy cost. The distribution of the heavier items within the load within a pack can affect the energy expenditure during load carriage, as well as the body mechanics of how the load is carried. Concentrating the heavier items higher in the pack and closer to the body can reduce energy cost of marching by as much as 25 percent as compared to a load that is placed low in the pack and away from the body (see figure C-2 on page C-4).

Increasing load weight can substantially increase Soldier energy expenditure during typical foot march conditions. When carrying loads less than or equal to 30 percent of Soldier’s bodyweight, energy expenditure remains constant; however, when Soldier’s load increases above 30 percent of bodyweight the rate of energy expenditure increases throughout the march.



## Hitting moving targets
### Considerations
Core concerns of estimating aim difficulty of hitting moving target

Estimate the fire control package calability of a human to hit a moving target

Hitting a moving target entails leading the projectile point of aim in front of the target in time and space

The target is constrained to one track,  meaning only forward movement in a direction from the shooter matters




# IRL Movement

