import sys
import re

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    inputs = []
    for fileLine in fileLines:
        conditions = re.findall('[#?]+', fileLine)
        groups = list(map(int, re.findall('[0-9]+', fileLine)))
        inputs.append([conditions, groups])
    return inputs

def checkIfSolutionsMatch(solution, test):
    for i in range(len(test)):
        if test[i] != solution[i] and solution[i] != '?':
            return False
    return True

def checkCombinations(solution, test, difference, groups):
    answer = 0
    for i in range(difference + 1):
        newTest = test + '.' * i + '#' * groups[0]
        if checkIfSolutionsMatch(solution, newTest):
            differenceRemaining = difference - i
            if len(groups) == 1:
                newTest += '.' * differenceRemaining
                answer += 1 if checkIfSolutionsMatch(solution, newTest) else 0
            else:
                newTest += '.'
                answer += checkCombinations(solution, newTest, differenceRemaining, groups[1:])
    return answer

def getNumberCombinations(input):
    if len(input[0]) == 0 or len(input[1]) == 0:
        return 1
    if len('.'.join(input[0])) == sum(input[1]) + len(input[1]) - 1:
        return 1
    if len(input[0]) == 1 and len(list(set(input[0][0]))) == 1 and input[0][0][0] == '?' and len(input[1]) == 1:
        return len(input[0][0]) - input[1][0] + 1
    solution = '.'.join(input[0])
    difference = len(solution) - sum(input[1]) - len(input[1]) + 1
    answer = checkCombinations(solution, '', difference, input[1])
    return answer

count = 0
def printInputAnswer(input, answer):
    global count
    count += 1
    print(str(count).rjust(4, ' ') + ' ' + '.'.join(input[0]).ljust(20, ' ') + ' - ' + ','.join(list(map(str, input[1]))).ljust(15, ' ') + ' - ' + str(answer))
    return answer


fileLines = loadInput(fileName)
inputs = getPuzzleInput(fileLines)
answer = 0
for input in inputs:
    number = getNumberCombinations(input)
    answer += number
    printInputAnswer(input, number)
print(answer)
