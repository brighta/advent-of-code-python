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

file = loadInput(fileName)
computer = getComputer(file)
output = computer.run()
print(",".join(output))