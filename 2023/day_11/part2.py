import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

ageOfGalaxy = 1000000

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    inputs = []
    for fileLine in fileLines:
        inputs.append([*fileLine])
    return inputs

def getGalaxyCoordinates(inputs):
    galaxies = []
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            if inputs[i][j] == '#':
                galaxies.append((j, i))
    return galaxies

def expandRows(inputs, galaxies):
    xIndexes = []
    for x in range(len(inputs[0])):
        distinctValues = list(set([row[x] for row in inputs]))
        xIndexes.append((0 if len(xIndexes) == 0 else xIndexes[-1]) + (ageOfGalaxy if len(distinctValues) == 1 and distinctValues[0] == '.' else 1))
    yIndexes = []
    for y in range(len(inputs[0])):
        distinctValues = list(set(inputs[y]))
        yIndexes.append((0 if len(yIndexes) == 0 else yIndexes[-1]) + (ageOfGalaxy if len(distinctValues) == 1 and distinctValues[0] == '.' else 1))
    newGalaxies = []
    for galaxy in galaxies:
        newGalaxies.append((xIndexes[galaxy[0]], yIndexes[galaxy[1]]))
    return newGalaxies

def getGalaxyDistancesCount(galaxies):
    count = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies[galaxies.index(galaxy1) + 1:]:
            if galaxy1 != galaxy2:
                count += abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])
    return count

fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
galaxies = getGalaxyCoordinates(inputs)
galaxies = expandRows(inputs, galaxies)
distancesCount = getGalaxyDistancesCount(galaxies)
print(distancesCount)
