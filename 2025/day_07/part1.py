import sys
from math import prod

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

def getStart(grid):
    return (grid[0].index('S'), 0)

def findSplitters(grid, start):
    global splitters
    newY = start[1] + 1
    if newY == len(grid):
        return
    if grid[newY][start[0]] != "^":
        findSplitters(grid, (start[0], newY))
    else:
        if (newY, start[0]) not in splitters:
            splitters.add((newY, start[0]))
            findSplitters(grid, (start[0] - 1, newY))
            findSplitters(grid, (start[0] + 1, newY))

lines = loadInput(fileName)
grid = getGrid(lines)
start = getStart(grid)
splitters = set()
findSplitters(grid, start)
print(len(splitters))