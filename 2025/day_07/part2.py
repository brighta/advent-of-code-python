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

def countTimelines(grid, start):
    global splitters
    newY = start[1] + 1
    if newY == len(grid):
        return 1
    if grid[newY][start[0]] != "^":
        return countTimelines(grid, (start[0], newY))
    else:
        newStart = (newY, start[0])
        if newStart in cache:
            return cache[newStart]
        else:
            result = countTimelines(grid, (start[0] - 1, newY)) + countTimelines(grid, (start[0] + 1, newY))
            cache[newStart] = result
            return result

lines = loadInput(fileName)
grid = getGrid(lines)
start = getStart(grid)
cache = {}
timelines = countTimelines(grid, start)
print(timelines)