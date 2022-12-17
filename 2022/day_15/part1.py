import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getSensorCoverage(line, row):
    sensorX = int(line.split(",")[0].split("=")[1])
    sensorY = int(line.split(":")[0].split("=")[2])
    beaconX = int(line.split(",")[1].split("=")[2])
    beaconY = int(line.split("=")[4])
    coveredValues = set()
    distanceRemaining = abs(sensorX - beaconX) + abs(sensorY - beaconY) - abs(sensorY - row)
    coveredValues.update(range(sensorX - distanceRemaining, sensorX + distanceRemaining))
    return coveredValues

file = loadInput(fileName)
row = 2000000
coveredValues = set()
for line in file:
    coveredValues.update(getSensorCoverage(line.rstrip(), row))
print(len(coveredValues))
