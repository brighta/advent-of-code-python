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
        memoryLine = line.replace('\\\\', '.')
        memoryLine = memoryLine.replace('\\"', '.')
        memoryLine = memoryLine.replace('"', '')
        memoryLine = re.sub('\\\\x[0-9a-f][0-9a-f]', '.', memoryLine)
        memoryCharacters += len(memoryLine)
    return codeCharacters - memoryCharacters


fileLines = loadInput(fileName)
answer = getAnswer(fileLines)
print(answer)
