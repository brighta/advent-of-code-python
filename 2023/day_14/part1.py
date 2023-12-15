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
        input.append(list(fileLine))
    return input

def rotateGrid(grid):
    return [''.join(x) for x in list(zip(*grid[::1]))]

def tiltGrid(grid):
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            newI = i
            while newI != 0:
                newI -= 1
                if grid[newI + 1][j] == 'O' and grid[newI][j] == '.':
                    grid[newI + 1][j] = '.'
                    grid[newI][j] = 'O'
                else:
                    newI = 0
    return grid

def getLoad(grid):
    load = 0
    for i in range(len(grid)):
        load += grid[i].count('O') * (len(grid) - i)
    return load


fileLines = loadInput(fileName)
grid = getPuzzleInput(fileLines)
grid = tiltGrid(grid)
answer = getLoad(grid)
print(answer)
