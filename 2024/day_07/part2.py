import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getEquations(file):
    equations = []
    for line in file:
        result = int(line.split(': ')[0])
        numbers = list(map(int, line.split(': ')[1].split(' ')))
        equations.append([result, numbers])
    return equations

def makeEquation(numbers):
    if len(numbers) == 1:
        return [numbers[0]]
    answers = []
    answers.extend(makeEquation([numbers[0] + numbers[1]] + numbers[2:]))
    answers.extend(makeEquation([numbers[0] * numbers[1]] + numbers[2:]))
    answers.extend(makeEquation([int("{}{}".format(numbers[0], numbers[1]))] + numbers[2:]))
    return answers

def isValidEquation(equation):
    answers = makeEquation(equation[1])
    return equation[0] in answers

def getValidEquations(equations):
    validEquations = []
    for equation in equations:
        if isValidEquation(equation):
            validEquations.append(equation[0])
    return validEquations

file = loadInput(fileName)
equations = getEquations(file)
validEquations = getValidEquations(equations)
print(sum(validEquations))