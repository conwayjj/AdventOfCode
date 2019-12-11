from IntCodeProcessor import IntCodeProcessor

grid = {(0,0):1}
x = 0
y = 0
heading = 'N'
mode = 0
xMax = 0
xMin = 0
yMax = 0
yMin = 0

def getColor():
    global grid
    retVal = 0
    if (x,y) in grid:
        retVal = grid[(x,y)]
    return retVal

def paintAndDrive(out):
    global grid
    global x
    global y
    global heading
    global mode
    global x, xMax, xMin
    global y, yMax, yMin
    #PAINT
    if mode == 0:
        grid[(x,y)] = out
        mode = 1
    #TURN/MOVE
    elif mode == 1:
        #TURN
        if heading == 'N':
            heading = 'W' if out == 0 else 'E'
        elif heading == 'W':
            heading = 'S' if out == 0 else 'N'
        elif heading == 'S':
            heading = 'E' if out == 0 else 'W'
        elif heading == 'E':
            heading = 'N' if out == 0 else 'S'
        #MOVE
        if heading == 'N':
            y += 1
        elif heading == 'E':
            x += 1
        elif heading == 'W':
            x -= 1
        elif heading == 'S':
            y -= 1
        # Set Bounds
        if x > xMax:
            xMax = x
        if y > yMax:
            yMax = y
        if y < yMin:
            yMin = y
        if x < xMin:
            xMin = x
        mode = 0
    
if __name__ == '__main__':
    with open('day11.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])

    procA = IntCodeProcessor(source, getInput = getColor, sendOutput = paintAndDrive)
    procA.run()

#print(grid)

print(len(grid))

#print(xMin, xMax, yMin, yMax)
outString = [[" " for x in range(xMax - xMin+1)] for y in range(yMax-yMin+1)]

for key in grid:
    #print(key,(xMax-xMin)-(key[0]-xMin),(yMax-yMin)-(key[1]-yMin))
    outString[(yMax-yMin)-(key[1]-yMin)][(key[0]-xMin)] = "█" if grid[key] == 0 else " "

for row in outString:
    rowStr = ""
    for char in row:
        rowStr += char
    print (rowStr)
