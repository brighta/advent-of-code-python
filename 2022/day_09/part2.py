import sys
from Classes import Coordinate

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def processAction(action, h1, h2, h3, h4, h5, h6, h7, h8, h9, t, tailPositions):
    for i in range(int(action.split(" ")[1])):
        h1.move(action.split(" ")[0])
        h2 = h2.moveTowards(h1)
        h3 = h3.moveTowards(h2)
        h4 = h4.moveTowards(h3)
        h5 = h5.moveTowards(h4)
        h6 = h6.moveTowards(h5)
        h7 = h7.moveTowards(h6)
        h8 = h8.moveTowards(h7)
        h9 = h9.moveTowards(h8)
        t = t.moveTowards(h9)
        tailPositions.add(str(t))
    return h1, h2, h3, h4, h5, h6, h7, h8, h9, t, tailPositions

file = loadInput(fileName)
h1 = Coordinate(0, 0)
h2 = Coordinate(0, 0)
h3 = Coordinate(0, 0)
h4 = Coordinate(0, 0)
h5 = Coordinate(0, 0)
h6 = Coordinate(0, 0)
h7 = Coordinate(0, 0)
h8 = Coordinate(0, 0)
h9 = Coordinate(0, 0)
t = Coordinate(0, 0)
tailPositions = {str(t)}
for line in file:
    h1, h2, h3, h4, h5, h6, h7, h8, h9, t, tailPositions = processAction(line.rstrip(), h1, h2, h3, h4, h5, h6, h7, h8, h9, t, tailPositions)
print(len(tailPositions))
