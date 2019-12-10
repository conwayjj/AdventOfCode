import math
from collections import defaultdict

with open("Day10.txt") as inFile:
    rows = inFile.readlines()

#print(rows)

astDict = {}
y = 0
xMax = 0
for row in rows:
    print (row)
    xMax = len(row)
    for x in range(len(row)):
      if row[x] == '#':
          astDict[(x,y)] = (x,y)
    y += 1
yMax = y

#print(astDict)

maxVisible = 0
maxDict = {}
maxAst = None
for astA in astDict:
    visualDict = defaultdict(list)
    for astB in astDict:
        vector = math.atan2(astDict[astA][0]-astDict[astB][0],astDict[astA][1]-astDict[astB][1])
        visualDict[vector].append(astB)
    if len(visualDict) > maxVisible:
        maxVisible = len(visualDict)
        maxDict = visualDict
        maxAst = astA

#print (maxVisible)
#print (maxDict)
#print (maxAst)
        
maxStack = 0

for entry in maxDict:
    if len(maxDict[entry]) > maxStack:
        maxStack = len(maxDict[entry])

rotDict = {}

#rotate dictionary to have radians from y axis instead of radians from x axis
for entry in maxDict:
    rotated = (2*math.pi - (entry % (2*math.pi)) ) % (2*math.pi)
    #print(entry,"->",rotated)
    rotDict[rotated] = maxDict[entry]
    #print(rotated)

rotDict[0].remove(maxAst)

angList = []
for key in rotDict:
    angList.append(key)

outArray = [["..." for x in range(xMax)] for y in range(yMax)]

#print (angList)
angList.sort()
#print (angList)
zapOrder = []
while len(angList) > 0:
    toRemove = []
    for i in range(len(angList)):
        #print(i, angList[i], rotDict[angList[i]])
        closest = 999999
        closeAst = None
        for ast in rotDict[angList[i]]:
            #print(rotDict[angList[i]], ast)
            dist = math.hypot(ast[0]-maxAst[0],ast[1]-maxAst[1])
            if ast[0] == maxAst[0]:
                print (ast, maxAst, dist)
            if  dist < closest:
                closest = dist
                closeAst = ast
        rotDict[angList[i]].remove(ast)
        if len(rotDict[angList[i]]) == 0:
            del rotDict[angList[i]]
            toRemove.append(angList[i])
        zapOrder.append(ast)
    for item in toRemove:
        angList.remove(item)


for i in range(len(zapOrder)):
    outArray[zapOrder[i][1]][zapOrder[i][0]] = '%03d' %i
    
outArray[maxAst[1]][maxAst[0]] = "$$$"

for row in outArray:
    print (row)
print(maxAst)

#print (zapOrder)
print (zapOrder[199])
