import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

rules = {'red': 12, 'green': 13, 'blue': 14}

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()


def getMyWinningNumbers(fileLines):
    myWinningNumbers = []
    for line in fileLines:
        numberSets = line.split(': ')[1].split(' | ')
        winningNumbers = [x for x in numberSets[0].split(' ') if x != '']
        myNumbers = set([x for x in numberSets[1].split(' ') if x != ''])
        myWinningNumbers.append(myNumbers.intersection(winningNumbers))
    return myWinningNumbers


fileLines = loadInput(fileName)
myWinningNumbers = getMyWinningNumbers(fileLines)
answer = 0
for myWinningNumber in myWinningNumbers:
    if not len(myWinningNumber) == 0:
        answer += pow(2, len(myWinningNumber) - 1)
print(answer)
