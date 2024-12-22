import sys
from math import floor

from classes import Machine
from classes import Values

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getMachines(file):
    machines = []
    for i in range(0, len(file), 4):
        buttonAString = file[i].strip()
        buttonAx = int(buttonAString.split('X+')[1].split(',')[0])
        buttonAy = int(buttonAString.split('Y+')[1])
        buttonA = Values(buttonAx, buttonAy)
        buttonBString = file[i+1].strip()
        buttonBx = int(buttonBString.split('X+')[1].split(',')[0])
        buttonBy = int(buttonBString.split('Y+')[1])
        buttonB = Values(buttonBx, buttonBy)
        prizeString = file[i+2].strip()
        prizeX = int(prizeString.split('X=')[1].split(',')[0])
        prizeY = int(prizeString.split('Y=')[1])
        prize = Values(prizeX, prizeY)
        machines.append(Machine(buttonA, buttonB, prize))
    return machines

def getTokensToWin(machine):
    winningCosts = []
    maxA = min(floor(machine.prize.x / machine.a.x), floor(machine.prize.y / machine.a.y), 100)
    for a in range(maxA, 0, -1):
        x = machine.a.x * a
        y = machine.a.y * a
        b = (machine.prize.x - x) / machine.b.x
        if b % 1 == 0 and machine.b.y * b + y == machine.prize.y:
            winningCosts.append(int(a * 3 + b))
    if len(winningCosts) != 0:
        return min(winningCosts)
    return 0

def getTokensToWinForAllMachines(machines):
    winningCosts = []
    for machine in machines:
        winningCosts.append(getTokensToWin(machine))
    return winningCosts

file = loadInput(fileName)
machines = getMachines(file)
winningCosts = getTokensToWinForAllMachines(machines)
print(sum(winningCosts))