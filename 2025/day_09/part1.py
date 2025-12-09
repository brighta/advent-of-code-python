import sys

if len(sys.argv) < 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getCoordinates(lines):
    coordinates = []
    for line in lines:
        coordinates.append(tuple(list(map(int, line.rstrip().split(",")))))
    return coordinates

def getRectanglesSizes(coordinates):
    rectangleSizes = {}
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            coordinate1 = coordinates[i]
            coordinate2 = coordinates[j]
            rectangleSizes[(coordinate1, coordinate2)] = getRectangleSizes(coordinate1, coordinate2)
    return dict(sorted(rectangleSizes.items(), key=lambda item: item[1], reverse=True))

def getRectangleSizes(coordinate1, coordinate2):
    return (abs(coordinate1[0] - coordinate2[0]) + 1) *(abs(coordinate1[1] - coordinate2[1]) + 1)

lines = loadInput(fileName)
coordinates = getCoordinates(lines)
rectangleSizes = getRectanglesSizes(coordinates)
print(rectangleSizes[next(iter(rectangleSizes))])