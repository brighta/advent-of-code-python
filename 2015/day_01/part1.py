import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

file = loadInput(fileName)
floor = 0
for character in file[0].rstrip():
    if character == "(":
        floor += 1
    else:
        floor -= 1
print(floor)
