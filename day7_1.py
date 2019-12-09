from itertools import permutations

source = [3,8,1001,8,10,8,105,1,0,0,21,42,67,88,105,114,195,276,357,438,99999,3,9,101,4,9,9,102,3,9,9,1001,9,2,9,102,4,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,2,9,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,1001,9,4,9,1002,9,4,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,101,4,9,9,102,3,9,9,1001,9,5,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]

#source = [1002, 4, 3, 4, 33]

def getInput():
    return int(input("INPUT:"))

def sendOutput(outVal):
    print("OUTPUT:",outVal)
    return

def getInsLen(opcode):
    insLen = -1
    if opcode in [1,2,7,8]:
        insLen = 4
    elif opcode in [3,4]:
        insLen = 2
    elif opcode in [5,6]:
        insLen = 3
    elif opcode in [99]:
        insLen = 1
    return insLen

def getParam(pointer, offset, mode, source):
    param = source[pointer+offset] if mode == 1 else source[source[pointer+offset]]
    return param

def processInstruction(pointer, source, inFunc=getInput, outFunc=sendOutput):
    #print(pointer, " : ", source[pointer],source[pointer+1],source[pointer+2],source[pointer+3])
    instruction = "%05d" % source[pointer]
    opcode = int(instruction[3:])
    cMode = int(instruction[0])
    bMode = int(instruction[1])
    aMode = int(instruction[2])
    insLen = getInsLen(opcode)
    #print(opcode, aMode, bMode, cMode, insLen)
    if insLen > 1:
        paramA = getParam(pointer, 1, aMode, source)
    if insLen > 2:
        paramB = getParam(pointer, 2, bMode, source)
    if insLen > 3:
        paramC = getParam(pointer, 3, cMode, source)
        
    #HALT
    if opcode == 99:
        return -1

    #ADD
    if opcode == 1:
        source[source[pointer+3]] = paramA + paramB
        return pointer + 4

    #MUL
    if opcode == 2:
        source[source[pointer+3]] = paramA * paramB
        return pointer + 4

    #INPUT
    if opcode == 3:
        source[source[pointer+1]] = inFunc()
        return pointer + 2

    #OUTPUT
    if opcode == 4:
        outFunc(paramA)
        return pointer + 2

    #JNZ
    if opcode == 5:
        return pointer + 3 if paramA == 0 else paramB

    #JEZ
    if opcode == 6:
        return pointer + 3 if paramA != 0 else paramB

    #LT
    if opcode == 7:
        source[source[pointer+3]] = 1 if paramA < paramB else 0
        return pointer + 4

    #EQ
    if opcode == 8:
        source[source[pointer+3]] = 1 if paramA == paramB else 0
        return pointer + 4
        
    print("Unexpected command %s at location: %d" % (instruction,pointer))
    return -1
    

def runProgram(source, inFunc=getInput, outFunc=sendOutput):
    pointer = 0
    localSource = source.copy()
    while pointer >= 0:
        pointer = processInstruction(pointer, localSource, inFunc, outFunc)


wire = 0
getInput = False

def inputFromWire(x):
    global wire
    global getInput
    retVal = x
    if getInput:
        retVal = wire
    getInput = not getInput
    return retVal

def outputToWire(outVal):
    global wire
    print("OUTPUT:", outVal, "put on wire.")
    wire = outVal

highestOut = 0
highestCombo = None
for perm in permutations(range(5)):
    wire = 0
    getInput = False
    for box in perm:
        runProgram(source, lambda : inputFromWire(box), outputToWire)
    print("FINAL OUTPUT:", wire)
    if wire > highestOut:
        highestOut = wire
        highestCombo = perm

print("HIGHEST OUTPUT:",highestOut,highestCombo)
#runProgram(source)
#print (source)
