import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    grid = []
    for fileLine in fileLines:
        grid.append(list(fileLine))
    return grid

def findStart(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                return x, y

def findPointsReached(grid, start, numSteps):
    currentPoints = [start]
    stepsTaken = 0
    while stepsTaken < numSteps:
        newSteps = []
        for point in currentPoints:
            pointOptions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for pointOption in pointOptions:
                newPoint = (point[0] + pointOption[0], point[1] + pointOption[1])
                if grid[newPoint[1] % len(grid)][newPoint[0] % len(grid[0])] != '#':
                    newSteps.append(newPoint)
        currentPoints = list(set(newSteps))
        stepsTaken += 1
    return len(currentPoints)


fileLines = loadInput(fileName)
grid = getPuzzleInput(fileLines)
start = findStart(grid)
# Will get there, eventually, with enough time and memory.
answer = findPointsReached(grid, start, 26501365)
print(answer)
