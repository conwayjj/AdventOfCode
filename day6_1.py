with open('day6.txt') as inFile:
    chart = inFile.readlines()

def pathToCOM(loc):
    orbits = 0
    curStar = loc
    path = set()
    while curStar != 'COM':
        orbits += 1
        curStar = starMap[curStar]
        path.add(curStar)
    return orbits, path

starMap = {}
for pair in chart:
    orbitee, orbiter = pair.strip().split(')')
    starMap[orbiter] = orbitee

print(starMap)

totalOrbits = 0
for star in starMap:
    orbits, path = pathToCOM(star)
    #print (star, orbits)
    totalOrbits += orbits

you = starMap['YOU']
santa = starMap['SAN']

youDist,youPath = pathToCOM(you)
santaDist,santaPath = pathToCOM(santa)

print("YOU Path:", youPath)
print("SAN Path:", santaPath)

overlap = []
for planet in youPath:
    if planet in santaPath:
        overlap.append(planet)
print("overlap", overlap)

shortest = len(youPath) + len(santaPath) - 2 * len(overlap) + 2
print("Shortest Path:", shortest)
print ("TOTAL:", totalOrbits)
        
