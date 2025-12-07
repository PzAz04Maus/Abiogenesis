---
name: Truck, 5-ton
category: Commercial Vehicle, Generic
subcategory: Heavy Truck
description: A progressively heavier cargo vehicle. As with the 2.5-ton truck, it is available in both civilian and military iterations.
barter_value:
  civilian: GG5,000
  military: GG6,000
street_price:
  civilian: $40,000
  military: $48,000
configuration: Standard
suspension:
  civilian: Std
  military: OR
crew: 1+2
cargo: 5 tons (+11 tons towed)
weight: 9 tons
travel_speed: 30/7 km/hr
combat_speed: 83/19 m
fuel: 240 L (D)
fuel_consumption: 30 L/hr
maintenance: "8"
armor:
  hull_front: "1"
  hull_side: "1"
  hull_rear: "1"
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: "3"
  soft_skinned: yes
equipment:
  armament: []
  sensors:
    - Headlights
  comms: []
  aux:
    civilian:
      - Hydraulic lift on tailgate (1 ton capacity)
    military: []
---
notes: |
  The 2.5-, 5-, and 10-ton trucks may be configured as open-bed, closed cargo box, or bulk liquid tank trucks.

  • Closed cargo box: Increase vehicle weight by 10%.
  • Bulk liquid tank capacity:
      - 2.5-ton truck: 2,200 liters
      - 5-ton truck: 5,500 liters
      - 10-ton truck: 9,500 liters
  • Bulk liquid tank configuration replaces normal cargo-handling equipment with an electric pump (100 L/min flow rate).

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

