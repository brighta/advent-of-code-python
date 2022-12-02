import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def calculatePaperNeededForPresent(dimensions):
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    firstSide = length * width
    secondSide = width * height
    thirdSide = height * length
    return 2*firstSide + 2*secondSide + 2*thirdSide + min(firstSide, secondSide, thirdSide)

file = loadInput(fileName)
paperNeeded = 0
for box in file:
    paperNeeded += calculatePaperNeededForPresent(box.rstrip().split("x"))
print(paperNeeded)
