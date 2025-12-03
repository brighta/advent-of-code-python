import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getRanges(file):
    ranges = []
    for line in file:
        for part in line.split(","):
            ranges.append(list(map(int, part.split("-"))))
    return ranges

def getInvalidIds(rangeValues):
    invalidIds = []
    for i in range(rangeValues[0], rangeValues[1] + 1):
        if isIdInvalid(i):
            invalidIds.append(i)
    return invalidIds

def isIdInvalid(id):
    stringI = str(id)
    if len(stringI) % 2 != 0:
        return False
    halfLength = int(len(stringI) / 2)
    return stringI[:halfLength] == stringI[halfLength:]

file = loadInput(fileName)
ranges = getRanges(file)
invalidIds = []
for rangeValues in ranges:
    invalidIds.extend(getInvalidIds(rangeValues))
print(sum(invalidIds))