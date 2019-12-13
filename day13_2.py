from IntCodeProcessor import IntCodeProcessor
from tkinter import *
from tkinter import ttk
import time

COLORS = ['white','black','red','blue','green']
FRAMETIME = 0.1

class ArcadeCabinet:
    def __init__(self, source):
        self.source = source.copy()
        self.processor = IntCodeProcessor(self.source, self.getInput, self.sendOutput)
        self.screen = {}
        self.outCount = 0
        self.outPos = [0,0]
        self.screenSize = [0,0]
        self.ballPos = [0,0]
        self.padPos = [0,0]
        self.score = 0
        self.display = Tk()
        self.display.grid()
        self.buttonDict = {}
        self.blockSize = [10,10]
        #self.display.mainloop()
        
    def getInput(self):
        retVal = 0
        if self.ballPos[0] > self.padPos[0]:
            retVal = 1
        if self.ballPos[0] < self.padPos[0]:
            retVal = -1
        return retVal

    def sendOutput(self, out):
        if self.outCount == 2:
            if self.outPos[0] == -1 and self.outPos[1] == 0:
                self.score = out
            else:
                if out == 4:
                    self.ballPos[0] = self.outPos[0]
                    self.ballPos[1] = self.outPos[1]
                if out == 3:
                    self.padPos[0] = self.outPos[0]
                    self.padPos[1] = self.outPos[1]
                #self.drawScreen(out)
                self.drawTkScreen(out)
        else:
            self.outPos[self.outCount] = out
        self.outCount = (self.outCount + 1) % 3
        

    def run(self):
        self.processor.run()

    def drawTkScreen(self, out):
        #Create canvas object
        if (self.outPos[0],self.outPos[1]) not in self.buttonDict:
            self.buttonDict[(self.outPos[0],self.outPos[1])] = Button(self.display)
            self.buttonDict[(self.outPos[0],self.outPos[1])].grid(row=self.outPos[1], column = self.outPos[0])
        self.buttonDict[(self.outPos[0],self.outPos[1])]["bg"] = COLORS[out]
        self.display.update()
        time.sleep(FRAMETIME)
        
    def drawScreen(self, out):
        if self.outPos[0] > self.screenSize[self.outCount][0]:
                self.screenSize[self.outCount][0] = self.outPos[0]
        if self.outPos[1] > self.screenSize[self.outCount][1]:
                self.screenSize[self.outCount][1] = self.outPos[1]
        self.screen[(self.outPos[0],self.outPos[1])] = out
        frame = [[" " for y in range(self.screenSize[1]+1)] for x in range(self.screenSize[0]+1)]
        for loc in self.screen:
            frame[loc[0]][loc[1]] = self.screen[loc]
        frameBuf =  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        frameBuf += "~~~~~~~~~~~~~ SCORE: %010d ~~~~~~~~~~~~\n" % self.score
        frameBuf +=  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        for y in range(self.screenSize[1]+1):
            rowStr = ""
            for x in range(self.screenSize[0]+1):
                rowStr += str(frame[x][y])
                ttk.Button(self.display, text = self.screen[loc]).grid(column = x, row = y)
            frameBuf += rowStr + '\n'
        print (frameBuf)
                
if __name__ == '__main__':
    with open('day13.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])
        #Put in quarters
        source[0] = 2

    game = ArcadeCabinet(source)
    game.run()

    print("SCORE:", game.score)
