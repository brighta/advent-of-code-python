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

def printGrid(grid):
    for row in grid:
        print("".join(row))

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

def copyGrid(grid):
    gridCopy = []
    for row in grid:
        gridCopy.append(row.copy())
    return gridCopy

def checkIfNewObstacleCoordinateCreatesLoop(grid, startingPoint, newObstacleCoordinate):
    gridCopy = copyGrid(grid)
    gridCopy[newObstacleCoordinate[1]][newObstacleCoordinate[0]] = 'O'
    # printGrid(gridCopy)
    distinctSteps = []
    nextPoint = Point(startingPoint.x, startingPoint.y, startingPoint.facing)
    while True:
        distinctSteps.append(nextPoint)
        nextPoint = nextPoint.move(gridCopy)
        if nextPoint is None:
            # print("{} - {}".format(nextPoint, distinctSteps))
            return False
        else:
            if nextPoint in distinctSteps:
                # print("{} - {}".format(nextPoint, distinctSteps))
                return True

def getValidNewObstacleCoordinates(distinctSteps, grid):
    validNewObstacleCoordinates = []
    for distinctStep in distinctSteps:
        # print()
        # print(distinctStep)
        # print(startingPoint)
        if checkIfNewObstacleCoordinateCreatesLoop(grid, startingPoint, distinctStep):
            validNewObstacleCoordinates.append(distinctStep)
    return validNewObstacleCoordinates


file = loadInput(fileName)
grid = getGrid(file)
startingPoint = getStartingPoint(grid)
# print(startingPoint)
distinctSteps = getDistinctSteps(grid, startingPoint)
distinctSteps.remove(startingPoint.getCoordinates())
validNewObstacleCoordinates = getValidNewObstacleCoordinates(distinctSteps, grid)
print(len(validNewObstacleCoordinates))
