import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getRanges(lines):
    ranges = []
    for i in range(len(lines)):
        line = lines[i].replace("\n", "")
        if line == "":
            break
        ranges.append(list(map(int, line.split("-"))))
    return ranges

def combineRanges(ranges):
    i = 0
    while i < len(ranges) - 1:
        first = ranges[i]
        second = ranges[i+1]
        if first[1] >= second[0] - 1:
            if first[1] <= second[1]:
                ranges[i] = [first[0], second[1]]
            ranges.remove(second)
        else:
            i += 1
    return ranges

def calculateNumberOfFreshInRange(ranges):
    count = 0
    for rangeItem in ranges:
        count += rangeItem[1] - rangeItem[0] + 1
    return count

lines = loadInput(fileName)
ranges = getRanges(lines)
ranges.sort()
newRanges = combineRanges(ranges)
count = calculateNumberOfFreshInRange(newRanges)
print(count)