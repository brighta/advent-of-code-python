import sys
from math import sqrt, prod

if len(sys.argv) < 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

if len(sys.argv) != 3:
    sys.exit("Please enter the number of connections")

numConnections = int(sys.argv[2])

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getCoordinates(lines):
    coordinates = []
    for line in lines:
        coordinates.append(tuple(list(map(int, line.rstrip().split(",")))))
    return coordinates

def getDistancesBetweenCoordinates(coordinates):
    distances = {}
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            coordinate1 = coordinates[i]
            coordinate2 = coordinates[j]
            distances[(coordinate1, coordinate2)] = getDistanceBetweenCoordinates(coordinate1, coordinate2)
    return dict(sorted(distances.items(), key=lambda item: item[1]))

def getDistanceBetweenCoordinates(coordinate1, coordinate2):
    return sqrt(abs(coordinate1[0] - coordinate2[0]) ** 2 + abs(coordinate1[1] - coordinate2[1]) ** 2 + abs(coordinate1[2] - coordinate2[2]) ** 2)

def generateCircuits(distances, numConnections):
    circuits = []
    for i in range(numConnections):
        distance = next(iter(distances))
        del distances[distance]
        coordinate1 = distance[0]
        coordinate2 = distance[1]
        coordinatesFound = False
        for j in range(len(circuits)):
            circuit = circuits[j]
            if coordinate1 in circuit:
                circuit.add(coordinate2)
                coordinatesFound = True
            if coordinate2 in circuit:
                circuit.add(coordinate1)
                coordinatesFound = True
        if not coordinatesFound:
            circuits.append({coordinate1, coordinate2})
        circuits = consolidateCircuits(circuits)
    return circuits

def consolidateCircuits(circuits):
    circuitsChanged = True
    while circuitsChanged:
        circuitsChanged = False
        for k in range(len(circuits) - 1):
            circuit1 = circuits[k]
            for l in range(k + 1, len(circuits)):
                circuit2 = circuits[l]
                union = circuit1.union(circuit2)
                if len(circuit1) + len(circuit2) > len(union):
                    circuits[k] = union
                    circuits.pop(l)
                    circuitsChanged = True
                    break
    return circuits


lines = loadInput(fileName)
coordinates = getCoordinates(lines)
distances = getDistancesBetweenCoordinates(coordinates)
circuits = generateCircuits(distances, numConnections)
circuitLengths = sorted(list(map(len, circuits)), reverse=True)
print(prod(circuitLengths[0:3]))