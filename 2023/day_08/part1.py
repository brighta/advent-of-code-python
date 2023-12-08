import sys
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
        parts = re.findall('[A-Z]+', fileLine)
        inputsMap[parts[0]] = [parts[1], parts[2]]
    return inputsMap


fileLines = loadInput(fileName)
directions = fileLines[0]
inputsMap = getPuzzleInput(fileLines[2:])
answer = 0
currentStep = 'AAA'
while currentStep != 'ZZZ':
    direction = directions[answer % len(directions)]
    currentStep = inputsMap[currentStep][1 if direction == 'R' else 0]
    answer += 1
print(answer)
