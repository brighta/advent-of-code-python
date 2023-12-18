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
        hash = fileLine.split('#')[1].split(')')[0]
        number = int(hash[0:5], 16)
        directionNumber = int(hash[5])
        direction = 'R' if directionNumber == 0 else 'D' if directionNumber == 1 else 'L' if directionNumber == 2 else 'U'
        input.append([direction, number])
    return input

def getCoordinates(input):
    currentPosition = (0, 0)
    coordinates = [currentPosition]
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
        currentPosition = (currentPosition[0] + move[0] * dig[1], currentPosition[1] + move[1] * dig[1])
        coordinates.append(currentPosition)
    coordinates.pop(-1)
    return coordinates



def getShoelace(coordinates):
    sum1 = 0
    sum2 = 0
    for i in range(len(coordinates) - 1):
        currentCoordinate = coordinates[i]
        nextCoordinate = coordinates[i+1]
        sum1 += currentCoordinate[0] * nextCoordinate[1]
        sum2 += currentCoordinate[1] * nextCoordinate[0]
    return int(abs(sum1 - sum2) / 2)

def getCount(input):
    return sum([row[1] for row in input])


fileLines = loadInput(fileName)
input = getPuzzleInput(fileLines)
coordinates = getCoordinates(input)
shoelace = getShoelace(coordinates)
count = getCount(input)
answer = int(shoelace - count / 2 + 1) + count
print(answer)
