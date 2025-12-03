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
    halfLength = int(len(stringI) / 2)
    for i in range(1, halfLength + 1):
        if len(stringI) % i != 0:
            continue
        isInvalid = True
        for j in range(i, len(stringI) - i + 1, i):
            if stringI[:i] != stringI[j:j+i]:
                isInvalid = False
                break
        if isInvalid:
            return True
    return False

file = loadInput(fileName)
ranges = getRanges(file)
invalidIds = []
for rangeValues in ranges:
    invalidIds.extend(getInvalidIds(rangeValues))
print(sum(invalidIds))