import sys
from math import floor

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def drawPixel(x, cycle, crt):
    if x-1 <= (cycle-1)%40 <= x+1:
        crt[floor(cycle/40)][(cycle-1)%40] = "#"
    return crt

def processAction(action, x, cycle, crt):
    actionParts = action.split(" ")
    if actionParts[0] == "noop":
        cycle += 1
        crt = drawPixel(x, cycle, crt)
    elif actionParts[0] == "addx":
        crt = drawPixel(x, cycle+1, crt)
        cycle += 2
        crt = drawPixel(x, cycle, crt)
        x += int(actionParts[1])
    return x, cycle, crt

def printCrt(crt):
    for y in range(len(crt)):
        print("".join(crt[y]))

file = loadInput(fileName)
crt = [["." for x in range(40)] for y in range(6)]
x = 1
cycle = 0
for line in file:
    x, cycle, crt = processAction(line.rstrip(), x, cycle, crt)
printCrt(crt)
