import sys
from classes import Grid

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def removeCoveredValues(y, coveredValues, uncoveredValues):
    rowY = uncoveredValues[y]
    newRowY = []
    for uncoveredValue in rowY:
        if uncoveredValue[1] < coveredValues[0]:
            newRowY.append(uncoveredValue)
        if uncoveredValue[0] > coveredValues[1]:
            newRowY.append(uncoveredValue)
        elif uncoveredValue[0] < coveredValues[0]:
            if uncoveredValue[1] > coveredValues[0]:
                newRowY.append((uncoveredValue[0], coveredValues[0]-1))
                if uncoveredValue[1] > coveredValues[1]:
                    newRowY.append((coveredValues[1]+1, uncoveredValue[1]))
        else:
            if uncoveredValue[1] > coveredValues[1]:
                newRowY.append((coveredValues[1]+1, uncoveredValue[1]))
    uncoveredValues[y] = newRowY
    return uncoveredValues

def updateUncoveredValues(line, uncoveredValues, min, max):
    sensorX = int(line.split(",")[0].split("=")[1])
    sensorY = int(line.split(":")[0].split("=")[2])
    beaconX = int(line.split(",")[1].split("=")[2])
    beaconY = int(line.split("=")[4])
    distance = abs(sensorX - beaconX) + abs(sensorY - beaconY)
    for y in range(sensorY - distance, sensorY + distance + 1):
        if min <= y <= max:
            remainingDistance = distance - abs(y - sensorY)
            xMin = sensorX - remainingDistance
            if xMin < min:
                xMin = min
            xMax = sensorX + remainingDistance
            if xMax > max:
                xMax = max
            coveredValues = (xMin, xMax)
            uncoveredValues = removeCoveredValues(y, coveredValues, uncoveredValues)
    return uncoveredValues

file = loadInput(fileName)
min = 0
max = 4000000
uncoveredValues = [[(min, max)] for _ in range(max+1)]
for line in file:
    uncoveredValues = updateUncoveredValues(line.rstrip(), uncoveredValues, min, max)
for i in range(len(uncoveredValues)):
    if len(uncoveredValues[i]) != 0:
        print(uncoveredValues[i][0][0] * 4000000 + i)
