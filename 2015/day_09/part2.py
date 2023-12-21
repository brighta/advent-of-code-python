import sys
import itertools

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    locationNames = set()
    routes = {}
    for line in fileLines:
        locations = list(line.split(' = ')[0].split(' to '))
        distance = int(line.split(' = ')[1])
        locationNames.update({locations[0], locations[1]})
        for locationPair in [locations, list(reversed(locations))]:
            if locationPair[0] in routes:
                routes[locationPair[0]][locationPair[1]] = distance
            else:
                routes[locationPair[0]] = {locationPair[1]: distance}
    return list(locationNames), routes

def getAnswer(locationNames, routes):
    maxAnswer = 0
    for path in list(itertools.permutations(locationNames)):
        answer = 0
        current = path[0]
        for next in path[1:]:
            answer += routes[current][next]
            current = next
        maxAnswer = max(maxAnswer, answer)
    return maxAnswer

fileLines = loadInput(fileName)
locationNames, routes = getPuzzleInput(fileLines)
answer = getAnswer(locationNames, routes)
print(answer)
