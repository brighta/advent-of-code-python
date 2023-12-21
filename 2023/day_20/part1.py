import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.read().splitlines()

def getPuzzleInput(fileLines):
    modules = {}
    for fileLine in fileLines:
        module = fileLine.split(' -> ')[0]
        if module == 'broadcaster':
            moduleValues = ['broadcaster', '']
        else:
            moduleValues = [module[0]]
            if moduleValues[0] == '%':
                moduleValues.append(0)
            else:
                inputs = {}
                for moduleLine in fileLines:
                    if module[1:] in moduleLine:
                        if module[1:] in moduleLine.split(' -> ')[1]:
                            inputs[moduleLine.split(' -> ')[0][1:]] = 0
                moduleValues.append(inputs)
            module = module[1:]
        moduleValues.append(list(fileLine.split(' -> ')[1].split(', ')))
        modules[module] = moduleValues
    return modules

def broadcast(modules):
    numHighPulses = 0
    numLowPulses = 1
    pulses = [('button', 'broadcaster', 0)]
    while len(pulses) != 0:
        newPulses = []
        for pulse in pulses:
            if pulse[1] in modules:
                module = modules[pulse[1]]
                nextPulse = None
                if module[0] == 'broadcaster':
                    nextPulse = pulse[2]
                elif module[0] == '%':
                    if pulse[2] == 0:
                        module[1] = (module[1] + 1) % 2
                        nextPulse = module[1]
                elif module[0] == '&':
                    module[1][pulse[0]] = pulse[2]
                    if set(module[1].values()) == {1}:
                        nextPulse = 0
                    else:
                        nextPulse = 1
                modules[pulse[1]] = module
                if nextPulse is not None:
                    for destination in module[2]:
                        newPulses.append((pulse[1], destination, nextPulse))
                        if nextPulse == 1:
                            numHighPulses += 1
                        else:
                            numLowPulses += 1
        pulses = newPulses.copy()
    return numHighPulses, numLowPulses

def getFinalValues(modules):
    numInSequence = numHighPulses = numLowPulses = 0
    sequenceFinished = False
    while numInSequence < 1000 and not sequenceFinished:
        sequenceFinished = True
        newNumHighPulses, newNumLowPulses = broadcast(modules)
        numHighPulses += newNumHighPulses
        numLowPulses += newNumLowPulses
        numInSequence += 1
        for module in modules.values():
            if module[0] == '%':
                if module[1] == 1:
                    sequenceFinished = False
    if numInSequence == 1000:
        return numInSequence, numHighPulses, numLowPulses
    else:
        return numInSequence, int(numHighPulses / numInSequence * 1000), int(numLowPulses / numInSequence * 1000)


fileLines = loadInput(fileName)
modules = getPuzzleInput(fileLines)
numInSequence, numHighPulses, numLowPulses = getFinalValues(modules)
print(numHighPulses * numLowPulses)
