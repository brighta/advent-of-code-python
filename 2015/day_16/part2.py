import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def stringToMap(string):
    string = string.replace(':', ',')
    stringParts = string.split(', ')
    return dict(zip(stringParts[::2], list(map(int, stringParts[1::2]))))

def getPuzzleInput(fileLines):
    measurements = stringToMap(fileLines[0])
    sues = []
    for fileLine in fileLines[1:]:
        valuesString = ' '.join(fileLine.split(' ')[2:])
        sues.append(stringToMap(valuesString))
    return measurements, sues

def getAnswer(measurements, sues):
    for i in range(len(sues)):
        sue = sues[i]
        correct = True
        for property in sue:
            if property in ['cats', 'trees']:
                if measurements[property] >= sue[property]:
                    correct = False
            elif property in ['pomeranians', 'goldfish']:
                if measurements[property] <= sue[property]:
                    correct = False
            elif measurements[property] != sue[property]:
                correct = False
        if correct:
            return i + 1
    return 0


fileLines = loadInput(fileName)
measurements, sues = getPuzzleInput(fileLines)
answer = getAnswer(measurements, sues)
print(answer)
