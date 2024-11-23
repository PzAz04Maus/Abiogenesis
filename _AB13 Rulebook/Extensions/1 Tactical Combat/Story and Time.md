# Mechanics
Players in Abiogenesis 

```
Individual scale - one location, the scene
Tactical level - a [sequence](https://en.m.wikipedia.org/wiki/Sequence_(filmmaking)), consisting of the softer decisions that go into a fight
Operational level - the chapter
Strategic level - the act

Abstraction
representative
```

# friction intensity
output 3@3d6

multiply the remaining 2 and add 1d5

players start with 4 frivtion slots
- their belongings
- their decisions
- 

### Chronological and Kairological time

### Driveshed & Walkshed
## Walk or driveshed
walkshed (plural walksheds) (transportation planning, urban studies) **The land area within a defined walking range of a specified location**.

https://www.mwcog.org/newsroom/2019/07/16/walksheds-show-planners-how-easily-people-can-walk-to-transit/

Planners assume that on average, a person can be expected to walk about ten minutes to get to a destination like a train station. That’s typically about a half mile in a straight line.

If we walked in that straight line – or “as the crow flies” -- the outer limits of a half-mile walk would form a perfect circle with the station at the center. But in the real world, as we navigate our way to or from a Metro station, ten minutes of walking often doesn’t get us as far as we would like. Blocks are sometimes very big, sidewalks may be missing, or a natural or man-made barrier may obstruct a direct path. As routes become more circuitous, the area covered by a ten-minute walk is often much tighter than the half-mile radius would suggest.

A walkshed is the area around a station – or any central destination -- that is reachable on foot for the average person.  An analysis of “walksheds” can help us understand the difficulties of walking to and from central points, like transit stations.

Sometimes the communities around station areas—typically those with smaller blocks and fewer barriers to walking—have fairly extensive walksheds. But at other stations, with large blocks, natural or man-made barriers to walking the distance that an average person will be able to walk can be a small fraction of the half-mile radius. Such constrained walksheds can be expanded with new pedestrian connections and enhancements to existing connections.
## Scales
Based on the size and travel distance of a form of transport in 10 minutes

A person is 6 feet across, with a footprint of 0.5 miles in 10 minutes.
A car is 6 feet across, 15 feet long and has a footprint of 5 miles in 10 minutes, residential area

A car is 6 feet across, 15 feet long and has a footprint of 10 miles in 10 minutes, expressway area

# Theory

---

# 

nonlinear card dice

4dx

the first dice is as normal
but the ordered pattern of the next 3 dice modifies the decision

a flush (678 or 15 14 13) adds or subtracts 1/2 the starting stair value depending on the last number being even or odd

a pair adds the first die to itself based on the last number being even or odd

a triple multiplies the first die with itself

no pattern does nothing

https://www.frontiernet.net/~jamesstarlight/LinearVsNonLinear.html

# Random walk for gear
have a grid of all the party's gear

walk the dice roll around the gear to determine what breaks


# Nonlinear dynamics suggestions
- GM secret roll pool - TW2000 style
- GM secret modifier to player's roll - roll to modify the player's result. This is unpredictable because the player is not privy to the result
- markov chain
# chatgpt result for nonlinear dynamics
- candidate: multiply by previous roll

Certainly! A **random walk** is a mathematical concept often used to describe a sequence of steps where each step is random, and the next step depends on the current state or position, typically according to some probability distribution.

In a **linear random walk**, each step is usually determined by a fixed probability distribution, independent of previous steps. For example, in a simple 1-dimensional random walk, at each step, the particle might move left or right by a fixed amount (say, \( \pm 1 \)) with equal probability.

However, in a **nonlinear random walk**, the situation changes. The "step size" (how much the position changes from one step to the next) or the **probability distribution** governing the next step is influenced by the **previous step(s)**, and this relationship is **nonlinear**.

### Nonlinear Random Walks: Key Concepts

1. **Nonlinear Step Size**:
   In a nonlinear random walk, the amount the walker moves in each step may not be constant. Instead, the step size could depend on the history of previous steps, possibly in a way that follows some nonlinear function. For example:

   - The step size could be proportional to the square of the previous step:  
     \( \text{step size} = \text{previous step}^2 \).
   - Or it could follow an exponential rule:  
     \( \text{step size} = e^{\text{previous step}} \).

   This means that each step is influenced by what happened before, and the system may evolve in a much more unpredictable and chaotic manner, because larger steps (or smaller ones) could amplify or suppress the movement over time.

2. **Probability Distribution**:
   In a typical random walk, the next step is determined by a fixed probability distribution (e.g., 50% chance to move left, 50% chance to move right). But in a nonlinear random walk, the probability distribution can change over time depending on the previous steps. 

   - For instance, the **probability of moving in a particular direction** might increase or decrease based on the size of the previous step, or the cumulative history of past steps. A nonlinear function could govern this.

   - Imagine a scenario where the walker’s step size increases exponentially depending on the last step: if the previous step was large, the next step might be even larger (and more likely to be in the same direction), leading to runaway behavior. Conversely, if the last step was small, the probability of taking larger steps in the future might decrease.

### Example of a Nonlinear Random Walk

Let's consider a 1-dimensional random walk where the step size depends on the square of the previous step. Here’s a possible rule for each step:

- Start at position \( x_0 = 0 \).
- On each step, the **step size** is given by \( \text{step size} = \text{previous step}^2 \).
- The direction of the step could still be random (say, flip a coin for left or right), but the size of each step increases (or decreases) depending on the magnitude of the previous step.

So, let’s walk through a few steps:

- **Step 1**: Suppose the first step is \( \pm 1 \) (we roll a fair coin for left or right).
  - If we move 1 step to the right: \( x_1 = 0 + 1 = 1 \).

- **Step 2**: The step size is now \( 1^2 = 1 \), so we move by 1 unit again, in a random direction.
  - If we move 1 step to the left: \( x_2 = 1 - 1 = 0 \).

- **Step 3**: The step size is now \( 1^2 = 1 \) again, so the next step is still 1 unit, but let’s say we move to the right: \( x_3 = 0 + 1 = 1 \).

- **Step 4**: Now, suppose we change the rule to something more nonlinear, like \( \text{step size} = \text{previous step}^2 \). Let’s say the previous step was 1, so now the step size is \( 1^2 = 1 \).

This could lead to "randomness" that is more persistent over time but also potentially more sensitive to initial conditions. **Small fluctuations** might become **amplified** or **suppressed**, depending on the underlying rule.

### Chaotic or Compounding Effects

A more pronounced example of a nonlinear random walk could involve compounding effects. Imagine if the step size were governed by a **nonlinear function** of the previous step's size. For example:

- Suppose the walker’s step size \( \Delta x_n \) depends on the **previous step's magnitude** raised to a power \( p \):
  \[
  \Delta x_n = \text{step size at step n} = (\Delta x_{n-1})^p
  \]
  This means that if the previous step was large, the step size at the next step becomes disproportionately larger (depending on the value of \( p \)).

  - For example, if \( p = 2 \) and \( \Delta x_{n-1} = 3 \), then \( \Delta x_n = 3^2 = 9 \), making the next step 9 times larger, creating a **feedback loop** where the walker accelerates or decelerates unpredictably.

This kind of walk could show behavior reminiscent of a **chaotic system** where tiny differences in earlier steps lead to drastically different trajectories, even though each step is based on random events.

### Why It’s Nonlinear

The key feature that makes this random walk nonlinear is that **the size or direction of each step is influenced by previous steps in a nonlinear way**. If each step were just randomly chosen with a constant probability distribution and no dependence on prior outcomes, it would be a linear random walk.

In contrast, by making the step size or direction depend on some **nonlinear function of the previous steps**, the walk becomes more complex, less predictable, and potentially chaotic.

### Conclusion

In summary, a nonlinear random walk means that the evolution of the walker's position is not governed by simple independent random steps but by a system where each step is influenced by the outcome of previous steps in a nonlinear way. This could involve:

- Nonlinear transformations of step sizes (e.g., squaring or exponentiating past steps).
- Modifying the probability distribution of the next step based on past movements.
  
The result is a system that behaves in a much more complicated and unpredictable way than a typical linear random walk.

---

Using a **random walk** on a dice roll is an interesting way to introduce some dynamism into what would normally be a simple, static outcome (the roll of a die). Essentially, instead of each roll being independent, you can treat the dice rolls as part of a sequence where each outcome is influenced by previous rolls, either directly or through some process.

Here's how you could set up a **random walk** using a dice roll:

### Basic Idea
The basic concept is that you start with an initial value (say, 0), and after each dice roll, the outcome determines the next "step" in the walk. The dice roll outcome could influence either the **step size** or **direction** of the walk, and depending on how you structure this, you could use various forms of randomness and dependence between rolls.

### Step-by-Step Guide: Random Walk with Dice Rolls

1. **Initial Setup:**
   - Start at an initial position, say \( x_0 = 0 \).
   - Determine the number of dice you're rolling. You could roll a single die, multiple dice, or even use the sum of several dice rolls.

2. **Roll the Die(s):**
   - For each roll, you will obtain a number from the die(s). This will be your **current step size** in the random walk. 
     - For example, if you're using a standard 6-sided die, the result of each roll will be a number between 1 and 6.
  
3. **Update Position:**
   - You can update the current position based on the result of the die roll. The movement could depend on the value of the dice:
     - **Simple random walk**: After each roll, move by the number you rolled. If you rolled a 3, the next position will be \( x_n = x_{n-1} + 3 \).
     - **Bipolar random walk (or back and forth)**: The dice roll could determine the direction of movement (positive or negative). For example, if you roll a 3, you move 3 steps forward; if you roll a 2, you move 2 steps backward.
     - **Nonlinear random walk**: Use a nonlinear function to modify the step size or direction based on the result of the previous rolls.

4. **Adding Nonlinear Effects:**
   - Instead of a simple movement of the exact number rolled, introduce some form of **nonlinear transformation**. For example:
     - Square the value of the dice roll: if you roll a 4, instead of adding 4, add \( 4^2 = 16 \) to the position.
     - Use an exponential or logarithmic function to adjust the step size.
     - Use the sum of previous rolls to determine the step size for the next one, for example: 
       \[
       \text{next step} = \text{step from roll } n + \text{(previous step size)}^2.
       \]
     - This would create compounding effects where large rolls could amplify the changes in position, and smaller rolls might dampen them.

5. **Optional: Introducing Feedback or Memory:**
   - Instead of purely using the result of the current roll, you could introduce a **feedback mechanism** where the current position or step size is influenced by the history of previous rolls. For example:
     - After each roll, the movement could be modified by some function of the **previous roll**. If the previous roll was very high, the movement might be amplified or reduced according to some nonlinear function.
     - A "bias" could also be introduced based on previous positions or past outcomes. For example, after rolling several low numbers, you could increase the likelihood of larger steps (or vice versa).

---

### Example 1: Simple Random Walk on a Single Die Roll

Let’s implement a **basic random walk** using a single 6-sided die. In this case, you update your position after each roll and just add or subtract the result to your position.

**Step-by-step:**
- Initial position: \( x_0 = 0 \).
- Roll the die and let’s assume the result is 4. Update position: \( x_1 = x_0 + 4 = 0 + 4 = 4 \).
- Roll the die again and get a 2. Update position: \( x_2 = x_1 + 2 = 4 + 2 = 6 \).
- Roll the die again and get a 5. Update position: \( x_3 = x_2 + 5 = 6 + 5 = 11 \).
- The walk continues.

### Example 2: Nonlinear Random Walk Using Squared Steps

Let’s say the step size is **nonlinearly** determined by the square of the dice roll. So, if you roll a 4, you would add \( 4^2 = 16 \) instead of just 4.

**Step-by-step:**
- Initial position: \( x_0 = 0 \).
- Roll a die: result is 4. The step size is \( 4^2 = 16 \), so:  
  \( x_1 = x_0 + 16 = 0 + 16 = 16 \).
- Roll the die again and get a 2. The step size is \( 2^2 = 4 \), so:  
  \( x_2 = x_1 + 4 = 16 + 4 = 20 \).
- Roll a die again and get a 6. The step size is \( 6^2 = 36 \), so:  
  \( x_3 = x_2 + 36 = 20 + 36 = 56 \).

Now the position grows much faster because each step is squared.

### Example 3: Bipolar Random Walk on a Dice Roll

In this variant, the direction of movement (positive or negative) is determined by the **dice roll**. For example, odd numbers could mean moving forward, and even numbers could mean moving backward.

**Step-by-step:**
- Initial position: \( x_0 = 0 \).
- Roll a die: result is 3 (odd, move forward). Update position:  
  \( x_1 = x_0 + 3 = 0 + 3 = 3 \).
- Roll the die again and get a 6 (even, move backward). Update position:  
  \( x_2 = x_1 - 6 = 3 - 6 = -3 \).
- Roll the die again and get a 5 (odd, move forward). Update position:  
  \( x_3 = x_2 + 5 = -3 + 5 = 2 \).

This results in a "bipolar" random walk where the direction alternates based on the dice roll.

### Example 4: Feedback-Based Random Walk

In this example, the next step is influenced by the **previous step**'s result. For example, after each roll, the next step size could be the result of the roll **multiplied by the previous step**.

**Step-by-step:**
- Initial position: \( x_0 = 0 \).
- Roll a die: result is 3. The step size is 3, so:  
  \( x_1 = x_0 + 3 = 0 + 3 = 3 \).
- Roll the die again and get a 2. The step size is \( 2 \times 3 = 6 \), so:  
  \( x_2 = x_1 + 6 = 3 + 6 = 9 \).
- Roll the die again and get a 4. The step size is \( 4 \times 6 = 24 \), so:  
  \( x_3 = x_2 + 24 = 9 + 24 = 33 \).

Here, the movement depends on the previous roll, and the walk "compounds" over time.

---

### Conclusion

A **random walk on a dice roll** adds an extra layer of complexity by introducing the idea of progression over time rather than treating each roll as independent. You can introduce nonlinearity by modifying the step size or direction in ways that depend on the history of previous rolls (e.g., squaring the roll, feedback loops, etc.).

This allows you to create more interesting, unpredictable, and complex behavior compared to the straightforward, independent outcomes of typical dice rolls.


