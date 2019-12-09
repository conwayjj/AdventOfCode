from IntCodeProcessor import IntCodeProcessor

if __name__ == '__main__':
    with open('day9.txt') as inFile:
        sourceTxt = inFile.read().strip().split(',')
        source = {}
        for i in range(len(sourceTxt)):
            source[i] = int(sourceTxt[i])

    procA = IntCodeProcessor(source)
    procA.run()
