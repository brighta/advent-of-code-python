import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def calculatePaperNeededForPresent(dimensions):
    sides = [int(dimensions[0]), int(dimensions[1]), int(dimensions[2])]
    sides.sort()
    return 2*sides[0] + 2*sides[1] + sides[0]*sides[1]*sides[2]

file = loadInput(fileName)
paperNeeded = 0
for box in file:
    paperNeeded += calculatePaperNeededForPresent(box.rstrip().split("x"))
print(paperNeeded)
