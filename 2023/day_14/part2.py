import sys
import math

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    input = []
    for fileLine in fileLines:
        input.append(list(fileLine))
    return input

def rotateGrid(grid):
    return [list(x) for x in list(zip(*reversed(grid[::1])))]

def tiltGrid(grid):
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            newI = i
            while newI != 0:
                newI -= 1
                if grid[newI + 1][j] == 'O' and grid[newI][j] == '.':
                    grid[newI + 1][j] = '.'
                    grid[newI][j] = 'O'
                else:
                    newI = 0
    return grid

def runCycle(grid):
    for _ in range(4):
        grid = tiltGrid(grid)
        grid = rotateGrid(grid)
    return grid

def getLoad(grid):
    load = 0
    for i in range(len(grid)):
        load += grid[i].count('O') * (len(grid) - i)
    return load

def findSequence(loads):
    sequence = loads.copy()
    numSkipped = 0
    while len(sequence) - numSkipped > 8:
        maxLen = math.floor(len(sequence) / 2)
        for x in range(2, maxLen):
            if sequence[0:x] == sequence[x:2*x]:
                return x, numSkipped
        sequence.pop(0)
        numSkipped += 1
    return 0, 0

fileLines = loadInput(fileName)
grid = getPuzzleInput(fileLines)
loads = [getLoad(grid)]
sequenceLength = numSkipped = 0
while sequenceLength == 0:
    grid = runCycle(grid)
    loads.append(getLoad(grid))
    sequenceLength, numSkipped = findSequence(loads)
sequence = loads[numSkipped:numSkipped + sequenceLength]
print(sequence[(1000000000 - numSkipped) % sequenceLength])
