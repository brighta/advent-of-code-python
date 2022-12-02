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
x=0
y=0
houses = {createFormattedHouse(x, y)}
for character in file[0]:
    if character == "^":
        y += 1
    if character == ">":
        x += 1
    if character == "v":
        y -= 1
    if character == "<":
        x -= 1
    houses.add(createFormattedHouse(x, y))
print(len(houses))
