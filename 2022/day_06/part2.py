import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getMarkerIndex(string, length):
    for i in range(length-1, len(string)):
        if len(set(list(string[i-(length-1):i+1]))) == length:
            return i

file = loadInput(fileName)
print(getMarkerIndex(file[0].rstrip(), 14)+1)
