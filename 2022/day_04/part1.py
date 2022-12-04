import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def checkForFullOverlap(firstStart, firstEnd, secondStart, secondEnd):
    if firstStart <= secondStart and firstEnd >= secondEnd or firstStart >= secondStart and firstEnd <= secondEnd:
        return True

file = loadInput(fileName)
count = 0
for row in file:
    elfParts = row.rstrip().split(",")
    if checkForFullOverlap(int(elfParts[0].split("-")[0]), int(elfParts[0].split("-")[1]), int(elfParts[1].split("-")[0]), int(elfParts[1].split("-")[1])):
        count += 1
print(count)
