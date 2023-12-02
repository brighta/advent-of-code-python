import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getGameDetails(file):
    games = {}
    for line in file:
        line = line.rstrip('\n')
        gameNumber = line.split(": ")[0].split(" ")[1]
        rounds = line.split(": ")[1].split("; ")
        selections = []
        for round in rounds:
            hand = {}
            for dice in round.split(", "):
                parts = dice.split(" ")
                if parts[1] in hand.keys():
                    print("contains " + parts[1])
                    hand[parts[1]] += int(parts[0])
                else:
                    hand[parts[1]] = int(parts[0])
            selections.append(hand)
        games[gameNumber] = selections
    return games

def validateGame(selections):
    for selection in selections:
        for rule in rules.keys():
            if rule in selection.keys():
                if selection[rule] > rules[rule]:
                    return False
    return True

file = loadInput(fileName)
games = getGameDetails(file)
sum = 0
for game in games.keys():
    if validateGame(games[game]):
        sum += int(game)
print(sum)