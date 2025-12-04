import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getGrid(file):
    grid = []
    for line in file:
        grid.append(list(line.replace('\n', '')))
    return grid

def getAccessibleRollCount(grid):
    count = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == "@" and isRollAccessible(x, y, grid):
                count += 1
    return count

def isRollAccessible(x, y, grid):
    adjacentPositions = []
    for x1 in range(max(0, x - 1), min(len(grid[0]), x + 2)):
        for y1 in range(max(0, y - 1), min(len(grid), y + 2)):
            if "{},{}".format(x, y) != "{},{}".format(x1, y1):
                adjacentPositions.append(grid[y1][x1])
    return adjacentPositions.count("@") < 4

file = loadInput(fileName)
grid = getGrid(file)
numAccessibleRolls = getAccessibleRollCount(grid)
print(numAccessibleRolls)