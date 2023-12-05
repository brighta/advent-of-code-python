import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getTransformation(seedsMap, section):
    transformations = []
    for transformation in section.split("\n")[1:]:
        transformations.append(list(map(int, transformation.split(' '))))
    newSeedsMap = {}
    for seed in seedsMap.keys():
        newSeedsMap[seed] = getNewNumber(seedsMap[seed], transformations)
    # print(newSeedsMap)
    return newSeedsMap

def getNewNumber(seed, transformations):
    for transformation in transformations:
        if seed in range(transformation[1], transformation[1] + transformation[2]):
            # print(str(seed) + ' - ' + str(seed + transformation[0] - transformation[1]) + ' (' +  str(transformation) + ')')
            return seed + transformation[0] - transformation[1]
    # print(str(seed) + ' - ' + str(seed))
    return seed


fileLines = loadInput(fileName)
sections = "\n".join(fileLines).split("\n\n")
seedsMap = {}
for seed in list(map(int, sections[0].split(": ")[1].split(" "))):
    seedsMap[seed] = seed
for section in sections[1:]:
    seedsMap = getTransformation(seedsMap, section)
print(min(seedsMap.values()))