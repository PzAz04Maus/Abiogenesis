# Accepted: [[Story Quality-Hazard final#Fatigue + Health + Survival|Trauma+Fatigue System]]

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
### Stage 1 rule: Easy injuries
Round the severity to the nearest half of the governing stat. Therefore, the injury either 
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

All temporary crushing effects that cause weakness

### Hazard Candidate: Messy criticals
All criticals do double damage
## old candidate of degree of crit
or dmg > stat = degree of crit? (min 1)
## Old candidate for degree of crit
1d6+MOS > stat = degree of crit


---

# Fatigue
starts at 0 and grows. Soft stacks on top of health condition.

If the health condition and fatigue combined passes the health condition limit, the character has to take a will check or fall unconscious.
    They regain consciousness when their combined health condition/fatigue score is reduced.

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
- +x: fatigue damage in excess of vitality from certain weapons
- x 2: adverse weather conditions
	- per condition

fatigue is reduced by...
- Standard rest. Reduces fatigue by half the health condition limit
- partial rest. Reduces fatigue by a quarter of the character's health condition limit
# Sustenance hazard
## health condition
If using the sustenance hazard, your condition worsens by ...
* failing to eat during the day
	- +1 health condition. 
	- Can only be reversed when receiving sufficient food.
- failing to drink during the day
	- +7 health condition. 
	- Can only be reversed when receiving sufficient water.

## Stage III: Headshot!
- Damage is increased by 4 when making a head shot

---
