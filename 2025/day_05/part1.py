import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getIngredientDetails(lines):
    ranges = []
    ingredients = []
    onIngredients = False
    for i in range(len(lines)):
        line = lines[i].replace("\n", "")
        if onIngredients:
            ingredients.append(int(line))
        elif line == "":
            onIngredients = True
        else:
            ranges.append(list(map(int, line.split("-"))))
    return ranges, ingredients

def getNumberOfFreshIngredients(ranges, ingredients):
    count = 0
    for ingredient in ingredients:
        if isIngredientFresh(ranges, ingredient):
            count += 1
    return count

def isIngredientFresh(ranges, ingredient):
    for range in ranges:
        if range[0] <= ingredient <= range[1]:
            return True
    return False

lines = loadInput(fileName)
ranges, ingredients = getIngredientDetails(lines)
count = getNumberOfFreshIngredients(ranges, ingredients)
print(count)