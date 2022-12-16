import sys
from math import sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def printGrid(xMin, xMax, yMin, yMax, grid):
    string1 = "      "
    string2 = "      "
    string3 = "      "
    for i in range(xMin, xMax + 1):
        number = str(i)
        string1 += number[0] + "    "
        string2 += number[1] + "    "
        string3 += number[2] + "    "
    print(string1)
    print(string2)
    print(string3)
    for i in range(yMin, yMax + 1):
        number = str(i)
        print(number.rjust(3) + " ", end="")
        print(grid[i])

def addScanToGrid(xMin, xMax, yMin, yMax, grid, line):
    lineParts = line.split(" -> ")
    for i in range(len(lineParts)-1):
        firstX = int(lineParts[i].split(",")[0])
        firstY = int(lineParts[i].split(",")[1])
        secondX = int(lineParts[i+1].split(",")[0])
        secondY = int(lineParts[i+1].split(",")[1])
        newXMin = min(xMin, firstX, secondX)
        newXMax = max(xMax, firstX, secondX)
        newYMax = max(yMax, firstY, secondY)
        newGrid = []
        for row in grid:
            if newXMin < xMin:
                row[:0] = ["." for x in range(xMin - newXMin)]
            if newXMax > xMax:
                row.extend(["." for x in range(newXMax-xMax)])
            newGrid.append(row)
        grid = newGrid
        xMin = newXMin
        xMax = newXMax
        if newYMax > yMax:
            grid.extend([["." for x in range(xMax - xMin + 1)] for y in range(newYMax - yMax + 1)])
            yMax = newYMax
        if firstX == secondX:
            for j in range(min(firstY, secondY), max(firstY, secondY)+1):
                grid[j][firstX-xMin] = "#"
        if firstY == secondY:
            for j in range(min(firstX, secondX), max(firstX, secondX)+1):
                grid[firstY][j-xMin] = "#"
    return xMin, xMax, yMin, yMax, grid

def dropSand(grid, sandX):
    sandY = 0
    sandStopped = False
    while (sandX > 0 and sandX < len(grid[0])-1 and sandY < len(grid)-1 and not sandStopped):
        if grid[sandY+1][sandX] == ".":
            sandY += 1
        elif grid[sandY+1][sandX-1] == ".":
            sandX -= 1
            sandY +=1
        elif grid[sandY+1][sandX+1] == ".":
            sandX += 1
            sandY +=1
        else:
            sandStopped = True
    grid[sandY][sandX] = "o"
    sandInAbyss = sandX == 0 or sandX == len(grid[0])-1 or sandY == len(grid)-1
    return grid, sandInAbyss

file = loadInput(fileName)
xMin = 500
xMax = 500
yMin = 0
yMax = int(file[0].split(" ")[0].split(",")[1])
grid = [["."] for y in range(yMin, yMax+1)]
for line in file:
    xMin, xMax, yMin, yMax, grid = addScanToGrid(xMin, xMax, yMin, yMax, grid, line)
sandInAbyss = False
unitsOfSand = 0
while not sandInAbyss:
    grid, sandInAbyss = dropSand(grid, 500 - xMin)
    unitsOfSand += 1
print(unitsOfSand-1)
