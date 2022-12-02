import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def doesStringContainPairOfTwoLetters(string):
    for i in range(len(string)-1):
        if string[i:i+2] in string[i+2:]:
            return True
    return False

def doesStringContainRepeatedLetterWithLetterInbetween(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def isStringNice(string):
    return doesStringContainPairOfTwoLetters(string) and doesStringContainRepeatedLetterWithLetterInbetween(string)


file = loadInput(fileName)
numberNice = 0
for string in file:
    if isStringNice(string.rstrip()):
        numberNice += 1
print(numberNice)
