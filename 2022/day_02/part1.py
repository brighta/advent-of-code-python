import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def splitFileIntoElves(file):
    elves = []
    currentElf = 0
    for line in file:
        line = line.rstrip()
        if line == "":
            elves.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(line)
    elves.append(currentElf)
    return elves


file = loadInput(fileName);
elves = splitFileIntoElves(file)
print(max(elves))
