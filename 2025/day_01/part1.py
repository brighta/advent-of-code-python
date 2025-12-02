import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getRotations(file):
    rotations = []
    for line in file:
        direction = line[0]
        number = int(line[1:])
        rotations.append([direction, number])
    return rotations

def moveDial(dial, rotation):
    if rotation[0] == "L":
        dial -= rotation[1]
    else:
        dial += rotation[1]
    return dial % 100

file = loadInput(fileName)
rotations = getRotations(file)
dial = 50
password = 0
for rotation in rotations:
    dial = moveDial(dial, rotation)
    if dial == 0:
        password += 1
print(password)