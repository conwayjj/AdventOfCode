class moon:
    def __init__(self, pos=[0,0,0], vel=[0,0,0], name=""):
        self.pos = pos
        self.vel = vel
        self.name = name

    def updateVel(self, moons):
        for moon in moons:
            for i in range(len(moon.pos)):
                if moon.pos[i] < self.pos[i]:
                    self.vel[i] -= 1
                elif moon.pos[i] > self.pos[i]:
                    self.vel[i] += 1

    def getEnergy(self):
        pe = sum([abs(x) for x in self.pos])
        ke = sum([abs(x) for x in self.vel])
        return pe*ke
        
    def updatePos(self):
        for i in range(len(self.pos)):
            self.pos[i] += self.vel[i]

    def __repr__(self):
        retStr = "MOON " + self.name + " POS: " + str(self.pos) + "VEL: " + str(self.vel)
        return retStr

def moonState(moons,axis):
    retStr = str(axis)
    for moon in moons:
        retStr+=moon.name
        retStr+=str(moon.pos[axis])
        retStr+="-"
        retStr+=str(moon.vel[axis])
    return retStr

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return int((a*b)/gcd(a,b))
    
moonA = moon(pos = [3,2,-6], vel = [0,0,0],name = "A")
moonB = moon(pos = [-13,18,10], vel = [0,0,0],name = "B")
moonC = moon(pos = [-8,-1,13], vel = [0,0,0],name ="C")
moonD = moon(pos = [5,10,4], vel = [0,0,0],name ="D")

moons = [moonA, moonB, moonC, moonD]

xPrevStates = {}
yPrevStates = {}
zPrevStates = {}
xCycle = None
yCycle = None
zCycle = None
steps = 0
while xCycle == None or yCycle == None or zCycle == None:
    xState = moonState(moons,0)
    yState = moonState(moons,1)
    zState = moonState(moons,2)
    #print(xState,yState,zState)
    if xCycle == None and xState in xPrevStates:
        xCycle = steps
    else:
        xPrevStates[xState] = 1

    if yCycle == None and yState in yPrevStates:
        yCycle = steps
    else:
        yPrevStates[yState] = 1

    if zCycle == None and zState in zPrevStates:
        zCycle = steps
    else:
        zPrevStates[zState] = 1
        
    for moon in moons:
        moon.updateVel(moons)
    for moon in moons:
        moon.updatePos()
    steps += 1
    if steps % 10000 == 0:
        print(steps)

print (moons)
print("XCYCLE:",xCycle,"YCYCLE:",yCycle,"ZCYCLE:",zCycle)
print("TOTAL CYCLE TIME:", lcm(zCycle,lcm(xCycle,yCycle)))

totalEnergy = 0
for moon in moons:
    totalEnergy += moon.getEnergy()
    print (moon.name, moon.getEnergy())
print("TOTAL ENERGY:",totalEnergy)
print("STEPS:", steps)
