import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def createFormattedHouse(x, y):
    return "{},{}".format(x, y)

file = loadInput(fileName)
santaX=0
santaY=0
roboX=0
roboY=0
houses = {createFormattedHouse(santaX, santaY)}
for i in range(len(file[0].rstrip())):
    x = 0
    y = 0
    character = file[0][i]
    if character == "^":
        y += 1
    if character == ">":
        x += 1
    if character == "v":
        y -= 1
    if character == "<":
        x -= 1
    if i % 2 == 0:
        santaX += x
        santaY += y
        houses.add(createFormattedHouse(santaX, santaY))
    else:
        roboX += x
        roboY += y
        houses.add(createFormattedHouse(roboX, roboY))
print(len(houses))
