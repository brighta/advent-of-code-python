import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

results = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
}
toolWorth = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def calculateScore(opponent, you):
    return results[opponent+you] + toolWorth[you]

file = loadInput(fileName)
score = 0
for game in file:
    gameParts = game.rstrip().split(" ")
    score += calculateScore(gameParts[0], gameParts[1])
print(score)

