import sys
from Classes import Coordinate

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def processAction(action, h, t, tailPositions):
    for i in range(int(action.split(" ")[1])):
        h.move(action.split(" ")[0])
        t = t.moveTowards(h)
        tailPositions.add(str(t))
    return h, t, tailPositions

file = loadInput(fileName)
h = Coordinate(0, 0)
t = Coordinate(0, 0)
tailPositions = {str(t)}
for line in file:
    h, t, tailPositions = processAction(line.rstrip(), h, t, tailPositions)
print(len(tailPositions))
