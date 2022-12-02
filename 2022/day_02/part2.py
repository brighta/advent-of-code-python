import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

results = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7
}

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def calculateScore(opponent, you):
    return results[opponent+you]

file = loadInput(fileName)
score = 0
for game in file:
    gameParts = game.rstrip().split(" ")
    score += calculateScore(gameParts[0], gameParts[1])
print(score)

