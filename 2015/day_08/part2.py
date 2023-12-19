import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getAnswer(fileLines):
    codeCharacters = 0
    memoryCharacters = 0
    for line in fileLines:
        codeCharacters += len(line)
        memoryLine = line.replace('\\', '..')
        memoryLine = memoryLine.replace('"', '..')
        memoryCharacters += len(memoryLine) + 2
    return memoryCharacters - codeCharacters


fileLines = loadInput(fileName)
answer = getAnswer(fileLines)
print(answer)
