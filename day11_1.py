from IntCodeProcessor import IntCodeProcessor

grid = {(0,0):1}
x = 0
y = 0
heading = ['N']
mode = [0]
xMax = 0
xMin = 0
yMax = 0
yMin = 0
loc = [x,y,xMax,xMin,yMax,yMin]

def getColor(grid, loc):
    retVal = 0
    if (loc[0],loc[1]) in grid:
        retVal = grid[(loc[0],loc[1])]
    return retVal

def paintAndDrive(grid, loc, mode, heading, out):
    #PAINT
    if mode[0] == 0:
        grid[(loc[0],loc[1])] = out
        mode[0] = 1
    #TURN/MOVE
    elif mode[0] == 1:
        #TURN
        if heading[0] == 'N':
            heading[0] = 'W' if out == 0 else 'E'
        elif heading[0] == 'W':
            heading[0] = 'S' if out == 0 else 'N'
        elif heading[0] == 'S':
            heading[0] = 'E' if out == 0 else 'W'
        elif heading[0] == 'E':
            heading[0] = 'N' if out == 0 else 'S'
        #MOVE
        if heading[0] == 'N':
            loc[1] -= 1
        elif heading[0] == 'E':
            loc[0] += 1
        elif heading[0] == 'W':
            loc[0] -= 1
        elif heading[0] == 'S':
            loc[1] += 1
        # Set Bounds
        if loc[0] > loc[2]:
            loc[2] = loc[0]
        if loc[1] > loc[4]:
            loc[4] = loc[1]
        if loc[1] < loc[5]:
            loc[5] = loc[1]
        if loc[0] < loc[3]:
            loc[3] = loc[0]
        mode[0] = 0
    
if __name__ == '__main__':
    with open('day11.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])

    procA = IntCodeProcessor(source, getInput = lambda : getColor(grid, loc), sendOutput = lambda x: paintAndDrive(grid, loc, mode, heading, x))
    procA.run()

#print(grid)

print(len(grid))

outString = [[" " for x in range(loc[2] - loc[3]+1)] for y in range(loc[4]-loc[5]+1)]

for key in grid:
    outString[(key[1]-loc[5])][(key[0]-loc[3])] = "█" if grid[key] == 0 else " "

for row in outString:
    rowStr = ""
    for char in row:
        rowStr += char
    print (rowStr)
