# SIMPLE VEHICLES
## Street Bike
```yaml
name: "Street Bike"
category: "Simple Vehicle"
subcategory: "Bicycle Variant"
description: ""
barter_value: "GG50"
street_price: "$250"
configuration: ""
suspension: "Std."
crew: ""
cargo: ""
weight: "9 kg"
travel_speed: "(6 + Fitness)/1"
combat_speed: "(17 + Fitness*3)/3"
fuel: ""
fuel_consumption: ""
maintenance: "1"
armor:
  hull_front: ""
  hull_side: ""
  hull_rear: ""
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: ""
  soft_skinned: ""
equipment:
  armament: []
  sensors: []
  comms: []
  aux: []
notes: ""
```

---

## Mountain Bike
```yaml
name: "Mountain Bike"
category: "Simple Vehicle"
subcategory: "Bicycle"
description: ""
barter_value: "GG70"
street_price: "$350"

configuration: ""
suspension: "OR"
crew: ""
cargo: ""
weight: "14 kg"

travel_speed: "(5 + Fitness)/(4 + Fitness)"
combat_speed: "(14 + Fitness*3)/(11 + Fitness*3)"

fuel: ""
fuel_consumption: ""

maintenance: "1"

armor:
  hull_front: ""
  hull_side: ""
  hull_rear: ""
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: ""
  soft_skinned: ""

equipment:
  armament: []
  sensors: []
  comms: []
  aux: []

notes: ""

```
(Insert text)

---

## Motorcycle, Cruiser
```yaml
name: "Motorcycle, Cruiser"
category: "Simple Vehicle"
subcategory: "Motorcycle"

description: "A large, moderately comfortable motorbike designed for long cross-country journeys on good roads."

barter_value: "GG2,100"
street_price: "$17,000"

configuration: ""
suspension: "Std"
crew: "1+1"
cargo: "50 kg"
weight: "370 kg"

travel_speed: "53/5 km/hr"
combat_speed: "147/14 m"

fuel: "25 L (G)"
fuel_consumption: "5 L/hr"

maintenance: "2"

armor:
  hull_front: ""
  hull_side: ""
  hull_rear: ""
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "1"
  soft_skinned: ""

equipment:
  armament: []
  sensors: ["Headlight"]
  comms: []
  aux: []

notes: ""

```
(Insert text)

---

## Motorcycle, Off-Road
```yaml
name: "Motorcycle, Off-Road"
category: "Simple Vehicle"
subcategory: "Motorcycle"

description: "A typical dirt bike used by recreational riders and, rarely during the Twilight War, by military scouts."

barter_value: "GG1,400"
street_price: "$5,500"

configuration: ""
suspension: "OR"
crew: "1+1"
cargo: "25 kg"
weight: "130 kg"

travel_speed: "40/12 km/hr"
combat_speed: "111/33 m"

fuel: "24 L (G)"
fuel_consumption: "6 L/hr"

maintenance: "2"

armor:
  hull_front: ""
  hull_side: ""
  hull_rear: ""
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "1"
  soft_skinned: ""

equipment:
  armament: []
  sensors: ["Headlight"]
  comms: []
  aux: []

notes: ""

```
(Insert text)

---

## Snowmobile
```yaml
name: "Snowmobile"
category: "Simple Vehicle"
subcategory: "Snow Vehicle"

description: "Optimized for snow and ice, a snowmobile uses skis for steering and tracks for propulsion. On any surface other than snow and ice, control checks suffer a -2 penalty."

barter_value: "GG625"
street_price: "$5,000"

configuration: ""
suspension: "OR"
crew: "1+1"
cargo: "50 kg"
weight: "340 kg"

travel_speed: "43/21 km/hr"
combat_speed: "120/58 m"

fuel: "50 L (G) or 50 L (D)"
fuel_consumption: "5 L/hr"

maintenance: "2"

armor:
  hull_front: ""
  hull_side: ""
  hull_rear: ""
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "2"
  soft_skinned: ""

equipment:
  armament: []
  sensors: ["Headlight"]
  comms: []
  aux: ["Heated seats", "Heated handlebars"]

notes: ""

```
(Insert text)

---

# PASSENGER VEHICLES

## Economy Car
```yaml
name: "Economy Car"
category: "Passenger Vehicle"
subcategory: "Standard Automobile"

description: "A small, light commuter vehicle whose main prewar advantages were low price and high fuel efficiency. Hybrid versions were also available, having become popular due to rising oil prices in the late 2000s."

barter_value:
  base: "GG2,100"
  hybrid: "GG3,500"

street_price:
  base: "$17,000"
  hybrid: "$21,000"

configuration: "Standard"
suspension: "Std"
crew: "1+3"

cargo:
  base: "150 kg"
  hybrid: "100 kg"

weight:
  base: "1.1 tons"
  hybrid: "1.2 tons"

travel_speed: "48/5 km/hr"
combat_speed: "133/14 m"

fuel:
  base: "50 L (G)"
  hybrid: "50 L (GH)"

fuel_consumption:
  base: "3.6 L/hr"
  hybrid: "2.3 L/hr"

maintenance:
  base: "3"
  hybrid: "6"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "2"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: []

notes: ""

```
(Insert text)

---

## Full-Size Car
```yaml
name: "Full-Size Car"
category: "Passenger Vehicle"
subcategory: "Standard Automobile"

description: "A standard passenger car designed to seat five adults in relative comfort. Diesel variants saw limited acceptance in North America, though they were common in Europe. Several hybrid models were introduced in the early 2010s following the success of hybrid economy cars."

barter_value:
  base: "GG3,250"
  hybrid: "GG5,500"

street_price:
  base: "$26,000"
  hybrid: "$33,000"

configuration: "Standard"
suspension: "Std"
crew: "1+4"

cargo:
  base: "350 kg"
  hybrid: "250 kg"

weight:
  base: "1.6 tons"
  hybrid: "1.7 tons"

travel_speed: "66/5 km/hr"
combat_speed: "183/14 m"

fuel:
  gasoline:
    base: "60 L (G)"
    hybrid: "60 L (GH)"
  diesel:
    base: "60 L (D)"
    hybrid: "60 L (DH)"

fuel_consumption:
  gasoline:
    base: "6.1 L/hr"
    hybrid: "4.1 L/hr"
  diesel:
    base: "4.2 L/hr"
    hybrid: "2.8 L/hr"

maintenance:
  base: "4"
  hybrid: "8"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "2"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: []

notes: ""

```
(Insert text)

---

## Muscle Car
```yaml
name: "Muscle Car"
category: "Passenger Vehicle"
subcategory: "High-Performance Automobile"

description: "A large, powerful car designed for straight-line acceleration and top speed. In 2013, muscle cars are impractical, but popular with survivors of a certain mindset."

barter_value: "GG3,500"
street_price: "$30,000"

configuration: "Standard"
suspension: "Std"
crew: "1+3"
cargo: "150 kg"
weight: "1.6 tons"

travel_speed: "75/5 km/hr"
combat_speed: "209/1_

```
(Insert text)

---

## Sports Car
```yaml
name: "Sports Car"
category: "Passenger Vehicle"
subcategory: "High-Performance Automobile"

description: "A light, swift, agile, and now extremely impractical vehicle. In opposed control checks, a sports car provides its driver a +2 bonus."

barter_value: "GG5,000"
street_price: "$60,000"

configuration: "Standard"
suspension: "Std"
crew: "1+1"
cargo: "50 kg"
weight: "1.2 tons"

travel_speed: "90/1 km/hr"
combat_speed: "250/3 m"

fuel: "50 L (G)"
fuel_consumption: "6.2 L/hr"

maintenance: "6"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "2"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: []

notes: "+2 bonus to opposed control checks."

```

---

## Jeep
```yaml
name: "Jeep"
category: "Passenger Vehicle"
subcategory: "4x4 Utility Vehicle"

description: "A light 4x4 vehicle designed for extensive off-road use. Formerly a military staple, jeeps were supplanted by light tactical vehicles in the 1980s."

barter_value: "GG5,000"
street_price: "$20,000"

configuration: "Standard"
suspension: "OR"
crew: "1+3"
cargo: "250 kg (+4 tons towed)"
weight: "1.2 tons"

travel_speed: "40/11 km/hr"
combat_speed: "111/31 m"

fuel: "50 L (G)"
fuel_consumption: "4.8 L/hr"

maintenance: "4"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: ["Self-recovery winch (1.5-ton limit; not suitable for towing)"]

notes: ""

```

---

## Light SUV
```yaml
name: "Light SUV"
category: "Passenger Vehicle"
subcategory: "SUV"

description: "Despite the name, few light SUVs had any off-road capability beyond that of a passenger car. Some manufacturers offered hybrid versions."

barter_value:
  base: "GG2,750"
  hybrid: "GG4,800"

street_price:
  base: "$22,000"
  hybrid: "$29,000"

configuration: "Standard"
suspension: "Std"
crew: "1+3"

cargo:
  base: "350 kg"
  hybrid: "300 kg"

weight:
  base: "1.8 tons"
  hybrid: "1.9 tons"

travel_speed: "59/8 km/hr"
combat_speed: "164/22 m"

fuel:
  base: "60 L (G)"
  hybrid: "60 L (GH)"

fuel_consumption:
  base: "4.9 L/hr"
  hybrid: "3.8 L/hr"

maintenance:
  base: "4"
  hybrid: "8"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "2"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: []

notes: ""
```

---

## Heavy SUV
```yaml
name: "Heavy SUV"
category: "Passenger Vehicle"
subcategory: "SUV"

description: "Unlike their smaller brethren, most heavy SUVs had at least moderate off-road capabilities. Luxury models traded this advantage for leather seats and premium sound systems (double Street Price and change Suspension to Std; no other game effect)."

barter_value: "GG4,500"
street_price: "$36,000"

configuration: "Standard"
suspension: "OR"
crew: "1+4"
cargo: "500 kg (+4 tons towed)"
weight: "2.1 tons"

travel_speed: "59/8 km/hr"
combat_speed: "164/22 m"

fuel:
  gasoline: "70 L (G)"
  diesel: "70 L (D)"

fuel_consumption:
  gasoline: "6 L/hr"
  diesel: "5.4 L/hr"

maintenance: "4"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: []

notes: "Luxury model: double Street Price and change suspension to Std (no other game effect)."

```
---

## Light Pickup

```yaml
name: "Light Pickup"
category: "Commercial Vehicle"
subcategory: "Pickup Truck"

description: "A small utility truck, seen worldwide in a variety of roles. Cargo carried in the bed is exposed and can be targeted independently of the vehicle."

barter_value: "GG1,750"
street_price: "$14,000"

configuration: "Standard"
suspension: "OR"
crew: "1+2"
cargo: "500 kg (+2 tons towed)"
weight: "1.5 tons"

travel_speed: "48/8 km/hr"
combat_speed: "133/22 m"

fuel: "60 L (G)"
fuel_consumption: "4.6 L/hr"

maintenance: "4"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: []

notes: ""
```

---

## Heavy SUV

```yaml
name: "Heavy Pickup"
category: "Commercial Vehicle"
subcategory: "Pickup Truck"

description: "A larger, heavier pickup, sold mostly on the North American market. This entry represents a king cab model with a second row of seats. Standard-cab models have Crew 1+2 and Cargo 1,000 kg."

barter_value: "GG2,750"
street_price: "$22,000"

configuration: "Standard"
suspension: "OR"
crew: "1+4"
cargo: "750 kg (+4.5 tons towed)"
weight: "1.9 tons"

travel_speed: "48/8 km/hr"
combat_speed: "133/22 m"

fuel:
  gasoline: "70 L (G)"
  diesel: "70 L (D)"

fuel_consumption:
  gasoline: "9 L/hr"
  diesel: "8 L/hr"

maintenance: "4"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: ["Self-recovery winch (3-ton limit; not suitable for towing)"]

notes: "Standard-cab model: Crew 1+2, Cargo 1,000 kg."

```

---

## Van

```yaml
name: "Van"
category: "Commercial Vehicle"
subcategory: "Van"

description: "A large box on wheels with an engine, available in both cargo and passenger models."

barter_value: "GG4,000"
street_price: "$32,000"

configuration: "Standard"
suspension: "Std"

crew:
  cargo_model: "1+1"
  passenger_model: "1+9"

cargo:
  cargo_model: "1.5 tons"
  passenger_model: "300 kg"

weight: "3.5 tons"

travel_speed: "53/8 km/hr"
combat_speed: "147/22 m"

fuel:
  gasoline: "80 L (G)"
  diesel: "80 L (D)"

fuel_consumption:
  gasoline: "11 L/hr"
  diesel: "10 L/hr"

maintenance: "4"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "2"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: []

notes: "Both cargo and passenger variants exist."

```
# COMMERCIAL VEHICLES


## Truck, 2.5 ton
```yaml
name: "Truck, 2.5-ton"
category: "Commercial Vehicle"
subcategory: "Medium Truck"

description: "A commercial delivery truck, typically used for intra-city transport. Military versions are the core of transportation units in armies worldwide."

barter_value:
  civilian: "GG4,000"
  military: "GG4,500"

street_price:
  civilian: "$30,000"
  military: "$36,000"

configuration: "Standard"

suspension:
  civilian: "Std"
  military: "OR"

crew: "1+2"

cargo: "2.5 tons (+6 tons towed)"
weight: "6.5 tons"

travel_speed: "30/5 km/hr"
combat_speed: "83/14 m"

fuel: "190 L (D)"
fuel_consumption: "24 L/hr"

maintenance: "8"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux:
    civilian: ["Hydraulic lift on tailgate (750 kg capacity)"]
    military: []

notes: |
  The 2.5-, 5-, and 10-ton trucks may be configured as open-bed, closed cargo box, or bulk liquid tank trucks.

  • Closed cargo box: Increase vehicle weight by 10%.
  • Bulk liquid tank capacity:
      - 2.5-ton truck: 2,200 liters
      - 5-ton truck: 5,500 liters
      - 10-ton truck: 9,500 liters
  • Bulk liquid tank configuration replaces normal cargo-handling equipment with an electric pump (100 L/min flow rate).



```
(Insert text)

---

## Truck, 5 ton
```yaml
name: "Truck, 5-ton"
category: "Commercial Vehicle"
subcategory: "Heavy Truck"

description: "A progressively heavier cargo vehicle. As with the 2.5-ton truck, it is available in both civilian and military iterations."

barter_value:
  civilian: "GG5,000"
  military: "GG6,000"

street_price:
  civilian: "$40,000"
  military: "$48,000"

configuration: "Standard"

suspension:
  civilian: "Std"
  military: "OR"

crew: "1+2"

cargo: "5 tons (+11 tons towed)"
weight: "9 tons"

travel_speed: "30/7 km/hr"
combat_speed: "83/19 m"

fuel: "240 L (D)"
fuel_consumption: "30 L/hr"

maintenance: "8"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux:
    civilian: ["Hydraulic lift on tailgate (1 ton capacity)"]
    military: []

notes: |
  The 2.5-, 5-, and 10-ton trucks may be configured as open-bed, closed cargo box, or bulk liquid tank trucks.

  • Closed cargo box: Increase vehicle weight by 10%.
  • Bulk liquid tank capacity:
      - 2.5-ton truck: 2,200 liters
      - 5-ton truck: 5,500 liters
      - 10-ton truck: 9,500 liters
  • Bulk liquid tank configuration replaces normal cargo-handling equipment with an electric pump (100 L/min flow rate).



```
(Insert text)

---

## Truck, 10-ton
```yaml
name: "Truck, 10-ton"
category: "Commercial Vehicle"
subcategory: "Heavy Truck"

description: "A yet heavier cargo truck, also available in civilian and military versions."

barter_value:
  civilian: "GG7,500"
  military: "GG8,500"

street_price:
  civilian: "$60,000"
  military: "$70,000"

configuration: "Standard"
suspension: "OR"

crew: "1+2"

cargo: "10 tons (+11 tons towed)"
weight: "19 tons"

travel_speed: "30/7 km/hr"
combat_speed: "83/19 m"

fuel: "480 L (D)"
fuel_consumption: "60 L/hr"

maintenance: "8"

armor:
  hull_front: "2"
  hull_side: "2"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "4"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Headlights"]
  comms: []
  aux: ["Cargo-handling crane (3-ton load limit)"]

notes: |
  The 2.5-, 5-, and 10-ton trucks may be configured as open-bed, closed cargo box, or bulk liquid tank trucks.

  • Closed cargo box: Increase vehicle weight by 10%.
  • Bulk liquid tank capacity:
      - 2.5-ton truck: 2,200 liters
      - 5-ton truck: 5,500 liters
      - 10-ton truck: 9,500 liters
  • Bulk liquid tank configuration replaces normal cargo-handling equipment with an electric pump (100 L/min flow rate).


```
(Insert text)

---

## Bus, Coach

```yaml
name: "Bus, Coach"
category: "Commercial Vehicle"
subcategory: "Passenger Transport"

description: "A standard long-distance coach designed for intercity travel."

barter_value: "GG4,200"
street_price: "$420,000"

configuration: "Standard"
suspension: "Std"
crew: "1+45"
cargo: "3 tons"
weight: "13.5 tons"

travel_speed: "43/2 km/hr"
combat_speed: "120/14 m"

fuel: "480 L (D)"
fuel_consumption: "38 L/hr"

maintenance: "8"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Civilian mapping GPS", "Headlights"]
  comms: []
  aux: ["Chemical toilet"]

notes: ""

```

---

## Motor Home

```yaml
name: "Motor Home"
category: "Commercial Vehicle"
subcategory: "Recreational Vehicle"

description: "A medium-sized family motor home built on a minibus chassis. Mobile living quarters come in a variety of sizes; this entry represents a typical mid-sized unit."

barter_value: "GG8,000"
street_price: "$70,000"

configuration: "Standard"
suspension: "Std"
crew: "1+4"
cargo: "500 kg"
weight: "4 tons"

travel_speed: "35/4 km/hr"
combat_speed: "97/12 m"

fuel: "100 L (D)"
fuel_consumption: "8 L/hr"

maintenance: "6"

armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Civilian mapping GPS", "Headlights"]
  comms: []
  aux:
    - "Diesel generator (1.25 kW, 2 L/hr)"
    - "Living quarters for 6 (chemical toilet, kitchenette, shower, water heater)"

notes: ""

```

---
## Semi-Tractor, Sleeper
```yaml
name: "Semi-Tractor"
category: "Commercial Vehicle"
subcategory: "Long-Haul Tractor"

description: "The backbone of commercial ground transport in most developed nations. The following traits represent a long-haul sleeper cab containing a small bunk area."

barter_value: "GG7,000"
street_price: "$125,000"

configuration: "Standard"
suspension: "Std"
crew: "1+2"

cargo: "250 kg (+41 tons towed)"
weight: "11 tons"

travel_speed: "43/4 km/hr"
combat_speed: "120/11 m"

fuel: "950 L (D)"
fuel_consumption: "17 L/hr"

maintenance: "12"

armor:
  hull_front: "2"
  hull_side: "2"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "4"
  soft_skinned: "yes"

equipment:
  armament: []
  sensors: ["Civilian mapping GPS", "Headlights"]
  comms: ["Vehicular CB radio"]
  aux:
    - "Sleeping quarters for 2 (bunks and very small appliances)"

notes: ""
```
(Insert text)