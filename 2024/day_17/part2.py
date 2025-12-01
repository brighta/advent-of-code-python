import sys

from classes import Computer

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getComputer(file):
    a = int(file[0].split(': ')[1])
    b = int(file[1].split(': ')[1])
    c = int(file[2].split(': ')[1])
    program = list(map(int, file[4].split(': ')[1].split(',')))
    return Computer(a, b, c, program)

def getValidAValues(validAValues):
    if len(validAValues) == 0:
        return []
    validValues = []
    nextValidValues = getValidAValues(validAValues[1:])
    if len(nextValidValues) == 0:
        return validAValues[0]
    for nextValue in nextValidValues:
        if type(nextValue) != type([]):
            nextValue = [nextValue]
        for value in validAValues[0]:
            validValues.append([value] + nextValue)
    return validValues

file = loadInput(fileName)
computer = getComputer(file)
validAValues = [[0], [1], [2], [3], [4], [5], [6], [7]]
for i in range(1, len(computer.program)):
    print(i)
    newValidAValues = []
    for j in range(8):
        for validA in validAValues:
            newA = validA + [j]
            a = int(''.join(list(map(str, newA + ['1' for _ in range(len(computer.program) - len(validA) - 1)]))))
            computer.a = a
            output = list(map(int, computer.run()))
            computer.reset()
            index = i * -1
            if len(output) == len(computer.program):
                print('i: {}, j: {}, a: {}, output: {}, program: {}'.format(i, j, str(a), output, computer.program))
                if output == computer.program:
                    print(a)
                    exit(0)
                elif output[index:] == computer.program[index:]:
                    print('i: {}, j: {}, a: {}, output: {}, program: {}'.format(i, j, str(a), output, computer.program))
                    newValidAValues.append(newA)
    validAValues = newValidAValues

# validAValues = [[1, 2]]
# for i in range(1, len(computer.program)):
#     print(i)
#     validValues = getValidAValues(validAValues)
#     # print(validValues)
#     validAValuesForIndex = []
#     for j in range(8):
#         aOptions = []
#         if len(validValues) == 0:
#             aOptions.append([j])
#         else:
#             for validValue in validValues:
#                 if type(validValue) != type([]):
#                     validValue = [validValue]
#                 aOptions.append(validValue + [j])
#         for aOption in aOptions:
#             aOption = aOption + [0 for _ in range(len(computer.program) - len(aOption) - 1)]
#             a = int(''.join(list(map(str, aOption))))
#             computer.a = a
#             output = list(map(int, computer.run()))
#             computer.reset()
#             index = i * -1
#             if len(output) == len(computer.program):
#                 if output == computer.program:
#                     print(a)
#                     exit(0)
#                 elif output[index:] == computer.program[index:]:
#                     print('i: {}, j: {}, a: {}, output: {}, program: {}'.format(i, j, str(a), output, computer.program))
#                     validAValuesForIndex.append(j)
#     if i == 0 and len(validAValuesForIndex) == 0:
#         validAValues.append([1, 2])
#     else:
#         validAValues.append(list(set(validAValuesForIndex)))
#
#
# for value in getValidAValues(validAValues):
#     print(value)
