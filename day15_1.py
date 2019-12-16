from IntCodeProcessor import IntCodeProcessor
from tkinter import *
from tkinter import ttk
import time
import os

COLORS = ['white','black','red','blue','green']
ICONS = [' ', "█", '♫', '═', '☺']
FRAMETIME = 0.01

SPACE = ' . '
WALL = '███'
OXYGEN = ' ☺ '
START = ' $ '

class RepairDroid:
    def __init__(self, source):
        self.source = source.copy()
        self.processor = IntCodeProcessor(self.source, self.getInput, self.sendOutput)
        self.pos = (0,0)
        self.map = {(0,0): START}
        self.xMax = 0
        self.xMin = 0
        self.yMax = 0
        self.yMin = 0
        self.direction = 1
        self.steps = 0
        self.oxLoc = None
        self.retHome = False


    def mapDist(self, start):
        curCells = [start]
        i = 0
        while len(curCells) > 0:
            toRemove = []
            toAppend = []
            for curCell in curCells:
                #print (curCell)
                if curCell in self.map and (self.map[curCell] == SPACE or self.map[curCell] == START):
                    toAppend.append((curCell[0]+1,curCell[1]))
                    toAppend.append((curCell[0]-1,curCell[1]))
                    toAppend.append((curCell[0],curCell[1]+1))
                    toAppend.append((curCell[0],curCell[1]-1))
                    self.map[curCell] = "%03d" %i
                toRemove.append(curCell)
            for cell in toRemove:
                curCells.remove(cell)
            for cell in toAppend:
                curCells.append(cell)
            i += 1
        self.printMap()
        print("Oxygen system %s steps away." % self.map[self.oxLoc])
            
    def getInput(self):
        #print("INPUT", self.direction)
        if self.retHome == False:
            return self.direction
        print("Returned Home")
        self.mapDist((0,0))
        
        
    def sendOutput(self, out):
        #print("OUTPUT", out)
        if self.direction == 1:
            targetCell = (self.pos[0], self.pos[1] + 1)
        elif self.direction == 2:
            targetCell = (self.pos[0], self.pos[1] - 1)
        elif self.direction == 3:
            targetCell = (self.pos[0] - 1, self.pos[1])
        elif self.direction == 4:
            targetCell = (self.pos[0] + 1, self.pos[1])

        if self.oxLoc != None and targetCell == (0,0):
            self.retHome = True
            
        if targetCell not in self.map:
            self.steps += 1
            
        #Track bounds of map
        if targetCell[0] > self.xMax:
            self.xMax = targetCell[0]
        elif targetCell[0] < self.xMin:
            self.xMin = targetCell[0]
        if targetCell[1] > self.yMax:
            self.yMax = targetCell[1]
        elif targetCell[1] < self.yMin:
            self.yMin = targetCell[1]

        

        #HIT A WALL, TURN LEFT
        if out == 0:
            if targetCell not in self.map:
                self.map[targetCell] = WALL
            if self.direction == 1:
                self.direction = 3
            elif self.direction == 2:
                self.direction = 4
            elif self.direction == 3:
                self.direction = 2
            elif self.direction == 4:
                self.direction = 1

        #SPACE AHEAD
        if out == 1:
            self.pos = targetCell
            if targetCell not in self.map:
                self.map[targetCell] = SPACE
            if self.direction == 1:
                self.direction = 4
            elif self.direction == 2:
                self.direction = 3
            elif self.direction == 3:
                self.direction = 1
            elif self.direction == 4:
                self.direction = 2
            if self.steps % 200 == 0:
                self.printMap()
        #OXYGEN TANK
        if out == 2:
            self.pos = targetCell
            self.map[targetCell] = OXYGEN
            self.oxLoc = targetCell
            self.printMap()
            print ("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            print("oxLoc Found:",self.oxLoc)
            
    def printMap(self):
        mapString = "----------------------MAP----------------------\n"
        for y in range(self.yMin, self.yMax+1):
            for x in range(self.xMin,self.xMax+1):
                mapString += self.map[(x,y)] if (x,y) in self.map else "XXX"
            mapString += '\n'
        mapString += "X %d - %d Y %d - %d" % ( self.xMin, self.xMax, self.yMin, self.yMax)
        print (mapString)
            
    def run(self):
        self.processor.run()
                    
if __name__ == '__main__':
    with open('day15.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])

    bot = RepairDroid(source)
    bot.run()
