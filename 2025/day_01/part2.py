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

def moveDial(initialDial, rotation):
    if rotation[0] == "L":
        dial = initialDial - rotation[1]
    else:
        dial = initialDial + rotation[1]
    zeroCount = (1 if dial < 0 and initialDial != 0 else 0) + abs(int(dial / 100)) + (1 if dial == 0 else 0)
    return zeroCount, dial % 100

file = loadInput(fileName)
rotations = getRotations(file)
dial = 50
password = 0
for rotation in rotations:
    zeroCount, dial = moveDial(dial, rotation)
    print("{}{:2} - {}, {} zeros".format(rotation[0], rotation[1], dial, zeroCount))
    password += zeroCount
print(password)