import sys
import math
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    time = int(''.join(re.findall(r'\d+', fileLines[0])))
    distance = int(''.join(re.findall(r'\d+', fileLines[1])))
    return [[time, distance]]

def getNumberOfSolutions(input):
    i = math.ceil(input[0] / 2)
    count = 0
    while True:
        if i * (input[0] - i) > input[1]:
            count += 1
            i += 1
        else:
            break
    answer = count * 2
    if math.ceil(input[0] / 2) == input[0] / 2:
        answer -= 1
    return answer


fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
answer = 1
for input in inputs:
    answer *= getNumberOfSolutions(input)
print(answer)