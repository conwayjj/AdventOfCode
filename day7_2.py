from itertools import permutations
import multiprocessing as mp
import threading


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


def forkProgram(source, inFunc=getInput, outFunc=sendOutput):
    p = threading.Thread(target=runProgram, args=(source, inFunc, outFunc))
    p.start()
    return p

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

def inputFromQueue(inQueue):
    return inQueue.get(True,10)

def outputToQueue(outQueue, obj):
    outQueue.put(obj, True, 10)

if __name__ == '__main__':
    with open('day7.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = [int(x) for x in sourceTxt]
    
    highestOut = 0
    highestCombo = None
    for perm in permutations(range(5,10)):
        wireAB = mp.Queue()
        wireBC = mp.Queue()
        wireCD = mp.Queue()
        wireDE = mp.Queue()
        wireEA = mp.Queue()
        wireAB.put(perm[1])
        wireBC.put(perm[2])
        wireCD.put(perm[3])
        wireDE.put(perm[4])
        wireEA.put(perm[0])
        wireEA.put(0)
        procA = forkProgram(source, lambda : inputFromQueue(wireEA), lambda x : outputToQueue(wireAB, x))
        procB = forkProgram(source, lambda : inputFromQueue(wireAB), lambda x : outputToQueue(wireBC, x))
        procC = forkProgram(source, lambda : inputFromQueue(wireBC), lambda x : outputToQueue(wireCD, x))
        procD = forkProgram(source, lambda : inputFromQueue(wireCD), lambda x : outputToQueue(wireDE, x))
        procE = forkProgram(source, lambda : inputFromQueue(wireDE), lambda x : outputToQueue(wireEA, x))
        procA.join()
        procB.join()
        procC.join()
        procD.join()
        procE.join()
        out = wireEA.get()
        #print("FINAL OUTPUT:", out)
        if out > highestOut:
            highestOut = out
            highestCombo = perm

print("HIGHEST OUTPUT:",highestOut,highestCombo)
