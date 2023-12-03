import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()


def getGearRatios(fileLines):
    gearRatios = []
    for i in range(0, len(fileLines)):
        matches = re.finditer(r'\*', fileLines[i])
        for match in matches:
            startIndex = match.start() - 1 if not match.start() == 0 else match.start()
            endIndex = match.start() + 1 if not match.start() == len(fileLines[i]) else match.start()
            startRowIndex = i - 1 if not i == 0 else i
            endRowIndex = i + 1 if not i == len(fileLines) - 1 else i
            gearRatios.append(getGearRatio(startIndex, endIndex, startRowIndex, endRowIndex))
    return gearRatios

def getGearRatio(startIndex, endIndex, startRowIndex, endRowIndex):
    partNumbers = []
    for y in range(startRowIndex, endRowIndex + 1):
        matches = re.finditer(r'\d+', fileLines[y])
        for match in matches:
            start = match.start()
            end = match.end()
            if start in range(startIndex, endIndex + 1) or end - 1 in range(startIndex, endIndex + 1):
                partNumbers.append(int(fileLines[y][start:end]))
    if len(partNumbers) == 2:
        return partNumbers[0] * partNumbers[1]
    return 0

fileLines = loadInput(fileName)
gearRatios = getGearRatios(fileLines)
answer = 0
for gearRatio in gearRatios:
    answer += gearRatio
print(answer)
