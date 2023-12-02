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
        line = line.replace('one',   'o1e')
        line = line.replace('two',   't2o')
        line = line.replace('three', 't3ree')
        line = line.replace('four',  'f4ur')
        line = line.replace('five',  'f5ve')
        line = line.replace('six',   's6x')
        line = line.replace('seven', 's7ven')
        line = line.replace('eight', 'e8ght')
        line = line.replace('nine',  'n9ne')
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
for lineNumbers in numbers:
    print(lineNumbers)
sum = sumNumbers(numbers)
print(sum)