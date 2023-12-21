import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def lookAndSay(input):
    matches = re.findall(r'((.)\2{0,})', input)
    newInput = ''.join([str(len(match[0])) + match[1] for match in matches])
    return newInput

def playGame(input, numTimes):
    for i in range(numTimes):
        input = lookAndSay(input)
    return len(input)


input = loadInput(fileName)[0]
answer = playGame(input, 50)
print(answer)
