import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getDisk(file):
    space = False
    index = 0
    disk = []
    for number in list(map(int, list(file[0]))):
        if space:
            nextValue = '.'
        else:
            nextValue = index
            index += 1
        disk.extend([nextValue for _ in range(number)])
        space = not space
    return disk

def removeSpaces(disk):
    while '.' in disk:
        value = disk.pop()
        if value != '.':
            index = disk.index('.')
            disk[index] = value
    return disk

def generateChecksumValues(disk):
    checksumValues = []
    for i in range(len(disk)):
        checksumValues.append(i * disk[i])
    return checksumValues

file = loadInput(fileName)
disk = getDisk(file)
disk = removeSpaces(disk)
checksumValues = generateChecksumValues(disk)
print(sum(checksumValues))