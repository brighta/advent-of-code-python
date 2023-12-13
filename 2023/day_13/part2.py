import sys
import math

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    grids = []
    grid = []
    for fileLine in fileLines:
        if fileLine == '':
            grids.append(grid)
            grid = []
        else:
            grid.append(fileLine)
    grids.append(grid)
    return grids

def rotateGrid(grid):
    return [''.join(x) for x in list(zip(*grid[::1]))]

def findNumberDifferent(string1, string2):
    numberDifferent = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            numberDifferent += 1
    return numberDifferent

def getReflectiveCount(grid):
    for bottomIndex in range(1, len(grid), 2):
        middle = bottomIndex / 2
        numberIncorrect = 0
        for i in range(0, math.ceil(middle)):
            numberIncorrect += findNumberDifferent(grid[i], grid[bottomIndex - i])
            if numberIncorrect > 1:
                break
        if numberIncorrect == 1:
            return math.ceil(middle)
    for topIndex in range(len(grid) - 2, 0, -2):
        middle = (len(grid) - 1 - topIndex) / 2
        numberIncorrect = 0
        for i in range(len(grid) - 1, len(grid) - 1 - math.ceil(middle), -1):
            numberIncorrect += findNumberDifferent(grid[i], grid[topIndex + len(grid) - 1 - i])
            if numberIncorrect > 1:
                break
        if numberIncorrect == 1:
            return len(grid) - 1 - math.floor(middle)
    return 0

def getReflectiveValue(grid):
    horizontalLength = getReflectiveCount(grid)
    if horizontalLength != 0:
        return horizontalLength * 100
    verticalLength = getReflectiveCount(rotateGrid(grid))
    if verticalLength != 0:
        return verticalLength
    return 0

fileLines = loadInput(fileName)
grids = getPuzzleInput(fileLines)
answer = 0
for grid in grids:
    answer += getReflectiveValue(grid)
print(answer)