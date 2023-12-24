import sys
import math

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    hails = []
    for fileLine in fileLines:
        hailParts = fileLine.split(' @ ')
        hails.append([list(map(int, hailParts[0].split(', '))), list(map(int, hailParts[1].split(', ')))])
    return hails

def getEdges(hails, minimum, maximum):
    for hail in hails:
        if hail[1][0] > 0:
            numTimes = math.floor((maximum - hail[0][0]) / hail[1][0])
        else:
            numTimes = math.floor((hail[0][0] - minimum) / hail[1][0] * -1)
        xCoords = [hail[0][0] + hail[1][0] * numTimes, hail[0][1] + hail[1][1] * numTimes, hail[0][2] + hail[1][2] * numTimes]
        if minimum <= xCoords[1] <= maximum and minimum <= xCoords[2] <= maximum:
            hail.append(xCoords)
        else:
            if hail[1][1] > 0:
                numTimes = math.floor((maximum - hail[0][1]) / hail[1][1])
            else:
                numTimes = math.floor((hail[0][1] - minimum) / hail[1][1] * -1)
            yCoords = [hail[0][0] + hail[1][0] * numTimes, hail[0][1] + hail[1][1] * numTimes, hail[0][2] + hail[1][2] * numTimes]
            if minimum <= xCoords[0] <= maximum and minimum <= xCoords[2] <= maximum:
                hail.append(yCoords)
            else:
                if hail[1][2] > 0:
                    numTimes = math.floor((maximum - hail[0][2]) / hail[1][2])
                else:
                    numTimes = math.floor((hail[0][2] - minimum) / hail[1][2] * -1)
                yCoords = [hail[0][0] + hail[1][0] * numTimes, hail[0][1] + hail[1][1] * numTimes, hail[0][2] + hail[1][2] * numTimes]
                hail.append(yCoords)
    return hails


fileLines = loadInput(fileName)
hails = getPuzzleInput(fileLines)
minimum = 7 if 'sample' in fileName else 200000000000000
maximum = 27 if 'sample' in fileName else 400000000000000
hails = getEdges(hails, minimum, maximum)
for hail in hails:
    print(hail)
# INCOMPLETE
