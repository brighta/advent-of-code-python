import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def processAction(action, x, cycle, signalStrength):
    actionParts = action.split(" ")
    xAdd = 0
    if actionParts[0] == "noop":
        cycle += 1
    elif actionParts[0] == "addx":
        cycle += 2
        xAdd = int(actionParts[1])
    if (cycle - 20) % 40 == 0:
        signalStrength += cycle * x
    elif actionParts[0] == "addx" and (cycle - 21) % 40 == 0:
        signalStrength += (cycle-1) * x
    x += xAdd
    return x, cycle, signalStrength

file = loadInput(fileName)
x = 1
cycle = 0
signalStrength = 0
for line in file:
    x, cycle, signalStrength = processAction(line.rstrip(), x, cycle, signalStrength)
print(signalStrength)
