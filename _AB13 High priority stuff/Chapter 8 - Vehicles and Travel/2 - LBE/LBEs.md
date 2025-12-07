# Generics 

All bags, pockets, civilian stuff are genericized
# samples

There are 6 current standards for a sample. These can be used for stage 1 rules

## #candidate
Could BT weight class the samples



# Type 56 Chicom
```yaml
name: "Chicom Type 56 Chest Rig"
category: "Chest Rig"
origin: "China (PLA)"
weight: "0.55 kg"
volume: "3–4 L"
mag_capacity:
  ak_30rd: 3
  stripper_clips: 6
pouches:
  primary:
    - "3× AK 30-round magazine pouches"
  auxiliary:
    - "2× grenade/utility pouches"
practical_load: "4–6 kg"
absolute_load: "8–10 kg"
description: "Iconic canvas chest rig issued with the Type 56 AK. Extremely durable, simple, silent. No padding or structure."
notes: ""
```


# AK 3-Cell, Modernized

```yaml
name: "AK 3-cell Chest Rig"
category: "Chest Rig"
origin: "Global / Commercial"
weight: "0.6–0.8 kg"
volume: "4–5 L"
mag_capacity:
  ak_30rd: 3
pouches:
  primary:
    - "3× AK magazine cells"
  auxiliary:
    - "Admin pocket (optional)"
    - "Side utility pouch (optional)"
practical_load: "5–7 kg"
absolute_load: "10–12 kg"
description: "Modern nylon rendition of the classic 3-cell AK chest rig with improved stitching and retention systems."
notes: ""
```

## PLA 5-Cell Chest Rig

```yaml
name: "PLA 5-cell Chest Rig"
category: "Chest Rig"
origin: "China (PLA variants)"
weight: "0.7–0.9 kg"
volume: "5–7 L"
mag_capacity:
  ak_30rd: 5
pouches:
  primary:
    - "5× rifle magazine pouches"
  auxiliary:
    - "2× grenade/utility pockets"
practical_load: "6–8 kg"
absolute_load: "12–14 kg"
description: "Later Chinese chest rig variant with expanded magazine capacity for sustained fire or squad automatic rifle roles."
notes: ""

```

## US M1956 Chest Rig (Improvised / Field-Modified LBEs)**

```yaml
name: "US M1956 Chest Rig"
category: "Chest Rig"
origin: "United States"
weight: "0.7–1.0 kg"
volume: "4–6 L"
mag_capacity:
  m14_20rd: 2–3
  m16_20rd: 3–4
pouches:
  primary:
    - "2× Universal ammo pouches (M14/M16)"
  auxiliary:
    - "First-aid/compass pouch"
practical_load: "5–7 kg"
absolute_load: "12–14 kg"
description: "Not an issued chest rig but commonly field-modified using M1956 components to shift ammo load forward. Used in early Vietnam."
notes: ""

```

## Rhodesian Chest Rig

```yaml
name: "Rhodesian Chest Rig"
category: "Chest Rig"
origin: "Rhodesia"
weight: "0.8–1.0 kg"
volume: "6–8 L"
mag_capacity:
  fnfal_20rd: 4–6
pouches:
  primary:
    - "4–6× FAL magazine pouches"
  auxiliary:
    - "Grenade/utility pockets"
practical_load: "6–8 kg"
absolute_load: "12–15 kg"
description: "Durable canvas chest rig used in the Bush War. Distributed weight well for long patrols, optimized for the FN FAL."
notes: ""

```

## South African Pattern 83 Chest Harness

```yaml
name: "South African Pattern 83 Chest Harness"
category: "Chest Rig"
origin: "South Africa"
weight: "1.2 kg"
volume: "8–12 L"
mag_capacity:
  fnfal_20rd: 6
  ak_30rd: 6
pouches:
  primary:
    - "6× rifle magazine cells"
  auxiliary:
    - "Large central utility pouch"
    - "Side grenade/utility pockets"
practical_load: "8–12 kg"
absolute_load: "16–20 kg"
description: "Legendary combat load-bearing system known for soft, quiet canvas and excellent weight distribution. Used throughout Africa."
notes: ""

```

## PLCE Chest Rig

```yaml
name: "British PLCE Chest Rig"
category: "Chest Rig"
origin: "United Kingdom"
weight: "0.9–1.2 kg"
volume: "6–9 L"
mag_capacity:
  sa80_30rd: 4–6
pouches:
  primary:
    - "Twin 3-cell SA80 magazine pouches"
  auxiliary:
    - "Radio pouch"
    - "Utility pouch"
practical_load: "6–8 kg"
absolute_load: "14–16 kg"
description: "Issued as part of the PLCE system. Rugged, roomy, and compatible with belt order and rucksacks."
notes: ""

```

## Microrig, Modern

```yaml
name: "Modern Micro Chest Rig"
category: "Chest Rig"
origin: "Global / Commercial Tactical"
weight: "0.4–0.7 kg"
volume: "2–3 L"
mag_capacity:
  ar15_30rd: 3
  ak_30rd: 3
pouches:
  primary:
    - "3× elastic rifle magazine inserts"
  auxiliary:
    - "Front admin pouch"
    - "Side wing pouches (optional)"
practical_load: "3–5 kg"
absolute_load: "8–10 kg"
description: "Ultra-lightweight modular micro rig used by modern SOF and police. Minimal structure, highly modular, optimized for speed."
notes: ""

```

## Alice LBE (Belt + Suspenders + Pouches)

```yaml
name: "US ALICE LBE"
category: "Load-Bearing Equipment"
type: "Belt Order / Harness"
origin: "United States"

weight: "1.0 kg"
volume: "9–12 L"
practical_load: "12–15 kg"
absolute_load: "20–22 kg"

components:
  - "LC-2 pistol belt"
  - "Y/H suspenders"
  - "2× Universal ammo pouches (3× 30rd STANAG each)"
  - "2× 1 Qt canteen pouches"
  - "Buttpack (5–8 L)"
  - "Compass/First Aid pouch"

mag_capacity:
  m16_30rd: 6
  m14_20rd: 4 (if using modified pouches)

pouch_details:
  ammo_pouches:
    count: 2
    capacity_each: "3× 30rd mags"
  canteens:
    count: 2
    water_total: "2 L"
  buttpack:
    volume: "5–8 L"

description: >
  Classic US load-bearing equipment used from Vietnam through the 1990s. Weight is carried primarily on the hips,
  with suspenders stabilizing the load. Designed for sustained field operations.

notes: ""
```

## US 1988 Pattern LBV

```yaml
name: "US LBV (1988 Pattern)"
category: "Load-Bearing Equipment"
type: "Vest"
origin: "United States"

weight: "1.5 kg"
volume: "6–10 L"
practical_load: "10–14 kg"
absolute_load: "18–20 kg"

components:
  - "Integrated 4-cell rifle magazine panel"
  - "Grenade/utility pockets"
  - "Pistol belt interface compatible with ALICE pouches"

mag_capacity:
  m16_30rd: 6
  m14_20rd: 4

pouch_details:
  integrated_mag_cells: 4
  grenade_pouches: 2

description: >
  The pre-MOLLE Load Bearing Vest issued in the late 1980s and 1990s. Offered better weight distribution than ALICE LBE
  but had limited modularity.

notes: ""

```