import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def generateActionsOrder(actions, line):
    actions[line.split(" ")[-1]] = line
    return actions

def updateSignals(actions, signals, letter):
    action = actions[letter]
    actionParts = action.split(" ")
    if actionParts[1] == "->":
        if actionParts[0].isnumeric():
            signals[letter] = int(actionParts[0])
        else:
            if not signals.keys().__contains__(actionParts[0]):
                signals = updateSignals(actions, signals, actionParts[0])
            signals[letter] = signals[actionParts[0]]
    elif actionParts[1] == "AND":
        if actionParts[0] != "1" and not signals.keys().__contains__(actionParts[0]):
            signals = updateSignals(actions, signals, actionParts[0])
        if not signals.keys().__contains__(actionParts[2]):
            signals = updateSignals(actions, signals, actionParts[2])
        if actionParts[0] == "1":
            firstNumber = 1
        else:
            firstNumber = signals[actionParts[0]]
        signals[actionParts[4]] = firstNumber & signals[actionParts[2]]
    elif actionParts[1] == "OR":
        if not signals.keys().__contains__(actionParts[0]):
            signals = updateSignals(actions, signals, actionParts[0])
        if not signals.keys().__contains__(actionParts[2]):
            signals = updateSignals(actions, signals, actionParts[2])
        signals[actionParts[4]] = signals[actionParts[0]] | signals[actionParts[2]]
    elif actionParts[1] == "LSHIFT":
        if not signals.keys().__contains__(actionParts[0]):
            signals = updateSignals(actions, signals, actionParts[0])
        signals[actionParts[4]] = signals[actionParts[0]] << int(actionParts[2])
    elif actionParts[1] == "RSHIFT":
        if not signals.keys().__contains__(actionParts[0]):
            signals = updateSignals(actions, signals, actionParts[0])
        signals[actionParts[4]] = signals[actionParts[0]] >> int(actionParts[2])
    elif actionParts[0] == "NOT":
        if not signals.keys().__contains__(actionParts[1]):
            signals = updateSignals(actions, signals, actionParts[1])
        signals[actionParts[3]] = ~ signals[actionParts[1]]
    return signals

def processLine(signals, line):
    lineParts = line.split(" ")
    if lineParts[0].isnumeric():
        signals[lineParts[2]] = int(lineParts[0])
    elif lineParts[1] == "AND":
        signals[lineParts[4]] = signals[lineParts[0]] & signals[lineParts[2]]
    elif lineParts[1] == "OR":
        signals[lineParts[4]] = signals[lineParts[0]] | signals[lineParts[2]]
    elif lineParts[1] == "LSHIFT":
        signals[lineParts[4]] = signals[lineParts[0]] << int(lineParts[2])
    elif lineParts[1] == "RSHIFT":
        signals[lineParts[4]] = signals[lineParts[0]] >> int(lineParts[2])
    elif lineParts[0] == "NOT":
        signals[lineParts[3]] = ~ signals[lineParts[1]]
    return signals

file = loadInput(fileName)
actions = {}
for line in file:
    actions = generateActionsOrder(actions, line.rstrip())
actions['b'] = "46065 -> b"
signals = {}
signals = updateSignals(actions, signals, "a")
print(signals["a"])
