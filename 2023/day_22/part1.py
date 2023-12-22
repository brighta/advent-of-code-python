import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    bricks = []
    for fileLine in fileLines:
        coords = fileLine.split('~')
        brick = [list(map(int, coords[0].split(','))), list(map(int, coords[1].split(',')))]
        bricks.append(brick)
    return bricks

def getBrickTower(bricks):
    maxX = max([item for row in [[brick[0][0], brick[1][0]] for brick in bricks] for item in row])
    maxY = max([item for row in [[brick[0][1], brick[1][1]] for brick in bricks] for item in row])
    maxZ = max([item for row in [[brick[0][2], brick[1][2]] for brick in bricks] for item in row])
    brickTower = [[['-' for _ in range(maxX + 1)] for _ in range(maxY + 1)]]
    brickTower.extend([[['.' for _ in range(maxX + 1)] for _ in range(maxY + 1)] for _ in range(maxZ)])
    for i in range(len(bricks)):
        brick = bricks[i]
        for z in range(brick[0][2], brick[1][2] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                for x in range(brick[0][0], brick[1][0] + 1):
                    brickTower[z][y][x] = i
    return brickTower

def brickCanMove(brick, brickTower):
    z = brick[0][2]
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if brickTower[z - 1][y][x] != '.':
                return False
    return True

def lowerBricks(bricks, brickTower):
    somethingMoved = True
    while somethingMoved:
        somethingMoved = False
        for brick in bricks:
            moved = True
            while moved:
                moved = False
                letter = brickTower[brick[0][2]][brick[0][1]][brick[0][0]]
                if brickCanMove(brick, brickTower):
                    moved = True
                    somethingMoved = True
                    for z in range(brick[1][2], brick[0][2] - 1, -1):
                        for x in range(brick[0][0], brick[1][0] + 1):
                            for y in range(brick[0][1], brick[1][1] + 1):
                                if z == brick[1][2]:
                                    brickTower[z][y][x] = '.'
                                brickTower[z - 1][y][x] = letter
                    brick[0][2] -= 1
                    brick[1][2] -= 1
    return bricks, brickTower

def getBricksAbove(brick, brickTower):
    bricksAbove = set()
    z = brick[1][2]
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if brickTower[z + 1][y][x] != '.':
                bricksAbove.update({brickTower[z + 1][y][x]})
    return bricksAbove

def numBricksBelow(brick, brickTower):
    bricksBelow = set()
    z = brick[0][2]
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if brickTower[z - 1][y][x] != '.':
                bricksBelow.update({brickTower[z - 1][y][x]})
    return len(bricksBelow)

def brickCanDisintegrate(brick, bricks, brickTower):
    bricksAbove = getBricksAbove(brick, brickTower)
    if len(bricksAbove) == 0:
        return True
    canDisintegrate = True
    for brickAbove in bricksAbove:
        if numBricksBelow(bricks[brickAbove], brickTower) == 1:
            canDisintegrate = False
    return canDisintegrate

def findNumDisintegrableBricks(bricks, brickTower):
    disintegrableBricks = []
    for brick in bricks:
        if brickCanDisintegrate(brick, bricks, brickTower):
            disintegrableBricks.append(brick)
    return len(disintegrableBricks)


fileLines = loadInput(fileName)
bricks = getPuzzleInput(fileLines)
brickTower = getBrickTower(bricks)
bricks, brickTower = lowerBricks(bricks, brickTower)
answer = findNumDisintegrableBricks(bricks, brickTower)
print(answer)
