import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getBanks(file):
    banks = []
    for line in file:
        banks.append(list(map(int, list(line.replace('\n', '')))))
    return banks

largestJoltage = 0

def getLargestJoltages(banks):
    largestJoltages = []
    count = 0
    for bank in banks:
        global largestJoltage
        largestJoltage = 0
        findLargestJoltage(0, bank)
        count += 1
        print("{:3} - {}".format(count, largestJoltage))
        largestJoltages.append(largestJoltage)
    return largestJoltages

def findLargestJoltage(number, bank):
    global largestJoltage
    if largestJoltage if len(str(largestJoltage)) < len(str(number)) else int(str(largestJoltage)[:len(str(number))]) > number:
        return
    if len(str(number)) == 12:
        if number > largestJoltage:
            largestJoltage = number
        return
    for i in range(len(bank)):
        newNumber = number * 10 + bank[i]
        newBank = bank[i+1:]
        findLargestJoltage(newNumber, newBank)

file = loadInput(fileName)
banks = getBanks(file)
largestJoltages = getLargestJoltages(banks)
print(largestJoltages)
print(sum(largestJoltages))

# ijklmnopqrst