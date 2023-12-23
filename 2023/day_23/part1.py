import sys

sys.setrecursionlimit(10000)

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    grid = []
    for fileLine in fileLines:
        grid.append(list(fileLine))
    return grid

def getPointValue(grid, point):
    return grid[point[1]][point[0]]

def printRoute(grid, route):
    newGrid = [row.copy() for row in grid]
    for point in route:
        newGrid[point[1]][point[0]] = 'O'
    print('Length: ' + str(len(route) - 1))
    for i in range(len(newGrid)):
        print(''.join(newGrid[i]) + '  -  ' + ''.join(grid[i]))
    print()

def findLongestHike(grid, endPoint, currentPoint, route):
    global longestHike
    currentValue = getPointValue(grid, currentPoint)
    if currentValue == '>':
        directions = [(1, 0)]
    elif currentValue == 'v':
        directions = [(0, 1)]
    elif currentValue == '<':
        directions = [(-1, 0)]
    elif currentValue == '^':
        directions = [(0, -1)]
    else:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for direction in directions:
        nextPoint = (currentPoint[0] + direction[0], currentPoint[1] + direction[1])
        if nextPoint == endPoint:
            route.append(nextPoint)
            longestHike = max(longestHike, len(route) - 1)
            break
        if nextPoint in route or nextPoint[0] < 0 or nextPoint[0] >= len(grid[0]) or nextPoint[1] < 0 or nextPoint[1] >= len(grid) or \
                (direction[0] == -1 and getPointValue(grid, nextPoint) == '>') or (direction[0] == 1 and getPointValue(grid, nextPoint) == '<') or \
                (direction[1] == -1 and getPointValue(grid, nextPoint) == 'v') or (direction[1] == 1 and getPointValue(grid, nextPoint) == '^') or \
                getPointValue(grid, nextPoint) not in ['.', '^', '>', 'v', '<']:
            continue
        newRoute = route.copy()
        newRoute.append(nextPoint)
        findLongestHike(grid, endPoint, nextPoint, newRoute)


fileLines = loadInput(fileName)
grid = getPuzzleInput(fileLines)
longestHike = 0
start = (1, 0)
end = (len(grid) - 2, len(grid[0]) - 1)
findLongestHike(grid, end, start, [start])
print(longestHike)
