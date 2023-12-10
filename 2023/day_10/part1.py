import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

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

def getNumberInLoop(i, j, inputs):
    count = 1
    indexes = [(i, j)]
    if j > 0 and (inputs[i][j-1] == 'L' or  inputs[i][j-1] == 'F' or inputs[i][j-1] == '-'):
        indexes.append((i, j-1))
    elif j < len(inputs[0]) - 1 and (inputs[i][j+1] == 'J' or  inputs[i][j+1] == '7' or inputs[i][j-1] == '-'):
        indexes.append((i, j+1))
    elif i > 0 and (inputs[i-1][j] == '7' or  inputs[i-1][j] == 'F' or inputs[i-1][j] == '|'):
        indexes.append((i-1, j))
    elif i < len(inputs) - 1 and (inputs[i+1][j] == 'L' or  inputs[i+1][j] == 'J' or inputs[i+1][j] == '|'):
        indexes.append((i+1, j))
    currentSymbol = inputs[indexes[1][0]][indexes[1][1]]
    while currentSymbol != 'S':
        if currentSymbol == '|':
            indexes.append((indexes[1][0] + indexes[1][0] - indexes[0][0], indexes[0][1]))
        elif currentSymbol == '-':
            indexes.append((indexes[1][0], indexes[1][1] + indexes[1][1] - indexes[0][1]))
        elif currentSymbol == 'L':
            if indexes[1][0] == indexes[0][0]:
                indexes.append((indexes[1][0] - 1, indexes[1][1]))
            else:
                indexes.append((indexes[1][0], indexes[1][1] + 1))
        elif currentSymbol == 'J':
            if indexes[1][0] == indexes[0][0]:
                indexes.append((indexes[1][0] - 1, indexes[1][1]))
            else:
                indexes.append((indexes[1][0], indexes[1][1] - 1))
        elif currentSymbol == '7':
            if indexes[1][0] == indexes[0][0]:
                indexes.append((indexes[1][0] + 1, indexes[1][1]))
            else:
                indexes.append((indexes[1][0], indexes[1][1] - 1))
        elif currentSymbol == 'F':
            if indexes[1][0] == indexes[0][0]:
                indexes.append((indexes[1][0] + 1, indexes[1][1]))
            else:
                indexes.append((indexes[1][0], indexes[1][1] + 1))
        else:
            print('ERROR')
        indexes.pop(0)
        currentSymbol = inputs[indexes[1][0]][indexes[1][1]]
        count += 1
    return count

fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
i, j = getStart(inputs)
numberInLoop = getNumberInLoop(i, j, inputs)
print(int(numberInLoop / 2))