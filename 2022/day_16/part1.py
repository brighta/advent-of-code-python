import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def generateValve(line):
    letter = line.split(" ")[1]
    flowRate = int(line.split(";")[0].split("=")[1])
    leadsToValves = "".join(line.split(" ")[9:]).split(",")
    return [letter, [flowRate, leadsToValves]]

def generateValves(file):
    valves = {}
    for line in file:
        valve = generateValve(line.rstrip())
        valves[valve[0]] = valve[1]
    return valves

def generateFlowRates(letter, valvesOpened, valves, timeRemaining):
    print(timeRemaining)
    flowRates = []
    if timeRemaining <= 20:
        return [0]
    valve = valves[letter]
    for leadsToValve in valve[1]:
        if leadsToValve not in valvesOpened:
            flowRatesWithoutOpen = generateFlowRates(leadsToValve, valvesOpened, valves, timeRemaining-1)
            valvesOpened.append(leadsToValve)
            flowRatesWithOpen = generateFlowRates(leadsToValve, valvesOpened, valves, timeRemaining-2)
            for flowRate in [valve[0] * (timeRemaining-1), 0]:
                for flowRateWithOpen in flowRatesWithOpen:
                    flowRates.append(flowRate + flowRateWithOpen)
                for flowRateWithoutOpen in flowRatesWithoutOpen:
                    flowRates.append(flowRate + flowRateWithoutOpen)
    return flowRates

file = loadInput(fileName)
valves = generateValves(file)
valvesOpened = ["AA"]
flowRates = generateFlowRates("AA", valvesOpened, valves, 30)
print(flowRates[0])
