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
    maxAnswer = 0
    for reindeer in reindeers:
        answer = 0
        reindeerDetails = reindeers[reindeer]
        timePerLoop = reindeerDetails[1] + reindeerDetails[2]
        timesFlownDecimal = numSeconds / timePerLoop
        fullTimesFlown = math.floor(timesFlownDecimal)
        answer += fullTimesFlown * reindeerDetails[0] * reindeerDetails[1]
        timeRemaining = round((timesFlownDecimal - fullTimesFlown) * timePerLoop)
        if timeRemaining >= reindeerDetails[1]:
            answer += reindeerDetails[0] * reindeerDetails[1]
        else:
            answer += reindeerDetails[0] * timeRemaining
        if answer > maxAnswer:
            maxAnswer = answer
    return maxAnswer


fileLines = loadInput(fileName)
reindeers = getPuzzleInput(fileLines)
answer = getAnswer(reindeers, 1000 if 'sample' in fileName else 2503)
print(answer)
