import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    inputs = []
    for fileLine in fileLines:
        inputs.append(list(map(int, fileLine.split(" "))))
    return inputs

def getNextNumber(inputSequence):
    sequences = [inputSequence]
    while len(list(set(sequences[-1]))) != 1 or sequences[-1][0] != 0:
        lastSequence = sequences[-1]
        differences = []
        for i in range(1, len(lastSequence)):
            differences.append(lastSequence[i] - lastSequence[i - 1])
        sequences.append(differences)
    nextNumber = 0
    for sequence in sequences:
        nextNumber += sequence[-1]
    return nextNumber


fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
answer = 0
for input in inputs:
    nextNumber = getNextNumber(input)
    answer += nextNumber
print(answer)
