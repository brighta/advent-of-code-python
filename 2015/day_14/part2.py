import sys
import math

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    reindeers = {}
    for line in fileLines:
        lineParts = line.split(' ')
        name = lineParts[0]
        speed = int(lineParts[3])
        flyingSeconds = int(lineParts[6])
        restingSeconds = int(lineParts[13])
        reindeers[name] = [speed, flyingSeconds, restingSeconds]
    return reindeers

def getAnswer(reindeers, numSeconds):
    race = {}
    for reindeer in reindeers:
        reindeerDetails = reindeers[reindeer]
        race[reindeer] = [0, 0, reindeerDetails, 1, reindeerDetails[1]]
    for _ in range(numSeconds):
        for reindeer in race:
            if race[reindeer][3] == 1:
                race[reindeer][1] += race[reindeer][2][0]
            if race[reindeer][4] == 1:
                if race[reindeer][3] == 1:
                    race[reindeer][3] = 0
                    race[reindeer][4] = race[reindeer][2][2]
                else:
                    race[reindeer][3] = 1
                    race[reindeer][4] = race[reindeer][2][1]
            else:
                race[reindeer][4] -= 1
        maxDistance = max([race[reindeer][1] for reindeer in race])
        for reindeer in race:
            if race[reindeer][1] == maxDistance:
                race[reindeer][0] += 1
    return max([race[reindeer][0] for reindeer in race])


fileLines = loadInput(fileName)
reindeers = getPuzzleInput(fileLines)
answer = getAnswer(reindeers, 1000 if 'sample' in fileName else 2503)
print(answer)
