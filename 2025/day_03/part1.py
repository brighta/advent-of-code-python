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

def getLargestJoltages(banks):
    largestJoltages = []
    for bank in banks:
        largestJoltages.append(getLargestJoltage(bank))
    return largestJoltages

def getLargestJoltage(bank):
    largestJoltage = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            number = bank[i] * 10 + bank[j]
            if largestJoltage < number:
                largestJoltage = number
    return largestJoltage

file = loadInput(fileName)
banks = getBanks(file)
largestJoltages = getLargestJoltages(banks)
print(sum(largestJoltages))