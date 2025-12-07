Pure Bulk system with free slots


1 kg is 1 bulk, 3.5 L is 1 bulk

Or 4 l is one bulk

Or guns are 25-40% of the Bounding box volume

| Item                         | Notes                | Wt, loaded | Vol        | Bulk                | Cost   |     |
| ---------------------------- | -------------------- | ---------- | ---------- | ------------------- | ------ | --- |
| Ak74                         |                      | 3.07       | 12.8 (3.2) | 3.07                |        |     |
| Magazine                     |                      |            |            | 1, pistol (generic) |        |     |
| Civilian box of bullets      | 20 ct                |            |            | 1                   |        |     |
| Ammo can                     |                      |            |            | 8                   |        |     |
| Magazine                     | 30 rounds            |            |            | 2, rifle (generic)  |        |     |
|                              |                      |            |            |                     |        |     |
| Mre                          | Does not spoil       |            |            | 2                   | $30    |     |
| Full nutrition, conventional | ready to eat, spoils |            |            | 4                   | Varies |     |
| Car battery                  |                      |            |            | 16                  |        |     |
|                              |                      |            |            |                     |        |     |

BaseNeed defaults to 2.5 liters of water per day. (1 bulk)

Can go up to 10 liters (3 bulk) at the extreme high endhottest

![[image-1.png]]

| Tags         | Notes                    |
| ------------ | ------------------------ |
| Wet ration   | .5 liters to daily water |
| Moist ration |                          |
|              |                          |

Bulk rankings for carry limits and encumbrance

Lbes have a max bulk limit

Armor adds to Bulk

Finding bulk for food: 

Find the calories per kg

Then find the daily value equivalent (2000 calories) of that

often ~0.3–0.8 kcal per gram once you factor in “stuff you carry but don’t eat”

By contrast, compact rations are ~2.5–4 kcal/g.

So as a rule of thumb, forage is 2–4× bulkier per calorie than rations.

Cap water credit from food at 2 bulk per day (you can’t live on soup alone in extreme heat).

Optionally: in very hot/desert conditions, say only 50–75% of water need can be met by food—you still must carry some separate water.

2. Playable Rule: 2000 kcal of forage

Let’s define a few forage quality bands and what 2000 kcal looks like in your units.

A. Poor forage (leafy, watery, low-fat stuff)

Think: greens, watery fruit, small bits of edible plant matter.

Weight: ~4 kg

Volume: ~14 L (lots of air and water)

Bulk:

Weight bulk = ceil(4 / 1) = 4

Volume bulk = ceil(14 / 3.5) = 4

→ 2000 kcal = 4 bulk

B. Average mixed forage (roots, some nuts, berries, etc.)

Think: what a decent forager would collect in wooded/temperate terrain with some variety.

Weight: ~2.5–3 kg

Volume: ~9–10.5 L

Take a middle value:

Weight ≈ 2.7 kg → 3 bulk

Volume ≈ 9.5 L → 9.5 / 3.5 = 2.7 → 3 bulk

Rule: In “normal” environments,
2000 kcal of forage ≈ 3 bulk

C. High-quality forage (nut-heavy, oily seeds, fat game scraps)

Think: a lot of nuts, acorns processed, or trimming off fatty meat.

Weight: ~1.5–2 kg

Volume: ~5–7 L

Example: 1.8 kg, 6 L:

Weight bulk = ceil(1.8 / 1) = 2

Volume bulk = ceil(6 / 3.5) = 2

→ 2000 kcal = 2 bulk

This is still less efficient than your 1 bulk rations, but better than raw “salad forage.”

3. Simple Table for Play

For 2000 kcal (about 1 day’s food):

Forage Quality	Description	Example Terrain	Bulk (per 2000 kcal)
Poor	leafy, watery, low-fat	scrub, cold, overgrazed, winter	4 bulk
Normal	mixed roots, fruits, some nuts	temperate forest, farmland fringes	3 bulk
Rich	nut-/grain-heavy, good hunting	old-growth forest, river valleys, orchards	2 bulk
Packed rations	processed/dried/cooked	carried supplies	1 bulk

Super easy to remember:

Forage bulk per day = 2–4; rations = 1.

4. Very Short “Rule Text” Version

Here’s something you can drop straight into your rules:

Foraged Food Bulk
A day’s worth of foraged food (≈2000 kcal) is bulkier than carried rations.

Rich terrain: 2 bulk

Normal terrain: 3 bulk

Poor terrain: 4 bulk
A day of packed rations is always 1 bulk.

If you’re using microterrain / hex tags, you can literally attach [forage-rich], [forage-poor], etc., and read bulk straight off the tag.

If you want next, I can:

Hook forage bulk directly into a foraging roll table (success degrees → calories → bulk), or

Build a “field processing” rule where players can convert X bulk of forage into fewer bulk of dried rations back at camp.

# cat 3

Slot and bulk system

