from collections import defaultdict
import string

startMap = "########################\n" + \
           "#...............b.C.D.f#\n" + \
           "#.######################\n" + \
           "#.....@.a.B.c.d.A.e.F.g#\n" + \
           "########################\n"

startMap =  "#################\n" + \
            "#i.G..c...e..H.p#\n" + \
            "########.########\n" + \
            "#j.A..b...f..D.o#\n" + \
            "########@########\n" + \
            "#k.E..a...g..B.n#\n" + \
            "########.########\n" + \
            "#l.F..d...h..C.m#\n" + \
            "#################\n"

startMap = "#################################################################################\n" + \
"#.#.........#...#....r#.......#...#.....#.....#...........#.......#......c......#\n" + \
"#X#.#####.#.#.#.#.###.#####.#.#.#.#.###.#.###.#.#######Q###.#.###.#.#####.###.#.#\n" + \
"#...#.....#...#...#.#.....#.#...#.....#.#.#...#.#.....#.....#.#.#.#.#...#.#.#.#.#\n" + \
"#.###.#############.#####.#.###########.#.#.#####.###.#.#####.#.#.###F#.#.#.#.###\n" + \
"#...#.#j......#.......P.#.#.#.......#...#.#.....#...#.#.#.....#...#...#.#...#...#\n" + \
"###.#.#.###.#.#.#######.#.###.#####.#.#.#.#####.###.#.###.#####.###.###.#######.#\n" + \
"#...#.#...#.#.#.......#.#.....#...#...#.#.....#.#...#...#.#...#.#...#...#.....M.#\n" + \
"#.###.#.###.#.#######.#.#######.#.#####.#.###.#.#.#####.#.#.###.#.#####.#.#######\n" + \
"#.#...#.#...#.#.....#.#.........#.......#.#.#.#...#.......#.....#.....#.#...#...#\n" + \
"#.#.#####.###.#.#.###.###################.#.#.###.#############.#.###.#.###.#.#.#\n" + \
"#.#...#...#...#.#...#.#...#.......#.....#...#.#...#.....#.....#.#...#.#...#...#.#\n" + \
"#.###.#.#####.#.###.#.#.#.#.#####.#.#.#####.#.#####.###.#.###.#.###.#.###.#.###.#\n" + \
"#...#.#..g..#.#.#...#.L.#.#.#..n#.#.#...#...#.....#.#..i#.#...#...#.#.#.#.#.#...#\n" + \
"#####.#####.###.#.#.#####.#.#.#.#.#####.#####.###.#.#.###.#.#####.###.#.#.#.#.###\n" + \
"#.....#...#.....#.#.#.......#.#.#...#...#...#...#...#.....#...#...#...#.#.#.#...#\n" + \
"#D#####.#.#######.###.#######.#.###.#.#.#.#.#############.###.#.###U###.#A#####.#\n" + \
"#.......#.#.H...#.....#...E...#...#...#.#.#...#.........#...#.#...#.#...........#\n" + \
"#.#######.#.###.#######.#########.#####.#.###.#.#######.#.###.###.#.###########.#\n" + \
"#.#.....#.#.#.#e........#.....N...#...#.#.#.....#.....#.#.#...#...#...#.......#y#\n" + \
"#.###.#.#.#.#.#########.#.#########.###.#.#######.###.#.###.#####.#.#.#.#####.#.#\n" + \
"#...#.#.#.#.#.....#.O.#.#.#.......#.....#.#...#.....#....z#.#...#.#.#.#.#...#.#.#\n" + \
"###.#.###.#.#.###.#.#####.#.#####.#.#####.#.#.###########.#.###.#.#.#.#.###.#.#.#\n" + \
"#.....#.V.#.#.#...#......o#.#.....#.#...#...#.T.......#.......#.#.#.#.......#.#.#\n" + \
"#######.###.#.#.#############.#####.#.#.#.###########.#########.#.###########.#.#\n" + \
"#.....#...#...#..b#...#.......#.....#.#.#.#.....#...#.........#.#.......#.....#.#\n" + \
"#.###.###.#######.#.#.#####.###.#####.###.#.#####.#.###.#####.#.#######.#.#######\n" + \
"#.#.#.#...#.....#...#...#...#...#.......#.#.#.....#...#.....#.#.......#.#.......#\n" + \
"#.#.#.#.#.#.###.#######.#.###.#########.#.#.#.#######.#####S#.#######.#.#.#####.#\n" + \
"#u#...#.#.#...#.......#.#.....#.......#.#.#.#...#...#.....#.#.....#...#.#.#.#..v#\n" + \
"#.###.#.#.###.#####.#.#.###.###.#####.#.#.#.###.#.#.#####.#######.#.###.#.#.#.#.#\n" + \
"#...#...#...#.#...#.#.#...#...#.#.#...#.#.....#.#.#.#.....#.......#.#.#.#...#.#.#\n" + \
"###.###W#####.#.###.#####.###.#.#.#.###.#.#####.#.#.#####.#.#######.#.#.###.#.###\n" + \
"#...#...#.......#...#...#.#.#...#...#...#.#.....#.#.....#...#.......#.#..d#.#...#\n" + \
"#.#######.#######.###.#.#.#.#####.###.#.#.#.#####.#####.#####.#######.###.#.###.#\n" + \
"#.......#a..#.#.Y.#...#...#.....#.....#.#.#.....#.....#...#...#...#.....#.#.#...#\n" + \
"#.#####.###.#.#.#.#.#######.#.#.#######.#.#####.###.#####.#.###.###.###.#.#.#.#.#\n" + \
"#.....#...#.#.#.#.#...#.#...#.#.#.......#.#...#.....#.....#.#.....#...#.#.#.#.#.#\n" + \
"#####.#.###.#.#.#####.#.#.###.###.#######.###.#######.#####.#.###.###.#.#.###.#.#\n" + \
"#....f#.......#....m..#.....#.......................#.......#...#.....#.......#.#\n" + \
"#######################################.@.#######################################\n" + \
"#...#.....#...#...#.#.......#.....#...........#.....#.#.......#...........#.....#\n" + \
"#.#.#.#.#.#.#.#.#.#.#.#.###.#.###.#####.#.###.###.#.#.#.#####.#.#######.#.###.#.#\n" + \
"#.#...#.#...#.#.#...#.#...#...#.........#...#...#.#...#.#...#.#.#.#...#.#.#...#.#\n" + \
"#######.#####.#.###.#.###.#############.###.###.#.###.#.#.###.#.#.#.#.#.#.#.###.#\n" + \
"#.....#.#.......#...#s#.#.#.........#...#...#...#...#.#.#.#...#...#.#...#...#.#.#\n" + \
"#.###.#.#############.#.#.#.#######.#.###.#####.#.#.###.#.#.#####.#.#########.#.#\n" + \
"#...#...#...............#.#.#.#.....#.#.#.....#t#.#...#.#.#.#.....#...#.......#.#\n" + \
"#.#.#####.###############.#.#.#.#####.#.#.###.#.#####.#.#.#.#########.#.#######.#\n" + \
"#.#.#...#.#.....#...#...#.....#.#...#.#.#.#.#.#.#.....#...#...#.......#.........#\n" + \
"#.#.#.#.#.#.###Z#.###.#.###.###.#.###.#.#.#.#.#.#.###.###.###.#.#######.#####.###\n" + \
"#.#.#.#.#...#.....#...#...#.#...#.#...#.#.#.#.#...#...#...#.#.#...#...#.#...#...#\n" + \
"###.#.#.#####.#####.#####.###.###.#.###.#.#.#.#########.###.#.#.#.###.#.#.#.###.#\n" + \
"#...#.#.....#.#.#...#...#.....#.........#...#...........#...#.#.#...#...#.#.#...#\n" + \
"#.###.#.#####.#.#.###.#.###.###############.#############.###.#####.#####.#.###.#\n" + \
"#.#...#....k....#.#...#.....#.......#...#.#.......#.....#...#...K.#.#.....#...#.#\n" + \
"#.#.#############.#####.#####.#####.#.#.#.#######.#.###.###.#####.#.#.#######.#.#\n" + \
"#...#.........#...#...#.....#...#.#...#.#.......#...#.........#...#.#.#.....#.#.#\n" + \
"#####.#######.#.###.#.#########.#.#####.#.#.###.#.###########.#.###.#.#.#####.#.#\n" + \
"#.....#.........#...#.#.........#...#...#.#...#.#.#.......#...#...#...#...#...#.#\n" + \
"#.###############B###.#.###########.#.#######.###.#.#####.#####.#.#.#####.#.###.#\n" + \
"#.....#.....#...#...#h#...........#.....#.....#...#.#...#.....#.#.#.....#.#...#w#\n" + \
"#.###.#.###.#.#.###.#####.#######.#####.#.#####.###.#.#.#########.#####.#.###.###\n" + \
"#...#...#...#.#...#.....#.......#...#.#.#.#.....#.#...#...#.....#...#.......#...#\n" + \
"#########.###.###.#####.#####.#####.#.#.#.#.#####.#######.#.###.###.#.#########.#\n" + \
"#.....#...#.....#.....#...#...#.....#.#.#...#.......#...#.#.#.......#...#.....#.#\n" + \
"#.###.#.###.#####.#######.#.###.#####.#.#.#####.#####.#.#.#.#############.###G#.#\n" + \
"#...#...#...#...#.......#.#...#.#...#...#.....#.....#.#...#.......#.......#.#...#\n" + \
"###.#####.###.#.###.###.#.#####.###.#.#######.#####.#.###########.#.#######.###.#\n" + \
"#...#.......#.#...#.#...#.#.....#...#...#...#.....#.#.......#...#.#.#.........#.#\n" + \
"#.###.#######.###.#.#.###.#.#####.#####.#.#.#####.#.#######.#.#.#.#.#.###.#####.#\n" + \
"#.....#...#...#.#.#.#...#.#.#...#.......#.#.......#...#...#...#...#.#.#.#.......#\n" + \
"#.#######.#.###.#.#####.#.#C#.#.#.#######.#########.###.#.#########.#.#.#########\n" + \
"#.......#.#...#.....R...#...#.#.#.#.....#.#.......#...#.#.....#.....#.#.........#\n" + \
"#######.#.###.###############.#.#.###.#.#.#.#####.#.#.#.#.###.#.#.###.###.#####.#\n" + \
"#.....#.#...#...#...........#.#.#.....#.#.#.....#...#..p#.#...#.#.#...#...#...#.#\n" + \
"#.#####.#.#.###.#.#########.#.#.#######.#.###.###########.###.###.#.###.#####.#.#\n" + \
"#.....#.#.#.#q#...#.....#.#.#.#.......#.#.#...#.....#...#...#...#.#...#.#x....#.#\n" + \
"#.###.#.#.#.#.#######.#.#.#.#.###.#####.#.#####.###.#.#I###.###.#.###.#.#.#####.#\n" + \
"#...#...J.#...........#...#.....#.......#.......#.....#..l..#.....#.....#.......#\n" + \
"#################################################################################\n"

##startMap = "###############\n" + \
##            "#d.ABC.#.....a#\n" + \
##            "######...######\n" + \
##            "#######@#######\n" + \
##            "######...######\n" + \
##            "#b.....#.....c#\n" + \
##            "###############\n"
##
##startMap = "#############\n" + \
##            "#g#f.D#..h#l#\n" + \
##            "#F###e#E###.#\n" + \
##            "#dCba...BcIJ#\n" + \
##            "######@######\n" + \
##            "#nK.L...G...#\n" + \
##            "#M###N#H###.#\n" + \
##            "#o#m..#i#jk.#\n" + \
##            "#############\n"

##startMap = "#############\n" + \
##            "#DcBa.#.GhKl#\n" + \
##            "#.###...#I###\n" + \
##            "#e#d##@##j#k#\n" + \
##            "###C#...###J#\n" + \
##            "#fEbA.#.FgHi#\n" + \
##            "#############\n"
mapSize = len(startMap)

# build GATE List
gates = []
for char in startMap:
    if char in string.ascii_uppercase:
        gates.append(char)
keys = []
for char in startMap:
    if char in string.ascii_lowercase:
        keys.append(char)

NUM_GATES = len(gates)
NUM_KEYS = len(keys)

WINLENGTH = 999999

yO = startMap.find('\n')+1

startPos = startMap.find('@')
startMap = startMap[:startPos-1-yO] + "@#@" + startMap[startPos+2-yO:]
#print(startMap)
startMap = startMap[:startPos-1] +    "###" + startMap[startPos+2:]
#print(startMap)
startMap = startMap[:startPos-1+yO] + "@#@" + startMap[startPos+2+yO:]

print(startMap)

MOVES = (-1,1,yO,-yO)

hist = defaultdict(lambda : defaultdict( lambda :defaultdict(int)))

startPosA = startMap.find('@')
startPosB = startMap.find('@',startPosA+1)
startPosC = startMap.find('@',startPosB+1)
startPosD = startMap.find('@',startPosC+1)

startPos = [startPosA, startPosB, startPosC, startPosD]
print(startPos,gates)

locations = []
locations.append((startPos,[],[],startMap,0))

def generateMoves(loc,curMap):
    toProcess = [[loc,[]]]
    moveDict = {loc:0}
    outList = []
    steps = 0
    while len(toProcess) > 0:
        toAdd = []
        toRemove = []
        steps += 1
        for obj in toProcess:
            curLoc = obj[0]
            toRemove.append(obj)
            #print("CUR LOC",curLoc)
            for move in MOVES:
                reqKeys = obj[1].copy()
                newLoc = curLoc + move
                #print("NEW LOC",newLoc)
                if newLoc not in moveDict:
                    moveDict[newLoc] = steps
                    if curMap[newLoc] == '.' or curMap[newLoc] == '@':
                        toAdd.append([newLoc,reqKeys])
                    if curMap[newLoc] in string.ascii_lowercase:
                        outList.append(((newLoc - loc), steps, reqKeys))
                    elif curMap[newLoc] in string.ascii_uppercase:
                        reqKeys.append(curMap[newLoc].lower())
                        toAdd.append([newLoc,reqKeys])
        for aLoc in toAdd:
            toProcess.append(aLoc)
        for rLoc in toRemove:
            toProcess.remove(rLoc)
    print(loc, outList)
    return outList

def generateAllMoves(curMap):
    outMoves = {}
    for pos in range(len(curMap)):
        if curMap[pos] == '@' or curMap[pos] in string.ascii_lowercase:
            outMoves[pos] = generateMoves(pos,curMap)
    return outMoves

def getMoves(loc, curMap):
    toProcess = [loc]
    moveDict = {loc:0}
    outList = []
    steps = 0
    while len(toProcess) > 0:
        toAdd = []
        toRemove = []
        steps += 1
        for curLoc in toProcess:
            toRemove.append(curLoc)
            #print("CUR LOC",curLoc)
            for move in MOVES:
                newLoc = curLoc + move
                #print("NEW LOC",newLoc)
                if newLoc not in moveDict:
                    moveDict[newLoc] = steps
                    if curMap[newLoc] == '.':
                        toAdd.append(newLoc)
                    if curMap[newLoc] in string.ascii_uppercase or curMap[newLoc] in string.ascii_lowercase:
                        outList.append(((newLoc - loc), steps))
        for aLoc in toAdd:
            toProcess.append(aLoc)
        for rLoc in toRemove:
            toProcess.remove(rLoc)
    return outList
                        

    
def branch(location, steps):
    global hist
    global MOVESDICT
    global WINLENGTH
    locs = location[0]
    keys = location[1]
    gates = location[2]
    curMap = location[3]
    curSteps = location[4]
    retLocs = []
    for loc in locs:
        #print (loc,"MD", MOVESDICT[loc])
        moveObjs = filter(lambda x : all (elem in keys for elem in x[2]), MOVESDICT[loc])
        #print(moveObjs)
        for moveObj in moveObjs:
            #print ("MO",moveObj)
            move = moveObj[0]
            movSteps = moveObj[1]
            newLocs = locs.copy()
            newLoc = loc + move
            #print (locs, newLocs, loc, newLoc)
            newLocs.remove(loc)
            newLocs.append(newLoc)
            newLocs.sort()
            newKeys = keys.copy()
            newGates = gates.copy()
            if newLoc < mapSize:
##                if curMap[newLoc] in ('#','\n'):
##                    continue
                if curMap[newLoc] in string.ascii_lowercase:
                    if curMap[newLoc] not in newKeys:
                        newKeys.append(curMap[newLoc])
                        newKeys.sort()
                elif curMap[newLoc] in string.ascii_uppercase:
                    #print("NEED KEY:", curMap[newLoc].lower(), newKeys)
                    if curMap[newLoc].lower() not in newKeys:
                        continue
                    else:
                        if curMap[newLoc] not in newGates:
                            newGates.append(curMap[newLoc])
                            newGates.sort()
                newMap = curMap[:newLoc] + '@' + curMap[newLoc + 1:]
                newMap = newMap[:loc] + '.' + newMap[loc + 1:]
                #print(curMap, newMap, loc, newLoc)
                if hist[str(newLocs)][str(newKeys)][str(newGates)] == 0:
                    #print(newMap,newLoc, newKeys, newGates)
                    hist[str(newLocs)][str(newKeys)][str(newGates)] = steps
                    if len(newKeys) == NUM_KEYS:
                        print("WINNER: ", curSteps+movSteps)
                        if curSteps+movSteps < WINLENGTH:
                            WINLENGTH = curSteps+movSteps
                        #retLocs.append("WINNER")
                    else:
                        retLocs.append((newLocs,newKeys,newGates,newMap,curSteps+movSteps))
##    print("OLDLOCS", locs, keys)
##    for retLoc in retLocs:
##        print("NEWLOC",retLoc[0], retLoc[1])
    return retLocs

MOVESDICT = generateAllMoves(startMap)
print(len(MOVESDICT),NUM_KEYS)

steps = 0
while len(locations) > 0:
    toAppend = []
    toRemove = []
    steps += 1
    curLocs = list(filter(lambda x: x[4]<= steps,locations))
    #print (curLocs)
    print("Steps:", steps, "TREE SIZE:",len(locations),"PROCESSED:,", len(curLocs))
    for location in curLocs:
        newLocations = branch(location, steps)
        for newLoc in newLocations:
            toAppend.append(newLoc)
        toRemove.append(location)
    for rLoc in toRemove:
        locations.remove(rLoc)
    for aLoc in toAppend:
        locations.append(aLoc)

print("SHORTEST PATH:", WINLENGTH)
