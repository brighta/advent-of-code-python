import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def calculatePriorityOfIncorrectItemInRucksack(firstHalf, secondHalf):
    for item in firstHalf:
        if item in secondHalf:
            return priorities.index(item)


file = loadInput(fileName)
prioritySum = 0
for rucksack in file:
    rucksack = rucksack.rstrip()
    halfRucksackSize = int(len(rucksack)/2)
    prioritySum += calculatePriorityOfIncorrectItemInRucksack(rucksack[0:halfRucksackSize], rucksack[halfRucksackSize:])
print(prioritySum)

