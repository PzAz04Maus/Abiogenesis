
{
    "animals": [
    {
	"category": "Predator",
	"type": "Alligator/Crocodile",
      "description": "Alligators and crocodiles are biologically different, but physically similar (and thus grouped into a single entry here). Both are predatory aquatic reptiles growing up to five meters long. Gators and crocs are ambush hunters, preferring to lurk underwater or along riverbanks in hopes that meat will blunder within snatching range. They are too stupid to learn to fear humans, and thus can pose a significant threat to travelers who leave the safety of motorized vehicles.",
      "range": "Tropical fresh water and some salt water in Africa, Asia, Australia, and the Americas (crocodiles); subtropical fresh water in North America (alligators).",
      "attributes": {
        "Awareness": 5,
        "Coordination": 5,
        "Fitness": 12,
        "Muscle": 12,
        "Cunning": 7
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 12,
        "Serious": 18,
        "Critical": 24
      },
      "armor": "1 (80% coverage)",
      "speed": {
        "Sprint": "27m",
        "Run": "10m",
        "Walk": "5m",
        "Stagger": "3m"
      },
      "attacks": [
        {
          "name": "Bite",
          "damage": 8,
          "penetration": "x2",
          "speed": "3/5/8"
        }
      ],
      "notes": "When attacking a human-sized target, a gator or croc’s preferred tactic is to grapple to submission, then drag the victim underwater to drown - or to violently spin and thrash to sever the grappled limb.",
      "meat": "50 kg"
    },
    {
      "category": "Bear",
      "types": [
        {
          "type": "Small (Black) Bear",
          "range": "Northwestern South American mountains; most of North America; southeast Asian forests and mountains.",
          "attributes": {
            "Awareness": 6,
            "Coordination": 6,
            "Fitness": 10,
            "Muscle": 12,
            "Cunning": 8
          },
          "wound_thresholds": {
            "Slight": 1,
            "Moderate": 11,
            "Serious": 17,
            "Critical": 22
          },
          "speed": {
            "Sprint": "24m",
            "Run": "12m",
            "Walk": "6m",
            "Stagger": "3m"
          },
          "attacks": [
            {
              "name": "Slap",
              "damage": 6,
              "penetration": "x4",
              "speed": "2/3/5"
            },
            {
              "name": "Bite",
              "damage": 7,
              "penetration": "x2",
              "speed": "3/5/8"
            }
          ],
          "meat": "60 kg"
        },
        {
          "type": "Large (Grizzly or Polar) Bear",
          "range": "Northern polar regions; sub-polar North America, Asia, and Europe.",
          "attributes": {
            "Awareness": 6,
            "Coordination": 5,
            "Fitness": 12,
            "Muscle": 14,
            "Cunning": 7
          },
          "wound_thresholds": {
            "Slight": 1,
            "Moderate": 12,
            "Serious": 18,
            "Critical": 24
          },
          "speed": {
            "Sprint": "30m",
            "Run": "15m",
            "Walk": "8m",
            "Stagger": "4m"
          },
          "attacks": [
            {
              "name": "Slap",
              "damage": 8,
              "penetration": "x4",
              "speed": "3/5/8"
            },
            {
              "name": "Bite",
              "damage": 10,
              "penetration": "x2",
              "speed": "4/6/9"
            }
          ],
          "meat": "120 kg"
        }
      ]
    },
    {
      "category": "Coyote",
      "description": "A predatory and scavenging canid, noted for its ability to colonize virtually any environment except inner cities. Due to the depopulation of native wolf and large cat populations, coyotes are the primary land predators in many areas of North America. They typically move and hunt in small bands (1d3+1 members) rather than the larger packs common to dogs and wolves.",
      "range": "Virtually all biomes of North and Central America.",
      "attributes": {
        "Awareness": 12,
        "Coordination": 8,
        "Fitness": 11,
        "Muscle": 5,
        "Cunning": 12
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 9,
        "Serious": 14,
        "Critical": 18
      },
      "speed": {
        "Sprint": "36m",
        "Run": "18m",
        "Walk": "9m",
        "Stagger": "4m"
      },
      "attacks": [
        {
          "name": "Teeth",
          "damage": 3,
          "penetration": "x3",
          "speed": "1/2/4"
        }
      ],
      "notes": "Coyotes will attack livestock as a matter of course, but generally avoid combat with humans.",
      "meat": "6 kg"
    },
    {
      "category": "Dog",
      "types": [
        {
          "type": "Small (Lap) Dog",
          "range": "Global.",
          "attributes": {
            "Awareness": 8,
            "Coordination": 8,
            "Fitness": 6,
            "Muscle": 3,
            "Cunning": 6
          },
          "wound_thresholds": {
            "Slight": 1,
            "Moderate": 5,
            "Serious": 8,
            "Critical": 10
          },
          "speed": {
            "Sprint": "24m",
            "Run": "12m",
            "Walk": "6m",
            "Stagger": "3m"
          },
          "attacks": [
            {
              "name": "Teeth",
              "damage": 2,
              "penetration": "x4",
              "speed": "1/2/4"
            }
          ],
          "meat": "1d3 kg"
        },
        {
          "type": "Large (Working) Dog",
          "range": "Global.",
          "attributes": {
            "Awareness": 8,
            "Coordination": 7,
            "Fitness": 8,
            "Muscle": 6,
            "Cunning": 7
          },
          "wound_thresholds": {
            "Slight": 1,
            "Moderate": 8,
            "Serious": 12,
            "Critical": 16
          },
          "speed": {
            "Sprint": "27m",
            "Run": "14m",
            "Walk": "7m",
            "Stagger": "4m"
          },
          "attacks": [
            {
              "name": "Teeth",
              "damage": 5,
              "penetration": "x3",
              "speed": "2/3/5"
            }
          ],
          "meat": "1d5+4 kg"
        }
      ]
    },
    {
      "category": "Great Cat",
      "types": [
        {
          "type": "Large Cat",
          "range": "America, Africa, southern Asia, throughout the Americas.",
          "attributes": {
            "Awareness": 11,
            "Coordination": 10,
            "Fitness": 9,
            "Muscle": 9,
            "Cunning": 9
          },
          "wound_thresholds": {
            "Slight": 1,
            "Moderate": 9,
            "Serious": 14,
            "Critical": 18
          },
          "speed": {
            "Sprint": "35m",
            "Run": "18m",
            "Walk": "9m",
            "Stagger": "5m"
          },
          "attacks": [
            {
              "name": "Claw",
              "damage": 6,
              "penetration": "x3",
              "speed": "2/3/5"
            },
            {
              "name": "Bite",
              "damage": 7,
              "penetration": "x2",
              "speed": "3/5/8"
            }
          ],
          "notes": "Large cats prefer to attack from above or the sides, leaping onto their prey and attempting to either break the neck or crush the windpipe.",
          "meat": "25 kg"
        },
        {
          "type": "Tiger",
          "range": "Southeast Asia, Russian Far East.",
          "attributes": {
            "Awareness": 11,
            "Coordination": 9,
            "Fitness": 11,
            "Muscle": 12,
            "Cunning": 9
          },
          "wound_thresholds": {
            "Slight": 1,
            "Moderate": 11,
            "Serious": 17,
            "Critical": 22
          },
          "speed": {
            "Sprint": "35m",
            "Run": "18m",
            "Walk": "9m",
            "Stagger": "5m"
          },
          "attacks": [
            {
              "name": "Claw",
              "damage": 6,
              "penetration": "x3",
              "speed": "2/3/5"
            },
            {
              "name": "Bite",
              "damage": 8,
              "penetration": "x2",
              "speed": "3/5/8"
            }
          ],
          "meat": "40 kg"
        }
      ]
    },
    {
      "category": "House Cat",
      "description": "A small domestic feline of the sort kept as a pet worldwide. In 2013, most have reverted to a predatory existence in feral colonies of up to several dozen. Many communities prize cats for rodent (and thereby disease) control, but few survivors are above hunting them as small game if sufficiently hungry.",
      "range": "Global, save for polar and sub-polar regions.",
      "attributes": {
        "Awareness": 11,
        "Coordination": 11,
        "Fitness": 5,
        "Muscle": 2,
        "Cunning": 9
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 4,
        "Serious": 6,
        "Critical": 8
      },
      "speed": {
        "Sprint": "27m",
        "Run": "14m",
        "Walk": "4m",
        "Stagger": "2m"
      },
      "attacks": [
        {
          "name": "Teeth and retractile claws",
          "damage": -3,
          "penetration": "Nil",
          "speed": "1/1/2"
        }
      ],
      "notes": "Cats are natural ambush hunters when seeking prey and prefer to attack from above. A house cat will not fight a larger opponent unless cornered or diseased, in which case it will attempt to attack the face. If grappled, the cat will attempt to break the grapple; Damage increases to -1 in such a circumstance.",
      "meat": "1 kg"
    },
    {
      "category": "Snake",
      "description": "Like most other predators described here, snakes are disinclined to attack humans, if for no other reason than people are too big for all but the largest constrictors to eat. However, poor judgment in wilderness areas can lead to potentially lethal encounters with venomous serpents.",
      "range": "Cobra-family serpents are found in most tropical and subtropical regions. Viper-family snakes are native globally, except for polar and arctic regions.",
      "attributes": {
        "Awareness": 4,
        "Coordination": 12,
        "Fitness": 4,
        "Muscle": 2,
        "Cunning": 8
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 3,
        "Serious": 5,
        "Critical": 6
      },
      "speed": {
        "Sprint": "9m",
        "Run": "5m",
        "Walk": "2m",
        "Stagger": "1m"
      },
      "attacks": [
        {
          "name": "Bite",
          "damage": -4,
          "penetration": "x4",
          "speed": "1/1/2"
        }
      ],
      "notes": "A snakebite cannot inflict more than a moderate injury, regardless of the damage value. However, any damage value greater than zero indicates the serpent has injected one dose of venom (see p. 181).",
      "meat": "0.25 kg"
    },
    {
      "category": "Wolf",
      "description": "Free of the threat of man, wolf populations have already begun expanding out of the northern and mountainous territories of their prewar refuges. Wolves typically live and hunt in packs (2d10 members) and are cooperative hunters, combining their efforts to bring down a single large prey animal.",
      "range": "Northern forest regions and forested mountains throughout the northern hemisphere, gradually expanding to southern latitudes and lower altitudes.",
      "attributes": {
        "Awareness": 12,
        "Coordination": 7,
        "Fitness": 11,
        "Muscle": 7,
        "Cunning": 9
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 10,
        "Serious": 15,
        "Critical": 20
      },
      "speed": {
        "Sprint": "36m",
        "Run": "18m",
        "Walk": "9m",
        "Stagger": "5m"
      },
      "travel_speed": "5 km/hr",
      "attacks": [
        {
          "name": "Teeth",
          "damage": 7,
          "penetration": "x2",
          "speed": "2/3/5"
        }
      ],
      "notes": "Wolves typically surround a target and launch multiple coordinated grappling attacks, subduing the victim and then tearing out its throat (called attacks to the head).",
      "meat": "12 kg"
    }
  ]
}