import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getStones(file):
    return list(map(int, file[0].split(' ')))

def blink(stones):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone)) % 2 == 0:
            stoneString = str(stone)
            stoneHalfLength = int(len(stoneString) / 2)
            newStones.extend([int(stoneString[:stoneHalfLength]), int(stoneString[stoneHalfLength:])])
        else:
            newStones.append(stone * 2024)
    return newStones

def blinkMultipleTimes(stones, numberTimes):
    for _ in range(numberTimes):
        stones = blink(stones)
    return stones


file = loadInput(fileName)
stones = getStones(file)
stones = blinkMultipleTimes(stones, 25)
print(len(stones))