from IntCodeProcessor import IntCodeProcessor
from tkinter import *
from tkinter import ttk
import time
import os
from collections import defaultdict

COMMANDS = "A,B,A,C,B,A,B,C,C,B\n" + \
            "L,12,L,12,R,4\n" + \
            "R,10,R,6,R,4,R,4\n" + \
            "R,6,L,12,L,12\n" + \
            "y\n"                 
            
            
class RepairDroid:
    def __init__(self, source):
        self.source = source.copy()
        self.processor = IntCodeProcessor(self.source, self.getInput, self.sendOutput)
        self.pos = (50,0)
        self.map = defaultdict(int)
        self.xMax = 44
        self.xMin = 0
        self.yMax = 100
        self.yMin = 0
        self.direction = 1
        self.steps = 0
        self.oxLoc = None
        self.retHome = False
        self.inLoc = -1
        self.sendX = True


    def getInput(self):
       retVal = self.pos[1]
       if self.sendX:
           retVal = self.pos[0]
       self.sendX = not self.sendX
       return retVal 
        
    def sendOutput(self, out):
        self.map[self.pos] = out
        if out == 0 and self.pos[0] > self.xMin and self.pos[0] < self.xMax:
            self.xMin = self.pos[0]
        if out == 1 and self.pos[0] > self.xMax:
            self.xMax = self.pos[0]
        if self.pos[0] > self.xMax:
            self.pos = (self.xMin, self.pos[1] + 1)
            if self.pos[1] > self.yMax:
                self.yMax = self.pos[1]
                self.yMin = self.yMax - 100
        else:
            self.pos = (self.pos[0] + 1, self.pos[1])
        #self.printMap()


            
    def printMap(self):
        mapString = "----------------------MAP----------------------\n"
        for y in range(self.yMin, self.yMax):
            for x in range(self.xMin,self.xMax):
                mapString += str(self.map[(x,y)]) if (x,y) in self.map else "X"
            mapString += '\n'
        mapString += "X %d - %d Y %d - %d" % ( self.xMin, self.xMax, self.yMin, self.yMax)
        print (mapString)
            
    def run(self):
        self.processor.run()

    def reset(self, source = None):
        if source != None:
            self.processor.source = source.copy()
        self.processor.PC = 0
            
if __name__ == '__main__':
    with open('day19.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])

    bot = RepairDroid(source)
    while (bot.map[bot.xMin+100,bot.yMin] != 1):
        bot.reset(source = source)
        bot.run()
        #print(bot.yMin)
        

    bot.printMap()
    print(bot.xMin,bot.xMax,bot.yMin,bot.yMax)
    zapped = 0
    total = 0
    for entry in bot.map:
        total += 1
        if bot.map[entry] == 1:
            zapped += 1
    print(total, zapped)
##    bot.printMap()
##    alignment = bot.analyzeMap()
##    print("TOTAL ALIGNMENT:", alignment)
##    path = bot.getPath()
##    print(chunkPaths(path))
##    print(len(path))
##    pathStr = ""
##    for com in path:
##        pathStr += str(com)
##    print (pathStr)
