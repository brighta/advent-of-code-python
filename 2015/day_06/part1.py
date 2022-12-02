import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def createGrid():
    return [[0 for x in range(1000)] for x in range(1000)]

def performActionOnGrid(action, grid):
    actionParts = action.split(" ")
    x1 = int(actionParts[-3].split(",")[0])
    y1 = int(actionParts[-3].split(",")[1])
    x2 = int(actionParts[-1].split(",")[0])
    y2 = int(actionParts[-1].split(",")[1])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if actionParts[0] == "toggle":
                grid[x][y] = abs(grid[x][y]-1)
            elif actionParts[0] == "turn":
                if actionParts[1] == "on":
                    grid[x][y] = 1
                elif actionParts[1] == "off":
                    grid[x][y] = 0
    return grid

def countLightsOn(grid):
    return sum([sum(i) for i in zip(*grid)])

file = loadInput(fileName)
grid = createGrid()
for row in file:
    grid = performActionOnGrid(row.rstrip(), grid)
print(countLightsOn(grid))
