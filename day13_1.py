from IntCodeProcessor import IntCodeProcessor

class ArcadeCabinet:
    def __init__(self, source):
        self.source = source.copy()
        self.processor = IntCodeProcessor(self.source, self.getInput, self.sendOutput)
        self.screen = {}
        self.outCount = 0
        self.outPos = [0,0]
        self.screenSize = [0,0]


    def getInput(self):
        return 0

    def sendOutput(self, out):
        if self.outCount == 2:
            self.screen[(self.outPos[0],self.outPos[1])] = out
            if self.outPos == self.screenSize:
                self.drawScreen()
        else:
            self.outPos[self.outCount] = out
            if out > self.screenSize[self.outCount]:
                self.screenSize[self.outCount] = out
        self.outCount = (self.outCount + 1) % 3
        

    def run(self):
        self.processor.run()

    def drawScreen(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        frame = [[" " for y in range(self.screenSize[1]+1)] for x in range(self.screenSize[0]+1)]
        for loc in self.screen:
            frame[loc[0]][loc[1]] = self.screen[loc]
        for y in range(self.screenSize[1]+1):
            rowStr = ""
            for x in range(self.screenSize[0]+1):
                rowStr += str(frame[x][y])
            print(rowStr)
                
if __name__ == '__main__':
    with open('day13.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])

    game = ArcadeCabinet(source)
    game.run()

    print(game.screen)

    print(sum(value == 2 for value in game.screen.values()))
