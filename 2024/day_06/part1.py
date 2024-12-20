import sys

from classes import Point

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getGrid(file):
    grid = []
    for line in file:
        grid.append(list(line.rstrip()))
    return grid

def getStartingPoint(grid):
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == '^':
                return Point(x, y)

def getDistinctSteps(grid, startingPoint):
    distinctSteps = []
    nextPoint = startingPoint
    while nextPoint is not None:
        distinctSteps.append(nextPoint)
        nextPoint = nextPoint.move(grid)
    return set([distinctStep.getCoordinates() for distinctStep in distinctSteps])


file = loadInput(fileName)
grid = getGrid(file)
startingPoint = getStartingPoint(grid)
distinctSteps = getDistinctSteps(grid, startingPoint)
print (distinctSteps)
print(len(distinctSteps))
