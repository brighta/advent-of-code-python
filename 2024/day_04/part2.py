import sys
import re
from math import ceil

regexPattern = r'mul\(\d{1,3},\d{1,3}\)'

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
            newRow.append('#')
        newRow.extend(grid[i])
        for j in range(end):
            newRow.append('#')
        newGrid.append(newRow)
    rotatedGrid = rotateGrid90(newGrid)
    # printGrid(rotatedGrid)
    # print('')
    newGrid = []
    for row in rotatedGrid:
        if len(row) - row.count('#') == len(grid[0]):
            newGrid.append(list(filter("#".__ne__, row)))
        else:
            numChars = len(row) - row.count('#')
            numToRemove = (int(ceil((len(row) - numChars) / 2)))
            # print("Num Chars: " + str(numChars) +", Num To Remove: " + str(numToRemove))
            if row[0] == '#':
                newRow = row[numToRemove:]
                for i in range(len(grid[0]) - len(newRow)):
                    newRow.append('#')
                newGrid.append(newRow)
            else:
                newRow = row[:len(row) - numToRemove]
                for i in range(len(grid[0]) - len(newRow)):
                    newRow.insert(0, '#')
                newGrid.append(newRow)
    return newGrid

def findMatchesInGrid(grid):
    count = 0
    for i in range(1, len(grid) - 1):
        row = grid[i]
        line = "".join(row.copy())
        count += findXMas(grid, line, i)
        # row.reverse()
        # line = "".join(row.copy())
        # count += findXMas(grid, line, i)
    return count

def findXMas(grid, line, i):
    indexes = findIndexesInLine(line)
    count = 0
    for index in indexes:
        if (grid[i-1][index+1] == 'M' and grid[i+1][index+1] == 'S') or (grid[i-1][index+1] == 'S' and grid[i+1][index+1] == 'M'):
            count += 1
            print('[' + str(i) + ',' + str(index) + ']')
    indexes = findIndexesInLine(line, True)
    for index in indexes:
        if (grid[i-1][index+1] == 'M' and grid[i+1][index+1] == 'S') or (grid[i-1][index+1] == 'S' and grid[i+1][index+1] == 'M'):
            count += 1
            print('[' + str(i) + ',' + str(index) + ']')
    return count

def findIndexesInLine(line, reverse=False):
    letters = 'SAM' if reverse else 'MAS'
    return [i for i in range(len(line)) if line.startswith(letters, i)]

def printGrid(grid):
    for line in grid:
        print("".join(line))

file = loadInput(fileName)
grid = getGrid(file)
# printGrid(grid)
# print()
newGrid = rotateGrid45(grid)
printGrid(newGrid)
print('')
count = findMatchesInGrid(newGrid)
print()
newGrid = reverseGrid(grid)
newGrid = rotateGrid45(newGrid)
printGrid(newGrid)
print('')
count += findMatchesInGrid(newGrid)
print()
print(count)
