import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def calculatePriorityOfBadges(firstRucksack, secondRucksack, thirdRucksack):
    for item in firstRucksack:
        if item in secondRucksack and item in thirdRucksack:
            return priorities.index(item)


file = loadInput(fileName)
prioritySum = 0
for i in range(0, len(file)-2, 3):
    prioritySum += calculatePriorityOfBadges(file[i].rstrip(), file[i+1].rstrip(), file[i+2].rstrip())
print(prioritySum)

