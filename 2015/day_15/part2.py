import sys
import math

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    ingredients = {}
    propertyNames = []
    for line in fileLines:
        name = line.split(':')[0]
        properties = line.split(': ')[1].split(', ')
        propertyValues = {}
        for property in properties:
            propertyParts = property.split(' ')
            if line == fileLines[0]:
                propertyNames.append(propertyParts[0])
            propertyValues[propertyParts[0]] = int(propertyParts[1])
        ingredients[name] = propertyValues
    return ingredients, propertyNames

def resolveIngredients(ingredients, propertyNames, currentIngredients, remainingIngredients, numRemainingIngredients):
    global maxAnswer
    if len(remainingIngredients) == 1:
        currentIngredients[remainingIngredients[0]] = numRemainingIngredients
        values = {property: 0 for property in propertyNames}
        calories = 0
        for ingredient in ingredients:
            quantity = currentIngredients[ingredient]
            for value in values:
                values[value] += quantity * ingredients[ingredient][value]
            calories += quantity * ingredients[ingredient]['calories']
        for value in values:
            if values[value] < 0:
                values[value] = 0
        answer = math.prod(list(values.values()))
        if calories == 500:
            maxAnswer = max(maxAnswer, answer)
    else:
        ingredient = remainingIngredients.pop(0)
        for i in range(1, numRemainingIngredients - len(remainingIngredients) + 1):
            currentIngredients[ingredient] = i
            resolveIngredients(ingredients, propertyNames, currentIngredients.copy(), remainingIngredients.copy(), numRemainingIngredients - i)


def getAnswer(ingredients, propertyNames, numSpoons):
    resolveIngredients(ingredients, propertyNames, {}, list(ingredients.keys()), numSpoons)



fileLines = loadInput(fileName)
ingredients, propertyNames = getPuzzleInput(fileLines)
maxAnswer = 0
getAnswer(ingredients, propertyNames[:-1], 100)
print(maxAnswer)
