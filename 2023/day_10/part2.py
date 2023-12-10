import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

unchecked = '\033[91m.\033[0m'
one =       '\033[96m1\033[0m'
two =       '\033[94m2\033[0m'
inside =    '\033[93mI\033[0m'

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    inputs = []
    for fileLine in fileLines:
        inputs.append([*fileLine])
    return inputs

def getStart(inputs):
    for i in range(len(inputs)):
        if 'S' in inputs[i]:
            return i, inputs[i].index('S')

def getLoopMap(i, j, inputs):
    loopMap = [[unchecked for x in range(len(inputs[0]))] for y in range(len(inputs))]
    loopMap[i][j] = "\033[92mS\033[0m"
    count = 1
    indexes = [(i, j)]
    facing = -1
    if j > 0 and (inputs[i][j-1] == 'L' or  inputs[i][j-1] == 'F' or inputs[i][j-1] == '-'):
        indexes.append((i, j-1))
        facing = 3
    elif j < len(inputs[0]) - 1 and (inputs[i][j+1] == 'J' or inputs[i][j+1] == '7' or inputs[i][j-1] == '-'):
        indexes.append((i, j+1))
        facing = 1
    elif i > 0 and (inputs[i-1][j] == '7' or inputs[i-1][j] == 'F' or inputs[i-1][j] == '|'):
        indexes.append((i-1, j))
        facing = 0
    elif i < len(inputs) - 1 and (inputs[i+1][j] == 'L' or  inputs[i+1][j] == 'J' or inputs[i+1][j] == '|'):
        indexes.append((i+1, j))
        facing = 2
    currentSymbol = inputs[indexes[1][0]][indexes[1][1]]
    while currentSymbol != 'S':
        loopMap[indexes[1][0]][indexes[1][1]] = '\033[92m' + currentSymbol + '\033[0m'
        if currentSymbol == '|':
            indexes.append((indexes[1][0] + indexes[1][0] - indexes[0][0], indexes[0][1]))
            if indexes[1][1] != 0 and loopMap[indexes[1][0]][indexes[1][1] - 1] == unchecked:
                loopMap[indexes[1][0]][indexes[1][1] - 1] = one if facing == 0 else two
            if indexes[1][1] != len(loopMap[0]) - 1 and loopMap[indexes[1][0]][indexes[1][1] + 1] == unchecked:
                loopMap[indexes[1][0]][indexes[1][1] + 1] = one if facing == 2 else two
        elif currentSymbol == '-':
            indexes.append((indexes[1][0], indexes[1][1] + indexes[1][1] - indexes[0][1]))
            if indexes[1][0] != 0 and loopMap[indexes[1][0] - 1][indexes[1][1]] == unchecked:
                loopMap[indexes[1][0] - 1][indexes[1][1]] = one if facing == 1 else two
            if indexes[1][0] != len(loopMap) - 1 and loopMap[indexes[1][0] + 1][indexes[1][1]] == unchecked:
                loopMap[indexes[1][0] + 1][indexes[1][1]] = one if facing == 3 else two
        elif currentSymbol == 'L':
            if indexes[1][1] != 0 and loopMap[indexes[1][0]][indexes[1][1] - 1] == unchecked:
                loopMap[indexes[1][0]][indexes[1][1] - 1] = one if facing == 3 else two
            if indexes[1][0] != len(loopMap) - 1 and loopMap[indexes[1][0] + 1][indexes[1][1]] == unchecked:
                loopMap[indexes[1][0] + 1][indexes[1][1]] = one if facing == 3 else two
            if facing == 3:
                indexes.append((indexes[1][0] - 1, indexes[1][1]))
                facing = 0
            else:
                indexes.append((indexes[1][0], indexes[1][1] + 1))
                facing = 1
        elif currentSymbol == 'J':
            if indexes[1][1] != len(loopMap[0]) - 1 and loopMap[indexes[1][0]][indexes[1][1] + 1] == unchecked:
                loopMap[indexes[1][0]][indexes[1][1] + 1] = one if facing == 2 else two
            if indexes[1][0] != len(loopMap) - 1 and loopMap[indexes[1][0] + 1][indexes[1][1]] == unchecked:
                loopMap[indexes[1][0] + 1][indexes[1][1]] = one if facing == 2 else two
            if facing == 1:
                indexes.append((indexes[1][0] - 1, indexes[1][1]))
                facing = 0
            else:
                indexes.append((indexes[1][0], indexes[1][1] - 1))
                facing = 3
        elif currentSymbol == '7':
            if indexes[1][1] != len(loopMap[0]) - 1 and loopMap[indexes[1][0]][indexes[1][1] + 1] == unchecked:
                loopMap[indexes[1][0]][indexes[1][1] + 1] = one if facing == 1 else two
            if indexes[1][0] != 0 and loopMap[indexes[1][0] - 1][indexes[1][1]] == unchecked:
                loopMap[indexes[1][0] - 1][indexes[1][1]] = one if facing == 1 else two
            if facing == 1:
                indexes.append((indexes[1][0] + 1, indexes[1][1]))
                facing = 2
            else:
                indexes.append((indexes[1][0], indexes[1][1] - 1))
                facing = 3
        elif currentSymbol == 'F':
            if indexes[1][1] != 0 and loopMap[indexes[1][0]][indexes[1][1] - 1] == unchecked:
                loopMap[indexes[1][0]][indexes[1][1] - 1] = one if facing == 0 else two
            if indexes[1][0] != 0 and loopMap[indexes[1][0] - 1][indexes[1][1]] == unchecked:
                loopMap[indexes[1][0] - 1][indexes[1][1]] = one if facing == 0 else two
            if facing == 3:
                indexes.append((indexes[1][0] + 1, indexes[1][1]))
                facing = 2
            else:
                indexes.append((indexes[1][0], indexes[1][1] + 1))
                facing = 1
        else:
            print('ERROR')
        indexes.pop(0)
        currentSymbol = inputs[indexes[1][0]][indexes[1][1]]
        count += 1
    return loopMap

def removeOutsides(loopMap):
    for i in range(len(loopMap)):
        for j in range(len(loopMap[i]) - 2):
            if loopMap[i][j] != unchecked:
                break
            loopMap[i][j] = ' '
        for j in range(int(len(loopMap[i])) - 1, 1, -1):
            if loopMap[i][j] != unchecked:
                break
            loopMap[i][j] = ' '
    for j in range(len(loopMap[0])):
        for i in range(len(loopMap) - 2):
            if loopMap[i][j] != unchecked and loopMap[i][j] != ' ':
                break
            loopMap[i][j] = ' '
        for i in range(int(len(loopMap)) - 1, 1, -1):
            if loopMap[i][j] != unchecked and loopMap[i][j] != ' ':
                break
            loopMap[i][j] = ' '
    changed = True
    while changed:
        changed = False
        for i in range(len(loopMap)):
            for j in range(len(loopMap[0])):
                if loopMap[i][j] == unchecked and (i > 0 and loopMap[i-1][j] == ' ' or i < len(loopMap) - 1 and loopMap[i+1][j] == ' ' or j > 0 and loopMap[i][j-1] == ' ' or j < len(loopMap[0]) - 1 and loopMap[i][j+1] == ' '):
                    loopMap[i][j] = ' '
                    changed = True
    return loopMap

def fillInUncheckeds(loopMap):
    changed = True
    while changed:
        changed = False
        for i in range(len(loopMap)):
            for j in range(len(loopMap[0])):
                if loopMap[i][j] == unchecked:
                    if i > 0 and loopMap[i-1][j] == one or i < len(loopMap) - 1 and loopMap[i+1][j] == one or j > 0 and loopMap[i][j-1] == one or j < len(loopMap[0]) - 1 and loopMap[i][j+1] == one:
                        loopMap[i][j] = one
                        changed = True
                    if i > 0 and loopMap[i-1][j] == two or i < len(loopMap) - 1 and loopMap[i+1][j] == two or j > 0 and loopMap[i][j-1] == two or j < len(loopMap[0]) - 1 and loopMap[i][j+1] == two:
                        loopMap[i][j] = two
                        changed = True
    return loopMap

def findAnswerNumber(loopMap):
    for i in range(len(loopMap)):
        for j in range(len(loopMap[0])):
            if loopMap[i][j] != ' ':
                return one if loopMap[i][j] == two else two

def removeWrongAndSetRightToI(loopMap, answerNumber):
    for i in range(len(loopMap)):
        for j in range(len(loopMap[0])):
            if loopMap[i][j] == answerNumber:
                loopMap[i][j] = inside
            elif loopMap[i][j] == (one if answerNumber == two else two):
                loopMap[i][j] = ' '
    return loopMap

def printLoopMap(loopMap):
    for row in loopMap:
        print(''.join(row))
    print()

fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
sI, sJ = getStart(inputs)
loopMap = getLoopMap(sI, sJ, inputs)
loopMap = removeOutsides(loopMap)
loopMap = fillInUncheckeds(loopMap)
answerNumber = findAnswerNumber(loopMap)
loopMap = removeWrongAndSetRightToI(loopMap, answerNumber)
printLoopMap(loopMap)
answer = sum(x for x in [y.count(inside) for y in loopMap])
print(answer)