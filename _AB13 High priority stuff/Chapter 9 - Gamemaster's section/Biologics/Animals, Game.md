{
  "animals": [
    {
      "category": "Game animal",
      "type": "Bison/Buffalo",
      "description": "The wild counterparts to domestic cattle. Range: Eastern Europe (rare); North America (rare); Africa; Southeast Asia.",
      "attributes": {
        "Awareness": 7,
        "Coordination": 5,
        "Fitness": 16,
        "Muscle": 16,
        "Cunning": 7
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 15,
        "Serious": 23,
        "Critical": 30
      },
      "speed": {
        "Sprint": "30m",
        "Run": "15m",
        "Walk": "8m",
        "Stagger": "4m"
      },
      "attacks": [
        {
          "name": "Hooves",
          "damage": 4,
          "penetration": "x4",
          "speed": "3/5/8"
        },
        {
          "name": "Gore",
          "damage": 12,
          "penetration": "x2",
          "speed": "5/8/11"
        }
      ],
      "notes": "Most buffalo will attack only in extreme circumstances, but some African species are viciously territorial and have been known to stalk small groups of people.",
      "meat": "350 kg"
    },
    {
      "category": "Game animal",
      "type": "Burrower",
      "description": "This entry represents any variety of non-predatory small land mammal, including ground squirrels, rabbits, beavers, pikas, marmots, and woodchucks. Range: Global.",
      "attributes": {
        "Awareness": 9,
        "Coordination": 9,
        "Fitness": 1,
        "Muscle": 1,
        "Cunning": 7
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 2,
        "Serious": 3,
        "Critical": 4
      },
      "speed": {
        "Sprint": "32m",
        "Run": "16m",
        "Walk": "8m",
        "Stagger": "4m"
      },
      "attacks": [
        {
          "name": "Bite",
          "damage": -1,
          "penetration": "x4",
          "speed": "1/2/4"
        }
      ],
      "notes": "Burrowers will attack only if cornered or grappled.",
      "meat": "1 to 5 kg (1d10/2)"
    },
    {
      "category": "Game animal",
      "type": "Fowl",
      "description": "Any one of a wide array of game birds, including both land- and waterfowl. This entry can also represent domestic poultry. Range: Global, except for extreme polar regions.",
      "attributes": {
        "Awareness": 6,
        "Coordination": 8,
        "Fitness": 3,
        "Muscle": 2,
        "Cunning": 5
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 4,
        "Serious": 6,
        "Critical": 8
      },
      "speed": {
        "Flap": "60m",
        "Glide": "20m",
        "Plummet Aimlessly": "10m",
        "Waddle": "3m"
      },
      "attacks": [
        {
          "name": "Peck, claw, or wing buffet",
          "damage": -2,
          "penetration": "Nil",
          "speed": "2/3/5"
        }
      ],
      "notes": "Fowl will attack only if grappled.",
      "meat": "1d6 kg"
    },
    {
      "category": "Game animal",
      "type": "Grazer",
      "description": "This entry represents the wide array of hoofed (and usually horned) herbivores present in most regions of the world, including deer, elk, gazelle, antelope, and similar creatures. Large, aggressive relatives such as moose should be represented with bison/buffalo traits. Range: Global, except for extreme polar regions and Australia.",
      "attributes": {
        "Awareness": 7,
        "Coordination": 7,
        "Fitness": 9,
        "Muscle": 7,
        "Cunning": 7
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
        "Stagger": "5m"
      },
      "attacks": [
        {
          "name": "Kick",
          "damage": 4,
          "penetration": "x4",
          "speed": "2/3/5"
        },
        {
          "name": "Gore",
          "damage": 5,
          "penetration": "x3",
          "speed": "4/6/9"
        }
      ],
      "notes": "Grazers attack only if an enemy enters close combat range and they cannot otherwise escape.",
      "meat": "30 kg"
    },
    {
      "category": "Game animal",
      "type": "Rat",
      "description": "The basic plague-bearing rodent, ubiquitous around the world. High reproductive rates and strong adaptation to a variety of environments make them a common dietary staple for urban survivors. Range: Global.",
      "attributes": {
        "Awareness": 9,
        "Coordination": 11,
        "Fitness": 1,
        "Muscle": 1,
        "Cunning": 9
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 2,
        "Serious": 3,
        "Critical": 4
      },
      "speed": {
        "Sprint": "16m",
        "Run": "8m",
        "Walk": "4m",
        "Stagger": "2m"
      },
      "attacks": [
        {
          "name": "Bite",
          "damage": -4,
          "penetration": "Nil",
        }
      ],
      "notes": "Rats will attack only if cornered or grappled.",
      "meat": "0.25 kg"
    },
    {
      "category": "Game animal",
      "type": "Swine",
      "description": "This entry includes both wild boars and feral pigs. Swine typically live in groups of 2d6x5. Range: Wild boars are native to Central Europe, the Mediterranean Basin, and most of Asia. Feral pigs are present throughout North and South America, most of Europe, and the Pacific islands.",
      "attributes": {
        "Awareness": 5,
        "Coordination": 6,
        "Fitness": 8,
        "Muscle": 8,
        "Cunning": 8
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 9,
        "Serious": 14,
        "Critical": 18
      },
      "armor": "1 (50% coverage)",
      "speed": {
        "Sprint": "24m",
        "Run": "12m",
        "Walk": "6m",
        "Stagger": "3m"
      },
      "attacks": [
        {
          "name": "Gore",
          "damage": 4,
          "penetration": "x2"
        }
      ],
      "notes": "Swine attack with upward slashes of their tusks, typically striking the legs or lower abdomens of human opponents.",
      "meat": "15 kg (European specimens), 30 kg (American and Asian swine)"
    }
  ]
}