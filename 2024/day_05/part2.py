import sys
from math import floor
import collections

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getData(file):
    orderingRules = []
    updates = []
    ordering = True
    for line in file:
        if line == "\n":
            ordering = False
        else:
            if ordering:
                orderingRules.append(list(map(int, line.split('|'))))
            else:
                updates.append(list(map(int, line.split(','))))
    return orderingRules, updates

def getRuleNumbers(number, orderingRules, after=True):
    return [rule[1 if after else 0] for rule in (list(filter(lambda x : x[0] == number, orderingRules)) if after else list(filter(lambda x : x[1] == number, orderingRules)))]

def getInvalidUpdates(orderingRules, updates):
    validUpdates = []
    for update in updates:
        if not isUpdateValid(orderingRules, update):
            validUpdates.append(update)
    return validUpdates

def isUpdateValid(orderingRules, update):
    for i in range(len(update)):
        number = update[i]
        befores = update[:i]
        expectedAfters = getRuleNumbers(number, orderingRules)
        if len(list(set(befores) & set(expectedAfters))) != 0:
            return False
        afters = update[i + 1:]
        expectedBefores = getRuleNumbers(number, orderingRules, False)
        if len(list(set(afters) & set(expectedBefores))) != 0:
            return False
    return True

def getFullOrder(orderingRules):
    beforePages = [orderingRule[0] for orderingRule in orderingRules]
    fullOrder = [x[0] for x in collections.Counter(beforePages).most_common()]
    afterPages = set([orderingRule[1] for orderingRule in orderingRules])
    missingAfterPages = afterPages.difference(set(fullOrder))
    fullOrder.extend(missingAfterPages)
    return fullOrder

def filterRules(invalidUpdate, orderingRules):
    filteredRules = []
    for orderingRule in orderingRules:
        if len(set(orderingRule).intersection(set(invalidUpdate))) == 2:
            filteredRules.append(orderingRule)
    return filteredRules

def getCorrectedValues(invalidUpdates, orderingRules):
    correctedValues = []
    for invalidUpdate in invalidUpdates:
        filteredRules = filterRules(invalidUpdate, orderingRules)
        correctedValues.append(getFullOrder(filteredRules))
    return correctedValues

def getMiddles(validUpdates):
    middles = []
    for validUpdate in validUpdates:
        middles.append(validUpdate[floor(len(validUpdate) / 2)])
    return middles

file = loadInput(fileName)
orderingRules, updates = getData(file)
invalidUpdates = getInvalidUpdates(orderingRules, updates)
correctedValues = getCorrectedValues(invalidUpdates, orderingRules)
middles = getMiddles(correctedValues)
print(sum(middles))