import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getCrates(file, indexOfSplit):
    numColumns = len(file[indexOfSplit-2].split(" "))
    crates = [[] for x in range(numColumns)]
    for i in range(indexOfSplit-2, -1, -1):
        index = 0
        for j in range(numColumns):
            crate = file[i][index+1]
            if crate != " ":
                cratesColumn = crates[j]
                cratesColumn.append(crate)
                crates[j] = cratesColumn
            index += 4
    return crates

def makeMovement(crates, move):
    moveParts = move.split(" ")
    numCrates = int(moveParts[1])
    fromColumn = int(moveParts[3])
    toColumn = int(moveParts[5])
    fromColumnCrates = crates[fromColumn-1]
    toColumnCrates = crates[toColumn-1]
    for i in range(numCrates):
        toColumnCrates.append(fromColumnCrates.pop())
    crates[fromColumn-1] = fromColumnCrates
    crates[toColumn-1] = toColumnCrates
    return crates

def getFirstOfEachColumn(crates):
    string = ""
    for crate in crates:
        string += crate[-1]
    return string

file = loadInput(fileName)
indexOfSplit = file.index("\n")
crates = getCrates(file, indexOfSplit)
for line in file[indexOfSplit+1:]:
    crates = makeMovement(crates, line.rstrip())
print(getFirstOfEachColumn(crates))
