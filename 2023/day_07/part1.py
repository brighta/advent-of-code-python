import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

cardOrders = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    inputsMap = {}
    for fileLine in fileLines:
        fileLineParts = fileLine.split(" ")
        inputsMap[fileLineParts[0]] = int(fileLineParts[1])
    return inputsMap

def getScoresMap(inputsMap):
    scoresMap = {}
    for i in range(len(inputsMap)):
        inputMapKey = list(inputsMap.keys())[i]
        scoresMap[getScore(inputMapKey)] = inputsMap[inputMapKey]
    return scoresMap

def getScore(hand):
    scoreParts = []
    scoreParts.append(getHandScore(hand))
    for card in hand:
        scoreParts.append(str(cardOrders.index(card)).rjust(2, '0'))
    return int(''.join(scoreParts))

def getHandScore(hand):
    cards = list(hand)
    distinctCards = list(set(cards))
    # Five of a Kind
    if len(distinctCards) == 1:
        return '7'
    # Four of a Kind
    if len(distinctCards) == 2 and (
            cards.count(distinctCards[0]) == 4 or
            cards.count(distinctCards[1]) == 4
    ):
        return '6'
    # Full House
    if len(distinctCards) == 2:
        return '5'
    # Three of a Kind
    if len(distinctCards) == 3 and (
            cards.count(distinctCards[0]) == 3 or
            cards.count(distinctCards[1]) == 3 or
            cards.count(distinctCards[2]) == 3
    ):
        return '4'
    # Two Pair
    if len(distinctCards) == 3:
        return '3'
    # One Pair
    if len(distinctCards) == 4:
        return '2'
    # High Card
    return '1'

fileLines = loadInput(fileName)
inputsMap = getPuzzleInput(fileLines)
scoresMap = getScoresMap(inputsMap)
keys = sorted(scoresMap.keys())
answer = 0
for i in range(1, len(keys) + 1):
    answer += i * scoresMap[keys[i - 1]]
print(answer)