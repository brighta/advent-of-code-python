import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def generateGrid(file):
    xLength = len(file[0].rstrip())
    yLength = len(file)
    return [[0 for x in range(xLength)] for y in range(yLength)]

def validateTree(grid, file, x, y, currentTallest):
    if int(file[y][x]) > currentTallest:
        grid[y][x] = 1
        currentTallest = int(file[y][x])
    return grid, currentTallest

def getScore(file, treeHeight, xStart, xEnd, xChange, yStart, yEnd, yChange):
    score = 1
    if xChange == 0:
        xRange = [xStart]
    else:
        xRange = range(xStart, xEnd, xChange)
    if yChange == 0:
        yRange = [yStart]
    else:
        yRange = range(yStart, yEnd, yChange)
    for x in xRange:
        for y in yRange:
            if int(file[y][x]) >= treeHeight:
                return score
            score += 1
    return score

def updateGrid(grid, file):
    for x in range(1, len(grid[0])-1):
        for y in range(1, len(grid)-1):
            treeHeight = int(file[y][x])
            grid[y][x] = getScore(file, treeHeight, x-1, 0, -1, y, y, 0) * \
                         getScore(file, treeHeight, x+1, len(grid[0]), 1, y, y, 0) * \
                         getScore(file, treeHeight, x, x, 0, y-1, 0, -1) * \
                         getScore(file, treeHeight, x, x, 0, y+1, len(grid)-1, 1)
    return grid

def getMaxScenicScore(grid):
    return max([max(i) for i in zip(*grid)])

file = loadInput(fileName)
grid = generateGrid(file)
grid = updateGrid(grid, file)
print(getMaxScenicScore(grid))

