SELECTED Candidate 11: integrated into health system
Source: combination of Traveller and Spycraft rules

## Durability
Starts at FIT+MUS+RES points. Damage allocates first to durability until empty, then to trauma.
## Trauma
starts at 0, grows with all injuries beyond the character's durability capacity.

If the trauma score passes a character's trauma limit of 21 points (or 15+FIT), the character is totally incapacitated from major trauma. (major trauma includes the severe, critical, or fatal ratings of the following document   [Ref](https://en.wikipedia.org/wiki/Abbreviated_Injury_Scale). )
	note: 21 is based on the rule of 3s

Major trauma requires critical care within a certain time period for a good prognosis, which can be extended by stabilization. Failure to apply critical care in this time period results in a poor prognosis.
## Good prognosis
A character with a good prognosis eventually returns to gameplay.
## Poor prognosis
A poor medical outcome means the character is permanently removed from gameplay, either through death or extreme disability.

---
you gain trauma by ...
- taking damage in excess of durability
* failing to eat during the day
	- gain 1 trauma. Can only be reversed when receiving sufficient food.
- failing to drink during the day
	- gain 7 trauma. Can only be reversed when receiving sufficient water.
 - life threatening injury (d)
	- gain 1 trauma per degree(d) of the wound per turn.
if unconscious with a life threatening injury
	- gain 1 trauma per degree of the wound

You can voluntarily earn trauma...
- You can only spend trauma on your turn with a 5 tick action.
- You cannot spend trauma while unconscious.
- you may...
	- reduce fatigue by 2 (1 trauma)
	- add 5 durability (1 trauma).
		- Can only happen once per exchange of fire.

you can lose trauma by...
- a day of normal rest by 1 point
- a day of bedrest by amount equal to Healing Factor.
- eating and drinking normally reverses 1 batch of starvation and dehydration damage 
- eating, drinking in excess reduces trauma by 1, to a maximum of 2.

Some trauma is temporary
 - You can gain 7 trauma for every minute with zero oxygen. This is reversed at a rate of 7 trauma per 5 ticks of finding breathable air.

### Stage 3: Trauma Criticals?
Trauma has stages that represent worsening vitality. At each step, the condition worsens.

at 1/4 Trauma...
- add status: -1 dice
at 1/2
- change status: -2 dice
at 3/4
- change status: -3 dice
#### Alternative: set trauma as a multiplier of

- [x] Determine Trauma Criticals ✅ 2023-11-12
# Fatigue Hazard
## Fatigue
starts at 0 and grows. Soft stacks on top of trauma.

If the trauma and fatigue combined passes the trauma limit, the character has to take a will check or fall unconscious.
    They regain consciousness when their combined trauma/fatigue score is reduced.

For logistical purposes, Unconscious characters execute their turns at the following rates:
- 10 ticks in an exchange of fire
- once in a tactical pause
- once per minute out of combat.

fatigue is increased by...
- +1: staying awake longer than 12 Hours
	- per day
	- test against will
- +1: not sleeping after a day of hard work or travel
	-  per work period
- +1 per encounter: not sleeping after a day of combat
	- per encounter
- +x: fatigue damage in excess of durability from certain weapons
- x 2: adverse weather conditions
	- per condition

fatigue is reduced by...
- Standard rest. Reduces fatigue by half the trauma limit
- partial rest. Reduces fatigue by a quarter of the character's trauma limit
# Sustenance hazard
## Trauma
If using the sustenance hazard, you can gain trauma by ...
* failing to eat during the day
	- +1 trauma. 
	- Can only be reversed when receiving sufficient food.
- failing to drink during the day
	- +7 trauma. 
	- Can only be reversed when receiving sufficient water.

# Critical conditions
Shooters inflict critical injuries with their side die.
	If the second die is an MOS of 5 or more, a critical injury occurs
	roll on the hit location chart

- [x] Design Critical conditions ⏫ ✅ 2023-11-12
- [x] Design Side dice 🔼 ✅ 2023-11-12


# Hit Locations
edit vanilla rules here
## Locations
damage is doubled when hitting the head.
# Accepted Candidate 4
Side die for critical hits: use the second die in an attack roll to determine whether the attack crits.

If the side dice succeeds ~~with a margin of success of 5 or higher~~, the target rolls on the hitlocation and critical wounds chart.
### Stage III Rule: nonvitals

limb damage is reduced by 20%.
	(hint: to find 20% of x, shift the decimal point of x by 1 left, multiply by 2 and round up.)
## Critical effects
### variables
- [x] location ✅ 2023-11-12
- [x] type ✅ 2023-11-12
- [x] time length (1 round to "permanent") ✅ 2023-11-12
- [x] intensity ✅ 2023-11-12
- [ ] develop fracture severity🔼 
- [ ] playtest
- [ ] how to handle disabling the chest or head

in other games, intensity, type and length are combined into 1 bloc or genericized
	In T13, intensity is done with static 
# Accepted Candidate For critical hit effects

### Effect type: Fracture
- [ ] TO DO🔼 
- [ ] Severity system?

Interim solution: any action requiring that bone to physiologically function automatically fails, including movement, standing, or holding a weapon.

The Critical margin is added to the weapon's total damage.
### Effect type: Bleed
The character incurs trauma equal to the severity of the bleeding wound.
### Effect type: weakness
module health is treated like a trauma limit

every point past module trauma limit represents injury severity

injury severity that equals the relevant statistic means the limb is rendered useless
### Term: Injury severity:
Applies a penalty to any action that uses the named tissue. If the penalty reduces the character's TN to zero, then the region is disabled.

- severity = module hp - atk damage. 
### Term: Disabled
- A severity that overcomes the character's TN means the inflicted injury has rendered the region useless.
#### Interim solution for non-load bearing tissues: 
Regions like the chest or head cannot be disabled.

### Stage 3 hazard: Intractable injuries
If the damage goes 1.5 times over module health, the injury is considered intractable on the field. Only the services of a hospital can save them now.

This effect stacks with the head trauma multiplier
## Roll table
### 1 nerve tissue
weakness effect targetting coordination
module health: 10
relevant stat: coordination
timespan: MOS of critical in turns. If MOS of damage is exceptional, the effect is intractable until treated.
### 2 bone tissue
fracture effect
module health: 5
special rule: fractures 
timespan: requires healing.
### 3 blood vessels
bleed effect
module health: 3
every point over the module's health is the severity of bleed trauma per turn
timespan: number of turns equal to severity of wound
### 4 muscle tissue
weakness effect targetting muscle
module health: 10
relevant stat: Mus
timespan: MOS of critical in turns. If MOS of damage is exceptional, the effect is intractable until treated.
### 5 stability
weakness effect targetting K-Value
test for falling down
### 6 sensory organs
weakness effect targeting perception
module health: 5
relevant stat: Perception
timespan: MOS of critical in turns. If MOS of damage is exceptional, the effect is intractable until treated.

### 6 alt - contusions

All temporary crushing effects that cause weaknwss

### Hazard Candidate: Messy criticals
All criticals do double damage
## old candidate of degree of crit
or dmg > stat = degree of crit? (min 1)
## Old candidate for degree of crit
1d6+MOS > stat = degree of crit

