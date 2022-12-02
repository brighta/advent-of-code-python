import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def isStringNice(string):
    if re.search("(ab|cd|pq|xy)", string) is not None:
        return False
    if len(re.findall("[aeiou]", string)) < 3:
        return False
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False


file = loadInput(fileName)
numberNice = 0
for string in file:
    if isStringNice(string.rstrip()):
        numberNice += 1
print(numberNice)
