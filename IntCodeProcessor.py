import threading
from IntCodeOps import OpCodes

class IntCodeProcessor:

    def getInput(self):
        return int(input("INPUT:"))

    def sendOutput(self, outVal):
        print("OUTPUT:",outVal)
        return
    
    def processNextInstruction(self):
        instruction = "%05d" % self.source[self.PC]
        opCode = int(instruction[3:])
        mode = instruction[2::-1]
        if opCode in OpCodes:
            return OpCodes[opCode](self, mode)
        else:
            print("Unexpected command %s at location: %d" % (instruction,pointer))
            return -1

    def run(self):
        self.PC = 0
        self.RB = 0
        while self.PC >= 0:
            self.PC = self.processNextInstruction()

    def forkAndRun(self):
        p = threading.Thread(target=self.run)
        p.start()
        return p
    
    def __init__(self, source, getInput=None, sendOutput=None):
        self.source = source.copy()
        self.PC = 0
        self.RB = 0
        if getInput != None:
            self.getInput = getInput
        if sendOutput != None:
            self.sendOutput = sendOutput
