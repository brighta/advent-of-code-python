import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read()

def getAnswer(input):
    return sum(list(map(int, re.findall('-?[0-9]+', input))))


input = loadInput(fileName)
answer = getAnswer(input)
print(answer)
