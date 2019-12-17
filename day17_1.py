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

A = 65
B = 66
C = 67
END = 10
R = 82
L = 76
D = 44

COMMANDS = [A,D, B,D,A,D, C,D,B,D,A, D,B,D,C,D,C,D,B,D,END,      # Main loop
            L,D,12,D,L,D,12,D,R,D,4, D,END,                      # A Process
            R,D,10,D,R,D,6, D,R,D,4, D,R,D,4,D,END,              # B Process
            R,D,6, D,L,D,12,D,L,D,12,D,END,                      # C Process
            79,END]                      
            
            
class RepairDroid:
    def __init__(self, source):
        self.source = source.copy()
        self.processor = IntCodeProcessor(self.source, self.getInput, self.sendOutput)
        self.pos = (0,0)
        self.map = {}
        self.xMax = 0
        self.xMin = 0
        self.yMax = 0
        self.yMin = 0
        self.direction = 1
        self.steps = 0
        self.oxLoc = None
        self.retHome = False
        self.inLoc = -1


    def getInput(self):
       self.inLoc += 1
       return COMMANDS[self.inLoc]
        
        
    def sendOutput(self, out):
        if out == 10:
            self.pos = (0 , self.pos[1] + 1)
            self.yMax = self.pos[1]
        else:
            self.map[self.pos] = chr(out)
            self.pos = (self.pos[0] + 1, self.pos[1])
            if self.pos[0] > self.xMax:
                self.xMax = self.pos[0]
        self.printMap()


            
    def printMap(self):
        mapString = "----------------------MAP----------------------\n"
        for y in range(self.yMin, self.yMax):
            for x in range(self.xMin,self.xMax):
                mapString += self.map[(x,y)] if (x,y) in self.map else "X"
            mapString += '\n'
        mapString += "X %d - %d Y %d - %d" % ( self.xMin, self.xMax, self.yMin, self.yMax)
        print (mapString)
            
    def run(self):
        self.processor.run()

    def analyzeMap(self):
        alignment = 0
        for loc in self.map:
            if self.map[loc] == '#':
                neighbors = [(loc[0] + 1, loc[1]),
                         (loc[0] - 1, loc[1]),
                         (loc[0], loc[1] + 1),
                         (loc[0], loc[1] - 1)]
                intersection = True
                for neighbor in neighbors:
                    intersection &= (neighbor in self.map and self.map[neighbor] == '#')
                if intersection:
                    align = loc[0] * loc[1]
                    print("ALIGNMENT for", loc, "=", align)
                    alignment += align
        return alignment

    def getPathLength(self, start, move):
        steps = 0
        loc = start
        nextStep = (loc[0] + move[0], loc[1] + move[1])
        #print(nextStep)
        while nextStep in self.map and self.map[nextStep] == '#':
            loc = nextStep
            steps += 1
            #print(loc,steps)
            nextStep = (loc[0] + move[0], loc[1] + move[1])
        #print("PL",steps, loc)
        return steps, loc

    def getNextDirection(self, loc, move):
        if move == (0,-1):
            lMove = (-1,0)
            rMove = (1,0)
        elif move == (0,1):
            lMove = (1,0)
            rMove = (-1,0)
        elif move == (1,0):
            lMove = (0,-1)
            rMove = (0,1)
        elif move == (-1,0):
            lMove = (0,1)
            rMove = (0,-1)

        lCell = (loc[0] + lMove[0], loc[1] + lMove[1])
        rCell = (loc[0] + rMove[0], loc[1] + rMove[1])

        lPath = False
        rPath = False
        
        if (lCell in self.map and self.map[lCell] == '#'):
            lPath = True
        if (rCell in self.map and self.map[rCell] == '#'):
            rPath = True

        if lPath and rPath:
            print("ERROR IN PATH Calculation")
            return "X", 0
        elif lPath:
            return "L", lMove
        elif rPath:
            return "R", rMove
        else:
            return "X", 0
            
        
    def getPath(self):
        for loc in self.map:
            if self.map[loc] == '^':
                curLoc = loc
        moveList = []
        turn = 'L'
        move = (-1,0) # Cheating and inputting defaults here
        while turn != 'X':
            moveList.append(turn)
            length, curLoc = self.getPathLength(curLoc, move)
            moveList.append(length)
            turn, move = self.getNextDirection(curLoc, move)
        return moveList
            
            
def chunkPaths(path):
    pathStr = ""
    for com in path:
        pathStr += str(com)

    substrings = []
    for start in range(len(pathStr)):
        for length in range(2, len(pathStr) - start):
            substr = pathStr[start:start+length]
            num = pathStr.count(substr)
            if num > 1 and (substr,num) not in substrings:
                substrings.append((substr,num))
    substrings.sort(key=lambda x: -len(x[0] * x[1]))
    #print (substrings)

    for substring1 in substrings:
        #print (substring1)
        tempStr1 = pathStr.replace(substring1[0],"A")
        for substring2 in substrings:
            tempStr2 = tempStr1.replace(substring2[0], "B")
            for substring3 in substrings:
                tempStr3 = tempStr2.replace(substring3[0],"C")
                #print(tempStr3)
                if len(tempStr3)-tempStr3.count("A")-tempStr3.count("B")-tempStr3.count("C") == 0:
                    print (tempStr3,"A",substring1,"B",substring2,"C",substring3)
                    
    return substrings
            
            
if __name__ == '__main__':
    with open('day17.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])

    bot = RepairDroid(source)
    bot.run()
    bot.printMap()
    alignment = bot.analyzeMap()
    print("TOTAL ALIGNMENT:", alignment)
    path = bot.getPath()
    print(chunkPaths(path))
    print(len(path))
    pathStr = ""
    for com in path:
        pathStr += str(com)
    print (pathStr)
