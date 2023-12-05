import sys
from datetime import datetime

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getTransformation(seedsRanges, section):
    transformations = []
    for transformation in section.split("\n")[1:]:
        transformations.append(list(map(int, transformation.split(' '))))
    newSeedsRanges = getNewRanges(seedsRanges, transformations)
    return newSeedsRanges


def getNewRanges(seedRanges, transformations):
    newSeedsRanges = []
    for transformation in transformations:
        destStart = transformation[0]
        destEnd = transformation[0] + transformation[2] - 1
        sourceStart = transformation[1]
        sourceEnd = transformation[1] + transformation[2] - 1
        internalNewSeedRanges = []
        for seedRange in seedRanges:
            seedStart = seedRange[0]
            seedEnd = seedRange[1]
            if seedStart >= sourceStart and seedEnd <= sourceEnd:
                newSeedsRanges.append([seedStart + destStart - sourceStart, seedEnd + destEnd - sourceEnd])
            elif sourceStart <= seedStart <= sourceEnd < seedEnd:
                newSeedsRanges.append([seedStart + destStart - sourceStart, destEnd])
                internalNewSeedRanges.append([sourceEnd + 1, seedEnd])
            elif sourceStart <= seedEnd <= sourceEnd:
                newSeedsRanges.append([destStart, seedEnd + destEnd - sourceEnd])
                internalNewSeedRanges.append([seedStart, sourceStart - 1])
            elif seedStart < sourceStart and seedEnd > sourceEnd:
                newSeedsRanges.append([destStart, destEnd])
                internalNewSeedRanges.append([seedStart, sourceStart - 1])
                internalNewSeedRanges.append([sourceEnd + 1, seedEnd])
            else:
                internalNewSeedRanges.append([seedStart, seedEnd])
        seedRanges = internalNewSeedRanges
    newSeedsRanges.extend(seedRanges)
    return newSeedsRanges


fileLines = loadInput(fileName)
sections = "\n".join(fileLines).split("\n\n")
seedsRanges = []
seedsList = list(map(int, sections[0].split(": ")[1].split(" ")))
index = 0
while index < len(seedsList):
    seedsRanges.append([seedsList[index], seedsList[index] + seedsList[index + 1] - 1])
    index += 2
for section in sections[1:]:
    seedsRanges = getTransformation(seedsRanges, section)
minimum = seedsRanges[0][0]
for seedsRange in seedsRanges:
    if seedsRange[0] < minimum:
        minimum = seedsRange[0]
print(minimum)
