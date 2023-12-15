import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    return list(fileLines[0].split(','))

def getBoxes(number):
    return [[] for _ in range(number)]

def getHashCode(currentValue, character):
    currentValue += ord(character)
    currentValue *= 17
    return currentValue % 256

def getHashCodeForString(string):
    currentValue = 0
    for character in list(string):
        currentValue = getHashCode(currentValue, character)
    return currentValue

def processInput(string, boxes):
    parts = re.split('[=-]', string)
    label = parts[0]
    boxIndex = getHashCodeForString(label)
    box = boxes[boxIndex]
    lensInBox = next((lens for lens in box if lens[0] == label), None)
    if '-' in string:
        if lensInBox is not None:
            box.pop(box.index(lensInBox))
    else:
        newLense = [label, int(parts[1])]
        if lensInBox is not None:
            box[box.index(lensInBox)] = newLense
        else:
            box.append(newLense)
    boxes[boxIndex] = box
    return boxes


fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
boxes = getBoxes(256)
for string in inputs:
    boxes = processInput(string, boxes)
answer = 0
for boxIndex in range(len(boxes)):
    box = boxes[boxIndex]
    for lensIndex in range(len(box)):
        lens = box[lensIndex]
        answer += ((boxIndex + 1) * (lensIndex + 1) * lens[1])
print(answer)
