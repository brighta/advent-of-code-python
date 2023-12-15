import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    return list(fileLines[0].split(','))

def getHashCode(currentValue, character):
    currentValue += ord(character)
    currentValue *= 17
    return currentValue % 256

def getHashCodeForString(string):
    currentValue = 0
    for character in list(string):
        currentValue = getHashCode(currentValue, character)
    return currentValue


fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
answer = 0
for string in inputs:
    answer += getHashCodeForString(string)
print(answer)
