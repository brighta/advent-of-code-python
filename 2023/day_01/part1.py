import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getNumbers(file):
    numbers = []
    for line in file:
        lineNumbers = re.findall(r'\d', line)
        numbers.append(lineNumbers)
    return numbers

def sumNumbers(numbers):
    sum = 0
    for lineNumbers in numbers:
        number = int(lineNumbers[0])*10 + int(lineNumbers[-1])
        sum += number
    return sum

file = loadInput(fileName)
numbers = getNumbers(file)
sum = sumNumbers(numbers)
print(sum)