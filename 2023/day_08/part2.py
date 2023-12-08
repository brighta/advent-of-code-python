import sys
import math
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    inputsMap = {}
    for fileLine in fileLines:
        parts = re.findall('[A-Z1-2]+', fileLine)
        inputsMap[parts[0]] = [parts[1], parts[2]]
    return inputsMap

def getCurrentSteps(keys):
    currentSteps = []
    for key in keys:
        if key[2] == 'A':
            currentSteps.append(key)
    return currentSteps

def getRepeatingLengths(currentSteps, inputsMap, directions):
    repeatingLengths = []
    for currentStep in currentSteps:
        answer = 0
        while currentStep[2] != 'Z':
            direction = directions[answer % len(directions)]
            currentStep = inputsMap[currentStep][1 if direction == 'R' else 0]
            answer += 1
        repeatingLengths.append(answer)
    return repeatingLengths


fileLines = loadInput(fileName)
directions = fileLines[0]
inputsMap = getPuzzleInput(fileLines[2:])
currentSteps = getCurrentSteps(inputsMap.keys())
repeatingLengths = getRepeatingLengths(currentSteps, inputsMap, directions)
print(math.lcm(*repeatingLengths))
