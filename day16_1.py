inSignal = "59738571488265718089358904960114455280973585922664604231570733151978336391124265667937788506879073944958411270241510791284757734034790319100185375919394328222644897570527214451044757312242600574353568346245764353769293536616467729923693209336874623429206418395498129094105619169880166958902855461622600841062466017030859476352821921910265996487329020467621714808665711053916709619048510429655689461607438170767108694118419011350540476627272614676919542728299869247813713586665464823624393342098676116916475052995741277706794475619032833146441996338192744444491539626122725710939892200153464936225009531836069741189390642278774113797883240104687033645"
realSig = ""
for i in range(10000):
    realSig = realSig + inSignal
inSignal = realSig    
#inSignal = "80871224585914546619083218645595"
intSig = []

for char in inSignal:
    intSig.append(int(char))
print(inSignal)
print(intSig)

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

def filterSignal(signal, filt):
    outSig = []
    for i in range(len(signal)):
        outSig.append(0)
        for j in range(len(signal)):
            outSig[i] += signal[j]*filt[i][j]
        outSig[i] = int(str(outSig[i])[-1])
    return outSig
        

def multiFilter(signal, filt, times):
    inSignal = signal
    for i in range(times):
        inSignal = filterSignal(inSignal, filt)
    return inSignal

fftFilter = buildFilter(len(inSignal))

outSig = filterSignal(intSig, fftFilter)

print(outSig)

hSig = multiFilter(intSig, fftFilter, 100)

print(hSig)
