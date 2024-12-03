import sys
import re

regexPattern = r'mul\(\d{1,3},\d{1,3}\)'

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getLine(file):
    wholeLine = ""
    for line in file:
        wholeLine += line
    return wholeLine

def getMatches(line):
    return re.findall(regexPattern, line)

def getProducts(matches):
    products = []
    for match in matches:
        match = match.lstrip("mul(").rstrip(")")
        parts = match.split(",")
        num1 = int(parts[0])
        num2 = int(parts[1])
        products.append(num1 * num2)
    return products

file = loadInput(fileName)
line = getLine(file)
matches = getMatches(line)
products = getProducts(matches)
print(sum(products))