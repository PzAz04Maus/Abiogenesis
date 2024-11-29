{
  "animals": [
    {
      "category": "Pack animal",
      "type": "Camel",
      "description": "An ill-tempered ungulate adapted for desert life. Camels have been domesticated for use as mounts, but rarely serve as draft animals. Range: Native to arid regions of Asia and northern Africa. A substantial wild population descended from domestic animals also exists in Australia.",
      "attributes": {
        "Awareness": 7,
        "Coordination": 5,
        "Fitness": 12,
        "Muscle": 12,
        "Cunning": 5
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 12,
        "Serious": 18,
        "Critical": 24
      },
      "speed": {
        "Sprint": "36m",
        "Run": "18m",
        "Walk": "9m",
        "Stagger": "4m"
      },
      "travel_speed": "20 km/hr",
      "load": "120/300 kg",
      "attacks": [
        {
          "name": "Hooves",
          "damage": 4,
          "penetration": "x4",
          "speed": "3/5/8"
        }
      ],
      "meat": "350 kg"
    },
    {
	  "category": "Pack animal",
      "type": "Donkey/Mule",
      "description": "Donkeys and mules are the most sure-footed of pack animals. A mule is a sterile cross between a donkey and a horse. Mules make much better pack animals than donkeys; the latter are ill-tempered (-1 penalty to all training attempts and control checks) but capable of reproduction. Range: Global.",
      "attributes": {
        "Awareness": 8,
        "Coordination": 5,
        "Fitness": 10,
        "Muscle": 10,
        "Cunning": 5
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 10,
        "Serious": 15,
        "Critical": 20
      },
      "speed": {
        "Sprint": "40m",
        "Run": "20m",
        "Walk": "10m",
        "Stagger": "4m"
      },
      "travel_speed": "14 km/hr",
      "load": "95/170 kg",
      "attacks": [
        {
          "name": "Hooves",
          "damage": 2,
          "penetration": "x4",
          "speed": "2/3/5"
        }
      ],
      "meat": "180 kg"
    },
    {
	  "category": "Pack animal",
	  "type": "Horse, draft",
      "description": "A draft horse is a 'cold-blood' horse, such as a Percheron, Belgian, or Clydesdale, bred for strength, docility, and endurance rather than agility or speed. Range: Global.",
      "attributes": {
        "Awareness": 9,
        "Coordination": 7,
        "Fitness": 14,
        "Muscle": 14,
        "Cunning": 5
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 13,
        "Serious": 20,
        "Critical": 26
      },
      "speed": {
        "Sprint": "36m",
        "Run": "18m",
        "Walk": "9m",
        "Stagger": "4m"
      },
      "travel_speed": "12 km/hr",
      "load": "115/210 kg",
      "attacks": [
        {
          "name": "Hooves",
          "damage": 4,
          "penetration": "x4",
          "speed": "3/5/8"
        }
      ],
      "meat": "250 kg"
    },
    {
	  "category": "Pack animal",
      "type": "Horse, riding (Quarter, Arabian, or Thoroughbred)",
      "description": "A riding horse is a 'warm-blood' breed, such as an Arabian, Thoroughbred, or Quarter Horse, bred for pleasure riding and racing. They are swift and sure-footed but lighter than draft horses. Range: Global.",
      "attributes": {
        "Awareness": 9,
        "Coordination": 7,
        "Fitness": 12,
        "Muscle": 12,
        "Cunning": 5
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 12,
        "Serious": 18,
        "Critical": 24
      },
      "speed": {
        "Sprint": "40m",
        "Run": "20m",
        "Walk": "10m",
        "Stagger": "4m"
      },
      "travel_speed": "14 km/hr",
      "load": "90/165 kg",
      "attacks": [
        {
          "name": "Hooves",
          "damage": 4,
          "penetration": "x4",
          "speed": "3/5/8"
        }
      ],
      "meat": "200 kg"
    },
    {
	  "category": "Pack animal",
      "type": "Ox",
      "description": "A domesticated cow or bull used for agricultural or as a pack animal. Range: Global.",
      "attributes": {
        "Awareness": 7,
        "Coordination": 5,
        "Fitness": 15,
        "Muscle": 15,
        "Cunning": 5
      },
      "wound_thresholds": {
        "Slight": 1,
        "Moderate": 14,
        "Serious": 21,
        "Critical": 28
      },
      "speed": {
        "Sprint": "30m",
        "Run": "15m",
        "Walk": "8m",
        "Stagger": "4m"
      },
      "travel_speed": "12 km/hr",
      "load": "180/325 kg",
      "attacks": [
        {
          "name": "Hooves",
          "damage": 4,
          "penetration": "x4",
          "speed": "3/5/8"
        },
        {
          "name": "Gore",
          "damage": 8,
          "penetration": "x3",
          "speed": "5/8/11"
        }
      ],
      "meat": "280 kg"
    },
    {
"category": "pack animal",
  "type": "Elephant",
  "description": "The largest land mammal. Elephants cannot be easily trained (-2 penalty on all appropriate checks), but are used as agricultural labor and pack animals in Asia.",
  "range": "Asia and parts of Africa",
  "attributes": {
    "Awareness": 8,
    "Coordination": 4,
    "Fitness": 15,
    "Muscle": 17,
    "Cunning": 5
  },
  "wound_thresholds": {
    "Slight": 1,
    "Moderate": 14,
    "Serious": 21,
    "Critical": 28
  },
  "armor": {
    "value": 1,
    "coverage": "90%"
  },
  "speed": {
    "sprint": "36m",
    "run": "18m",
    "walk": "9m",
    "stagger": "4m"
  },
  "travel_speed": "18 km/hr",
  "load_capacity": {
    "normal": "300 kg",
    "maximum": "600 kg"
  },
  "attacks": [
    {
      "name": "Gore",
      "damage": 15,
      "penetration": "x4",
      "speed": "6/9/12"
    },
    {
      "name": "Trample",
      "damage": 30,
      "penetration": "x4",
      "speed": "10/15/23"
    }
  ],
  "meat": "2 tons"
}
]
}