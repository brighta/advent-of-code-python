import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the file name for the input file.")

fileName = sys.argv[1]

def loadInput(fileName):
    with open(fileName) as file:
        return file.readlines()

def getLists(file):
    lists = []
    for line in file:
        parts = line.split(" ")
        lists.append(list(map(int, parts)))
    return lists

def isListSafe(list):
    listSorted = list.copy()
    listSorted.sort()
    listSortedReverse = list.copy()
    listSortedReverse.sort(reverse=True)
    if list != listSorted and list != listSortedReverse:
        return False
    for i in range(len(listSorted) - 1):
        difference = listSorted[i+1] - listSorted[i]
        if not 1 <= difference <= 3:
            return False
    return True

def getNumberSafe(lists):
    count = 0
    for list in lists:
        if isListSafe(list):
            count += 1
    return count

file = loadInput(fileName)
lists = getLists(file)
numberSafe = getNumberSafe(lists)
print(numberSafe)