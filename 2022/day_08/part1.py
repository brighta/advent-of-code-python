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

def updateGrid(grid, file):
    grid[0] = [1 for x in range(len(grid[0]))]
    grid[len(grid)-1] = [1 for x in range(len(grid[0]))]
    for y in range(len(grid)):
        grid[y][0] = 1
        grid[y][len(grid[0])-1] = 1
    for x in range(1, len(grid[0])-1):
        currentTallest = int(file[0][x])
        for y in range(1, len(grid[0])-1):
            grid, currentTallest = validateTree(grid, file, x, y, currentTallest)
    for x in range(1, len(grid[0])-1):
        currentTallest = int(file[len(grid)-1][x])
        for y in range(len(grid[0])-1, 0, -1):
            grid, currentTallest = validateTree(grid, file, x, y, currentTallest)
    for y in range(1, len(grid[0])-1):
        currentTallest = int(file[y][0])
        for x in range(1, len(grid[0])-1):
            grid, currentTallest = validateTree(grid, file, x, y, currentTallest)
    for y in range(1, len(grid[0])-1):
        currentTallest = int(file[y][len(grid[0])-1])
        for x in range(len(grid[0])-1, 0, -1):
            grid, currentTallest = validateTree(grid, file, x, y, currentTallest)
    return grid

def countTreesVisible(grid):
    return sum([sum(i) for i in zip(*grid)])

file = loadInput(fileName)
grid = generateGrid(file)
grid = updateGrid(grid, file)
print(countTreesVisible(grid))

