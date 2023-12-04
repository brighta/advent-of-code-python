import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()


def validateScratchcards(fileLines):
    for line in fileLines:
        cardNumber = int(line.split('Card ')[1].split(':')[0])
        numberSets = line.split(': ')[1].split(' | ')
        winningNumbers = [x for x in numberSets[0].split(' ') if x != '']
        myNumbers = set([x for x in numberSets[1].split(' ') if x != ''])
        numberOfWinners = len(myNumbers.intersection(winningNumbers))
        if numberOfWinners != 0:
            addWinningCard(cardNumber, list(range(cardNumber + 1, cardNumber + numberOfWinners + 1)))
        else:
            addWinningCard(cardNumber, [])

def getNumberCardsWon(cardNumber):
    answer = 1
    if cardNumber in winningCards.keys():
        for winningCard in winningCards[cardNumber]:
            answer += getNumberCardsWon(winningCard)
    return answer

winningCards = {}
def addWinningCard(cardNumber, cardsWon):
    winningCards[cardNumber] = cardsWon

fileLines = loadInput(fileName)
validateScratchcards(fileLines)
answer = 0
for cardNumber in winningCards.keys():
    answer += getNumberCardsWon(cardNumber)
print(answer)
