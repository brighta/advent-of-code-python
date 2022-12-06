import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getMarkerIndex(string):
    for i in range(3, len(string)):
        if len({string[i], string[i-1], string[i-2], string[i-3]}) == 4:
            return i

file = loadInput(fileName)
print(getMarkerIndex(file[0].rstrip())+1)
