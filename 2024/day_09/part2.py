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
    for i in range(disk[-1], 1, -1):
        count = disk.count(i)
        indexOfFile = disk.index(i)
        indexOfPlace = findSubListIndex(['.' for _ in range(count)], disk[:indexOfFile])
        if indexOfPlace is not None:
            disk = replaceValuesFromindex(['.' for _ in range(count)], indexOfFile, disk)
            disk = replaceValuesFromindex([i for _ in range(count)], indexOfPlace, disk)
    return disk

def generateChecksumValues(disk):
    checksumValues = []
    for i in range(len(disk)):
        if disk[i] != '.':
            checksumValues.append(i * disk[i])
    return checksumValues

def findSubListIndex(subList, list):
    subListLength = len(subList)
    for index in (i for i, e in enumerate(list) if e == subList[0]):
        if list[index:index+subListLength] == subList:
            return index
    return None

def replaceValuesFromindex(values, index, list):
    return list[:index] + values + list[index + len(values):]

file = loadInput(fileName)
disk = getDisk(file)
disk = removeSpaces(disk)
checksumValues = generateChecksumValues(disk)
print(sum(checksumValues))