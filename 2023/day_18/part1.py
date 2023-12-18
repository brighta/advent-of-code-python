import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    input = []
    for fileLine in fileLines:
        parts = fileLine.split()
        input.append([parts[0], int(parts[1])])
    return input

def generateDigMap(input):
    currentPosition = (0, 0)
    digMap = {0: [0]}
    for dig in input:
        if dig[0] == 'U':
            move = (-1, 0)
        elif dig[0] == 'D':
            move = (1, 0)
        elif dig[0] == 'L':
            move = (0, -1)
        elif dig[0] == 'R':
            move = (0, 1)
        else:
            move = (0, 0)
            print("ERROR - Dig Direction = \"" + dig[0] + "\"")
        for _ in range(dig[1]):
            newPosition = (currentPosition[0] + move[0], currentPosition[1] + move[1])
            if newPosition[0] in digMap:
                digMap[newPosition[0]].append(newPosition[1])
            else:
                digMap[newPosition[0]] = [newPosition[1]]
            currentPosition = newPosition
    return digMap

def getGrid(x, y):
    return [[' ' for _ in range(x + 1)] for _ in range(y + 1)]

def getGridWithDigsMarked(digMap):
    minimum = 0
    for i in digMap:
        minimum = min(minimum, min(digMap[i]))
    maximum = 0
    for i in digMap:
        digMap[i] = [x+abs(minimum) for x in digMap[i]]
        maximum = max(maximum, max(digMap[i]))
    newDigMap = {}
    minimum = min(digMap.keys())
    for i in digMap:
        newDigMap[i + abs(minimum)] = digMap[i]
    x = maximum
    y = max(newDigMap.keys())
    grid = getGrid(x, y)
    for y in newDigMap:
        for x in newDigMap[y]:
            grid[y][x] = '#'
    return grid

def markOutsides(grid):
    changed = True
    while changed:
        changed = False
        for i in range(len(grid)):
            for j in range(len(grid[i]) - 2):
                if grid[i][j] == ' ' and (j == 0 or grid[i][j-1] == 'O'):
                    changed = True
                    grid[i][j] = 'O'
            for j in range(int(len(grid[i])) - 1, 1, -1):
                if grid[i][j] == ' ' and (j == len(grid[0]) - 1 or grid[i][j+1] == 'O'):
                    changed = True
                    grid[i][j] = 'O'
        for j in range(len(grid[0])):
            for i in range(len(grid) - 2):
                if grid[i][j] == ' ' and (i == 0 or grid[i-1][j] == 'O'):
                    changed = True
                    grid[i][j] = 'O'
            for i in range(int(len(grid)) - 1, 1, -1):
                if grid[i][j] == ' ' and (i == len(grid) or grid[i+1][j] == 'O'):
                    changed = True
                    grid[i][j] = 'O'
    return grid

def getAnswer(grid):
    answer = len(grid) * len(grid[0]) - sum([row.count('O') for row in grid])
    return answer


fileLines = loadInput(fileName)
input = getPuzzleInput(fileLines)
digMap = generateDigMap(input)
grid = getGridWithDigsMarked(digMap)
grid = markOutsides(grid)
answer = getAnswer(grid)
print(answer)
