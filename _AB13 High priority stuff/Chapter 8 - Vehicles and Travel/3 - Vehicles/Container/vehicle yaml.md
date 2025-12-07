---
name: ""
category: ""
subcategory: ""
description: ""
barter_value: ""
street_price: ""
configuration: ""
suspension: ""
crew: ""
cargo: ""
Bulk (N):
Wt Limit (N):
Volume (N):
weight: ""
travel_speed: ""
combat_speed: ""
fuel: ""
fuel_consumption: ""
maintenance: ""
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
---

```yaml
# MAXIMAL VEHICLE YAML SCHEMA
name: ""
category: ""                # Simple, Passenger, Commercial, Technical, Military, Watercraft
subcategory: ""             # Optional detailed type
description: ""             # Verbatim text goes here
barter_value: ""
street_price: ""
configuration: ""           # Std, Turreted, CIH, Flush Deck, etc.
suspension: ""
crew: ""
cargo: ""
Cargo, n: 
	- Bulk: 
	- Wt: 
	- Vol: 
weight: ""
travel_speed: ""
combat_speed: ""
fuel: ""
fuel_consumption: ""
maintenance: ""
armor:
  hull_front: ""
  hull_side: ""
  hull_rear: ""
  turret_front: ""
  turret_side: ""
  turret_rear: ""
  suspension: ""
  soft_skinned: ""          # yes/no or statline
equipment:
  armament: []
  sensors: []
  comms: []
  aux: []
notes: ""
# Twilight: 2013 — Vehicle Reference
```