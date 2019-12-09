xSize = 25
ySize = 6
picSize = xSize * ySize
with open('day8.txt') as inFile:
    pic = inFile.readline().strip()

print(pic)

numLayers = int(len(pic) / (picSize))

fewestZeros = picSize
score = 0
print(len(pic),picSize, numLayers)
for i in range(numLayers):
    zeros = pic.count('0', i*picSize, i*picSize+picSize)
    if zeros < fewestZeros:
        fewestZeros = zeros
        score = pic.count('1', i*picSize, i*picSize+picSize) * pic.count('2', i*picSize, i*picSize+picSize)
        print(len(pic), i*picSize, pic[i*picSize:i*picSize+picSize], score)    
print (fewestZeros, score)

outPic = [0 for i in range(picSize)]
for i in range(picSize):
    curLoc = i
    while pic[curLoc] == '2':
        curLoc += picSize
        if curLoc > len(pic):
            print("ERROR")
            break
    outPic[i] = pic[curLoc]


for j in range(ySize):
    outLine = ""
    for i in range(xSize):
      outLine += "X" if outPic[i+j*xSize]=='0' else " "
    print(outLine)
