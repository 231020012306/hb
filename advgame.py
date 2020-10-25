locations = {0: "you are sitting in the front of the computer learning pyhton",
             1: "you are standing at the end of a road before a small brick building",
             2: "you are at the top a hill",
             3: "you are inside a building,a well house for a small stream",
             4: "you are in a valley besides a stream",
             5: "you are in the forest"
             }
exits = {1: {"Q": 0},
         2: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         3: {"N": 5, "Q": 0},
         4: {"W": 1, "Q": 0},
         5: {"N": 1, "W": 3, "Q": 0},
         6: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4, },
              2: {"5": 5, },
              3: {"1": 1, },
              4: {"1": 1, "3": 3, },
              5: {"2": 2, "1": 1, }
              }

vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY'": "4",
    "FOREST": "5"
}

loc = 1
while True:
    avilableExits = ",".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Avilable  Exits are " + avilableExits).upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("you cannot go in that direction!!!!")