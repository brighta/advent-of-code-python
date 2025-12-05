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
    newRanges = ranges.copy()
    for rangeItem in ranges:
        newRanges.remove(rangeItem)
        # print("{} -> {}".format(rangeItem, newRanges))
        rangeIncorporated = False
        rangeIncluded = False
        for i in range(len(newRanges)):
            newRange = newRanges[i]
            if rangeItem[0] < newRange[0] < rangeItem[1]:
                rangeIncorporated = True
                newRange[0] = rangeItem[0]
            if rangeItem[0] < newRange[1] < rangeItem[1]:
                rangeIncorporated = True
                newRange[1] = rangeItem[1]
            if rangeIncorporated:
                # print("    Adding range: {}".format(newRange))
                newRanges[i] = newRange
            if newRange[0] <= rangeItem[0] and newRange[1] >= rangeItem[1]:
                # print("    Range Included - {} <= {} and {} >= {}".format(newRange[0], rangeItem[0], newRange[1], rangeItem[1]))
                rangeIncluded = True
        if not rangeIncluded:
            # print("    Adding range: {}".format(rangeItem))
            newRanges = [rangeItem] + newRanges
        # print("        {}".format(newRanges))
    return newRanges

def calculateNumberOfFreshInRange(ranges):
    count = 0
    for rangeItem in ranges:
        count += rangeItem[1] - rangeItem[0] + 1
    return count

lines = loadInput(fileName)
ranges = getRanges(lines)
ranges.sort()
newRanges = combineRanges(ranges)
newRanges.sort()
while newRanges != ranges:
    ranges = newRanges
    newRanges = combineRanges(ranges)
    newRanges.sort()
# print(newRanges)
count = calculateNumberOfFreshInRange(newRanges)
print(count)