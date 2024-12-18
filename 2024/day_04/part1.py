import sys
import re

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

def reverseGrid(grid):
    newGrid = []
    for row in grid:
        row.reverse()
        newGrid.append(row)
    return newGrid

def rotateGrid90(grid):
    newGrid = []
    for j in range(len(grid[0])):
        newRow = []
        for i in range(len(grid)):
            newRow.append(grid[i][j])
        newGrid.append(newRow)
    return newGrid

def rotateGrid45(grid):
    newGrid = []
    for i in range(len(grid)):
        start = len(grid) - 1 - i
        end = len(grid) - start - 1
        newRow = []
        for j in range(start):
            newRow.append('.')
        newRow.extend(grid[i])
        for j in range(end):
            newRow.append('.')
        newGrid.append(newRow)
    return rotateGrid90(newGrid)



def findMatchesInGrid(grid):
    count = 0
    for row in grid.copy():
        line = "".join(row.copy())
        count += findMatchesInLine(line)
        row.reverse()
        line = "".join(row.copy())
        count += findMatchesInLine(line)
    return count

def findMatchesInLine(line):
    return len(re.findall(r'XMAS', line))

def printGrid(grid):
    for line in grid:
        print("".join(line))

file = loadInput(fileName)
grid = getGrid(file)
count = findMatchesInGrid(grid)
newGrid = rotateGrid90(grid)
count += findMatchesInGrid(newGrid)
newGrid = rotateGrid45(grid)
count += findMatchesInGrid(newGrid)
newGrid = reverseGrid(grid)
newGrid = rotateGrid45(newGrid)
count += findMatchesInGrid(newGrid)
print(count)
