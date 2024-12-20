import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

cache = {}

def addToCache(remainingBlinks, number, answer):
    cache[remainingBlinks, number] = answer
    return answer

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getStones(file):
    return list(map(int, file[0].split(' ')))

def getFinalNumberOfStones(remainingBlinks, number):
    if (remainingBlinks, number) in cache:
        return cache[remainingBlinks, number]
    if remainingBlinks == 0:
        return 1
    newRemainingBlinks = remainingBlinks - 1
    if number == 0:
        return addToCache(remainingBlinks, number, getFinalNumberOfStones(newRemainingBlinks, 1))
    numberString = str(number)
    if len(numberString) % 2 == 0:
        numberHalfLength = int(len(numberString) / 2)
        return addToCache(remainingBlinks, number, getFinalNumberOfStones(newRemainingBlinks, int(numberString[:numberHalfLength])) + getFinalNumberOfStones(newRemainingBlinks, int(numberString[numberHalfLength:])))
    return addToCache(remainingBlinks, number, getFinalNumberOfStones(newRemainingBlinks, number * 2024))

def blinkMultipleTimes(stones, numberTimes):
    count = 0
    for stone in stones:
        count += getFinalNumberOfStones(numberTimes, stone)
    return count


file = loadInput(fileName)
stones = getStones(file)
count = blinkMultipleTimes(stones, 75)
print(count)