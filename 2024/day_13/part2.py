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
        prizeX = int(prizeString.split('X=')[1].split(',')[0]) +  10000000000000
        prizeY = int(prizeString.split('Y=')[1]) + 10000000000000
        prize = Values(prizeX, prizeY)
        machines.append(Machine(buttonA, buttonB, prize))
    return machines

def getTokensToWin(machine):
    numerator = machine.prize.y * machine.b.x - machine.prize.x * machine.b.y
    denominator = machine.a.y * machine.b.x - machine.b.y * machine.a.x
    if denominator == 0:
        return 0
    a = numerator / denominator
    b = (machine.prize.x - a * machine.a.x) / machine.b.x
    if a % 1 != 0 or b % 1 != 0 or a < 0 or b < 0:
        return 0
    return int(a * 3 + b)

def getTokensToWinForAllMachines(machines):
    winningCosts = []
    for machine in machines:
        winningCosts.append(getTokensToWin(machine))
    return winningCosts

file = loadInput(fileName)
machines = getMachines(file)
winningCosts = getTokensToWinForAllMachines(machines)
print(sum(winningCosts))