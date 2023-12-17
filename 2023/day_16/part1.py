import sys
import collections

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

def getAnswerGrid(grid):
    return [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

def getFacingsGrid(grid):
    return [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

def printAnswerGrid(answerGrid):
    for row in answerGrid:
        for item in row:
            print('.' if item == 0 else '#', end='')
        print()
    print()

def fillAnswerGrid(grid, answerGrid, facingsGrid, startingPoint, facing):
    while True:
        if facing in facingsGrid[startingPoint[0]][startingPoint[1]]:
            return answerGrid, facingsGrid
        if facing == 'N':
            if startingPoint[0] == 0:
                return answerGrid, facingsGrid
            nextPoint = (startingPoint[0] - 1, startingPoint[1])
        elif facing == 'E':
            if startingPoint[1] == len(grid[0]) - 1:
                return answerGrid, facingsGrid
            nextPoint = (startingPoint[0], startingPoint[1] + 1)
        elif facing == 'S':
            if startingPoint[0] == len(grid) - 1:
                return answerGrid, facingsGrid
            nextPoint = (startingPoint[0] + 1, startingPoint[1])
        elif facing == 'W':
            if startingPoint[1] == 0:
                return answerGrid, facingsGrid
            nextPoint = (startingPoint[0], startingPoint[1] - 1)
        else:
            print('FACING ERROR')
            exit()
        if startingPoint[1] != -1:
            facingsGrid[startingPoint[0]][startingPoint[1]].append(facing)
        nextSymbol = grid[nextPoint[0]][nextPoint[1]]
        answerGrid[nextPoint[0]][nextPoint[1]] += 1
        if nextSymbol == '.':
            pass
        elif nextSymbol == '/':
            if facing == 'N':
                facing = 'E'
            elif facing == 'E':
                facing = 'N'
            elif facing == 'S':
                facing = 'W'
            elif facing == 'W':
                facing = 'S'
        elif nextSymbol == '\\':
            if facing == 'N':
                facing = 'W'
            elif facing == 'E':
                facing = 'S'
            elif facing == 'S':
                facing = 'E'
            elif facing == 'W':
                facing = 'N'
        elif nextSymbol == '|':
            if facing == 'E' or facing == 'W':
                answerGrid, facingsGrid = fillAnswerGrid(grid, answerGrid, facingsGrid, nextPoint, 'N')
                facing = 'S'
        elif nextSymbol == '-':
            if facing == 'N' or facing == 'S':
                answerGrid, facingsGrid = fillAnswerGrid(grid, answerGrid, facingsGrid, nextPoint, 'E')
                facing = 'W'
        else:
            print('SYMBOL ERROR')
            exit()
        startingPoint = (nextPoint[0], nextPoint[1])


fileLines = loadInput(fileName)
grid = getPuzzleInput(fileLines)
answerGrid = getAnswerGrid(grid)
facingsGrid = getFacingsGrid(grid)
answerGrid, facingsGrid = fillAnswerGrid(grid, answerGrid, facingsGrid, (0, -1), 'E')
print(sum([len(x) - collections.Counter(x)[0] for x in answerGrid]))
