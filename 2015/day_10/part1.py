import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def lookAndSay(input):
    newInput = ''
    number = input[0]
    count = 1
    for nextNumber in list(input)[1:]:
        if nextNumber == number:
            count += 1
        else:
            newInput += str(count) + str(number)
            number = nextNumber
            count = 1
    newInput += str(count) + str(number)
    return newInput

def playGame(input, numTimes):
    for _ in range(numTimes):
        input = lookAndSay(input)
    return len(input)


input = loadInput(fileName)[0]
answer = playGame(input, 40)
print(answer)
