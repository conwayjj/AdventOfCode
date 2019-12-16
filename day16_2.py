inSignal = "59738571488265718089358904960114455280973585922664604231570733151978336391124265667937788506879073944958411270241510791284757734034790319100185375919394328222644897570527214451044757312242600574353568346245764353769293536616467729923693209336874623429206418395498129094105619169880166958902855461622600841062466017030859476352821921910265996487329020467621714808665711053916709619048510429655689461607438170767108694118419011350540476627272614676919542728299869247813713586665464823624393342098676116916475052995741277706794475619032833146441996338192744444491539626122725710939892200153464936225009531836069741189390642278774113797883240104687033645"
#inSignal = "03036732577212944063491565474664"
realSig = ""
import math

repeats = 10000
for i in range(repeats):
    realSig = realSig + inSignal
inSignal = realSig    
#inSignal = "80871224585914546619083218645595"
intSig = []

for char in inSignal:
    intSig.append(int(char))
#print(inSignal)
#print(intSig)

def lcm(a,b):
    return int((a*b)/math.gcd(a, b))

def buildFilter(size):
    fftFilter = []
    pattern = [0,1,0,-1]
    for i in range(size):
        fftFilter.append([])
        curPattern = 3
        for j in range(size+1):
            if j%(i+1) == 0:
                #print(curPattern)
                curPattern = ((curPattern+1) % 4)
                #print(i,j,curPattern, pattern[curPattern])
            fftFilter[i].append(pattern[curPattern])
        fftFilter[i].pop(0)
    return fftFilter

def filterSignal(signal):
    outSig = []
    pattern = [0,1,0,-1]
    lenSignal = len(signal)
    repLen = int(lenSignal/10000)
    for i in range(lenSignal):
        outSig.append(0)
        curPattern = 0
        for j in range(lenSignal):
            if (j+1)%(i+1) == 0:
                curPattern = (curPattern + 1) % 4
            #print(i,j,curPattern)
            outSig[i] += signal[j]*pattern[curPattern]
        #print (outSig[i])
        outSig[i] = int(str(outSig[i])[-1])
    return outSig
        
def filterSignalEnd(signal, offset):
    outSignal = [0 for _ in range(len(signal))]
    if offset < len(signal)/2:
        print("UNSUPPORTED")
    else:
        outSignal[-1] = signal[-1]
        #print(len(signal)-2, offset)
        for i in range(len(signal)-2,offset,-1):
            #print(i, outSignal[i+1])
            outSignal[i] = (outSignal[i+1] + signal[i]) % 10
    return outSignal
    
def multiFilter(signal, times):
    inSignal = signal
    for i in range(times):
        print(i)
        inSignal = filterSignal(inSignal)
    return inSignal

def multiFilterSignalEnd(signal, offset, times):
    inSignal = signal
    for i in range(times):
        print(i)
        inSignal = filterSignalEnd(inSignal, offset)
    return inSignal

#fftFilter = buildFilter(len(inSignal))

#outSig = filterSignal(intSig)
#print(outSig)
##hSig = multiFilter(intSig, 100)
##print(hSig)

offset = int(inSignal[0:7])
print(offset)
#offset = 20


##offsetStr = ""
##print(offset)
##for char in offset:
##    offsetStr += str(char)
##offset = int(offsetStr)

print("OFFSET:",offset)
hSig = multiFilterSignalEnd(intSig, offset-1, 100)
#print(hSig)
output = hSig[offset:offset+8]
print("OUTPUT:",output)
