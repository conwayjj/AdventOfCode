from collections import defaultdict
import math

with open('day14.txt') as inFile:
    eqs = inFile.readlines()

resources = defaultdict(int)
    
chemDict = {}
for eq in eqs:
    ins, out = eq.split('=>')
    ins = ins.strip().split(',')
    out = out.strip()
    for i in range(len(ins)):
        print(ins[i])
        ins[i] = ins[i].strip().split(' ')
        ins[i][0] = int(ins[i][0])
    out = out.split(' ')
    out[0].strip()
    out[1].strip()
    chemDict[out[1]] = {'ins': ins, 'num': int(out[0])}
print (chemDict)
            
def getReagents(out, number):
    global chemDict
    global requiredInputs
    ins = chemDict[out]['ins']
    outNum = chemDict[out]['num']
    for inp in ins:
        curReagent = requiredInputs[inp[1]]
        if curReagent > 0 and inp[1] != 'ORE':
            backOutReagent(inp[1],curReagent)
        requiredInputs[inp[1]] = curReagent + inp[0]*math.ceil(float(number)/outNum)
        if inp[1] != 'ORE':
            getReagents(inp[1], requiredInputs[inp[1]])
ore = 0

def getResources(out, number):
    global ore
    #print(out,number, resources[out])
    if out == 'ORE':
        ore += number
    else:
        while resources[out] < number:
            times = math.ceil((float(number)-resources[out])/chemDict[out]['num'])
            resources[out] += chemDict[out]['num']*times
            for inp in chemDict[out]['ins']:
                getResources(inp[1], inp[0]*times)
        resources[out] -= number

print (chemDict['FUEL'])

print(ore)
i = 2870000
while ore < 1000000000000:
    ore = 0
    getResources('FUEL', i)
    i+= 1
    print(i,':',ore)
    
print(ore)
