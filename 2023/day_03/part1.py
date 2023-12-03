import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()


def getPartNumbers(fileLines):
    partNumbers = []
    for i in range(0, len(fileLines)):
        matches = re.finditer(r'\d+', fileLines[i])
        for match in matches:
            start = match.start()
            end = match.end()
            if isPartNumber(fileLines, i, start, end):
                number = fileLines[i][start:end]
                partNumbers.append(int(number))
    return partNumbers


def isPartNumber(fileLines, i, start, end):
    startIndex = start - 1 if not start == 0 else start
    endIndex = end + 1 if not end == len(fileLines[i]) else end
    if i != 0:
        for value in fileLines[i - 1][startIndex:endIndex]:
            if not value == '.':
                return True
    if i != len(fileLines) - 1:
        for value in fileLines[i + 1][startIndex:endIndex]:
            if not value == '.':
                return True
    if not start == 0 and not fileLines[i][startIndex] == '.':
        return True
    if not end == len(fileLines[i]) and not fileLines[i][end] == '.':
        return True
    return False


fileLines = loadInput(fileName)
partNumbers = getPartNumbers(fileLines)
answer = 0
for partNumber in partNumbers:
    answer += partNumber
print(answer)
